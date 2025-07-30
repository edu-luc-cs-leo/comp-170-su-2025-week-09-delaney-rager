def factorial(n):
    """Computes recursively n! = 1 * 2 * ... * (n-1) * n
    """
    if n == 0:
        # Base case, 0! is by definition 1
        result = 1
    else:
        # Recursive case: n! = (n-1)! * n
        result = n * factorial(n-1)
    return result

def fibonacci(n):
    """Computes recursively the Fibonacci sequence
    F(n) = F(n-1) + F(n-2)
    for n > 2, with initial conditions F(1) = 1 and F(2) = 2
    """
    if n == 1 or n == 2:
        # Base case
        result = n
    else:
        # Recursive case
        result = fibonacci(n-1) + fibonacci(n-2)
    return result

# ITERATIVE VERSIONS OF ASSIGNMENT METHODS

def sum_of_digits_iterative(n):
    sum = 0
    while n > 1:
        # Obtain the last digit to add to sum. The last digit is always the remainder of
        # the integer division by base of the number system in use (here: 10).
        sum += n % 10 
        # Remove the last digit. This can be done by integer division of the number with
        # its number base (here: 10). For exampe 24 // 10 = 2 (and thus 4 is gone!)
        n //= 10
    # Done
    return sum + n

def count_occurrences_iterative(data_list, target):
    count = 0
    # Iterate over the input list
    for i in range(len(data_list)):
        # Check if current list item matches target value
        if data_list[i] == target:
            # If it does, increment the counter
            count += 1
    # Done
    return count


# WRITE YOUR CODE BELOW

#sum of digits 
def sum_of_digits(number: int)->int:            #function that inputs an integer number and returns an integer number
    if number < 10:                             #base case where there is only one digit in the input, so its answer is itself
        result = number
    else:
        result = number % 10 + sum_of_digits(number // 10)    #number % 10 gives the last digit in the current number while number // 10 divides the input number by ten without a decimal, removing the last digist
                                                              #the adding of the numbers gives us the sum
    return result
#testing sum of digits
print(sum_of_digits(4444))
print(sum_of_digits(1234))
print(sum_of_digits(4))

#count occurances 
def count_occurrences(list: list, target: int)->int:    #input is a list and an integer number and the output is an integer
    count = 0                                           #base case: if there is no list it sets the count to 0
    if list:                                                #making sure the list empty    
        if list[0] == target:                               #checks if the first element of the list is the same as the target number
            count += 1                                      #adds one to count if the first element is the target number
        count = count + count_occurrences(list[1:], target)     #runs the function again and adds to count
    return count
#testing count occurances 
print(count_occurrences([1,2,3,1,4,1],1))    
print(count_occurrences([],1))


#converting factorial to an iterative method 
def factorial_iterative(n:int)-> int:                   #input is an integer and the output is an integer
    result = 1                                          #our base case scenario where 0! = 1 or 1!=1
    if n > 1:                                           #checking if n is greater than one
        for i in range(2,n+1):                              # this for loop goes through each number up to n and multiplies them together exluding 1 and 0
            result = i * result
    return result

#testing factorial 
print(factorial_iterative(4))
print(factorial_iterative(0))
print(factorial_iterative(5))

#converting fibonacci to an iterative method
def fibonacci_iterative(n: int)->int:              #function input is an integer and the output is an integer
    result = 0                                     #if n = 0, return 0
    if n == 1:                                     #if n=1, return 1
        result = 1          
    n_minus_2 = 0                                  #initalizing our n-1 and n-2 variables before our loop
    n_minus_1 = 1    
    if n >= 2:                      
        for i in range (2, n + 1):                 #for loop between 2 and n
            result = n_minus_1 + n_minus_2         # adds the two previous numbers
            n_minus_2 = n_minus_1                  #n-2 becomes n-1
            n_minus_1 = result                     # n-1 becomes the result
    return result        


#testing fibonacci iterative
print(fibonacci_iterative(0))        
print(fibonacci_iterative(1))        
print(fibonacci_iterative(2))        
print(fibonacci_iterative(3))       
print(fibonacci_iterative(4))       
print(fibonacci_iterative(5))       

