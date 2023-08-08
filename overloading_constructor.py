class student:
    def __init__(self, name):
        self.name = name

    def __init__(self, name, email):
        self.name = name
        self.email = email

# This line will generate an error
# st = student("rahul")

# This line will call the second constructor
st = student("rahul", "rahul@gmail.com")
print("Name: ", st.name)
print("Email id: ", st.email)


str = "Rohan"
str2 = "SUMIT"
# Calling function
str2 = str.join(str2)
# Displaying result
print(str2)

Q = "JavaTpoint, Python Interview Questions!"
print(Q[2:25:2])

list_1 = ["A", "B", "C"]
s_1 = "Javatpoint"
# creating enumerate objects
object_1 = enumerate(list_1)
object_2 = enumerate(s_1)

print("Return type:", type(object_1))
print(list(enumerate(list_1)))
print(list(enumerate(s_1)))

#Converting list of tuples to dictionary by using dict() constructor
color=[('red',1),('blue',2),('green',3)]
d=dict(color)
print (d)#Output:{'red': 1, 'blue': 2, 'green': 3}




class A:
    def func1(self):
        print('Function 1 from class A')

    def func2(self):
        print('Function 2 from class A')

class B(A):
    def func1(self):
        print('Modified feature 1 from class A by class B')

    def func2(self):
        print('Function 2 from class B')

obj = B()
obj.func1()
obj1 = A()
obj1.func1()

names = ["Johny", "Lenny", "Jimmy", "Timmy"]

# reverse the order of items in names
names.reverse()

# print contents of names to the console
print(names)

# output
# ['Timmy', 'Jimmy', 'Lenny', 'Johny']
my_numbers = [1, 2, 3, 4, 5]

my_numbers_reversed = reversed(my_numbers)

# print original list
print(my_numbers)
print(list(my_numbers_reversed))
# reversing original list
my_numbers_reversed = my_numbers[::-1]
print(my_numbers_reversed)
# check the data type of my_numbers_reversed using the type() function
print(my_numbers_reversed)
print(type(my_numbers_reversed))
for number in reversed(my_numbers):
  print(number)

# input list
lst = [10, 11, 12, 13, 14, 15]
# the above input can also be given as
# lst=list(map(int,input().split()))
l = []  # empty list

# iterate to reverse the list
for i in lst:
    # reversing the list
    l.insert(0, i)
# printing result
print(l)

tup = (1,2,3,4)
reversed_tup = tup[::-1]
print(reversed_tup)


# Reversing a list using reversed()
def Reverse(tuples):
    new_tup = ()
    for k in reversed(tuples):
        new_tup = new_tup + (k,)
    print(new_tup)


# Driver Code
tuples = (10, 11, 12, 13, 14, 15)
Reverse(tuples)

# Code 1:

# Given number list
numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Empty list
ansList = []

# Iterate through each number
# form the list
for num in numberList:

    # 0 and 1 is not a
    # prime number
    # so skip this number
    if num == 0 or num == 1:
        continue

    # loop from 2 to half of the
    # given number
    for i in range(2, num // 2 + 1):

        # If number is divisible by any
        # number (i) then it is not
        # a prime number
        if num % i == 0:
            break

    # If not divisible then it is
    # a prime number
    else:

        # if number is prime
        # then append to the list
        ansList.append(num)

# If list is non-empty then
# print th elements
if len(ansList):

    print("Prime Number : ", end="-> ")

    # printing the prime number
    # from the ansList
    for ans in ansList:
        print(ans, end="\n")

else:
    print("No any number from the given list is Prime")



# Program to check if a number is prime or not

num1 = 29

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num1 == 1:
    print(num1, "is not a prime number")
elif num1 > 1:
    # check for factors
    for i in range(2, num1):
        if (num1 % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num1, "is not a prime number")
    else:
        print(num1, "is a prime number")