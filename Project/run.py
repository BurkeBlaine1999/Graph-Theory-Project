from match import *

sentinel = 1

while sentinel ==1:
    print("--- Regular expression to NFA (non-deterministic finite automota) ---\n")
    print("Would you like to ..")
    print("1)Make a conversion of a regex to  NFA")
    print("2)Project Info")
    print("3)Exit")
    Choice=int(input())
    if Choice == 1:
        Query=input("Enter your regular expresion:") 
        data=input("Enter your test data:") 
        print(match(Query,data))     
    elif Choice == 2:
        print("\nThompsons Construction is a method of transforming a\nregular expression into an equivalent nondeterministic finite automaton(NFA)")
        print("\nAuthor : Blaine Burke \nVersion 1.0 \nCreated for my 3rd year Graph theory Project\n")
    elif Choice == 3:
        sentinel =0
    else:
        print("Invalid Choice!")

