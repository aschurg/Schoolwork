from BinaryTree import BinaryTree
from Decoder import decode
import sys

treeList = []
tree = BinaryTree(None)

def makeTree(tList):
    #creates tree from list of letters and codes
    for i in tList:
        insertNode(tree, i[0], i[1])
    #print(printexp(tree))

def insertNode(node, letter, code):
    #iterates through letters and codes and inserts letters into tree
    if len(code) == 1:
        if code == '0':
            if node.getLeftChild() != None:
                invalidCode()
            else:
                node.insertLeft(letter)

        elif code == '1':
            if node.getRightChild() != None:
                invalidCode()
            else:
                node.insertRight(letter)


    elif code[0] == '0':
        goLeft(node)
        insertNode(node.getLeftChild(), letter, code[1:])

    elif code[0] == '1':
        goRight(node)
        insertNode(node.getRightChild(), letter, code[1:])

    else:
        invalidCode()

def goLeft(node):
    #moves to left child of node if it exists, otherwise
    #creates empty node as left child of node
    if node.getLeftChild() != None:
        if node.getLeftChild().key != None:
            invalidCode()
        else:
            pass
    else:
        node.insertLeft(None)

def goRight(node):
    #moves to right child of node if it exists, otherwise
    #creates empty node as right child of node
    if node.getRightChild() != None:
        if node.getRightChild().key != None:
            invalidCode()
        else:
            pass
    else:
        node.insertRight(None)

def invalidCode():
    #prints error message and terminates program
    print("Error: Not a valid code")
    quit()

def printexp(tree):
    #used to print tree for testing/debugging
  sVal = ""
  if tree:
      sVal = '(' + printexp(tree.getLeftChild())
      sVal = sVal + str(tree.getRootVal())
      sVal = sVal + printexp(tree.getRightChild())+')'
  return sVal

def findComp(chars, bits):
    #finds and returns compression ratio
    uncompressed = chars*8
    return bits/uncompressed

def printResults(bits, chars, message):
    print("Success:", message)
    print("Number of bits =", bits)
    print("Number of characters =", chars)
    print("Compression ratio =", findComp(chars, bits))

def getFile(filename):
    #opens file and breaks into message and list of coding scheme
    text = open(filename, "r")
    doneCoding = False
    for i in text:
        if doneCoding == True:
            makeTree(treeList)
            return i.strip()
        else:
            if i == '\n':
                doneCoding = True
            else:
                line = i.split()
                treeList.append(line)
def encoder(filename):
    #runs everything
    message = getFile(filename)
    numbits = len(message)
    decoded = decode(tree, tree, message)
    numchars = len(decoded)
    printResults(numbits, numchars, decoded)

filename = sys.argv[1]
encoder(filename)
