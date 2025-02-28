# lambada function = function written in 1 line using lambada keyword
#                    accepts any number of arguments, but only has one expression
#                    (think of its as a shortcut)
#                    (useful if needed for a short period of time, throw-away)
# lambada parameters:expression



double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name +" "+ last_name
age_check = lambda age: True if age >= 18 else False


print(double(5))
print(multiply(5,6))
print(add(5,6,7))
print(full_name("Bro", "Code"))
print(age_check(18))

