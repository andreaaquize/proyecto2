from proyecto import llenado
from proyecto import elipse
from proyecto import linea
from proyecto import circulo
from proyecto import rectangulo
from proyecto import triángulo
from proyecto import printingCANVAS

canvas1=[]
#archivo= open(str(os.getcwd()) + "\\" + nombre + "_Encriptado" +  ".txt", "w")

inst=0

while inst!=5:

  print("1. Agregar una línea")
  print("2. Agregar una elipse o circulo")
  print("3. Agregar un rectángulo o cuadrado")
  print("4. Agregar un triángulo")
  print("5. Terminar el programa")

  inst=int(input())

  if inst==1:

     x3=int(input("Ingrese la coordenada x de su primer punto: "))

     y3=int(input("Ingrese la coordenada y de su primer punto: "))

     x4=int(input("Ingrese la coordenada x de su segundo punto: "))

     y4=int(input("Ingrese la coordenada y de su segundo punto: "))

     canvas1=llenado(canvas1)
     canvas1=linea(x3,y3,x4,y4,canvas1)
     printingCANVAS(canvas1)

  if inst==2:

    dif= input("¿Desea dibujar una elipse o un círculo? ")

    if dif=="elipse":

        #La elipse no es perfectamente funcional, ya que nadie del grupo había visto elipses antes,
        # entonces detro del código existe un error de índole matemático, mas no de programación.

        fx3 = int(input("Ingrese la coordenada x de su primer foco: "))
        fy3 = int(input("Ingrese la coordenada y de su primer foco: "))
        fx4 = int(input("Ingrese la coordenada x de su segundo foco: "))
        fy4 = int(input("Ingrese la coordenada y de su segundo foco: "))
        e1 = float(input("Ingrese la excentricidad de su elipse: "))

        canvas1=llenado(canvas1)
        canvas1= elipse(fx3,fy3,fx4,fy4,e1,canvas1)
        printingCANVAS(canvas1)



    elif dif=="círculo":

        x3=int(input("Ingrese la coordenada x del centro de su círculo: "))
        y3=int(input("Ingrese la coordenada y del centro de su círculo: "))
        radio=int(input("Ingrese el radio de su círculo: "))

        canvas1=llenado(canvas1)
        canvas1=circulo(x3,y3,radio,canvas1)
        printingCANVAS(canvas1)




  if inst==3:
     x1=int(input("Ingrese la coordenada x de su primer punto: "))
     y1=int(input("Ingrese la coordenada y de su primer punto: "))
     b=int(input("Ingrese su base: "))
     h = int(input("Ingrese su altura: "))

     canvas1 = llenado(canvas1)
     canvas1 = rectangulo(x1, y1, b, h, canvas1)
     printingCANVAS(canvas1)



  if inst==4:
     x1=int(input("Ingrese la coordenada x de su primer punto: "))
     y1=int(input("Ingrese la coordenada y de su primer punto: "))
     b=int(input("Ingrese su base: "))
     h = int(input("Ingrese su altura: "))

     canvas1 = llenado(canvas1)
     canvas1 = triángulo(x1,y1,b,h,canvas1)
     printingCANVAS(canvas1)





