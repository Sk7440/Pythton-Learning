#while performing concatination in python through input with numbers its act as 27 plus is 28 but the output is 271 
# to prevent this we use typecasting or conversion



# age= input("Enter your age")
# print(age +1)
# output
# Enter your age : 21
# Traceback (most recent call last):
#   File "C:\Users\cz\Desktop\Corvit Ai Course\Python Learning\Python fundamentals\Type Conversion\Typecasting.py", line 7, in <module>
#     print(age +1)
#           ~~~~^~
# TypeError: can only concatenate str (not "int") to str

# To prevent this 

# int(), float () type casting or type conversion
# this is type casting
age= int(input("Enter your age : "))   
#  implicit
print(age +1)
# type casting is perform by developer 
# type conversion is by default by python
# this is type conversion
#  explicit
print(2.5 +1)
