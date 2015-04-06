from nltk.corpus import words

def isSentenceContainNonDictionaryWords(sentence):
    for word in sentence.split(' '):
        if word not in words.words():
            return True
    return False

def searchCouponCode(text):
    data = text.lower().split('\n')
    result = []
    for i in range(len(data)):
        if 'coupon' in data[i] or 'code' in data[i]:
            if isSentenceContainNonDictionaryWords(data[i]):
                result.append(data[i])
            elif isSentenceContainNonDictionaryWords(data[i+1]):
                result.append((data[i],data[i+1]))
    return result
