# Short Programming Questions (8)
# (1) Find all “legendary” 3­digit numbers [2 pts.]

# A number n is “legendary” if its digits are arranged from left to right in strictly ascending order
# (that is, each successive digit is greater than the previous one). For example:
# The number 123 is a legendary number because 1 < 2 < 3.
# The number 354 is not legendary because even though 3 < 5, 5 > 4.
# The number 122 is not legendary because even though 1 < 2, 2 == 2.
# Your task is to write a piece of code (save it as a2­1.py​) which can compute a list of all 3­digit
# legendary numbers and print out the result.
                # ANSWER
a = int(input("inter the number"))
b = int(input("inter the number"))
c = int(input("inter the number"))
if b>a and c>b:
    print(a,b,c,"is legendary number")
else:
    print(a,b,c,"is not legendary number")