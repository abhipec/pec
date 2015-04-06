import re
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer

def removeUrls(text):
    match_urls = re.compile(ur'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))')
    urls = match_urls.findall(text)
    removedContent = []
    for url in urls:
        text = text.replace(url[0],'')
        removedContent.append(url[0])
    # remove some left out http:// and https:// but logging only once
    if text.find('https') > -1:
        text = text.replace('https://','')
        removedContent.append('https://')
    if text.find('http') > -1:
        text = text.replace('http://','')
        removedContent.append('http://')
    return text, removedContent

def changeCase(text):
    return text.lower()
# remove between, if, to from stop words
# these will be needed later
stopWords = set(stopwords.words('english')) - set(['between','if','to'])
wnl = WordNetLemmatizer()
def removeCommonWords(text):
    words = wordpunct_tokenize(text)
    updatedWords = []

    for word in words:
        # remove single letter characters
        if len(word) == 1:
            # percent is important in our context
            if word == '%':
                updatedWords.append('percent')
            if word == '$':
                updatedWords.append('dollar')
            continue
        # rs is important in our context
        if word == 'rs':
            updatedWords.append('rupee')
            continue
        # remove words containing \ or /
        if word.find('\\') > -1 or word.find('/') > -1 or word.find('"') > -1 or word.find(')') > -1:
            continue
        # remove stopwords
        if word in stopWords:
            continue
        # stemming
        updatedWords.append(wnl.lemmatize(word))

    return ' '.join(updatedWords)


def completeCleanUp(text):
    text = changeCase(text)
    text, removedContent = removeUrls(text)
    return removeCommonWords(text)
