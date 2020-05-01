# <div align="center"> Graph Theory Project </div>

## <div align="center">Introduction</div>
When I came to approaching this project I had to watch several youtube videos , read through many pages on stackoverflow and rewatch several labs provided by my lecturerer. 

## <div align="center">The Problem statement</div>
 > <div align="center"> You must write a program in the Python programming language that can
 > build a non-deterministic finite automaton (NFA) from a regular expression </div>

This was the project statement provided to us by our lecturer [Ian McLoughlin](https://github.com/ianmcloughlin).
NFA stands for a **Nondeterministic finite automaton** . An automaton performs a range of functions according to a predetermined set
of coded instructions. The language accepted by finite automata can be easily described by simple expressions 
called Regular Expressions. Regular expressions are used to match character combinations in strings.

## <div align="center">Running the Code</div>
### Prerequisites
In order to run the code you are required to have [Python](https://www.python.org/) and a text editor. I used [Visual Studio Code](https://code.visualstudio.com/) as it is my prefered text editor.

### Launching the Application

When running the applicaion you must navigate to the 'project' directory and enter cmd. Once there you have two choices.

* Use the built in UI
  * Enter 'python run.py'.
  * Select your choice from the UI.
  
* Run the program using Argparse 
  * Enter 'python run.py' followed by your regular expression and data.
    for example "python run.py -r a.b -d ab" . -r being yor regular expression and -d being your sample data
  * The result will then be printed to the command prompt.
  
## <div align="center">Running the premade Tests</div>

<div align="center">------------------------------------TO BE COMPLETED------------------------------------</div>

 ## <div align="center">Algorithms Used</div>
   
 In order to do this project I used several different algorithms such as Thompsons construction algorithm and the shunting yard algorithm.
 
 ### Shunting yard algorithm
 The Shunting yard algorithm is a method for parsing mathematical expressions specified in infix notation.
 I used it so I could could produce a postfix notation from an infix notation.
 
 
<hr>

 ### Thompsons construction algorithm
 
Created by [ken Thompson](https://en.wikipedia.org/wiki/Ken_Thompson) ,Thompson's construction algorithm  is a method of transforming a regular expression into an equivalent nondeterministic finite automaton (NFA).As stated above , an automaton performs a range of functions according to a predetermined set of coded instructions. The language accepted by finite automata can be easily described by simple expressions called Regular Expressions. Regular expressions are used to match character combinations in strings.


 ## <div align="center">How it works</div>
 
Upon submitting your regular expression and data it is broken down and processed in order to determine if it is true or false.
I will explain how each class and function works to achieve this.

 #### <div align="center">Match.py</div>
 
When it comes to my match.py class it contains the followes and match function.

In the followes function it simply takes a state and adds it to a set and then it follows all the epsilon arrows.
   
> ```
>  def followes(state,current): #Follow e's
>     #Only do something when we havent already seen the state
>     if state not in current:       
>     #Put the state into current
>     current.add(state)
>     #ee weather state is labelled by e/epsilon
>     if state.label is None:
>     #Loop through the states pointed to by this state.
>     for x in state.edges:
>     #follow all of their epsilons too.
>     followes(x,current)
> ```

Below the followes function is the match function 


The match string works by returning true or false dependinf on if the regular expression fully matches the Data.

It first compiles the regular expression into a nfa using the
*compile* function in compiler.py.

> ```
> nfa = compile(regex)
> ```

We then use the followes function in order to follow all epsilon arrows

> ```
>    current = set() # Current set of states we are in
>    #add the first state and all of the states it points to and follow all epsilon aarows
>    followes(nfa.start,current)
> ```

The following code then proceeds to loop through the characters in 's' until it makes it to the end. It then returns if the regex and data match .


> ```
>  for c in s:
>     #keep track of where we were
>    previous = current
>   #Create a new empty set for states we are about to be in
>  current = set()
> #Loop through previous states
>for state in previous:
>   # Only follow aarows not labeled by e/epsilon
>  if state.label is not None:
>     #if the label of the state is equal to the character weve read:
>    if state.label == c:
>       #Add the state at the end of the aarow to current
>      for x in state.edges:                       
>         followes(state.edges[0],current)
>    
>   # Ask the NFA if it matches the string s
>  return nfa.accept in current
> ```


 #### <div align="center">compiler.py</div>
 
 In the compiler we change the regular expression into a postfix regular expression using *shunting.py* and create an empty array to keep track of all fragments fromt he postfix.
 
> ```
>   postfix = shunt(infix)#Changes regular expression to postfix regular expression
>   postfix = list(postfix)[::-1]#turning postfix into a list and reversing list
>   nfa_stack = []
> ```
 
in the below code we receive the start and accept states from *operators.py*.We then create a new fragment using the start and accept states.Add the new fragment to the stack and return.
 
> ``` 
>while postfix:
>      #pop a character from postfix
>     c = postfix.pop()
>
>       if c =='.':#And
>            start , accept = ConcatOperator(nfa_stack)   
>       elif c == '|':#Or
>            start , accept = OrOperator(nfa_stack)             
>       elif c == '*':# 0 or many
>            start , accept = KleeneyOperator(nfa_stack)            
>       elif c == '?': #1 OR 0
>            start , accept = QuestionOperator(nfa_stack)  
>       elif c == '+': #1 OR More
>            start , accept = PlusOperator(nfa_stack)  
>       else:
>          accept = State()
>         start = State(label=c,edges=[accept])
>        #create new instance of fragment to represent the new NFA
>          
>     newfrag = Fragment(start,accept) 
>     #push the new NFA to the stack
>     nfa_stack.append(newfrag) 
>      #the NFA stack should only have excactly 1 NFA on it (The answer)
>       
>  return nfa_stack.pop()  
> ```
 

 #### <div align="center">Shunting.py</div>

 In my code I created a list in order to append and pop items off and onto the stack.
 
> ```
>   infix = list(infix)[::-1]
>   # Operator stack
>   opers = []
>   # Postfix regular expression
>   postfix = []
> ```

I also had to assign each operator precedence or importance
> ```
>   prec = {'*': 100,'+':95,'?':90, '.': 80, '|': 60, ')': 40, '(': 20}
> ```


The code below would check to see if the character is a bracket or not. If an opening bracket is detected it is pushed to the operators stack and if a closing bracket is detected it searches for the opening bracket to get rid of it.

> ```
> while infix:
>      # Pop a character from the input
>       c = infix.pop()
>
>    if c == '(':
>         # Push and open to the opers stack
>         opers.append(c)
>    elif c == ')':
>        # Pop the operators stack until you find an open bracket
>         while opers[-1] != '(':
>              postfix.append(opers.pop())
>               # Get rid of the '('
>         opers.pop()
> ```

If 'c' is not a bracket we then check to see if its in the precendence list or 'prec'. If it is , it's added to the operators stack and if it is not it's added to the chraracter output.

>```
>elif c in prec:
>            # Push any operators onto the operators stack that have higher Precedence to the output
>            while opers and prec[c] < prec[opers [- 1]]:
>                postfix.append(opers.pop())
>            # Push C onto the operator Stack
>            opers.append(c)
>
>       elif c in ['(', ')','.','|','*','?','+']:
>           # Push C onto the operator Stack
>          opers.append(c)
>       else:
>          # Push out characters to the output
>          postfix.append(c)
>```

We then pop all the operators into the outputand return the postfix.

>```
>   # Pop all operators to the output
>   while opers:
>       postfix.append(opers.pop())
>
>    # Convert output list to String
>   return ''.join(postfix)
>```


#### <div align="center">Operators.py</div>

In *operators.py* there are several different functions that are called upon in the compiler. These functions are used if a character is equal to any of the operators given such as the kleene star or the '.' operator. 

For example the Keleene star works by creating new start and accept states and then points their edges.
Fore example ,  the start state we point the edges toward the recently popped off fragment and give it a new accept state.

>```
>def KleeneOperator(nfa_stack):
>   #pop 1 fragment off the stack 
>  frag = nfa_stack.pop()
> #create new start and accept states
>accept=State()
>    start=State(edges=[frag.start,accept]) # points at start state of fragment just popped and new accept state
>   #point the arrows
>  frag.accept.edges = (frag.start,accept) # old accept state points at the old start state and the new accept state
> #create new instance of fragment to represent the new NFA
>
>   return(start,accept) 
>```

#### <div align="center">State.py</div>

In state.py we simply just create a new state to be used.

>```
>class State:
>   #All states have 0,1,2 edges leading from it
>  edges = []  
> #Label for the aarows(None means epsilon)
>    label = None
>   
>  #Constructor for the class
> def __init__(self,label=None,edges=None):
>    self.edges = edges if edges else []
>   self.label = label
>```

#### <div align="center">Fragment.py</div>

In Fragment.py we simply just create a new fragment from the given start and accept states.

>```
>class Fragment:
>   #Start of the NFA fragment
>   start = None
>  #Accept state of NFA fragment
> accept = None
>#Constructor
>def __init__(self,start,accept):
>   self.start = start
>  self.accept = accept
>```     

## <div align="center">References</div>

* [Ian McLoughlin](https://github.com/ianmcloughlin) - Provided tutorial Videos to follow , lecture notes and more to help guide me.
* [Geeks for geeks](https://www.geeksforgeeks.org/) - Helped with debugging
* [Stack Overflow](https://stackoverflow.com/) - Helped with figuring out how to do some operators.
* [Barry Brown](https://www.youtube.com/watch?v=RYNN-tb9WxI&t=110s) - Youtube video explaining regex to NFA which helped me understand the topic more
* [Made by Evan](http://madebyevan.com/fsm/) - Provided a Finite State Machine Designer to draw my automaton




