"""
Author: Jonathan Lander
Date: 9/14/18
Purpose: To create a PDF searchable
"""
import PyPDF2
def main():
    words = []
    time = []
    instructor = []
    classType = [()]
    words = getWords()
    sections = getSections(words)
    cleanSections(sections)
    for i in sections:
        print(i)
    """
    seperateTimeWords(words,time,classType,instructor)
    print(len(classType))
    classType = getClassNumber(classType,words, time, instructor)
    for c in classType:
        print(c)
    print(len(words))
    print(len(time))
    print(len(instructor))
    print(len(classType))
    """


def cleanSections(sections):
    i = 0
    while i < len(sections)-1:
        if sections[i][0] == 'Report':
            del sections[i]
        i = i + 1

def getSections(words):
    add = False
    section = []
    sections = []
    for w in words:
        section.append(w)
        if '__________________' in w:
            sections.append(section)
            section = []
    return sections





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

def seperateTimeWords(words,time, classType,instructor):
    del classType[0]
    keywords = ['C01)', 'C01', 'ITV', 'TBA', 'C01/', 'C02', 'C02/', 'C02)', 'V01', 'V01/', 'V01)', 'UNDG', '(E', '(E.',
                'X01.', 'X01', 'NOT', 'THE', 'AH,']
    i = 0
    while i < len(words):
        try:
            if 'Time' in words[i-2] and '0am' in words[i] or '5am' in words[i] or '0pm' in words[i] or '5pm' in words[i]:
                time.append(words[i - 1] + ':' + words[i] + '-' + words[i + 2] + ":" + words[i + 3])
                i = i + 4
            if 'Time' in words[i] and 'TBA' in words[i+1]:
                time.append('TBA')
            if 'Instructor' in words[i]:
                instructor.append(words[i+1])

        except IndexError:
            print('Could not finish. Did not read enough characters')
        add = True
        for x in keywords:
            if words[i] == x:
                add = False
        if words[i].isupper() and 5 > len(words[i]) > 2 and add:
            classType.append((words[i], i+1))
        i = i + 1
    i = 0

def getClassNumber(classType, words,time, instructor):
    holder = [x[1] for x in classType]
    cn = [x[0]for x in classType]
    i = 0
    l = [()]
    del l[0]
    for h in holder:
        future = words[h][:3]
        if future == ' ' or future.isdigit() and time:
            l.append((cn[i], future, words[h][3:6], holder[i]))
            holder[i] = future
        else:
            del cn[i]
            del holder[i]
        i = i + 1

    return l

#Calling the functions.
main()

