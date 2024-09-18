#definicion del triagulo 

print("Considere un triagulo de lados a,b y c definidos a continuacion:")

side_a:int=input("ingrese un valor")
side_b:int=input("ingrese un valor")
side_c:int=input("ingrese un valor")

#obtención del perimetro

print("el perimetro del triamgulo es:")

perimeter_input:float=(side_a+side_b+side_c)/2
print(perimeter_input)

print("el area del triangulo es la siguiente")

area_input:float=(perimeter_input*[perimeter_input-side_a]*[perimeter_input-side_b]*[perimeter_input-side_c])//2
print(area_input)
