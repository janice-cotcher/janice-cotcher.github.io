# Program to add natural numbers up to
# sum = 1+2+3+...+n

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1

# print the sum
print("The sum is " + str(sum))