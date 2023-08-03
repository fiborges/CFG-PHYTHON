#loops

#For LOOP allows you to repeat a block of code multiple times

#Print Numbers from 1 to 5:
for number in range(5):
    print(number)
#Calculate the Sum of Numbers from 1 to 10
sum = 0
for num in range(1, 11):
    sum += num
print("Sum of numbers from 1 to 10:", sum)

#print all the letters one by one
for character in 'Banana':
    print(character)


#Print all the letters one by one withe < > around them ex: <b>
for character in 'Banana':
    print('<' + character + '>')

#print all the names in the list
for name in ['Mary', 'Ranjit', 'Fatima']:
    print(name)

#print the number of index in the list
for number in range(5): # 0,1,2,3,4
    print("executing FOR LOOP - run No {}".format(number + 1))

total = 0
print("*** This statement is OUTSIDE THE LOOP")
print("Before the loop executes, our TOTAL is equal to = ", total, '\n')
print("--------------------------------------------------------")

for number in range(3): # remember --> 0, 1, 2
    print("This is loop execution for digit: " + str(number) + " inside the loop \n")
    print("Updating total... (+ 1) \n")
    total = total + 1 # every time the loop executes, we add 1 to the total

print("--------------------------------------------------------")
print("***This statementWe is OUTSIDE the loop now")
print("The final TOTAL value is: " + str(total))

#Generate Multiplication Table for a Number

num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#Check if a Number is Prime
num = 17
is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


#Print a Triangle of Stars

for i in range(1, 6):
    print("*" * i)


#Draw a Square Using Turtle Graphics:

import turtle

t = turtle.Turtle()
for _ in range(4):
    t.forward(100)
    t.left(90)

turtle.done()
