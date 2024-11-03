import math
def is_prime(n):
        # edge case handling (if n is less than 2)
    if n < 2:
        return False  # Numbers less than 2 are not prime
        
    for divisor in range(2, int(math.sqrt(n)) + 1): # go up to sqrt (n)
        if n % divisor == 0: # if n is divisible by divisor. the looping continues so long a divisor is not found
            return False # n is not prime
            break # exit loop
    else: 
        return True # n is prime. 
    

def count_primes(k,m):
        """
    Counts the number of prime numbers within a specified range [k, m].

    Parameters:
        k (int): The starting integer of the range.
        m (int): The ending integer of the range.

    Returns:
        int: The count of prime numbers within the range [k, m].
        
    Example:
        >>> count_primes(1, 10)
        4  # Prime numbers in range: 2, 3, 5, 7
    """
    counter = 00
    for n in range(k,m+1): # Loop through each number in the range
        if n < 2:  # Skip numbers less than 2, as they are not prime
            continue
             
         # Check if the current number n is prime     
        is_prime = True #flag variable which will be set to false if divisor is found
        for divisor in range(2, int(math.sqrt(n)) + 1): # go up to sqrt (n)
            if n % divisor == 0: # if n is divisible by divisor. the looping continues so long a divisor is not found
              is_prime = False
              break # exit loop
                
        else: 
            counter += 1 # n is prime. 
    return counter

is_prime(313)

count_primes(100,151)