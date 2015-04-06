import os

def emailPath(id):
    path = 'data' + '/' + id[:2] + '/' + id[2:4] + '/' + id[4:6] + '/' + id[6:] + '/'
    return path


def saveRawEmail(id, data):
    if type(data) != 'str':
        data = str(data)

    path = emailPath(id)
    if not os.path.isdir(path):
        os.makedirs(path)
    newfile = open(path + 'raw','w')
    newfile.write(data)
    newfile.close()

def readRawEmail(id):
    path = emailPath(id)
    if os.path.isfile(path + 'raw'):
        newfile = open(path + 'raw','r')
        data = newfile.read()
        newfile.close()
        return data
    else :
        return None

def writeFile(id, data, filename):
    path = emailPath(id) + 'attachments/'
    if not os.path.isdir(path):
        os.makedirs(path)
    f = open(path + filename,'w')
    f.write(data)
    f.close()
