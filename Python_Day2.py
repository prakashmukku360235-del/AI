#list

Student1="Anitha"
Student2="Prakash"
Student3="Dhakshith"
Student4="Nitya"

#print(Student1,"\n", Student2,"\n", Student3,"\n", Student4)

students=["Anitha","Prakash","Dhakshith","Nitya"]
#print(students)

students[0]="Prakash"
students[1]="Anitha"

#print(students)

Employee=["Anitha",37,5.7,True] 
#print(Employee[2])

#Dictionary

Employee1=[{"Name":"Anitha",
           "Age":37,
           "Height":5.7,
           "Married":True},
            {"Name":"Prakash",
             "Age":35,
            "Height":5.9,
            "Married":True},
            {"Name":"Nitya",
             "Age":3,
             "Height":1.2,
             "Married":False},
             {"Name":"Dhakshith",
             "Age":7,
             "Height":3.5,
             "Married":False}]
print(Employee1[1]["Height"])

Employee1=input("Enter the employee name: ")
