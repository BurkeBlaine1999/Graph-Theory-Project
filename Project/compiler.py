from fragment import Fragment
from shunting import shunt
from state import State
from operators import *

#This code could be cleaned up
def compile(infix): 
    postfix = shunt(infix)#Changes regular expression to postfix regular expression
    postfix = list(postfix)[::-1]#turning postfix into a list and reversing list
 
    #Keeps track of all created fragments from postfix
    nfa_stack = []
    
    while postfix:
        #pop a character from postfix
        c = postfix.pop()

        if c =='.':#And
            start , accept = ConcatOperator(nfa_stack)   
        elif c == '|':#Or
            start , accept = OrOperator(nfa_stack)             
        elif c == '*':# 0 or many
            start , accept = KleeneyOperator(nfa_stack)            
        elif c == '?': #1 OR 0
            start , accept = QuestionOperator(nfa_stack)  
        elif c == '+': #1 OR More
            start , accept = PlusOperator(nfa_stack)  
        else:
            accept = State()
            start = State(label=c,edges=[accept])
            #create new instance of fragment to represent the new NFA
               
        newfrag = Fragment(start,accept) 
        #push the new NFA to the stack
        nfa_stack.append(newfrag) 
        #the NFA stack should only have excactly 1 NFA on it (The answer)
        
    return nfa_stack.pop()      