def productocartesiano(lista1, lista2):
    producto = []
    for elemento1 in lista1:
        for elemento2 in lista2:
            producto.append((elemento1, elemento2))
            
    return producto

print(productocartesiano([1,2,3], ['a','b','c']))

