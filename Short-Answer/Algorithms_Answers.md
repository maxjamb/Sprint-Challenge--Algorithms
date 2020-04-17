#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(1)

    The number of calculations remain the same no matter how large n gets

b) O(n)

    The number of calculations will increase in line with the input

c) O(n)

    The number of calcualtions will increase inline with the input, essentially returning 2 until it hits the base case of 0.

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

def throw_egg(n)
lower_than_floorf = []
floorf_or_higher = []

if max(lower_than_floorf) = (min(floorf_or_higher) - 1):
return min(min(floorf_or_higher)

if -1 egg:
floorf_or_higher = n
return throw_egg(n -1)

else:
lower_than_floorf = n
throw_egg(n +1)

Run through the above and then run a basecase method to stop the function where the two arrays meet. This is recursive with a liner run time, O(n)
