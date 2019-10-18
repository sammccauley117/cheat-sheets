# To print without a newline
import sys
sys.stdout.write('...')

# Built in
str(var) # Cast string
int(var) # Cast int
float(var) # Cast float
bin(var) # Cast binary
bool(var) # Cast bool
type(var) # Returns type of object
chr(i) # Ascii code to character
ord(c) # Character to ascii code
max(a) # Returns highest value of list a (number or highest alphabetically [z])
min(a) # Same as max but for minimum
range(start, stop, step) # Returns list [start, stop) STOP NOT INCLUDED. Can go in 'step' increments
sum(a) # Sum elements of an iterable

# Strings
a[2:5] # [2,5)
a.strip() # Removes all inital and trailing whitespace
a.lower() # makes string lowercase
a.upper() # Makes string uppercase
a.replace("H", "J") # Replaces H's with J's
a.split(",") # Returns ['Hello', ' World!'] (note: the ',' isn't included in either split)
a.isalnum() # Returns true if all characters in the string are alphanumeric
a.isalpha() # Returns true if all characters in the string are in the alphabet
a.isdecimal() # Returns true if all characters in the string are decimals
a.isdigit() # Returns true if all characters in the string are digits
a.join("...") # Concatenates "..." to the end of a
a.startswith("...") # Returns true if string starts with "..."
'x: {}  y: {}'.format(x,y) # String formatting

# Logic/Conditionals
x is y # Returns true if x and y are the same object
x in y # Returns true if x is somewhere in the sequence of y (iterable)
print("A") if a > b else print("B") # Shorthand if else
x = a if conditional else b # Shorthand if else
elif # else if
break # Leaves the most recent loop
continue # Stop the current iteration, and continue with the next

# Lists
x.append(y) # Adds y to the end of x list
x.insert(1, "yeet") # Value "yeet" is placed at index 1
x.remove("banana") # Removes the FIRST occurance of banana
x.pop() # Removes the last value
x.count("orange") # Returns number of occurences of "orange"
x.extend(y) # Concatenates elements of list y to x
x.index("apple") # Returns index of FIRST occurence of "apple"
x.reverse() # Reverses x
'...'.join(x) # 'apple...banana...orange'
l = [item/10 for item in items if item > x] # List comprehension

# Tuples (immutable lists)
t = ("apple", "banana", "cherry")

# Sets (A set is a collection which is unordered and unindexed--will be different every time)
s = {"apple", "banana", "cherry"} # Print will be different order every time
s.add("orange") # Adds "orange" to the set
s.remove("apple") # Removes "apple" (error if it does not exist)
s.discard("apple") # Removes "apple" (no error)
s.isdisjoint(t) # Returns true if s and t have NO intersection (independent)
s.issubset(t) # Returns true if s is a subset of t
s.issuperset(t) # Returns true if s is a superset of t
s.union(t) # Union of s and t
s.intersection(t) # Intersection of s and t

# Dictionaries
d = {
  "brand": "Ford",
  "model": "Bronco",
  "year": 1969 # Note how the mapped values don't have to be the same type
}
d["brand"] # Access value of "brand" key
for x in d: # loops through the KEYS, not values
for x in d.values(): # Loops through the values
for x, y in d.items(): # Loops thoguh both keys and values
d["color"] = "orange" # Adds item
d.pop("year") # Removes "year" pair

# Functions
def func():
def func(var = "default"): # Default value

# Lambda Functions
syntax: lambda arguments : expression
lambda a : a + 10 # Adds 10 to a
Example:
    def myfunc(n):
      return lambda a : a * n
    mydoubler = myfunc(2) # mydoubler = lambda a : a * 2
    print(mydoubler(11))  # Prints 22

# Filters
Example:
    def myFunc(x):
      if x < 18: return False
      return True
    ages = [5, 12, 17, 18, 24, 32]
    adults = filter(myFunc, ages)

# Classes
class Person:
  def __init__(self, name, age): # Initialization
    self.name = name
    self.age = age
  def hello(self):
    print "Hello my name is", self.name
me = Person('Sam', 20) # Create a Person object
me.age = 21 # Changes me.age to 21
me.hello() # Calls hello function
del me # Deletes object

# Try / Except
try :
    x = y / 0
except:
    print("Can't divide by zero")
