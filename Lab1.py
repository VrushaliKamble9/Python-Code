#Write a program that asks the user to enter an integer n, and, using a for loop along with an appropriately selected range(), computes and prints out the sum of all integers from 3 to n. For example, if n = 10, your program must print 52. You can assume that users will enter valid inputs. There is no need to check for the input validity.
n = int(input("please enter number"))
sum=0
for i in range (3, n+1):
  sum +=i
print(sum)

#Repeat Exercise [1] but sum only the odd numbers. For example, if n = 10, your program must print 24.
n = int(input("please enter number"))
sum=0
for i in range (3, n+1):
  if i % 2 ==0:
   sum +=!
print(sum)
#Repeat Exercise [1] but sum only the multiples of 3. For example, if n = 10, your program must print 18.
n = int(input("please enter number"))
sum=0
for i in range (3, n+1):
  if i % 3 ==0:
   sum +=i
print(sum)

#Repeat Exercise [1], but use the Python’s built-in sum function to compute the relevant sums without using loops. For example, sum(range(2, 4)) evaluates to 5 (=2+3).
n = int(input("please enter number"))
tsum=sum(i for i in range(2, n+1))
print(tsum)

oddsum=sum(i for i in range(2, n+1) if i %2!=0)
print(oddsum)

divi3=sum(i for i in range(2, n+1) if i % 3==0)
print(divi3)

#Write a program that asks the user to enter an integer n and prints the countdown from n to 0 (including both 0 and n).
n = int(input("please enter number"))
for i in range (0, n+1):
  print(n)
  n=n-1
  

#Write a program that asks the user to enter an integer n, and prints n!. Recall that n! stands for the factorial of n, which is 1 if n = 0, and 1 × 2 × … × n if n > 0.
n = int(input("please enter number"))
factorial = 1
for i in range(1,n+1):
  factorial = i * factorial
print(factorial)

#Write a program that asks the user to enter an integer n, and prints n is positive if n > 0, n is negative if n < 0, and n is zero, in all other cases.
n = int(input("please enter number"))
if n > 0:
  print("number is positive")

elif n < 0 :
  print("number is negative") 

else:
  print("number is zero") 

n1 = input("please enter number")
if n1.isdigit():
    n = int(input("please enter number"))
    if n > 0:
      print("number is positive")

    elif n < 0 :
      print("number is negative") 

    else:
      print("number is zero") 
else:
   print("input is string")

a = int(input("please enter number"))
b = int(input("please enter number"))
secrete=5
if a>0 and b>0:
  print("number is positive")
elif a<0 and b<0:
  print("number is negative") 
elif a==0 or b==0:
  print("one number is 0") 
else:
  print("numbers have opposite signs")
if a==secrete or b== secrete:
  print("you also guessed my secret number!")
else:
  print("no luck this time")

n = int(input("please enter number"))
sum=0
i=1
while i <=n:
  i1= i**2
  sum= sum+i1
  i+=1
print(sum)


secrete = 5
guess= False

while not guess:
    guess = int(input("please enter number"))
    if guess== secrete:
      print("well done")
      guess = True
    else:
      guess = False

#Write a while loop that runs forever using True as the loop continuation condition, and use the break statement to exit the loop once the secret number is correctly guessed.
secrete = 5
guess= False

while True:
    guess = int(input("please enter number"))
    if guess== secrete:
      print("well done")
      guess = True
      break
