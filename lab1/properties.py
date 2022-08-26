#Функція яка провіряє матрицю на рефлективність
def reflexive(mat):
    #print(mat)
    #print("matrix")
    for id, row in enumerate(mat):
        #print(id, row, row[id])
        if row[id] == 0:
            return False

    return True
# Функція яка провіряє матрицю на іррефлексивність index  не підходить
def irreflexive(mat):
    #print(mat)
    #print("matrix")

    for id, row in enumerate(mat):
        #print(id, row, row[id])
        if row[id] == 1:
            return False

    return True


# Функція яка провіряє матрицю на симетричність оптимальна кількість кроків
def symmetrical(mat):
    for id, row in enumerate(mat):
        #print(id, row, row[id])
        for col in range(id+1,len(mat)):
            #print(row[col])
            #print('id',id)
            if row[col] !=  mat[col][id]:
                #print(row[col],mat[col][id])
                return False

    return True
# Функція яка провіряє матрицю на асиметричність
def assymetricRelation(mat):
    if irreflexive(mat) and antisymmetry(mat):
        return True

    return False


# Функція яка провіряє матрицю на антисиметричність
def antisymmetry(mat):
    for id, row in enumerate(mat):
        for col in range(id + 1, len(mat)):
            if row[col] == mat[col][id]:
                #print(row[col], mat[col][id])
                return False


    return True

# Функція яка провіряє матрицю на Транзитивність
def transitivity(mat):
    for id, row in enumerate(mat):
        for cid, col in enumerate(row):
            if mat[id][cid] == 1:
                for tr in range(len(mat)):
                    if mat[cid][tr] == 1:
                        if mat[id][tr] != 1:
                            return False

    return True