#raising exceptions

""" height = float(input("Height:"))
weight = int(input("Weight:"))

if height > 3:
    raise ValueError("Human height must not be greater than 3")

bmi = round(weight / height ** 2, 3)
print("BMI: ", bmi) """


fruits = ["pear", "mango", "orange"]
#print(len(fruits))

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("fruit pie")
    else: 
        print(fruit + " pie")
    
make_pie(2)