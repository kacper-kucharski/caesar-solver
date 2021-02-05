import english_quadgrams

VALID_LETTERS = "abcdefghijklmnopqrstuvwxyz"

VALID_LETTERS_LIST = []

for c in VALID_LETTERS:
    VALID_LETTERS_LIST.append(c)

def encrypt_caesar(plaintext, shift):
    s = ""
    for i in range(len(plaintext)):
        caps = False
        if (plaintext[i] != " "):
            caps = not plaintext[i].islower() 
            char = plaintext[i].lower()           
            indx = "" 
            try:
                indx = VALID_LETTERS_LIST.index(char)
            except:
                s += plaintext[i]
            if (indx != ""):
                if (indx + shift >= len(VALID_LETTERS_LIST)):
                    s += VALID_LETTERS_LIST[indx + shift - len(VALID_LETTERS_LIST)] if not caps else VALID_LETTERS_LIST[indx + shift - len(VALID_LETTERS_LIST)].upper()
                else:
                    s += VALID_LETTERS_LIST[indx + shift] if not caps else VALID_LETTERS_LIST[indx + shift].upper()
        else:
            s += " "
    return s

def decrypt_caesar(ciphertext, shift):
    s = ""
    for i in range(len(ciphertext)):
        caps = False
        if (ciphertext[i] != " "):
            caps = not ciphertext[i].islower()
            char = ciphertext[i].lower()
            indx = ""
            try:
                indx = VALID_LETTERS_LIST.index(char)
            except:
                s += ciphertext[i]
            if (indx != ""):
                if (indx - shift < 0):
                    s += VALID_LETTERS_LIST[indx - shift + len(VALID_LETTERS_LIST)] if not caps else VALID_LETTERS_LIST[indx - shift + len(VALID_LETTERS_LIST)].upper()
                else:
                    s += VALID_LETTERS_LIST[indx - shift] if not caps else VALID_LETTERS_LIST[indx - shift].upper()
        else:
            s += " "
    return s

def quadgram_fitness(text):
    quadgrams = []
    valueOfQuadgrams = 0
    text = text.lower()
    for char in text:
            try:
                VALID_LETTERS_LIST.index(char)
            except:
                index = text.find(char)
                text = text[0 : index : ] + text[index + 1 : :]
    for i in range(0, len(text)-3):
        quadgrams.append(text[i:i+4])
    for q in quadgrams:
        try:
            valueOfQuadgrams += english_quadgrams.quadgram_score[q]
        except:
            valueOfQuadgrams += 23
    return valueOfQuadgrams

def solve_caesar(ciphertext):
    bestResult = ["", 999]
    for i in range(0, len(VALID_LETTERS_LIST)):
        text = decrypt_caesar(ciphertext, i)
        val = quadgram_fitness(text)
        if (val < bestResult[1]):
            bestResult[0] = text
            bestResult[1] = val
    return bestResult[0]
