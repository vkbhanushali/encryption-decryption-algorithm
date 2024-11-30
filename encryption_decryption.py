from ntpath import join

def encrypt(pt, key3):
    # Substitution cipher encryption
    encpt = ""
    for i in range(0, len(pt), 2):
        row1 = 0
        col1 = 0
        row2 = 0
        col2 = 0
        for j in range(5):
            for k in range(5):
                if TL[j][k] == pt[i]:
                    row1 = j
                    col2 = k
                    break
            if row1 != 0 and col2 != 0:
                break
        for j in range(5):
            for k in range(5):
                if BR[j][k] == pt[i + 1]:
                    row2 = j + 5
                    col1 = k + 5
                    break
            if row2 != 0 and col1 != 0:
                break
        encpt = encpt + agg[row1][col1] + agg[row2][col2]

    # Transposition cipher encryption
    fence = [[] for i in range(key3)]
    rail = 0
    var = 1

    for char in encpt:
        fence[rail].append(char)
        rail += var

        if rail == key3 - 1 or rail == 0:
            var = -var

    res = ''
    for i in fence:
        for j in i:
            res += j

    return res

def decrypt(encpt, key):
    # Transposition cipher decryption
    fence = [[] for i in range(key)]
    rail = 0
    var = 1

    for char in encpt:
        fence[rail].append(char)
        rail += var

        if rail == key - 1 or rail == 0:
            var = -var

    rFence = [[] for i in range(key)]

    i = 0
    l = len(encpt)
    encpt = list(encpt)
    for r in fence:
        for j in range(len(r)):
            rFence[i].append(encpt[0])
            encpt.remove(encpt[0])
        i += 1

    rail = 0
    var = 1
    r = ''
    for i in range(l):
        r += rFence[rail][0]
        rFence[rail].remove(rFence[rail][0])
        rail += var

        if rail == key - 1 or rail == 0:
            var = -var

    # Substitution cipher decryption
    decpt = ""
    for i in range(0, len(r), 2):
        row1 = 0
        col1 = 0
        row2 = 0
        col2 = 0
        for j in range(5):
            for k in range(5):
                if TR[j][k] == r[i]:
                    row1 = j
                    col2 = k + 5
                    break
            if row1 != 0 and col2 != 0:
                break
        for j in range(5):
            for k in range(5):
                if BL[j][k] == r[i + 1]:
                    row2 = j + 5
                    col1 = k
                    break
            if row2 != 0 and col1 != 0:
                break

        decpt = decpt + agg[row1][col1] + agg[row2][col2]

    return decpt

pt = input("Enter Plaintext : ")
if len(pt) % 2 != 0:  # Check for odd length
    pt += 'x'  # Add padding to make the length even

key1 = 'VROQGDKWZPMFSIEXCBHUYLNAT'
key2 = 'KOZCSEGXPMVDFLANIUWBQHRYT'
key3 = 3

TL = []
TR = [['a', 'b', 'c', 'd', 'e'],
      ['f', 'g', 'h', 'i', 'k'],
      ['l', 'm', 'n', 'o', 'p'],
      ['q', 'r', 's', 't', 'u'],
      ['v', 'w', 'x', 'y', 'z']]

BL = [['a', 'b', 'c', 'd', 'e'],
      ['f', 'g', 'h', 'i', 'k'],
      ['l', 'm', 'n', 'o', 'p'],
      ['q', 'r', 's', 't', 'u'],
      ['v', 'w', 'x', 'y', 'z']]

BR = []

alpha = [i for i in range(0, 26) if i + 65 != 74]
for i in range(5):
    L = []
    for j in range(5):
        ch = chr(alpha[i * 5 + j] + 65)
        L.append(ch)
    TL.append(L)
    BR.append(L)

K1 = list(key1)
K2 = list(key2)
n = -1
for i in range(25):
    n += 1
    n %= 5
    m = i // 5
    TR[m][n] = K1[i]
    BL[m][n] = K2[i]

seq = ''
for i in range(5):
    for j in range(10):
        if j > 4:
            k = j - 5
            seq = seq + str(TR[i][k])
        else:
            seq = seq + str(TL[i][j])

for i in range(5):
    for j in range(10):
        if j > 4:
            k = j - 5
            seq = seq + str(BR[i][k])
        else:
            seq = seq + str(BL[i][j])

SL = list(seq)
agg = []
for i in range(10):
    L = []
    for j in range(10):
        L.append(SL[i * 10 + j])
    agg.append(L)

encpt = encrypt(list(pt), key3)
print("Encrypted text: ", encpt)
decpt = decrypt(list(encpt), key3)
print("Decrypted text: ", decpt)