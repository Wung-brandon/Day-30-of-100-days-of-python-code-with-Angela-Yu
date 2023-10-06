#The 4 main keywords when it comes to Error handling and catching exceptions
#TRY, EXCEPT, ELSE and FINALLY

#FileNotFound error
#with open("data.tex") as f:
 #   f.read()
try: 
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("A New File")
#multiple except block of code
except KeyError as error_message:
    print(f"the key {error_message} does not exist")
#if the file does not exist, the else block will never be triggered or executed
else:
    content = file.read()
    print(content)
#the finally block will always be executed no matter what happens
finally:
    #file.close()
    #print("The file is closed")
    #raising our own exceptions
    raise TypeError("this is an error i made up")
    
#KeyError
#a_dictionary = {"key": "value"}
#value = a_dictionary["non-existent value"]

#IndexError
#fruit_list = ["apple", "orange", "mango"]
#fruit = fruit_list[3]

#TypeError
#text = "abc"
#print(text + 5)

#NameError
#name = "berry"
#print(namee)