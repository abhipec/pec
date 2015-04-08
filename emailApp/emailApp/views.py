import datetime
import os
import shutil

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline


from django.shortcuts import Http404, render_to_response
from django.template import RequestContext

from emailApp.models import Email, Dashboard, Rule
import emailApp.gmailUtil as gmail
import emailApp.emailParse as emp
import emailApp.cleanText as cleanUp
import emailApp.emailUtil as emailUtil
import emailApp.semantics as semantics
labelsMapping = []

text_clf = Pipeline([('vect', CountVectorizer()),
                    ('tfidf', TfidfTransformer()),
                    ('clf', SGDClassifier(loss='hinge', penalty='l2',
                    alpha=1e-3, n_iter=5, random_state=42)),
                    ])

def startup():
    global labelsMapping
    trainingData = []
    trainigLabels = []
    global text_clf
    emails = Email.objects.all()
    labels = []
    for email in emails:
        if email.category == 'others' or email.category == 'promotional':
            if email.textCleanHtml:
                trainingData.append(email.textCleanHtml + ' ' + email.subject + ' ' + email.sender )
                labels.append(email.category)
    count = 0
    tempDict = {}
    for label in labels:
        if tempDict.get(label,-1) == -1:
            tempDict[label] = count
            labelsMapping.append(label)
            trainigLabels.append(count)
            count = count + 1
        else :
            trainigLabels.append(tempDict[label])

    _ = text_clf.fit(trainingData,trainigLabels)

    return None

def refresh(request):
    startup()
    gmail_service = gmail.generateServiceToken()
    messages = gmail.ListMessagesWithLabels(gmail_service,'me','UNREAD')
    print(messages)
    for message in messages:
        messageId = message['id']
        try:
            email = Email.objects.get(messageId = messageId)
            print(email, "Exists")
        except Email.DoesNotExist:
            email = Email()
            data = gmail.GetMimeMessage(gmail_service, 'me',messageId)
            # save email
            emailUtil.saveRawEmail(messageId,data)
            email.saved = True
            email.messageId = messageId
            email.attachments = ''
            # parse email
            emp.emailParse(email,data)
            if email.textPlain:
                email.textCleanPlain = cleanUp.completeCleanUp(email.textPlain)

            if email.textHtml:
                email.textCleanHtml = cleanUp.completeCleanUp(email.textHtml)

            # apply category
            dataToPredict = []
            if email.textCleanHtml:
                dataToPredict.append(email.textCleanHtml + ' ' + email.subject + ' ' + email.sender)
            else :
                dataToPredict.append(email.subject + ' ' + email.sender)
            predicted1 = text_clf.predict(dataToPredict)
            for i in range(len(predicted1)):
                print(email,labelsMapping[predicted1[i]])

            email.category = labelsMapping[predicted1[0]]
            # update label
            # gmail.ModifyMessage(gmail_service, 'me', email.messageId, {'removeLabelIds': ['UNREAD'], 'addLabelIds': ['Label_28']})

            #email.save()
            if email.category == 'promotional' and email.textCleanHtml:
                couponCode = semantics.searchCouponCode(email.textCleanHtml)
                if couponCode:
                    print("coupon code found")
                    dashboard = Dashboard()
                    dashboard.data = couponCode
                    dashboard.source = email
                    dashboard.timeStamp = email.timeStamp
                    dashboard.validTill = email.timeStamp + datetime.timedelta(days=7)
                    # dashboard.save()

            # apply rules

            # rule based on category
            rules = Rule.objects.filter(ruleType = 'category', name = email.category)
            if rules:
                for rule in rules:
                    print(rule)

            # rule based on sender
            rules = Rule.objects.filter(ruleType = 'sender', name = email.sender)
            print(rules)
            if rules:
                for rule in rules:
                    data = filter(None, rule.rule.split(','))
                    print(data)
                    if data[0] == 'download':
                        if not os.path.isdir(data[1]):
                            os.makedirs(data[1])
                        attachments = filter(None, email.attachments.split(','))
                        print(attachments)
                        if attachments:
                            for attachment in attachments:
                                filePath = emailUtil.emailPath(messageId) + 'attachments/' + attachment
                                fileName, fileExtension = os.path.splitext(filePath)
                                print(filePath)
                                print(fileName, fileExtension)

                            if len(data) == 3:
                                if data[2] =='date':
                                    now = datetime.datetime.now()
                                    fileName = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
                            shutil.copy(filePath, data[1] + fileName + fileExtension)

    raise Http404

def fetchAllUnreadEmails(request):
    gmail_service = gmail.generateServiceToken()
    messageIdFile = open('tmp.txt','r')
    messages = messageIdFile.read().split('\n')
    messages = filter(None,messages)

    for message in messages:
        email = Email.objects.filter(messageId = message)
        if not email:
            print(message)
            data = gmail.GetMimeMessage(gmail_service, 'me',message)
            print(message,'email received')
            email = Email()
            email.messageId = message
            email.attachments = ''
            emp.emailParse(email,data)
            email.category = 'notification'
            email.save()

    messageIdFile.close()
    raise Http404

def cleanText(request):
    # some multipart/mixed emails are not parsed properly and all text fileds empty
    emails = Email.objects.all()
    print("Toatal emails = ", len(emails))

    for email in emails:
        if email.category =='notification':
            if email.textPlain:
                email.textCleanPlain = cleanUp.completeCleanUp(email.textPlain)

            if email.textHtml:
                email.textCleanHtml = cleanUp.completeCleanUp(email.textHtml)
            email.removedContentPlain = ''
            email.removedContentHtml = ''
            email.save()

    raise Http404

def dashboard(request):
    items = Dashboard.objects.all()
    return render_to_response('dashboard.html', locals(), context_instance=RequestContext(request))

def home(request):

    emails = Email.objects.all().order_by('timeStamp')[::-1]

    return render_to_response('home.html', locals(), context_instance=RequestContext(request))


def messagePage(request, messageId):
    try:
        email = Email.objects.get(messageId = messageId)
    except Email.DoesNotExist:
        raise Http404

    data = emailUtil.readRawEmail(messageId)
    data = emp.returnHtml(data)
    if not data:
        data = emp.returnText(messageId)
    # email.attachments = ''
    # emp.emailParse(email,emailUtil.readRawEmail(messageId))
    # email.save()

    if email.attachments:
        attachments = filter(None, email.attachments.split(','))
        displayMessage = "This email has attachment"
        for attachment in attachments:
            filePath = emailUtil.emailPath(messageId) + 'attachments/' + attachment

    return render_to_response('message.html', locals(), context_instance=RequestContext(request))

def saveAllUnreadEmails(request):
    gmail_service = gmail.generateServiceToken()
    emails = Email.objects.filter(saved = False)


    for email in emails:
        message = email.messageId
        email = Email.objects.get(messageId = email.messageId)
        if not email.saved:
            print(message)
            data = gmail.GetMimeMessage(gmail_service, 'me',email.messageId)
            print(message,'email received')
            emailUtil.saveRawEmail(message,data)
            email.saved = True
            email.save()

    raise Http404

def updateLables(request):
    gmail_service = gmail.generateServiceToken()
    emails = Email.objects.all()
    for email in emails:
        email = Email.objects.get(messageId = email.messageId)
        gmail.ModifyMessage(gmail_service, 'me', email.messageId, {'removeLabelIds': ['UNREAD'], 'addLabelIds': ['Label_28']})
        email.saved = False
        email.save()
    raise Http404
