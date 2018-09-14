import PyPDF2


def main():
    words = []
    time = []
    classType = []
    words = getWords()
    seperateTimeWords(words,time,classType)

    print(sorted(classType))

def createFile():
    newfile = open('test.txt', 'w')
    file = open('test.PDF', 'rb')
    pdfreader = PyPDF2.PdfFileReader(file)
    pages = pdfreader.getNumPages()
    for page in range(pages):
        pageObj = pdfreader.getPage(page)
        newfile.write(pageObj.extractText())
    file.close()
    newfile.close()

def getWords():
    with open('test.txt') as f:
        words = []
        c = []
        s = ''
        for i in range(600000):
            r = f.read(1)
            if r == ' ':
                words.append(s.join(c))
                c = []
            elif r == ':':
                words.append(s.join(c))
                c = []
            else:
                c.append(r)
    print(words)
    return words

def seperateTimeWords(words,time, classType):
    keywords = ['C01)', 'C01', 'ITV', 'TBA', 'C01/', 'C02', 'C02/', 'C02)', 'V01', 'V01/', 'V01)', 'UNDG', '(E', '(E.',
                'X01.', 'X01', 'NOT', 'THE']
    i = 0
    while i < len(words):
        try:
            if '0am' in words[i] or '5am' in words[i] or '0pm' in words[i] or '5pm' in words[i]:
                time.append(words[i - 1] + ':' + words[i] + '-' + words[i + 2] + ":" + words[i + 3])
                i = i + 4
        except IndexError:
            print('Could not finish. Did not read enough characters')

        if words[i].isupper() and 5 > len(words[i]) > 2:
            classType.append(words[i])
        i = i + 1
    print(len(classType))
    i = 0
    while i < len(classType) - 1:
        for blacklist in keywords:
            if classType[i] == blacklist:
                del classType[i]
            if classType[i-1] == blacklist:
                del classType[i-1]
            if classType[i+1] == blacklist:
                del classType[i+1]
        i = i + 1


    for classT in classType:
        print(classT)



main()
