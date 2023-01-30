"""
7 fallos consecutivos permitidos
"""
lista=[0,0,0,0,0,0,0,(13/37)**7]

print("7 fallos permitidos")

"""
El 100 del bucle siguiente hace referencia al dinero disponible,
es decir, se dispone de 100€ para apostar.
pk muestra la probabilidad de perder los 100€ tras 7 fallos.
"""
for k in range(8,100):
    pk=lista[7]+(24/37)*((13/37)**7)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=pk


print("100", pk)

for k in range(8,500):
    pk=lista[7]+(24/37)*((13/37)**7)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=pk

print("500", pk)

for k in range(8,1000):
    pk=lista[7]+(24/37)*((13/37)**7)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=pk

print("1000", pk)

for k in range(8,1500):
    pk=lista[7]+(24/37)*((13/37)**7)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=pk

print("1500", pk)

for k in range(8,2000):
    pk=lista[7]+(24/37)*((13/37)**7)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=pk

print("2000", pk)


for k in range(8,3000):
    pk=lista[7]+(24/37)*((13/37)**7)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=pk

print("3000", pk)

for k in range(8,5000):
    pk=lista[7]+(24/37)*((13/37)**7)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=pk

print("5000", pk)

for k in range(8,10000):
    pk=lista[7]+(24/37)*((13/37)**7)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=pk

print("10000", pk)

for k in range(8,50000):
    pk=lista[7]+(24/37)*((13/37)**7)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=pk

print("50000", pk)

"""
8 fallos
"""
lista=[0,0,0,0,0,0,0,0,(13/37)**8]

print("8 fallos permitidos")

for k in range(9,100):
    pk=lista[8]+(24/37)*((13/37)**8)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=lista[8]
    lista[8]=pk

print("100", pk)

for k in range(9,500):
    pk=lista[8]+(24/37)*((13/37)**8)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=lista[8]
    lista[8]=pk

print("500", pk)

for k in range(9,1000):
    pk=lista[8]+(24/37)*((13/37)**8)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=lista[8]
    lista[8]=pk

print("1000", pk)

for k in range(9,1500):
    pk=lista[8]+(24/37)*((13/37)**8)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=lista[8]
    lista[8]=pk

print("1500", pk)

for k in range(9,2000):
    pk=lista[8]+(24/37)*((13/37)**8)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=lista[8]
    lista[8]=pk

print("2000", pk)


for k in range(9,3000):
    pk=lista[8]+(24/37)*((13/37)**8)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=lista[8]
    lista[8]=pk

print("3000", pk)

for k in range(9,5000):
    pk=lista[8]+(24/37)*((13/37)**8)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=lista[8]
    lista[8]=pk

print("5000", pk)

for k in range(9,10000):
    pk=lista[8]+(24/37)*((13/37)**8)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=lista[8]
    lista[8]=pk

print("10000", pk)

for k in range(9,50000):
    pk=lista[8]+(24/37)*((13/37)**8)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=lista[8]
    lista[8]=pk

print("50000", pk)

"""
9 fallos
"""
lista=[0,0,0,0,0,0,0,0,0,(13/37)**9]

print("9 fallos permitidos")

for k in range(10,100):
    pk=lista[9]+(24/37)*((13/37)**9)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=lista[8]
    lista[8]=lista[9]
    lista[9]=pk

print("100", pk)

for k in range(10,500):
    pk=lista[9]+(24/37)*((13/37)**9)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=lista[8]
    lista[8]=lista[9]
    lista[9]=pk

print("500", pk)

for k in range(10,1000):
    pk=lista[9]+(24/37)*((13/37)**9)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=lista[8]
    lista[8]=lista[9]
    lista[9]=pk

print("1000", pk)

for k in range(10,1500):
    pk=lista[9]+(24/37)*((13/37)**9)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=lista[8]
    lista[8]=lista[9]
    lista[9]=pk

print("1500", pk)

for k in range(10,2000):
    pk=lista[9]+(24/37)*((13/37)**9)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=lista[8]
    lista[8]=lista[9]
    lista[9]=pk

print("2000", pk)


for k in range(10,3000):
    pk=lista[9]+(24/37)*((13/37)**9)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=lista[8]
    lista[8]=lista[9]
    lista[9]=pk

print("3000", pk)

for k in range(10,5000):
    pk=lista[9]+(24/37)*((13/37)**9)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=lista[8]
    lista[8]=lista[9]
    lista[9]=pk

print("5000", pk)

for k in range(10,10000):
    pk=lista[9]+(24/37)*((13/37)**9)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=lista[8]
    lista[8]=lista[9]
    lista[9]=pk

print("10000", pk)

for k in range(10,50000):
    pk=lista[9]+(24/37)*((13/37)**9)*(1-lista[0])
    lista[0]=lista[1]
    lista[1]=lista[2]
    lista[2]=lista[3]
    lista[3]=lista[4]
    lista[4]=lista[5]
    lista[5]=lista[6]
    lista[6]=lista[7]
    lista[7]=lista[8]
    lista[8]=lista[9]
    lista[9]=pk

print("50000", pk)
