import typing

#pedir numero al usuaio
number_user=float(input("inserte·un·numero:"))
is_even=number_user%2==0 
is_positive=number_user>=0

if is_even and is_positive:
    print(f"El número: {number_user} es par y positivo")
elif is_even and not is_positive:
    print(f"El número: {number_user} es par y negativo")
elif is_positive and not is_even:
    print(f"El número: {number_user} es impar y positivo")
elif not is_even and not is_positive:
    print(f"El número: {number_user} es impar y negativo")