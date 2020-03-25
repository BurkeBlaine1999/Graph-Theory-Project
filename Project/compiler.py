from fragment import Fragment
from shunting import shunt
from state import State

#This code could be cleaned up
def compile(infix): 
    postfix = shunt(infix)#Changes regular expression to postfix regular expression
    postfix = list(postfix)[::-1]#turning postfix into a list and reversing list
 
    #Keeps track of all created fragments from postfix
    nfa_stack = []
       
    #Loop through while we have stuff left in the postfix regular expression , taking the next character off of it.
    #If it is any of the special characters we do something special otherwise we just create a new NFA fragment
    # with a new start state, a new accept state and the start state is labeled with whatever character we read.
    
    while postfix:
        #pop a character from postfix
        c = postfix.pop()
        if c =='.': 
            
            #if you come across the . operator we should have at least 2 nfa fragments on the nfa stack.
            # if not we have an invalid postfix expression.(Problem for shunting)
            
            #pop 2 fragments off the stack(Might be able pop 2 things off the stack in 1 statement)
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()  
            #point frag2's accept state at frag 1's start state
            frag2.accept.edges.append(frag1.start) #Join the 1st fragments start state to the 2nds accept
            #create new instance of fragment to represent the new NFA
            newfrag = Fragment(frag2.start,frag1.accept) # Creates the path joing the states
            #push the new NFA to the stack
    
        elif c == '|':
            #Pop 2 fragments off the stack (Might be able pop 2 things off the stack in 1 statement)
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()  
            #Create 2 new states , a new start and accept state (when doing | need to create 2 new states)
            accept = State()
            start = State(edges=[frag2.start,frag1.start])#new start points at the 2 old start states
            # Point the old accept states at the new one
            frag2.accept.edges.append(accept) # Old accept states have to point to the new accept states
            frag1.accept.edges.append(accept)
            #create new instance of fragment to represent the new NFA          
            newfrag = Fragment(start,accept) #Create new fragment
            #push the new NFA to the stack
            
        elif c == '*':
            #pop 1 fragment off the stack 
            frag = nfa_stack.pop()
            #create new start and accept states
            accept=State()
            start=State(edges=[frag.start,accept]) # points at start state of fragment just popped and new accept state
            #point the arrows
            frag.accept.edges = (frag.start,accept) # old accept state points at the old start state and the new accept state
            #create new instance of fragment to represent the new NFA
            newfrag = Fragment(start,accept) # new fragment with new start and accept states as its states
            #push the new NFA to the stack
        else:
            accept = State()
            start = State(label=c,edges=[accept])
            #create new instance of fragment to represent the new NFA
            newfrag = Fragment(start,accept)
            
        #push the new NFA to the stack
        nfa_stack.append(newfrag) 
        #the NFA stack should only have excactly 1 NFA on it (The answer)
    return nfa_stack.pop()
        # could also be put at the bottom of all the ifs/elses
        # You can appened multiple elements to a list by using 'extend'
        # You might be able pop multiple things at once --> research + improve efficiency