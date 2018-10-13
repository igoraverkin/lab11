import array
import operator
import re

counts=str(0)
OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
def toPolish(newCounts):
    operStack =['']
    mytext = ""
    i=0
    for token in newCounts: 
        if token =='--':
            token='+'
        elif token =='+-' or token=='-+':
            token='-'
        if (token not in OPERATORS) and (token !='(') and (token!=')'):          
            mytext+=token + ' '
        elif token in OPERATORS:
            if token=='*' or token=='/':
                if operStack[i] =='':
                    operStack.pop(i) # why? just magic
                    operStack.append(token)
                elif operStack[i] =='+' or operStack[i]=='-':
                    operStack.append(token)
                else:
                    mytext+=operStack.pop() +' '        
                    operStack.append(token)
            else:
                if operStack[i] =='': 
                    operStack.pop(i) #same as just magic
                    operStack.append(token)
                elif operStack[i]!='':
                    mytext+=operStack[i] +' '
                    operStack.pop()
                    operStack.append(token)
        elif token =='(':
            if operStack[i] =='': 
                operStack.pop(i) #same as just magic
                operStack.append(token)
                operStack.append('')
                i=operStack.index(token)+1
            elif operStack[i]!='':
                operStack.append(token)
                operStack.append('')
                i = operStack.index(token)+1
        elif token ==')':
            i=0
            operStack.append(token)
            operStack.remove('(')
            operStack.remove(')')
            for _ in range(len(operStack)):
                mytext+=operStack.pop() + ' '
            operStack.append('')
    for _ in range(len(operStack)):
        mytext+=operStack.pop() + ' '
    
    return mytext

def calc(counts):
    
    counts = counts.replace(" ", '')    
    stack = [0]
    newCounts = re.findall(r'\d+|[\*,\+,\-,\/,\(,\)]', counts) #deep dark magic

    mytext = toPolish(newCounts)
    for token in mytext.split(" "): 
        if token in OPERATORS:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(OPERATORS[token](op1,op2))
        elif token:
            stack.append(float(token))
    return stack.pop()
print(calc(counts))



