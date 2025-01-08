# Question 1

# Write a function that prints "Fizz" when the number is divisible by 3, "Buzz" when the number is divisible by 5
# and "FizzBuzz" when the number is divisible by both 3 and 5.
# If the number is not divisible by either 3 or 5, the function should return the number itself.


def fizz_buzz(number):
    """Returns Fizz if number is divisible by 3, Buzz if divisible by 5, FizzBuzz if divisible by both 3 and 5.
    If not divisible by either 3 or 5, returns the number itself.
    >>> fizz_buzz(3)
    'Fizz'
    >>> fizz_buzz(5)
    'Buzz'
    >>> fizz_buzz(15)
    'FizzBuzz'
    """
    return "FizzBuzz" if ((number % 3 == 0) and (number % 5 == 0)) else "Fizz" if number % 3 == 0 else "Buzz" if number % 5 == 0 else number 


# Question 2

# Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.


def sum_of_squares(numbers):
    """Returns the sum of the squares of all the numbers in a list.
    >>> sum_of_squares([1, 2, 3])
    14
    >>> sum_of_squares([2, 4, 6])
    56
    """
    sum = 0

    for num in numbers:
        sum += num**2
    return sum
   

# Question 3

# Write a function that counts the number of vowels in a string.


def count_vowels(string):
    """Returns the number of vowels in a string.
    >>> count_vowels("hello")
    2
    >>> count_vowels("aeiou")
    5
    """
    return string.count("a") + string.count("e") + string.count("i") + string.count("o") + string.count("u")


# Question 4

# Write a function that counts the number of repeated characters in a string.

def count_repeats(string):
    """Returns the number of repeated characters in a string.
    >>> count_repeats("hello")
    2
    >>> count_repeats("aeiou")
    0
    """

    for s in range(0, len(string)): 
        count = 1; 
        for t in range(s+1, len(string)):
            if(string[s] == string[t] and string[s] != ' '): 
                count = count + 1; 
        # setting the string t to 0 to avoid printing the characters already taken 
        string = string[:t] + '0' + string[t+1:]; 

        # If the count is greater than 1, the character is considered as duplicate 
        if(count > 1 and string[s] != '0'): 
            return count
        
    # No duplicate
    count = 0
    
    return count 


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
