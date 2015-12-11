from Tree import *


def preorder(tree):
    if is_empty_tree(tree):
        return []
    else:
        return [root(tree)]+preorder(left_subtree(tree))+preorder(right_subtree(tree))

def stack():
    return ('stack',[])

def contents(stacks):
    return stacks[1]

def top(stacks):
    return contents(stacks)[0]

def is_stack(objects):
    return type(objects)==tuple and objects[0]=='stack'

def stack_empty(stacks):
    return contents(stacks)==[]

def push(stacks,element):
     return contents(stacks).append(element)

def pop(stacks):
    return contents(stacks).pop(0)

def is_operator(op):
    if op=="+" or op=="-" or op=="*" or op=="/":
        return True
    else:
        return False

def evalPostfix(tree):
    st=postorder(tree)
    stk=stack()

    for op in st:
        if is_operator(op)==True:
            f, s =pop(stk),pop(stk)
            push(stk,apply_operator(op,f,s))
            print '1', stk
                 
        else:
            push(stk,op)
            print '2',stk
    return top(stk)

def apply_operator(op,f,s):
    if op=='+':
        return f+s
    elif op=='-':
        return f-s
    elif op=='*':
        return f*s
    elif op=='/':
        return float(f/s)
