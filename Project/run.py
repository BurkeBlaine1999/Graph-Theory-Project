from match import *

print("Welcome to my regular expressions to NFA (non-deterministic finite automota)")
print("1)Enter regular expression")

Query=input("Enter your regular expresion:") 
data=input("Enter your test data:") 

print(match(Query,data))

