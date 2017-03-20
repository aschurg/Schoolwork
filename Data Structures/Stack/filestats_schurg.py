"""Program opens a text file (bill.txt) located within the same folder.
Uses a stack and dictionary to return 10 words that occur the most frequently in the file"""
import sys

class Stack:
     """Stack used for turning letters into words
     """
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


letterList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctLetter = "'-"

wordDict = {}
wordStack = Stack()

lineCount = 0
wordCount = 0
charCount = 0

def addToDict(word):
     """
     Recieves word. If the word is actually a word (not empty), increments
     word count. Either adds new word to dictionary, or updates amount of
     a specific word found.
     """
     global wordCount
     word.reverse()
     key =  "".join(word)
     if key:
          wordCount += 1
          if key in wordDict:
               wordDict[key] += 1
          else:
               wordDict.update({key: 1})

def analyzeFile(fileName):
     """
     Opens file. Iterates through each letter counting lines at every '\n',
     adding chars to a word stack, popping words at every space and line end,
     sends words to add to dictionary.
     Also counts every character.
     """
     file = open(fileName, 'r')
     text = file.read()
     global lineCount
     global charCount

     for i in text:
          if i == '\n':
               lineCount += 1
               word = []
               while not wordStack.isEmpty():
                    word.append(wordStack.pop())
               addToDict(word)

          elif i in letterList:
               wordStack.push(i.lower())
               charCount += 1
          elif i in punctLetter:
               wordStack.push(i)
               charCount += 1
          elif i == ' ':
               word = []
               while not wordStack.isEmpty():
                    word.append(wordStack.pop())
               addToDict(word)
               charCount += 1
          else:
               charCount += 1

def printResults():
     """
     Prints all results including top ten words and their frequencies.
     """
     print("This file has:")
     print(charCount, "characters")
     print(lineCount, "lines")
     print(wordCount, "words")
     print("The top 10 most frequent words are:")
     topTen = sorted(wordDict.items(), key=lambda x:-x[1])[:10]
     for key in topTen:
          print("{1} {0}".format(*key))

def filestats_schurg(file):
     """
     Called with a file name string. Counts the lines, characters, and words
     in given file. Prints these results and the 10 most frequently used words.
     """
     analyzeFile(file)
     printResults()

filename = sys.argv[1]
filestats_schurg(filename)
