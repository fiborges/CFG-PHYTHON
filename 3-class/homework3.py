'''
Question 1
Create a program that tells you whether or not you need an umbrella when you leave the house.
The program should:
1. Ask you if it is raining using input()
2. If the input is 'y', it should output 'Take an umbrella'
3. If the input is 'n', it should output 'You don't need an umbrella'

'''

# Ask if it's raining
is_raining = input("Is it raining? (y/n): ")

# Check the input and provide a response
if is_raining.lower() == 'y':
    print("Take an umbrella")
elif is_raining.lower() == 'n':
    print("You don't need an umbrella")
else:
    print("Invalid input. Please enter 'y' for yes or 'n' for no.")


'''
Question 2
I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit. I've
written a program to check that I can afford the cost, but something doesn't seem right.
Have a look at my program and work out what I've done wrong
my_money = input('How much money do you have? ')
boat cost = 20 + 5
if my_money < boat_cost:
print('You can afford the boat hire')
else:
print('You cannot afford the board hire')
'''

my_money = float(input('How much money do you have? '))
boat_cost = 20 + 5
if my_money >= boat_cost:
    print('You can afford the boat hire')
else:
    print('You cannot afford the boat hire')



'''
Question 3
Your friend works for an antique book shop that sells books between 1800 and 1950 and wants to
quickly categorise books by the century and decade that they were written.
Write a program that takes a year (e.g. 1872) and outputs the century and decade (e.g. "Nineteenth
Century, Seventies")

'''

def get_century_name(year):
    if 1800 <= year <= 1899:
        century = "Nineteenth"
    elif 1900 <= year <= 1999:
        century = "Twentieth"
    else:
        century = "Unknown"

    return century

def get_decade_name(year):
    decade = (year % 100) // 10
    if decade == 0:
        decade_name = "Zeroes"
    elif decade == 1:
        decade_name = "Tens"
    elif decade == 2:
        decade_name = "Twenties"
    elif decade == 3:
        decade_name = "Thirties"
    elif decade == 4:
        decade_name = "Forties"
    elif decade == 5:
        decade_name = "Fifties"
    elif decade == 6:
        decade_name = "Sixties"
    elif decade == 7:
        decade_name = "Seventies"
    elif decade == 8:
        decade_name = "Eighties"
    elif decade == 9:
        decade_name = "Nineties"
    else:
        decade_name = "Unknown"

    return decade_name

year = int(input("Enter a year: "))
century_name = get_century_name(year)
decade_name = get_decade_name(year)

print("{} Century, {}".format(century_name, decade_name))

