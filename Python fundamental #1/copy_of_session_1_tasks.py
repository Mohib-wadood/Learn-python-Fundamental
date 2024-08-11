

# Write your code here
print('"Data " "science" "metorship" "Program" "started" "By" "Campusx "')
print("Data",end='-')
print("science",end='-')
print("metorship",end='-')
print("Program",end='-')
print("started",end='-')
print("By",end='-')
print("Campusx")

"""### Q2:- Write a program that will convert celsius value to fahrenheit."""

# Write your code here
C=int(input("Enter value of C: "))
F= (9%5*C)+32
print(F)

"""### Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax."""

from re import A
# Write your code here
a=int(input("Enter first Number :"))
b=int(input("Enter Second Number :"))
temp= a
a=b
b=a
print(b)
print(temp)

"""### Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input."""

# Write your code here
import math
def euclidean_distance(x1,y1,x2,y2):
  distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
  return distance
# Take values of the first coordinate
x1=float(input("enter value of x-coordinate of first piont: "))
y1=float(input("enter value of y-coordinate of first piont: "))

# Take the values of the second coordinate
x2=float(input("enter value of x-coordinate of second piont: "))
y2=float(input("enter value of y-coordinate of second piont: "))

# Calculating the distance
distance = euclidean_distance(x1, y1, x2, y2)

print(f"The Euclidean distance between the points ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}")

"""### Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.

"""

def extract_integer_from_string(r):
    # Initialize an empty string to store digits
    digits = ""

    # Iterate through each character in the string
    for char in r:
        # Check if the character is a digit
        if char.isdigit():
            digits += char

    # Convert the resulting string of digits to an integer
    if digits:
        return int(digits)
    else:
        return None  # In case there are no digits in the string

# Write your code here
p=int(input("Enter Principle : ")) # the initail amount of money that was deposite or loaned
r=str(input("Enter rate of charges: ")) # the percentage of principle charged as intrest per period

r=extract_integer_from_string(r)
print(r)




t=int(input("Enter time: ")) # the duration for which the money is deposite
simple_interest= p*r*t%100
print(simple_interest)

"""### Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

For example:
Input:
heads -> 4
legs -> 12
<br>
Output:
dogs -> 2
chicken -> 2




"""

# Write your code here
def find_dogs_and_chickens(total_heads ,toatal_legs):

 # calculate number of chicken (c) using the equation
 chickens = (4* total_heads - total_legs)//2
 # calculate number of dogs (d) using the equation
 dogs = total_heads-chickens
 if chickens < 0 or dogs < 0 or 4 * dogs + 2 * chickens != total_legs:
    return "No solution exist with the given total heads and total legs"
 return dogs , chickens

total_heads = int(input("Enter number of Heads :"))
total_legs = int(input("Enter number of legs :"))

result = find_dogs_and_chickens(total_heads , total_legs)

if isinstance(result, str):
    print(result)
else:
    dogs, chickens = result
    print(f"Number of dogs: {dogs}")
    print(f"Number of chickens: {chickens}")

"""### Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user."""

# Write your code here
def sum_of_squares(n):
  total_sum = 0

  for i in range(1,n+1):
    total_sum += i**2
  return total_sum

n = int(input("Enter a positve integer n: "))

result = sum_of_squares(n)

print(f"The sum of squares of the first {n} natural numbers is: {result}")

# Take Number from the user
n = int(input("Enter positive integer : "))

 # formula for the sum of the  square of n natural numbers
sum_natral = (n * ( n + 1 ) * (2 * n + 1)) // 6

# Display result
print(f'sum of the square of first {n} natural number is : {sum_natral  }')

"""### Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user."""

# Write your code here
a1 = int(input("Enter the first term of the squence "))
a2 = int(input("Enter the second term of the squence "))

d = a2 - a1

n = int(input("Enter the number of terms :"))

an = a1 + (n-1) * d


print(f"Nth term of the arithmetic series is :{an}")

"""56### Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user."""

# Write your code here
import math

def find_fraction_sum(a, b, c, d):
    # Find the numerator of the resulting fraction
    numerator = a * d + b * c

    # Find the denominator of the resulting fraction
    denominator = b * d

    # Simplify the fraction by finding the greatest common divisor (GCD)
    gcd = math.gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd

    return numerator, denominator

# Get inputs for the first fraction
a = int(input("Enter the numerator of the first fraction: "))
b = int(input("Enter the denominator of the first fraction: "))

# Get inputs for the second fraction
c = int(input("Enter the numerator of the second fraction: "))
d = int(input("Enter the denominator of the second fraction: "))

# Calculate the sum of the fractions
numerator, denominator = find_fraction_sum(a, b, c, d)

# Display the result
print(f"The sum of the fractions is: {numerator}/{denominator}")

# Get inputs for the first fraction
a = int(input("Enter the numerator of the first fraction: "))
b = int(input("Enter the denominator of the first fraction: "))

# Get inputs for the second fraction
c = int(input("Enter the numerator of the second fraction: "))
d = int(input("Enter the denominator of the second fraction: "))

 # Find the numerator of the resulting fraction
numerator = a * d + b * c
denominator = b * d

print(f"The sum of the fractions is: {numerator}/{denominator}")

"""### Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.



Input:<br>
Dimensions of the milk tank<br>
H = 20cm, L = 20cm, B = 20cm
<br><br>
Dimensions of the glass<br>
h = 3cm, r = 1cm
"""

# Write your code here
h = int(input("Enter hight of the tank :"))
l = int(input("Enter length of the tank :"))
b = int(input("Enter breadth of the tank :"))

area_tank = h * l * b

r = int(input("Radius of the glass :"))
gh = int(input("Hieght of the glass :"))
pi = float(input("Enter pi value :"))

area_glass = pi * r**2 * gh

glasses_obtained = area_tank % area_glass

print(f"The glasses obtain from tank is :{glasses_obtained}")

