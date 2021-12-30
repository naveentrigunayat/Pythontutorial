#                                         Input and Output

Input - The data given to the computer is called input.
Output – The results returned by the computer are called output.



#                             Output Statements

print ( ) Function - The print() function is used to print the specified message to the output screen/device. The message can be a string, or any other object.

Syntax:- print(objects, sep=‘character’, end=‘character’, file=sys.stdout, flush=False)

sep - Separate the objects by given character. Character can be any string. Default is ‘ ’ or can write none.
end – It indicates ending character for the line. Default is ‘\n’ or can write none.
file - An object with a write method. Default is sys.stdout or can write none.
flush - A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False


print ( ) – This function is used to display a blank line.

print(“string”) -  When a string is passed to the function, the string is displayed as it is.
Ex:- 
print(“Welcome to Geeky Shows”)
print(‘Welcome to Geeky Shows’)
print(“Like”, “Share”, “Subscribe”)
print(10)

print(“Welcome”)
print(“to”)
print(“Geeky Shows”)


print(object) -  We can pass objects like list, tuples and dictionaries to display the elements of those objects.
Ex:- 
data = [10, 20, -50, 21.3, ‘Geekyshows’]
print(data)


print(“string” sep=‘’) – It separates string with given sep character. Character can be any string. Default is ‘ ’ or can write none.
Ex:- 
print(“Like”, “Share”, “Subscribe”, sep=‘’)
print(“Like”, “Share”, “Subscribe”, sep=‘***’)


print(“string” end=‘’) – When ending character is passed. It prints given character at the end. Default is ‘\n’ or can write none.
Ex:- 
print(“Welcome”, end=‘\n’)

print(“Welcome”, end=‘’)
print(“to”, end=‘’)
print(“GeekyShows”)

print(“Welcome”, end=‘\t’)
print(“to”, end=‘\t’)
print(“GeekyShows”)


print(variable list) – This is used to display the value of a variable or a list of variable.
Ex:- 
a = 10
print(a)
Output: 10

x = 20
y = 30
print(x, y)
Output: 20 30          <----- List of variable’s value in the output screen,   are separated by a space by default. we can change this by sep


print(x, y, sep=‘,’)
Output: 20, 30


print(“String”, variable list) – This is used to display the string along with variable.
Ex:- 
m = 40
print(“Value: ”, m)
Output: Value: 40

name = “Rahul”
age = 62
print(“My Name is ”, name, “and My age is”, age)
Output: My Name is Rahul and My age is 62


input( ) – This function is used to accept input from keyboard. 
This function will stop the program flow until the user gives an input and end the input with the return key. 
Whatever user gives as input, input function convert it into a string. If user enters an integer value still input() function convert it into a string. 
So if you need an integer you have to use type conversion. 
Syntax:- input([prompt])
prompt is a string or message, representing a default message before input. It is optional
Ex:- 
name = input( )
name = input(“Your Name: ”)
mobile = input(“Enter Your Mobile Number: ”)


Whatever user gives as input, input function convert it into a string. If user enters an integer value still input() function convert it into a string. 
So if you need an integer you have to use type conversion. 
Ex:- 
mobile = input(“Enter Your Mobile Number: ”)
mb = int(mobile)

mobile = int ( input (“Enter Your Mobile Number: ”) )
price = float ( input (“Total Price: ”) )
mobile = complex ( input (“Enter Complex Number: ”) )
