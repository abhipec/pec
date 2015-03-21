import pickle
from bs4 import BeautifulSoup
from flanker import mime

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

    return cleanText(soup.get_text()).encode('utf-8')

f = open('shopclues.txt','r')
plain = open('plain1.txt','w')
html = open('html1.html','w')
htmlText = open('htmlText1.txt','w')
data = pickle.load(f)
msg = mime.from_string(str(data))
print('multipart', msg.content_type.is_multipart())
print('singlepart', msg.content_type.is_singlepart())
print('container', msg.content_type.is_message_container())
print('body', msg.body)
print('enclosed', msg.enclosed)
# print(msg.headers.items())
for part in msg.parts:
        if part.content_type == 'text/plain':
            plain.write(cleanText(part.body.encode('utf-8')))
        elif part.content_type == 'text/html':
            htmlText.write(htmlToText(part.body))
            html.write(part.body.encode('utf-8'))
f.close()
plain.close()
html.close()
htmlText.close()
