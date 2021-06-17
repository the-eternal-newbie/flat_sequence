"""
Flatonacci secuence is a secuence which is result from the same given secuence 
plus the sum of the last 3 numbers of the secuence. 
The challenge is to create a flatonacci function that given a signature returns the first 
n elements - signature included of the so seeded sequence. So, if we are to 
start our Flatonacci sequence with [1, 1, 1] as a starting input (AKA signature) and n = 8,
we have this sequence:
[1, 1 ,1, 3, 5, 9, 17, 31]
Another example; if signature is the secuence [0, 0, 1] we should get some thing
like:
[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
- Signature will always contain 3 numbers 
- n will always be a non-negative number
- if n == 0, then return an empty list and be ready for anything else which is not
clearly specified ;)
Note. Please note that we are gonna test the funcion against a lot of different signatures and n's
"""


def flatonacci(signature: list, n: int):
    sequence = []
    """
    This conditional verifies some cases to provide safety to the function,
    (even if we know the stated scenarios):
        - n is bigger than 0 (it's a non-negative number)
        - signature is equal to 3 and contains only integers and/or float numbers
        - a second safety layer is added by wrapping all inside an exception block
    """
    try:
        if n < 0 or len(signature) != 3 or not all(isinstance(s, (int)) for s in signature):
            return sequence
        else:
            sequence += signature
            while (len(sequence) < n):
                sequence.append(sum(sequence[-3:]))
    except (NameError, RuntimeError, TypeError, ValueError) as error:
        return ['Something went wrong. Please verify the input data and try again.', error]
    return sequence
