from state import State

# Fragment

# Fragments are pieces of NFA that are broken up into seperate parts
# has 2 things in it
# 1 - the start state 
# 2- the accept state

class Fragment:
    #Start of the NFA fragment
    start = None
    #Accept state of NFA fragment
    accept = None
    #Constructor
    def __init__(self,start,accept):
        self.start = start
        self.accept = accept
        
      