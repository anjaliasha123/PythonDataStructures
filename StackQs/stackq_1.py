# -*- coding: utf-8 -*-
"""StackQ-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZwH0IcaQmqyPsyYkqL2eNYh3AqIbTsdP

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if: Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order.
"""

import unittest

def areParanthesisBalanced(expr) : 
    stack = [] 
    #Write Your Code here
    if len(expr)<1:
        return False
    l = [i for i in expr]
    if l[0] not in ['(','{','{']:
        return False
    closeHash = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    
    for i in l:
        if i not in closeHash.keys():
            stack.append(i)
        else:
            if closeHash[i] != stack[-1]:
                print(stack[-1])
                print(closeHash[i])
                return False
            else:
                stack.pop()
    if len(stack)>0:
        return False
    return True
expr = "{()}[]"; 
actual = areParanthesisBalanced(expr)
print(actual)

expr = "{(){[]"
actual = areParanthesisBalanced(expr)
print(actual)

