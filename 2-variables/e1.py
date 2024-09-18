import typing

volumen_reservorio: float = 4.445e8
lluvia: float = 5e6

#Nuevo valor de lluvia 

Lluvia·que·circula·libremnete=lluvia-(lluvia*0.10)
print(Lluvia·que·circula·libremnete)

#Variable agregada 

lluvia+=volumen_reservorio
print(lluvia)

volumen_reservorio+=Lluvia·que·circula·libremnete
print(volumen_reservorio)

volumen_reservorio=volumen_reservorio+(volumen_reservorio*0.05 )
print(volumen_reservorio) 

Evaporacion=volumen_reservorio-(volumen_reservorio*0.02)
print(Evaporacion)

Nuevo_volumen_resorvorio=volumen_reservorio-float(2.5**5)
print(Nuevo_volumen_resorvorio)