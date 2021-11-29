num1 = 42 
num2 = 2.3
# these are variables
boolean = True
# this is a boolean
string = 'Hello World'
# this is a string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# this is an array
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# this is a list
fruit = ('blueberry', 'strawberry', 'banana')
# this is a multi-line string
print(type(fruit))
# this prints the fruit
print(pizza_toppings[1])
# this prints sausage
pizza_toppings.append('Mushrooms')
# this adds Mushrooms to the array
print(person['name'])
# this prints out the name in the variable person
person['name'] = 'George'
# this makes the current name equal to the new name which is George
person['eye_color'] = 'blue'
# adds the eyecolor blue
print(fruit[2])
# prints banana

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
# if num1 is greater than 45 it will print It's greater if not then print It's lower
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
''' if len(string) is less than 5, it will print 'It's a short word!'
else if len(string) is greater than 15 it will print 'It's a long word!'
else it will print 'Just right!'
'''
for x in range(5):
    print(x)
# if x < 5 
for x in range(2,5):
    print(x)
# if x = 2 - 5
for x in range(2,10,3):
    print(x)
# x = 2, 2 < 10, 3++
x = 0
while(x < 5):
    print(x)
    x += 1
# 0,1,2,3,4
pizza_toppings.pop()
# gets rid of last value in array
pizza_toppings.pop(1)
# gets rid of value 1 in array

print(person)
# prints values inside of person
person.pop('eye_color')
# gets rid of eye_color
print(person)
# prints new value without eye_color

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
# for every topping, if the topping is Pepperoni, continue the array, if it's Olives, then stop
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()
# for every number < 10 print Hello
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)
# for every number < 4 print Hello
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
# for num < 10 print Hello
print_hello_x_or_ten_times(4)
# for num < 4 print Hello


"""
Bonus section
"""

# print(num3) <--- prints num3
# num3 = 72 <--- num3 is set as 72
# fruit[0] = 'cranberry' <--- array value of 0 is cranberry
# print(person['favorite_team']) <--- prints persons favorite_team in list
# print(pizza_toppings[7]) <--- prints pizza_toppings array value of 7
#   print(boolean) <--- prints true or false
# fruit.append('raspberry') <--- adds raspberry as a value at the end of the array
# fruit.pop(1) <--- removes value 1 in the fruit array.