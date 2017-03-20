
message = []

def decode(root, node, code):
    #recursive method to read binary message and return string
    if len(code) == 0:
        if(node.key) == None or node == None:
            invalidMess()
        else:
            message.append(node.key)
            mess = ''.join(message)
            return mess
    elif node.getRightChild() == None and node.getLeftChild() == None:
        if node.key == None:
            invalidMess()
        else:
            message.append(node.key)
            return(decode(root, root, code))
    elif code[0] == '0':
        return(decode(root, goLeft(node), code[1:]))
    elif code[0] == '1':
        return(decode(root, goRight(node), code[1:]))
    else:
        invalidMess()

def goLeft(node):
    #returns left child if it exists
    if node.getLeftChild() == None:
        invalidMess()
    else: 
        return node.getLeftChild()
            
def goRight(node):
    #returns right child if it exists
    if node.getRightChild() == None:
        invalidMess()
    else:  
        return node.getRightChild()

    
def invalidMess():
    #prints error message
    print("Error: cannot decode message")
    quit()
