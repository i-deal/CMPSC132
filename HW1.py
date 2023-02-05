def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(25, 25)
        False
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
    """
    #- YOUR CODE STARTS HERE
    from math import sqrt

    height = (perimeter + sqrt((perimeter ** 2) - ( 16 * area))) / 4 # quadratic formula for the longest side
    length = area / height
    if height.is_integer() and length.is_integer(): # check if both sides are integers
        return(int(height))
    else:
        return False


def get_index(num, digit):
    """
        >>> get_index(1495, 5)
        1
        >>> get_index(1495, 1)
        4
        >>> get_index(1495423, 4)
        3
        >>> get_index(1495, 7)
        -1
    """
    #- YOUR CODE STARTS HERE
    index = 1
    while num > 0: # iterates through integer, compares the rightmost digit to the target each time
        if num % 10 == digit:
            return index
        num = num // 10
        index += 1
    return -1


def unique_largest(num):
    """
        >>> unique_largest(123132)
        False
        >>> unique_largest(7264578364)
        True
        >>> unique_largest(2)
        True
        >>> unique_largest(444444)
        False
    """
    #- YOUR CODE STARTS HERE
    num1=num
    largest=0
    count=0
    while num1 > 0: # find the largest digit
        if num1%10>largest:
            largest=num1%10
        num1=num1//10
    
    while num > 0: # check how many times the largest digit is repeated
        if num%10==largest:
            count+=1
        num=num//10
    
    if count>1:
        return False
    return True



def joined_list(n):
    """
        >>> joined_list(5) 
        [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
        >>> joined_list(-8) 
        [-8, -7, -6, -5, -4, -3, -2, -1, -1, -2, -3, -4, -5, -6, -7, -8]
    """
    #- YOUR CODE STARTS HERE
    lst=[]
    if n>1:
        for num in range(1,n+1): # insert the numbers leading up and down to n at the middle of the list
            lst.insert(len(lst)//2,num)
            lst.insert(len(lst)//2,num)
        return lst
    elif n<1:
        for num in range(n,0):
            lst.insert(len(lst)//2,num)
            lst.insert(len(lst)//2,num)
        return lst



def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    #- YOUR CODE STARTS HERE
    sequence=[num]
    while num > 1:
        if num%2==0:
            num=num//2
            sequence+=[num]
        else:
            num=(3*num)+1
            sequence+=[num]
    return sequence


def is_isomorphic(word1, word2):
    """
        >>> is_isomorphic("egg", "add")
        True
        >>> is_isomorphic ("foo", "car") 
        False
        >>> is_isomorphic ("badc", "baba") 
        False
    """
    #- YOUR CODE STARTS HERE
    dict={}
    for i in range(len(word1)): # for each unique letter in word1, check if it is possible to assign it to a unique letter in word2
        for key in dict:
            if word2[i]==dict[key] and key != word1[i]:
                return False
        dict[word1[i]]= word2[i]
    n=''
    for letter in word1: # check if word2 can be reacreated from remapping word1
        n+=dict[letter]
    if n==word2:
        return True
    return False


def translate(translation_file, msg):
    """
        >>> translate('bigtext.txt', 'c u in 5.')
        'see you in 5.'
        >>> translate('bigtext.txt', 'gr8, cu')
        'great, see you'
        >>> translate('bigtext.txt', 'b4 lunch, luv u!')
        'before lunch, love you!'
    """
    # Open file and read lines into one string all the way to the end of the file ayy abbreviations.txt
    with open(translation_file) as file:   
        contents = file.read()

    #- YOUR CODE STARTS HERE
    contents = contents.split('\n') # seperate text contents into a dictioniary for quick translation
    translate_dict={}
    for pair in contents:
        lst=[]
        lst=pair.split('=')
        translate_dict[lst[0]]=lst[1]

    msg=msg.split(" ")
    punct='.?!,;:'
    holder={}
    for i in range(len(msg)): # seperate words from any connected punctuations by using slicing to remove the punctuation character
        last=len(msg[i])-1
        if msg[i][last] in punct:
            temp=msg[i][last]
            holder[i]=temp
            msg[i]=msg[i][0:last:]
    
    count=1
    for i in holder: # re insert the punctuation marks at the original locations
        msg.insert(i+count,holder[i])
        count+=1
    
    temp_msg = ''
    for word in msg: # for each word check if it can be translated
        if word in translate_dict:
            temp_msg += ' ' + translate_dict[word]
        elif word in punct:
            temp_msg += word
        else:
            temp_msg += ' ' + word
    
    translated_msg = temp_msg.strip(' ')
    return translated_msg


def addToTrie(trie, word):
    """      
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> addToTrie(trie_dict, 'art')
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}}
        >>> addToTrie(trie_dict, 'moon') 
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}, 'm': {'o': {'o': {'n': {'word': True}}}}}
    """
    #- YOUR CODE STARTS HERE
    current = trie
    for letter in word: # iterate through the letters in word, if the letter is already in the trie, search the next dictionary
        if letter not in current:
            current[letter]={}
        current = current[letter]
    current['word']= True


def run_tests():
    import doctest

    # Run tests in all docstrings
    #doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace rectangle with the name of the function you want to test
    doctest.run_docstring_examples(addToTrie, globals(), name='HW1',verbose=True)   

if __name__ == "__main__":
    run_tests()

