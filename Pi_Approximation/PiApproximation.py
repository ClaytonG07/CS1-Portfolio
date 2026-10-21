#PiApproximation.py

"""This program will find the number of terms required to approximate pi within
an error tolerance."""


print("This program finds the number terms required to approximate pi within an error tolerance")
error = float(input("Input error tolerance"))
pi = 3.14159265358979
counter = 1
pi_approx = 0
running_error = error + 1
running_approx = 0

print("number of terms", "\t" ,"Pi Approximation")
while abs(running_error) > error:
    running_approx = 4 * ((-1) ** (counter + 1)) / ((2 * counter) - 1)
    pi_approx += running_approx
    running_error = pi_approx - pi
    print(counter, end = "\t\t\t\t\t")
    print(pi_approx)
    counter += 1
    
        
print(f"After {counter - 1} terms, pi is approximately {pi_approx}")
print(f"Our error is {abs(running_error)} which is less than or equal to {error}")