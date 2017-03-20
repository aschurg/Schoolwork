"""Program takes name of an xml file as input. Checks for validity by ensuring
each tag has a corresponding closing tag"""

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


def xmlCheck(filename):
    """
    Xmlcheck accepts the text file. Then the file is broken up into seperate
    items to enter to the output. Items in list are either an opening or closing
    tag or non-tag text
    """
    #return(filename.read())
    final = []
    wordList = []
    openTag = Stack()
    closeTag = Stack()
    word = []
    checkClose = []
    checkOpen = []
    text = ''.join(filename.read())
    #print(text)
    tagging = False
    close = False
    valid = True
    for i in text:
        if i == '<':
            #indicates begininning of a tag
            tagging = True
            if wordList:
                sendOut(wordList, final)
                wordList = []
        elif i == '/' and tagging == True:
            #indicates tag is a closing tag
            close = True
            word.append(i)
        elif tagging == True and close == False:
            #if i is in an opening tag
            openTag.push(i)
            if i == '>':
                #indicates opening tag is over
                while openTag.isEmpty() == False:
                    x = openTag.pop()
                    word.append(x)
                    checkOpen.append(x)
                tagging = False
                sendOut(word, final)
                word = []
        elif tagging == True and close == True:
            #if i is in a closing tag
            closeTag.push(i)
            if i == '>':
                #indicates closing tag is over
                close = False
                while closeTag.isEmpty() == False:
                    x = closeTag.pop()
                    word.append(x)
                    checkClose.append(x)
                tagging = False
                sendOut(word, final)
                word = []

        elif i == '\n':
            #insert space for line break
            wordList.append(' ')
        else:
            wordList.append(i)

    formatOut(final)

def checkMatch(closer, opener):
    """checks if closing tag matches opening tag.
    ends program if tags don't match"""
    if opener.pop() != closer.pop():
        print("INVALID XML")
        quit()

def sendOut(word, final):
    """collapses white spaces"""
    j = None
    while word and word[0] == ' ':
        word.pop(0)
    if word:
        final.append(word)

def formatOut(xml):
    """formats the file correctly and prints it to screen"""
    offset = 0
    final = []
    closeStack = Stack()
    openStack = Stack()
    for i in xml:
        if i[0] == '/':
            #indicates closing tag
            #sends two tags from stacks to checkMatch
            i.pop(1)
            i.pop(0)
            i.reverse()
            i.insert(0, '<')
            i.append('>')
            offset -= 1
            for k in range(offset):
                final.append('    ')
            line = ''.join(i)
            closeStack.push(line)
            valid = checkMatch(closeStack, openStack)
            i.insert(1, '/')
            final.append(''.join(i) + '\n')
        elif i[0] == '>':
            #indicates end of tag
            i.pop(0)
            i.reverse()
            i.append('>')
            i.insert(0, '<')
            for k in range(offset):
                final.append('    ')
            offset += 1
            line = ''.join(i)
            openStack.push(line)
            final.append(line + '\n')
        else:
            for j in range(offset):
                final.append('    ')
            i = ''.join(i)
            i = i.split()
            final.append(' '.join(i) + '\n')
    print(''.join(final))

def main():
    """runs the whole thing"""
    file = input("enter file name: ")
    text = open(file)
    xmlCheck(text)

main()
