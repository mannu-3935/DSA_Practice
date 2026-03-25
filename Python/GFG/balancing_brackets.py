'''Parenthesis Checker :balanced if
- Each opening bracket has a corresponding closing bracket of the same type.
- Opening brackets must be closed in the correct order.
s = "[{()}]"  --> True
s = "[()()]{}" --> True
s = "([]" --> False
s = "([{]})" --> False
'''

def isBalanced(s):
    lst=[]
    open="{[("
    close="}])"
        
    for char in s:
        if char in open:
            lst.append(char)
        elif char in close:
            if not lst or open.index(lst.pop()) != close.index(char):
                return False
    return len(lst)==0

s = "[()()]{}"
print(isBalanced(s))