from bs4 import BeautifulSoup
from flanker import mime
import re
from dateutil import parser as dateParser
import emailApp.emailUtil as emailUtil

emailRegex = re.compile(("([a-zA-Z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+\/=?^_`"
                    "{|}~-]+)*(@|\sat\s)(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?(\.|"
                    "\sdot\s))+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)"))
def cleanText(text):
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text

def htmlToText(html):
    soup = BeautifulSoup(html)

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    return cleanText(soup.get_text())

def emailParse(email, data):
    msg = mime.from_string(str(data))
    sender = msg.headers['From'].encode('ascii','ignore')
    senderEmail = re.search(emailRegex,sender)
    if not senderEmail:
        print(sender)
    email.sender = senderEmail.group(0)
    email.subject = msg.headers['Subject'].encode('ascii','ignore')
    date = msg.headers['Date'].encode('ascii','ignore')
    if date.find('(') > -1:
        date = date[:date.find('(')]
    print(date)
    email.timeStamp = dateParser.parse(date)
    if msg.content_type.is_multipart():
        for part in msg.parts:
            if part.content_type == 'text/plain':
                email.textPlain = cleanText(part.body.decode('utf-8').encode('ascii'))
            elif part.content_type == 'text/html':
                email.textHtml = htmlToText(part.body.decode('utf-8').encode('ascii'))
            elif part.content_type == 'application/pdf' or part.content_type == 'application/octet-stream':
                filename = part.headers['content-Disposition'][1]['filename']
                emailUtil.writeFile(email.messageId, part.body, filename)
                email.attachments = email.attachments + filename.decode('utf-8').encode('ascii') + ','
    elif msg.content_type.is_singlepart():
        if msg.headers['Content-Type'] == 'text/plain':
            email.textPlain = cleanText(msg.body.decode('utf-8').encode('ascii'))
        elif msg.headers['Content-Type'] == 'text/html':
            email.textHtml = htmlToText(msg.body.decode('utf-8').encode('ascii'))


def returnHtml(email):
    msg = mime.from_string(str(email))
    if msg.content_type.is_multipart():
        for part in msg.parts:
            if part.content_type == 'text/html':
                return part.body
    elif msg.content_type.is_singlepart():
        if msg.headers['Content-Type'] == 'text/html':
            return msg.body

def returnText(email):
    msg = mime.from_string(str(email))
    if msg.content_type.is_multipart():
        for part in msg.parts:
            if part.content_type == 'text/plain':
                return part.body
    elif msg.content_type.is_singlepart():
        if msg.headers['Content-Type'] == 'text/plain':
            return msg.body
