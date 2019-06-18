import os

from math import sqrt


def redondeo (boaty):

    conver = int(boaty)

    if boaty-conver >= 0.5:
        conver =conver +1

    return conver


def llenado (canvas):
    
    canvas=[]

    llenar =["."]
    borde=["."]

   for i in range (80):
        if i != 79:
             llenar.append(" ")
        else:
             llenar.append(".")

        borde.append(".")

   for i in range (42):
       if i ==0 or i==41:
          canvas.append(borde.copy())
       else:
          canvas.append(llenar.copy())

   return canvas



def linea (x1,y1,x2,y2, canvas):

    if x1 == x2:
        for k in range (y1,y2 +1):
            canvas[42-k].pop(x1)
            canvas[42-k].insert(x1,"*")

    elif y1==y2:

        for k in range (x1,x2+1):
            canvas[42-y1].pop(k)
            canvas[42-y1].insert(k,"*")

    else:

        m= (y2-y1)/(x2-x1)

        b=y1-m*x1
        for k in range (x1,x2 + 1):
            y=int(m*k + b)
            canvas[42-y].pop(k)
            canvas[42-y].insert(k,"*")


    return canvas



def rectangulo (x1,y1,b,h,canvas):

    linea(x1,y1,x1+b,y1,canvas)
    linea(x1,y1+h,x1+b,y1+h,canvas)
    linea(x1,y1,x1,y1+h,canvas)
    linea(x1+b,y1,x1+b,y1+h,canvas)
    
    return canvas



def triángulo (x1,y1,b,h,canvas):

    linea(x1,y1,x1+b,y1,canvas)

    a=redondeo(x1+b/2)
    linea(x1,y1,a,y1+h,canvas)
    linea(a,y1+h,x1+b,y1,canvas)
    
    return canvas


def circulo (x1,y1,rad,canvas):

    for k in range (x1-rad, x1+rad+1):

        y2=redondeo(y1 + sqrt(rad*rad-(k-x1)*(k-x1)))
        y3=redondeo(y1- sqrt(rad*rad-(k-x1)*(k-x1)))

        if y2==y3:
            canvas[42-y2].pop(k)
            canvas[42-y2].insert(k,"*")
        else:
            canvas[42-y2].pop(k)
            canvas[42-y3].pop(k)
            canvas[42-y2].insert(k,"*")
            canvas[42-y3].insert(k,"*")

    return canvas

def elipse (fx1,fy1,fx2,fy2,e,canvas):
    
    #la elipse no es perfectamente funcional, pero es debido a un error matemático, ya que nadie del grupo había trabajado con elipses antes. 

    if fy2==fy1:

        alfa=(fx1+fx2)/2
        beta=fy1
        c=fx2-alfa
        a= c/e
        b= sqrt(a**2 - c**2)

        lim1= redondeo(b+alfa)
        lim2= redondeo(alfa-b)

        for k in range(lim2,lim1+1):

            y1 =redondeo(beta- sqrt(b**2(1- ((k-alfa)**2)/(a**2))))
            y2 =redondeo(beta+ sqrt(b**2(1- ((k-alfa)**2)/(a**2))))

            canvas[42-y1].pop(k)
            canvas[42-y2].pop(k)
            canvas[42-y2].insert(k,"*")
            canvas[42-y1].insert(k,"*")

    elif fx1==fx2:

        alfa=fx1
        beta=(fy1+fy2)/2
        c= fy2-beta
        a=c/e
        b=sqrt(a**2 - c**2)
        lim1= redondeo(b+alfa)
        lim2= redondeo(alfa-b)

        for k in range(lim1,lim2+1):

            y1 =redondeo(beta- sqrt(a**2(1- ((k-alfa)**2)/(b**2))))
            y2 =redondeo(beta+ sqrt(a**2(1- ((k-alfa)**2)/(b**2))))

            canvas[42-y1].pop(k)
            canvas[42-y2].pop(k)
            canvas[42-y2].insert(k,"*")
            canvas[42-y1].insert(k,"*")
            
      
     return canvas




def printingCANVAS (canvas):
    for i in range (42):
       for j in range (81):
          print(canvas [i] [j], end="")
       print()









