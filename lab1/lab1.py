import jsonimport
import properties

variant = "vartest2"

matrix = jsonimport.getmatrix(variant)
def Realtionschek(matrix):
    for row in matrix:
        print(row)
    print("Reflective: ",properties.reflexive(matrix))
    print("Irreflective: ",properties.irreflexive(matrix))
    print("Symmetrical: ",properties.symmetrical(matrix))
    print("AssymetricRelation: ",properties.assymetricRelation(matrix))
    print("Antisymmetry: ",properties.antisymmetry(matrix))
    print("Transitivity: ",properties.transitivity(matrix))
    #print('test)')

Realtionschek(matrix)

for x in range(1,31):
    variant = 'var'+ str(x)
    print(variant)
    matrix = jsonimport.getmatrix(variant)
    Realtionschek(matrix)
    #print("Transitivity: ", properties.transitivity(matrix))


#Функція яка стов
# def transitiveClosure (matrix):
#     result = ""
#     length = len(matrix)
#     for k in range(0, length):
#         for row in range(0, length):
#             for col in range(0, length):
#                 matrix[row] [col] = matrix[row][col] or (matrix[row][k] and matrix[k][col])
#         result += ("\n W" + str(k) +" is: \n" + str(matrix).replace("]," , "] \n") + "\n")
#     result += ("\n Transitive closure is \n" + str(matrix).replace("]," , "]\n"))
#     print (result)
#     return result
# transitiveClosure(matrix)
