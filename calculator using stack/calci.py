operators=['+','-','*','/','%','^']
priority={'+':1,'-':1,'*':2,'/':2,'%':3,'^':3}
def postfix(expr):
    stack=[]
    arr=''
    for i in exp:
        if(i not in operators):
            arr=arr+i
        else:
            while(stack and stack[-1]!='(' and priority[i]<=priority[stack[-1]]):
                arr=arr+stack.pop()
            stack.append(i)
    while(stack):
        arr=arr+stack.pop()
    return arr
def calculate(inputs):
    stack=[]
    for a in inputs:
        if a.isdigit():
            stack.append(a)
        else:
            op1=int(stack.pop())
            op2=int(stack.pop())
        if (a=='+'):
            stack.append(op2+op1)
        elif (a=='-'):
            stack.append(op2-op1)
        elif (a=='*'):
            stack.append(op2*op1)
        elif (a=='/'):
            stack.append(op2/op1)
        elif (a=='%'):
            stack.append(op2%op1)
        elif (a=='^'):
            stack.append(op2^op1)
    return stack.pop()
#taking inputs from user
exp=input("enter an expression to evaluate:")
postfixexp=postfix(exp)
print("pstfixexpression:",postfixexp)
result=calculate(postfixexp)
print("answer is:",result)
