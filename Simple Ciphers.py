def formatString(s):
    import string
    # Forces string to be lower, removes all white spaces, and puncuation for consistency
    s = "".join(s.split())
    s = s.lower()
    s = s.translate(str.maketrans('','', string.punctuation))
    return ''.join(s)    
 

def relativeFrequency(string):    
    # Takes the set from string and creates tuple of (letter, Relative Frequency)
    string = formatString(string)
    freqs = [(value, '%.5f' % (string.count(value)/ len(string))) for value in set(string)] 

    # Sorts the value in reverse order (Largest to smallest)
    freqs.sort(key = lambda x: x[1], reverse = True)
    
    return freqs


def shiftEncrypt(string, shift):
    #Encrypys text using Shift Cipher by the shift amount or the key
    string = formatString(string)
    result = ""    
    # Goes through the string and shifts the string by a set key
    for i in range(len(string)):        
        char = string[i]    
        # Converts letters to ASCII values and shifts it by specified amount
        result += chr((ord(char) + shift - 97) % 26 + 97)
        
    return result


def shiftDecrypt(string, shift):
    # Decrypt with known key / shift sequence
    string = formatString(string)
    result = ""    
    # Goes through the string and shifts the string by a set key
    for i in range(len(string)):        
        char = string[i]
        # Converts letters to ASCII values and shifts it by specified amount
        result += chr(((ord(char) - shift - 97) % 26 + 97))
    return result


def bruteForceShift(string):
    # Brute Force for solving the Shift Cipher incrmenting the shift amount by 1 each time
    string = formatString(string)
        
    for letter in range(0, 26):
        print('{:>2}: {}'.format(letter, shiftDecrypt(string, letter)))
        print()


def egcd(a, b):
    # Find the Extended Eculidian Distance for Modular Inverse
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

 
def modularInverse(a, m):
    # Finds Modular inverse and returns results
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        # If modular inverse does not exists return None
        print('Modular Inverse does not exists for', a)
        return None
    else:
        return x % m
    
    
def affineEncrypt(string, key):
    # Encrypts text using the Affine Cipher method
    string = formatString(string)
    results = ''
    for t in string:
        results += chr((key[0] * (ord(t) - 97) + key[1] ) % 26 + 97)
    return results
   
 
def affineDecrypt(string, key):
    # Decrypts Affine Encrypted text using modularInverse 
    string = formatString(string)
    results = ''
    for letter in string:
        results += chr((modularInverse(key[0], 26) * (ord(letter) - 97 - key[1])) % 26 + 97)
    return results


def generateKey(string, key):
    # Repeats the Key length until it matches the string length
    string = formatString(string)
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key += key[i % len(key)]
    return key
     
     
def encryptVigenere(string, key):
    # Eecrypts Vigenere text with the given key
    string = formatString(string)
    result = ""
    for i in range(len(string)):
        result += chr((ord(string[i]) + ord(key[i]) - 97) % 26 + 97)
                
    return result
     
     
def decryptVigenere(string, key):
    # Decrypts Vigenere text with the given key
    string = formatString(string)
    result = ""
    for i in range(len(string)):
        result += chr((ord(string[i]) - ord(key[i]) - 97) % 26 + 97)
        
    return result


if __name__ == '__main__':
    
    # For Shift Cipher
    # Affine key uses original Decrypted text provided
    original = 'ifweallunitewewillcausetheriverstostainthegreatwaterswiththeirblood'
    string = 'xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpitghlxiwiwtxgqadds'
    shiftKey = 15
    
    #****************************************************************************
    
    # For Vigenere Cipher
    string2 = 'Hellenism was the combination of Greek, Persian, and Egyptian cultures. During this remarkable time period, people were encouraged to pursue a formal education and produce many different kinds of art. New forms of math, science, and design made a great impact on society.'
    
    vigKeyword = 'cat'
    vigKeyword2 = 'dog'
        
    key = generateKey(string2, vigKeyword)
    key2 = generateKey(string2, vigKeyword2)
    vigEncryptedText = encryptVigenere(string2, key)
    vigEncryptedText2 = encryptVigenere(string2, key2)
    
    #****************************************************************************
    
    print('\nQuestion 1')
    x = relativeFrequency(string)
    print("Letter|Frequency")
    for i in x:
        print(i)
    print()
    
    #****************************************************************************
    
    print('*' * 50 , '\nQuestion 2')
    print('Brute Force to Find Key')
    bruteForceShift(string)    
    print('{}: {}'.format('shift key', shiftKey))
    print('{}: {}'.format('Original Text  ',original))
    print('{}: {}'.format('Shift Decrtpyed', shiftDecrypt(string, shiftKey)))
    print('{}: {}\n'.format('Shift Encrtpyed', shiftEncrypt(original, shiftKey)))
    print('Does Original match the Encrypted text after Decrypted text?: {}\n'.format(original == shiftDecrypt(string, shiftKey)))
    
    #****************************************************************************

    print('*' * 50, '\nQuestion 3')
    affinekey = [11, 20]
    a = affineEncrypt(original, affinekey)
    print('{}: {}'.format('Original Text   ',original))
    print('{}: {}'.format('Affine Encrypted', a))
    print('{}: {}\n'.format('Affine Decrpyted', affineDecrypt(a, affinekey)))
    print('Does Original match the Encrypted text after Decrypted text?: {}\n'.format(original == affineDecrypt(a, affinekey)))
    
    #****************************************************************************
    
    print('*' * 50, '\nQuestion 4')
    print('Keyword: {}'.format(vigKeyword))
    print('{}: {}'.format('Original Text',formatString(string2)))
    print('Encrypted: {}'.format(vigEncryptedText))
    print('Decrypted: {}'.format(decryptVigenere(vigEncryptedText, key)))
    print('Does Original match the Encrypted text after Decrypted text?: {}\n'.format(formatString(string2) == decryptVigenere(vigEncryptedText, key)))
    print()
    print('Keyword: {}'.format(vigKeyword2))
    print('Encrypted: {}'.format(vigEncryptedText2))
    print('Decrypted: {}'.format(decryptVigenere(vigEncryptedText2, key2)))
    print('Does Original match the Encrypted text after Decrypted text?: {}\n'.format(formatString(string2) == decryptVigenere(vigEncryptedText2, key2)))