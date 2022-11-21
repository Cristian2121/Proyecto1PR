import numpy as np

def distancia_euclidiana(vector, centroide):
    cen = np.array(centroide)
    vec = np.array(vector)

    resta_cuadrada = np.square(cen - vec)
    suma = np.sum(resta_cuadrada)
    dis = np.sqrt(suma)

    return dis

"""patron = np.array( (183, 125, 44) )

d_c1 = distancia_euclidiana(patron, (206.6, 168.8, 131))
d_c2 = distancia_euclidiana(patron, (89, 130.6, 59))
d_c3 = distancia_euclidiana(patron, (24.8, 44.4, 179.8))

if d_c1 > d_c2 > d_c3 or d_c2 > d_c1 > d_c3:
    print("El patrón pertenece a la clase C3")
elif d_c1 > d_c3 > d_c2 or d_c3 > d_c1 > d_c2:
    print("El patrón pertenece a la clase C2")
elif d_c3 > d_c2 > d_c1 or d_c2 > d_c3 > d_c1:
    print("El patrón pertenece a la clase C1")"""