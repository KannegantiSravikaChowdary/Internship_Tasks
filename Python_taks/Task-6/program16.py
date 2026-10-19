# Caesar Cipher
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem

def caesarCipher(s, k):
    result = []
    k = k % 26  # Normalize shift to within alphabet range
    for ch in s:
        if ch.isalpha():
            # Handle uppercase separately
            if ch.isupper():
                shifted = chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
            else:
                shifted = chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
            result.append(shifted)
        else:
            # Non-alphabet characters remain unchanged
            result.append(ch)
    
    return "".join(result)
