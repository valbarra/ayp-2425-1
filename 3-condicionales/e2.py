import typing

client_name=input("Indique su nombre")
age_client=int(input("inserte su edad"))

ticket_price="$2.00" #en caso de definir descuento 

is_free=age_client<=4
price_adult=age_client<=18
price_elder=age_client>=60
 
if age_client>=0: 

    if is_free :
        print (f"El cliente {client_name} tiene {age_client} años y su entrada de cine cuesta: $0 ")
    elif price_adult:
        print(f"El cliente {client_name} tiene {age_client} años y su entrada de cine cuesta: $1.50")
    elif price_elder: 
        print(f"El cliente {client_name} tiene {age_client} años y su entrada de cine cuesta: $1.00 ")
    else:
        print(f"El cliente {client_name} tiene {age_client} años y su entrada de cine cuesta: $2.00 ")
        

    
