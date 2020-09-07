#NEITH LOPEZ BAUTISTA
#PROYECTO 1

"""
This is the LifeStore-SalesList data:

lifestore-searches = [id_search, id product]
lifestore-sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore-products = [id_product, name, price, category, stock]
"""

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches




#print(len(lifestore_products))
#print(len(lifestore_sales))
#print(len(lifestore_searches))

#A continuación se definirán los administradores, quiénes seran los únicos habilitado para ver la información disponible sobre la situación de ventas de la empresa.
usuarios_admon = [["A", "5657"], ["B", "7879"]]
#Se le pedirá al usuario que ingrese los datos de usuario y contraseña
usr_inpt = input("ingresa el usuario: ")
pss_inpt = input("Ingresa la contraseña: ")

#una vez obtenidos los datos se procederá a corroborar dichos datos con la lista usuarios_admon, con la finalidad de permitirles o no el acceso.
admon_perm = 0

for usuario in usuarios_admon:
    if usuario[0] == usr_inpt and usuario[1] == pss_inpt:
        print("Bienvenido a LifeStore")
        admon_perm = 1
        break
    else:
        print("Datos no encontrados")
        continue
        
#MENÚ DE OPCIONES

if admon_perm == 1:

  print("Tienes permisos para acceder a los reportes de ventas. \nPor favor elige una de las siguientes opciones (A,B,C): \n \n 1.A: Productos más vendidos y productos rezagados  \n 2.B: Productos por reseña de servicio \n 3.C: Total de ingresos y ventas")
  
  reporte_selec = input ("Opción: ")
  op_aceptada = 0
  while op_aceptada != 1:
    if reporte_selec == "A":
      print("Seleccionaste la opción A")
      op_aceptada = 1
      
       #LISTA UNO: Lista con los 50 productos con mayores ventas.
      contador = 0
      total_sales= [] #En esta lista se pondrá la cuenta de cada iteración. [[id1, contador], [id2, contador]]

      for producto in lifestore_products:
        for venta in lifestore_sales:
          if producto [0]==venta[1]:
            contador +=1
        
        lista_uno = [producto[0], producto [1], contador]
        total_sales.append (lista_uno)
        contador = 0
        
      #for total in total_sales:
        #print("\nID producto:", total[0], "\n" , "Nombre: ", total[1],"\n", "No. Ventas:", total[2]) # resultado, lista de todos los productos, sin ordenar

      #ordenar de mayor a menor según el número de ventas.
      sales_ordenados= []

      while total_sales:
        mayor = total_sales [0][2]
        lista_actual = total_sales[0]
        for sal in total_sales:
          if sal[2]> mayor:
            mayor = sal[2]
            lista_actual= sal
        sales_ordenados.append(lista_actual)
        total_sales.remove(lista_actual)

        #imprimir la lista con los 50 productos más vendidos.
      print("----------------------------------------------------------------")
      print ("\n","       TOP 50 PRODUCTOS MÁS VENDIDOS       ", "\n")
      print("----------------------------------------------------------------")

      for indice in range (0,50):
          print("\n", "ID más vendido: ", sales_ordenados[indice][0])
          print ("Nombre",sales_ordenados[indice][1])
          print ("No. ventas",sales_ordenados[indice][2])

      #__________________________________________________________________________
      #LISTA CON LOS 96 PRODUCTOS CON MAYORES BÚSQUEDAS
      #SEGUNDA LISTA 
      contador = 0
      total_searches= [] #En esta lista se pondrá la cuenta de cada iteración. [[id1, contador], [id2, contador]]

      for producto in lifestore_products:
        for search in lifestore_searches:
          if producto [0]==search[1]:
            contador +=1
        
        lista_dos = [producto[0], producto [1], contador]
        total_searches.append (lista_dos)
        contador = 0
        
      #for total in total_searches:
        #print("\nID producto:", total[0], "No. búsquedas: ", total[2]) 
      #ordenar de mayor a menor según el número de búsquedas.
      searches_ordenados= []

      while total_searches:
        mayor = total_searches [0][2]
        lista_actual = total_searches[0]
        for sear in total_searches:
          if sear[2]> mayor:
            mayor = sear[2]
            lista_actual= sear
        searches_ordenados.append(lista_actual)
        total_searches.remove(lista_actual)
      #imprimir la lista con los 50 productos más vendidos.
      #print (len(searches_ordenados))

      print("----------------------------------------------------------------")      
      print ("\n","      TOP 96 PRODUCTOS CON MAYORES BÚSQUEDAS       ", "\n")
      print("----------------------------------------------------------------")

      for indice in range (0,96):
        print("\n", "ID más búscado: ", searches_ordenados[indice][0])
        print ("Nombre",searches_ordenados[indice][1])
        print ("No. búsquedas",searches_ordenados[indice][2])

      #LISTA CON LOS PRODUCTOS MENOS VENDIDOS POR CATEGORÍA

      #Obtener las categorias contenidas en el código

      categorias=[]
      categorias_contenidas= []
      for categoria in lifestore_products:
        if categorias_contenidas == categoria[3]:
          continue
        else:
          categorias.append(categoria[3])
          categorias_contenidas=categoria[3]

      #print("Las categorias de los productos son: ","\n", (categorias))

      for categoria in categorias:
        cuenta_venta_categoria=0
        for producto in lifestore_products:
          for ventas in lifestore_sales:
            if ventas[1]==producto[0] and producto[3]==categoria:
              cuenta_venta_categoria+=1

      print("----------------------------------------------------------------")      
      print ("\n","      LISTADO POR CATEGORÍAS DE PRODUCTOS       ", "\n")
      print("----------------------------------------------------------------")
      print("Categoria: ", categoria, " - ", "No. ventas: ",cuenta_venta_categoria)
      



    #MENÚ 2: PRODUCTOS POR RESEÑA EN EL SERVICIO 
    elif reporte_selec == "B":
      print ("Seleccionaste la opción B")
      op_aceptada = 1
    #Mostrar un listado con las mejores reseñas y otra para las peores, considerando los productos con devolución.
    #Para obtener el listado, primero se deberá obtener el promedio por producto del score de las reseñas (0-5), en dónde 5 es la máxima calificación.
      contador = 0
      sum_score = 0
      mean_products = [] 
      for producto in lifestore_products:
        for venta in lifestore_sales:
          if producto[0] == venta[1]:
            contador += 1
            sum_score += venta[2]
        promedio = sum_score / contador
        lista_E = [producto[0], producto[1], promedio]
        mean_products.append(lista_E)

      #print(mean_products)

      #En lo subsiguiente se mostrará la lista con los 20 productos con mejor score.
      #ordenar de mayor a menor
      score_ordenados= []

      while mean_products:
        mayor = mean_products [0][2]
        lista_actual = mean_products[0]
        for prom in mean_products:
          if prom [2]> mayor:
            mayor = prom [2]
            lista_actual= prom
        score_ordenados.append(lista_actual)
        mean_products.remove(lista_actual)
      #imprimir la lista con los 50 productos más vendidos.
      #print (len(score_ordenados))

      print("----------------------------------------------------------------")
      print ("\n","      TOP 20: PRODUCTOS CON MEJOR SCORE      ", "\n")
      print("----------------------------------------------------------------")
      for indice in range (0,20):
        print("\n", "ID_Score: ", score_ordenados[indice][0])
        print ("Nombre",score_ordenados[indice][1])
        print ("Score promedio (alto): ",score_ordenados[indice][2])


      #Lista 2-B con los 20 peores score
      #se obtienen los promedios de cada producto, como en la lista anterior 2A
      contador = 0
      sum_score = 0
      mean_products = [] 
      for producto in lifestore_products:
        for venta in lifestore_sales:
          if producto[0] == venta[1]:
            contador += 1
            sum_score += venta[2]
        promedio = sum_score / contador
        lista_E = [producto[0], producto[1], promedio]
        mean_products.append(lista_E)


      #ordenar de menor a mayor
      score_bajos= []

      while mean_products:
        menor = mean_products [0][2]
        lista_low = mean_products[0]
        for low in mean_products:
          if low [2]< menor:
            menor = low [2]
            lista_low= low
        score_bajos.append(lista_low)
        mean_products.remove(lista_low)
      #print(score_bajos)

      print("----------------------------------------------------------------")
      print ("\n","      20 PRODUCTOS CON PEOR SCORE      ", "\n")
      print("----------------------------------------------------------------")
      for indice in range (0,20):
        print("\n", "ID: ", score_bajos[indice][0])
        print ("Nombre",score_bajos[indice][1])
        print ("Score promedio (bajo): ",score_bajos[indice][2])
        




    #MENÚ 3
    elif reporte_selec == "C":
      print( "Seleccionaste la opción C")
      op_aceptada = 1
      contador = 0
      total_sales= [] #En esta lista se pondrá la cuenta de cada iteración. [[id1, contador], [id2, contador]]

      for producto in lifestore_products:
        for venta in lifestore_sales:
          if producto [0]==venta[1]:
            contador +=1
        
        lista_uno = [producto[0], producto [1], contador]
        total_sales.append (lista_uno)
        contador = 0
      #print(total_sales)  
      #multiplicar el precio al número de ventas
      
      lista_multi_total=[]
      for productop in total_sales:
        for precio in lifestore_sales:
          if productop [0]== venta [1]:
            lista_multli = int(lifestore_products[2])*int(total_sales[2])
            contador=1
            lista_multi_total.append(lista_multli)
      print(lista_multi_total)  

          #Ingresos por mes

      #compras_meses=[]

      #for date_sale in lifestore_sales:
       # for producto in lifestore_products:
        #  if date_sale[3][6:10] == 2020 and venta[0] == producto[0]:
         #   compras_mes = int(venta[1]*producto[2])
          #  compras_meses.append(compras_mes)
      #print(compras_meses) 


      
    else:
      print ("Opción no disponible")
      reporte_selec = input("Selecciona una opción disponible: ")








  #En caso de no tener el usuario y contraseñas conrrectas, #no será posible ver la información de ventas 


else:
  print("Acceso denegado, por favor corrobora tus credenciales con el equipo de LifeStore")



