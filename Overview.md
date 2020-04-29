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

<hr>

 ### Thompsons construction algorithm
 
Created by [ken Thompson](https://en.wikipedia.org/wiki/Ken_Thompson) ,Thompson's construction algorithm  is a method of transforming a regular expression into an equivalent nondeterministic finite automaton (NFA).As stated above , an automaton performs a range of functions according to a predetermined set of coded instructions. The language accepted by finite automata can be easily described by simple expressions called Regular Expressions. Regular expressions are used to match character combinations in strings.





