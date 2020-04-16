#Runner class , Call this to run the program
#Imports
from match import match 
from match import followes 
import argparse

#Allow for command line arguements
parser = argparse.ArgumentParser(description='Enter a regular expression and some test data!' , prog='Graph Theory Project')
parser.add_argument('-v','--version', action='version',version='%(prog)s 1.0')
parser.add_argument('-i','--info', help='Explains what thompsons construct is.', action='version',version='Thompsons Construction is a method of transforming a \n regular expression into an equivalent nondeterministic finite automaton(NFA)')
parser.add_argument('-e','--example',help='Returns an example input.',action='version',version='Try entering " python run.py -r a.b -d ab "')
parser.add_argument('-r','--regex',help='Enter a regular expression.')
parser.add_argument('-d','--data',help='Enter your test data for your regular expression.')
args=parser.parse_args()


#If no arguements are passed
if not any(vars(args).values()):  
    sentinel = 1

    while sentinel == 1:
        #while sentinel ==1:
        print("\n--- Regular expression to NFA (non-deterministic finite automota) ---\n")
        print("Would you like to ..")
        print("1)Make a conversion of a regex to  NFA")
        print("2)Project Info")
        print("3)Exit")

        Choice=int(input())

        if Choice == 1:
            regex=input("Enter your regular expresion:") 
            data=input("Enter your test data:") 
            isTrue = match(regex,data)

            if isTrue == True: 
                print("Your regular Expression " + regex + " when given the data " + data + " returns True!")
            elif isTrue == False:
                print("Your regular Expression " + regex + " when given the data " + data + " returns False!")   

        elif Choice == 2:
            print("\nThompsons Construction is a method of transforming a\nregular expression into an equivalent nondeterministic finite automaton(NFA)")
            print("\nAuthor : Blaine Burke \nVersion 1.0 \nCreated for my 3rd year Graph theory Project\n")
        elif Choice == 3:
            sentinel =0
        else:
            print("Invalid Choice!")

#If any arguements are passed
elif any(vars(args).values()):   
    isTrue = match(args.regex,args.data)
    if isTrue == True: 
        print("Your regular Expression " + args.regex + " when given the data " + args.data + " returns True!")
    elif isTrue == False:
        print("Your regular Expression " + args.regex + " when given the data " + args.data + " returns False!")   




