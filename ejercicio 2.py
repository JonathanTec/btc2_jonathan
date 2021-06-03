A = [1,2,3]
B = ['a', 'b', 'c']
f = [(1, 'a'), (2, 'b'), (3, 'c')]

def esfuncion(f, A, B):
    lista_de_preimagenes = []
    
    # Verificamos que f sea subconjunto de A x B
    for (preimagen, imagen) in f:
        lista_de_preimagenes.append(preimagen)
        if preimagen not in A or imagen not in B:
            # print('f no es subconjunto de AxB')
            return False
        
    # Verificamos que todo elemento de A es una preimagen
    if lista_de_preimagenes != A:
        # print('dominio de f no es A')
        return False
    
    # Verificamos la unicidad de la imagen.
    for (preimagen1, imagen1) in f:
        for (preimagen2, imagen2) in f:
            if preimagen1 == preimagen2 and imagen1 != imagen2:
                # print('no hay unicidad en las imágenes')
                return False
    return True

A = [1,2,3]
f = [(1, 1), (1, 2), (2, 3)]
print(esfuncion(f, A, A))
g = [(1, 1), (2, 2), (3, 3)]
print(esfuncion(g, A, A))

