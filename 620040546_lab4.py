from Tree import *
def stack():
    return ("stack", [])

def contents(stk):
    return stk[1]

def top(stk):
    return contents(stk)[len(contents(stk)) - 1]

def is_stack(stk):
    return type(stk) == tuple and stk[0] == "stack"

def stack_empty(stk):
    if is_stack(stk):
        return not contents(stk) != []

def push(stk, ele):
    return contents(stk).append(ele)

def pop(stk):
    return contents(stk).pop()

def is_operator(arg):
    if arg == "+" or arg == "-" or arg == "/" or arg == "*":
        return True
    else:
        return False

def evalPostfix(tree):
    lt = postorder(tree)
    stk = stack()
    for ele in lt:
        if is_operator(ele) == True:
            first, second = pop(stk),pop(stk)
            push(stk, apply_operator(ele, first, second))
            print 't', stk
        else:
            push(stk, ele)
            print '2', stk
    return top(stk)


def apply_operator(operand, second, first):
    if operand == '+':
        return first + second
    elif operand == '-':
        return first - second
    elif operand == '/':
        return first / second
    else:
        return first * second
