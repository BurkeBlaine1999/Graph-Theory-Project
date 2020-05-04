class State:  
    #Constructor for the class
    def __init__(self,label=None,edges=None):
        #All states have 0,1,2 edges leading from it
        self.edges = edges if edges else []
        #Label for the aarows(None means epsilon)
        self.label = label
 