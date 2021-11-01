# Don't delete me
print(5+5, "hey")
age = 26
print(age+10)
val = 10/5+3*3
print(val)
val + ((10/5) + (3*3))
print (val)
"""This is a knockoff
multiline comment
"""
# this
# also
# works

msg=("Comment")
print(msg)


# legal variable names
age = 26 #give the variable that means something, age = someone's age, etc.
age1 = 1 #yes
age_2 = 2 #underscores are good
#age-3 = 3 not good, don't use "-"
#4age=4 don't start with a number
Age = 6 #works --> not good though. lowercase for variables
age_of_user = 7 #this also works
#return = 5 return is a keyword, not a variable

# operators
import math

result= 10//3

print(result)

# / --> float division
# // --> integer division (math.floor)

#modulus operator
#gives the remainder of some division
10/3
pizza = 10
people = 3
print(10%3) #or
print("leftover", pizza % people)

number = 345345
limit = 10
print(number % limit)

#raising numbers to a power
import math
result = math.pow(3, 5)
print(3 ** 3)
print(result)

#01 numbers
age = 25
print(age)

#this is a comment

age1 = 1
age_2 = 2
#invalid name -> age-3 = 3
#invalid name -> 4age = 4
Age = 6 #not recommended
age_of_user = 7 #recommend underscores for multiple words based on this guide:
#https://www.python.org/dev/peps/pep-0008/#function-and-variable-names

#return = 5 --> Cannot assign to keywords
#https://docs.python.org/3/reference/lexical_analysis.html#keywords

########## OPERATORS ##########
result = 20 / 3 #6.6666....
print(result) 

print("Here is a floor version (crop decimal):", 20 // 3) #6

result = 5**2 #raising a number to a power (5^)
print(result)

#You can use round instead. 
print(round(20/3), 0)

print(result / age) #can use variables in place of literals. This will not change variable values

#guess the output:
print(20 / 3 + 1)

#think of it like this because of operator precedence:
print((20 / 3) + 1)

#You can, however, force certain operations to happen first with ()
print(20 / (3 + 1))

######### MODULUS AND POWER ############

#5 * 5 * 5 * 5* 5
print(5**5)

#The remainder of 78 / 11 is 1.
print(78 % 11)

#02 strings
msg = "Hey"
print(msg)
msg1 = "You're cute"
print(msg1)

msg2 = "She said \"eww\""
print(msg2)

print(msg, msg1, msg2)

#if you're expecting 1 argument --> concatenation
full_message = msg + "..." + msg2
print(full_message)

print("Hey" "there")

msg = ("this is a long string...."
"continued")

print(msg)
