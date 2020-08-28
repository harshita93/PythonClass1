"""Little red bus : Fast tour of most of the Python.
At evry stop, we will do a quick anneccodote. No time to stop and linger beacuse
we want to see everything"""

print('My name is' , __name__)

print('The file is', __file__)
print(__doc__)


import collections
import collections as m
print(m.__name__) #information on the module
print(m.__doc__)


#Quoting characters
print('One')
print("Two")
print('''Three''')
print("""Four""")

print('Don\'t you forget about me')  #Backslash escape
print('''she said , "hello Raymond!"''')

print(r'Don\'t you forgot about me') #raw string
#ways to enter new line
print('Three\nblind\nmice\n')   #cooked string


#easyfacts
#default __name__ of the module is '__main__
#importing a module changes its __name__.


#import grand_tour

# if __name__ == '__main__':
#     print('i was run with default name')
# else:
#     print("i was imported")




###################










