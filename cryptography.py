import random
import sys


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
k = 5
mode = 26
alphabet_copy = alphabet.copy()
monoalphabetic = []
for i in range(26):
    r = random.choice(alphabet_copy)
    alphabet_copy.remove(r)
    monoalphabetic.append(r)

# رمزگذاری معکوس جمع
def Additive_Cipher_Encryption(word:str, k:int):
    encrypted = ''
    for i in word:
        if i in alphabet:
            p = alphabet.index(i)
            c = (p + k) % mode
            encrypted = encrypted + alphabet[c]
        else:
            pass
    return encrypted

# رمزگشایی معکوس جمع
def Additive_Cipher_Decryption(word:str, k:int):
    decrypted = ''
    for i in word:
        if i in alphabet:
            p = alphabet.index(i)
            c = (p - k) % mode
            decrypted = decrypted + alphabet[c]
        else:
            pass
    return decrypted

# رمزگذاری معکوس ضرب
def Multiplicative_Cipher_Encryption(word:str, k:int):
    encrypted = ''
    k_list = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    if k in k_list:
        for i in word:
            if i in alphabet:
                p = alphabet.index(i)
                c = (p * k) % mode
                encrypted = encrypted + alphabet[c]
            else:
                pass
    else:
        print('k should be in k_list = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]')
    return encrypted

# رمزگشایی معکوس ضرب
def Multiplicative_Cipher_Decryption(word:str, k:int):
    decrypted = ''
    k_list = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    k_reverse_list = [1, 9, 21, 15, 3, 19, 7, 23, 11, 5, 17, 25]
    if k in k_list:
        k = k_reverse_list[k_list.index(k)]
        for i in word:
            if i in alphabet:
                p = alphabet.index(i)
                c = (p * k) % mode
                decrypted = decrypted + alphabet[c]
            else:
                pass
    else:
        print('k should be in k_list = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]')
    return decrypted

# رمزگذاری تک الفبایی
def Monoalphabetic_Cipher_Encryption(word:str):
    encrypted = ''
    for i in word:
        if i in alphabet:
            p = alphabet.index(i)
            encrypted = encrypted + monoalphabetic[p]
        else:
            pass
    return encrypted

# رمزگشایی تک الفبایی
def Monoalphabetic_Cipher_Decryption(word:str):
    decrypted = ''
    for i in word:
        if i in monoalphabetic:
            p = monoalphabetic.index(i)
            decrypted = decrypted + alphabet[p]
        else:
            pass
    return decrypted

# رمزگذاری کلید خودکار
def Autokey_Cipher_Encryption(word:str,r=1):
    encrypted = ''
    ind = []
    keys = []
    for i in word:
        if i in alphabet:
            ind.append(alphabet.index(i))
    for i in range(len(ind)):
        keys.append(ind[i - r])
    j = 0
    for i in word:
        if i in alphabet:
            p = alphabet.index(i)
            c = (p + keys[j]) % mode
            encrypted = encrypted + alphabet[c]
            j += 1
        else:
            pass
    return encrypted,keys

# رمزگشایی کلید خودکار
def Autokey_Cipher_Decryption(word:str,keys:list,r=1):
    decrypted = ''
    ind = []
    for i in range(len(keys)):
        ind.append(keys[(i + r) % len(keys)])
    j = 0
    for i in word:
        if i in alphabet:
            p = alphabet.index(i)
            c = (p - keys[j]) % mode
            decrypted = decrypted + alphabet[c]
            j += 1
        else:
            pass
    return decrypted

def main():
    print('alphabet      :', alphabet)
    print(150 * '-')
    print('mono alphabet :', monoalphabetic)
    print(150 * '-')
    print('k =', k)
    print(150 * '-')
    print('mode =', mode)
    print(150 * '-')
    a = Additive_Cipher_Encryption('salam z', k)
    print('Additive Cipher Encryption :', a)
    print(150 * '-')
    b = Additive_Cipher_Decryption(a, k)
    print('Additive Cipher Decryption :',b)
    print(150 * '-')
    c = Multiplicative_Cipher_Encryption('salam z', k)
    print('Multiplicative Cipher Encryption :', c)
    print(150 * '-')
    d = Multiplicative_Cipher_Decryption(c, k)
    print('Multiplicative Cipher Decryption :', d)
    print(150 * '-')
    e = Monoalphabetic_Cipher_Encryption('salam z')
    print('Monoalphabetic Cipher Encryption :', e)
    print(150 * '-')
    f = Monoalphabetic_Cipher_Decryption(e)
    print('Monoalphabetic Cipher Decryption :', f)
    print(150 * '-')
    g,h = Autokey_Cipher_Encryption('salam z')
    print('Autokey Cipher Encryption :', g)
    print(150 * '-')
    i = Autokey_Cipher_Decryption(g,h)
    print('Autokey Cipher Decryption :', i)
    print(150 * '-')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
