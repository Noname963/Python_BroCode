# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created

name = "Bro"

def display_name():
    # name = "Code"
    print(name)

display_name()
print(name)

# L = Local
# E = Enclosing
# G = Global
# B = Built-in
