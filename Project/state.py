# 
class State:
    #All states have 0,1,2 edges leading from it
    edges = []  
    #Label for the aarows(None means epsilon)
    label = None
    
    #Constructor for the class
    def __init__(self,label=None,edges=None):
        self.edges = edges if edges else []
        self.label = label
 