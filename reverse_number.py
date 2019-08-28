#
# A simple fun program that reverses the number 
# that is given as input.
# 
# Example: 
# Input		Output
#  345           543 
#  123           321 
#   67            76

n = int(input("Enter a number: "))

rev = 0
while(n > 0): 
   dig = n % 10
   rev = (rev * 10) + dig
   n = n // 10

print("Reverse of the number is: ", rev )

