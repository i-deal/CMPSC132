# LAB1
# REMINDER: The work in this assignment must be your own original work and must be completed alone

def intersection(d1, d2):
    """
        >>> intersection({'a':5, 'b':7, 'd':5},{'d':5, 'a':5, 'b':9, 'c':12}) 
        {'a': 5, 'd': 5}
        >>> intersection({'a':5, 'b':7, 'd':5},{'d':8, 'a':51, 'b':9, 'c':12}) 
        {}
        >>> dict_one = {'a':5, 'b':7, 'd':5, 'c':'32', 'art':35.6}
        >>> dict_two = {'d':8, 'a':51, 'b':9, 'c':'32'}
        >>> intersection(dict_one, dict_two) 
        {'c': '32'}
        >>> dict_one
        {'a': 5, 'b': 7, 'd': 5, 'c': '32', 'art': 35.6}
        >>> dict_two
        {'d': 8, 'a': 51, 'b': 9, 'c': '32'}
    """
    intersect = {}

    for key in d1: # for each key in d1 check if d2 has the same key, if it does, check if it has the same value paired with it
        if key not in d2:
            pass
        elif d1[key]==d2[key]:
            intersect[key] = d1[key]

    return intersect

def frequency(d):
    """
        >>> frequency({'a':2, 'b': 2, 'c':1, 'd':1, 'e': 5, 'f': 1}) 
        1
        >>> frequency({'a':2, 'b': 2, 'c':1, 'd':1})                 
        2
        >>> frequency({'a':2, 'b': 2, 'c':1, 'd':1, 'h': 2, 't': 6, 'rr': 6, 'rws':6})   
        2
        >>> frequency({'a':2, 'b': 2, 'c':1, 'd':1, 'h': 2, 't': 6, 'rr': 6, 'rws':6, 'ret': 6, 'z': 5}) 
        6
    """
    # - YOUR CODE STARTS HERE -
    d_repeats={}
    largest = 0
    most_repeated = ''

    for key in d: # for each value in d, add it as a key in d_repeats with the count of its frequency as its value
        count = 0
        temp = d[key]
        for key2 in d:
            temp2 = d[key2]
            if temp2 == temp:
                count += 1
                d_repeats[temp] = count
    
    for key in d_repeats: # find the key with the largest value
        temp = d_repeats[key]
        if temp > largest:
            most_repeated = key
            largest = temp

    return most_repeated

def invert(d):
    """
        >>> invert({'one':1, 'two':2,  'three':3, 'four':4})
        {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
        >>> invert({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3, 'un':1})
        {3: 'three'}
        >>> invert({'123-456-78':'Sara', '987-12-585':'Alex', '258715':'sara', '00000':'Alex'}) 
        {'Sara': '123-456-78', 'sara': '258715'}
    """
    # - YOUR CODE STARTS HERE -
    inverted = {}
    duplicates = []

    for key in d: # for each key in d, save its value and check for duplicates
        temp = d[key]
        if temp in inverted and temp not in duplicates: # if a duplicate exists add the value to duplicates
            duplicates += [temp]
        else: # if a duplicate does not exist add the inverted key/value pair to inverted
            inverted[temp] = key
    
    for key in duplicates:
        del inverted[key]
    
    return inverted

def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=False)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace intersection with the name of the function you want to test
    #doctest.run_docstring_examples(intersection, globals(), name='LAB1',verbose=True)   

if __name__ == "__main__":
    run_tests()

