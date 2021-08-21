# (2) Find the “digit product” for all 2­digit numbers [2 pts.]

# The digit product of a number n is the multiplicative product of all of its digits. For example, the
# digit product of the number 8724 is 8 * 7 * 2 * 4 = 448. Your task is to write a piece of code
# (save it as a2­2.py​) which can compute and print out the digit products of all 2­digit numbers.

    # ANSWE

i=int(input("Enter any  number:"))
prod=1
while (i>0):
    prod=prod*(i%10)
    i = i//10
print("product of digit:",prod)

