def shunt(infix):  # Could probably made more efficient
    infix = list(infix)[::-1]
    # Operator stack
    opers = []
    # Postfix regular expression
    postfix = []

    """Operator Precedence. (Dictionary) 
     --> Sets some operators to be more important than others
    """
    prec = {'*': 100,'+':95,'?':90, '.': 80, '|': 60, ')': 40, '(': 20}
   
    """Loop through the input one character at a time
    in order to get rid of the brackets
    """
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
            # Push any operators onto the operators stack that have higher Precedence to the output
            while opers and prec[c] < prec[opers [- 1]]:
                postfix.append(opers.pop())
            # Push C onto the operator Stack
            opers.append(c)

        elif c in ['(', ')','.','|','*','?','+']:
            # Push C onto the operator Stack
            opers.append(c)
        else:
            # Push out characters to the output
            postfix.append(c)

    # Pop all operators to the output
    while opers:
        postfix.append(opers.pop())

    # Convert output list to String
    return ''.join(postfix)
