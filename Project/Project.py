#Blaine Burke - Thompsons Construct

#====================================================================
class State:
    #All states have 0,1,2 edges leading from it
    edges = [] 
    #Label for the aarows(None means epsilon)
    label = None 
    #Constructor for the class
    def __init__(self,label=None,edges=[]):
        self.edges = edges
        self.label = label
 
#====================================================================    

class Fragment:
    #Start of the NFA fragment
    start = None
    #Accept state of NFA fragment
    accept = None
    #Constructor
    def __init__(self,start,accept):
        self.start = start
        self.accept = accept
              
#==============================================================================================

def shunt(infix):  # Could probably made more efficient
    infix = list(infix)[::-1]
    # Operator stack
    opers = []
    # Output list
    postfix = []
    # Operator Precedence. (Dictionary) 
    prec = {'*': 100,'+':95,'?':90, '.': 80, '|': 60, ')': 40, '(': 20}

    # Loop through the input one character at a time
    while infix:
        # Pop a character from the input
        c = infix.pop()

        # Decide what to do based on the character
        if c == '(':
            # Push and open to the opers stack
            opers.append(c)
        elif c == ')':
            # Pop the operators stack until you find an open bracket
            while opers[-1] != '(':
                postfix.append(opers.pop())
                # Get rid of the '('
            opers.pop()
        elif c in prec:
            # Push any operators on the opers stack with higher prec to the output
            while opers and prec[c] < prec[opers [- 1]]:
                postfix.append(opers.pop())
            # Push c to the operator stack
            opers.append(c)

        elif c in ['(', ')','.','|','*','?','+']:
            # Push c to the operator stack
            opers.append(c)
        else:
            # Typically, we just push the character to the output.
            postfix.append(c)

    # Pop all operators to the output
    while opers:
        postfix.append(opers.pop())

    # Convert output list to String
    return ''.join(postfix)

#==============================================================================================

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
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()  
            #point frag2's accept state at frag 1's start state
            frag2.accept.edges.append(frag1.start) #Join the 1st fragments start state to the 2nds accept
            #create new instance of fragment to represent the new NFA
            start,accept = frag2.start,frag1.accept
    
        elif c == '|':#Or
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
            
        elif c == '*':# 0 or many
            #pop 1 fragment off the stack 
            frag = nfa_stack.pop()
            #create new start and accept states
            accept=State()
            start=State(edges=[frag.start,accept]) # points at start state of fragment just popped and new accept state
            #point the arrows
            frag.accept.edges = (frag.start,accept) # old accept state points at the old start state and the new accept state
            #create new instance of fragment to represent the new NFA
            
        elif c == '?': #1 OR 0
            #pop 1 fragment off the stack 
            frag = nfa_stack.pop()
            #create new start and accept states      
            accept=State()# Empty Accept state
            start=State(edges=[frag.start,accept]) #Points at itself and nothing
            frag.accept.edges.append(accept) 

        elif c == '+': #1 OR More
            #pop 1 fragment off the stack 
            frag = nfa_stack.pop()
            #create new start and accept states    
            accept=State()
            start=State(edges=[frag.start]) 
            frag.accept.edges = [frag.start,accept]

        elif c == '-': #
            #pop 1 fragment off the stack 
            frag = nfa_stack.pop()
            #create new start and accept states    
            accept=State()
            start=State(edges=[frag.start]) 
            frag.accept.edges = [frag.start,accept]

        else:
            accept = State()
            start = State(label=c,edges=[accept])
            #create new instance of fragment to represent the new NFA
               
        newfrag = Fragment(start,accept) 
        #push the new NFA to the stack
        nfa_stack.append(newfrag) 
        #the NFA stack should only have excactly 1 NFA on it (The answer)
    return nfa_stack.pop()
        # You might be able pop multiple things at once --> research + improve efficiency
#==============================================================================================            

#Add a state to a set and follow all the epsilon aarows       
def followes(state,current): #Follow e's
    
    #Only do something when we havent already seen the state
    if state not in current:       
        #Put the state into current
        current.add(state)
        #ee weather state is labelled by e/epsilon
        if state.label is None:
            #Loop through the states pointed to by this state.
            for x in state.edges:
                #follow all of their epsilons too.
                followes(x,current)
    
    
#==============================================================================================

def match(regex,s): 
    nfa = compile(regex)  
    current = set() # Current set of states we are in
    #add the first state and all of the states it points to and follow all epsilon aarows
    followes(nfa.start,current)
    
    #Previous set of states
    previous = set() #redundant as its about to be set to the value of current(CAN BE DELETED for efficiency)
    
    #Loop through characters in s
    for c in s:
        #keep track of where we were
        previous = current
        #Create a new empty set for states we are about to be in
        current = set()
        #Loop through previous states
        for state in previous:
            # Only follow aarows not labeled by e/epsilon
            if state.label is not None:
                #if the label of the state is equal to the character weve read:
                if state.label == c:
                    #Add the state at the end of the aarow to current
                    for x in state.edges:                       
                        followes(state.edges[0],current)
    
    # Ask the NFA if it matches the string s
    return nfa.accept in current


print("Your regular expression is " + Query)
print("Your Test data is " + data)
print("\n")
print("Answer : " ,match(Query,data))#*
