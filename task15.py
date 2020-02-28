# Write the code, which will print numbers from 0 till your age. And if your age
# is odd, will be printed all odd numbers till your age, if even all even numbers.

age = int(input("Enter your age: "))
for num in range(1, age+1):
     if num % 2 == 0 and age % 2 == 0:
         print(num)
     elif num % 2 != 0 and age % 2 != 0:
         print(num)




