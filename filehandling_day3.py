#file handling in python    
#file open
#Relative path : input.txt
#Actual/absolute  path : C:\Users\Admin\OneDrive\Documents\AI_Procject\input.txt
#file=open("Knowldge\kinput1.txt","r")

#read and store the file content

#content=file.read()

#close the file
#file.close()

#print(content)

def openfile():
    file_name=input("Enter the file name to open: ")
    with open(file_name,"r") as file:
        print("I am reading the file",file_name)
        content=file.read()  
    print(content)