import time

def addition_zn(n):
    return [[(i + j) % n for j in range(n)] for i in range(n)]

# print(addition_zn(5))

def multiplication_zn(n):
    return [[(i * j) % n for j in range(1,n)] for i in range(1,n)]

# print(multiplication_zn(5))

def nombre_premiers(k):
    t = time.time() 

    nombre_premiers = []
    tab = []
    for i in range(2,k):
        zero = 0
        tab = multiplication_zn(i)
        # print(tab)
        for j in tab:
            # print(j)
            for w in j:
                if w == 0:
                    zero += 1

        if zero == 0 :
            nombre_premiers.append(i)

    return time.time() - t

# print(nombre_premiers(1000))

def nombre_premiers_2(k):
    t = time.time() 

    nombre_premiers = []

    for i in range(2,k):
        zero = 0
        for j in range(2,i):
            if i % j == 0:
                zero += 1
        if zero == 0:
            nombre_premiers.append(i)  
        
    return time.time() - t

# print(nombre_premiers_2(20000))

def nombre_premiers_3(k):
    t = time.time() 

    nombre_premiers = [i for i in range(2,k)]

    for j in nombre_premiers:

        nombre = 2
        while j*nombre <= nombre_premiers[-1] :
                
                # print (j*nombre)
                if j*nombre in nombre_premiers:
                    index = nombre_premiers.index(j*nombre)
                    nombre_premiers.pop(index)

                # print (nombre_premiers)
                nombre += 1

    return time.time() - t

# print(nombre_premiers_3(50000))