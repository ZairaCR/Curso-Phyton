ingreso_mensual = 10100
gasto_mensual = 1000

#in aniidado y el
# if
if ingreso_mensual >= 10000:
    print("estas bien en cualquier parte del mundo") 
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deuda")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("bien, puedes ahorra incluso")
    else:
        print("y pa, estas gastando demas, cuidado con tus finanzas")
    
elif ingreso_mensual >= 1000:
    print("estas bien en latinoamerica")
    
elif ingreso_mensual > 500:
    print("estas bien en Argentina")

elif ingreso_mensual > 200:
    print("estas bien en Venezuela")
    
else:
    print("sos pobre")