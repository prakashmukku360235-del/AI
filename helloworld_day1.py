# intro to pythonpython
#print("Hello python World")

text1="Hello Python World"
#print(text1)

#t1="enter first name"
#t2="enter last name"
#t3=t1+" "+t2
#print(t3)

#fname=input("enter first name")
#lname=input("enter last name")

n1=8
n2=7
n3=n1+n2
#print(n3)

#functions
t1=input("enter first name: ")
t2=input("enter last name: ")
session= int(input("enter how many session : "))
def calculatecost(session):
    cost=99
    trainingcost=session*cost
    return trainingcost

def fullname(t1,t2):
    output= t1+" "+t2
    return(output)

result=calculatecost(session)

print(result)
result2=fullname(t1,t2)
print(result2)
