from state import State

def ConcatOperator(nfa_stack):
    frag1 = nfa_stack.pop()
    frag2 = nfa_stack.pop()  
    #point frag2's accept state at frag 1's start state
    frag2.accept.edges.append(frag1.start) #Join the 1st fragments start state to the 2nds accept
    #create new instance of fragment to represent the new NFA
    start,accept = frag2.start,frag1.accept

    return(start,accept)
    
def OrOperator(nfa_stack):
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

    return(start,accept)   
            
def KleeneOperator(nfa_stack):
    #pop 1 fragment off the stack 
    frag = nfa_stack.pop()
    #create new start and accept states
    accept=State()
    start=State(edges=[frag.start,accept]) # points at start state of fragment just popped and new accept state
    #point the arrows
    frag.accept.edges = (frag.start,accept) # old accept state points at the old start state and the new accept state
    #create new instance of fragment to represent the new NFA

    return(start,accept) 
    
def QuestionOperator(nfa_stack):
    #pop 1 fragment off the stack 
    frag = nfa_stack.pop()
    #create new start and accept states      
    accept=State()# Empty Accept state
    start=State(edges=[frag.start,accept]) #Points at itself and nothing
    frag.accept.edges.append(accept) 

    return(start,accept) 

def PlusOperator(nfa_stack):
    #pop 1 fragment off the stack 
    frag = nfa_stack.pop()
    #create new start and accept states    
    accept=State()# Empty Accept state
    start=State(edges=[frag.start]) #new start point at the old start state
    frag.accept.edges = [frag.start,accept]

    return(start,accept) 