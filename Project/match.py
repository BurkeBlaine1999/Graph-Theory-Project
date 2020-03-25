from state import state
from compiler import compile

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
    #this funciton will return true if and only if the regular expresion regex
    # fully matches the string s. It returns false otherwise

    #Compile the regular expression into an nfa
    nfa = compile(regex)
    
    #Try to match the regular expression to the string s
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

print(match("a.b|b*","bbbbbb"))