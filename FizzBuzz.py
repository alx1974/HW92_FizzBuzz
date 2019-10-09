#HW9.2 FizzBuzz

number = 0
i = 1
number = input("Select a number between 1 and 100: ")
print(number) #Obergrenze
print()
while i <= int(number):
    if (i % 3 == 0) and (i % 5 == 0): #durch 3 und 5 teilbar
        print("fizzbuzz")
    elif i % 3 == 0: # durch 3 teilbar
        print("fizz")
    elif i % 5 == 0: # durch 5 teilbar
        print("buzz")
    else:
        print(i)
    i = i + 1
