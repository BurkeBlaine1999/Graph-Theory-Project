#Imports
from match import match 
from match import followes 

#Local Variables
sentinel = 1

#While Loop for menu
while sentinel ==1:
    print("\n--- Regular expression to NFA (non-deterministic finite automota) ---\n")
    print("Would you like to ..")
    print("1)Make a conversion of a regex to  NFA")
    print("2)Project Info")
    print("3)Exit")
    Choice=int(input())
    if Choice == 1:
        Query=input("Enter your regular expresion:") 
        data=input("Enter your test data:") 
        isTrue = match(Query,data)

        if isTrue == True:
            print("Your regular Expression " + Query + " when given the data " + data + " returns True!")
        elif isTrue == True:
            print("Your regular Expression " + Query + " when given the data ' " + data + " ' returns False!")   
    
    elif Choice == 2:
        print("\nThompsons Construction is a method of transforming a\nregular expression into an equivalent nondeterministic finite automaton(NFA)")
        print("\nAuthor : Blaine Burke \nVersion 1.0 \nCreated for my 3rd year Graph theory Project\n")
    elif Choice == 3:
        sentinel =0
    else:
        print("Invalid Choice!")

