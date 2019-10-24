  #Sign your name: Rowdy Alexander

'''
#  1. Make the following program work.
#    '''
print("This program takes three numbers and returns the sum.")
total = 0
for i in range(3):
    UserInput=int(input("Enter a number: "))
    total+=UserInput
print("The total is:",total)



'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(2,101):
    print(i)



'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
i=10
while i>=0:
    print(i)
    i-=1
print("blast off")





'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
i=random.randint(1,10)
print(i)





'''
  5. Write a Python program that will:

     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.

'''
h=0
k=0
i=0
for i in range(7):
    v=int(input("give me a number:"))
    i+=v
    if i<0:
        k+=1
    elif i>0:
        h+=1

print("the Total of your Numbers is:",i)
print("the number of postive numbers in your set is:",h)
print("the number of negative numbers in your set is:",k)
