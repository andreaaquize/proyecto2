# Proyecto2  

## Integrantes   

- Alexia Alegría  
- Andrea Aquize 
- Emilia Borja

## Requisitos  

- Crear una matriz vacía previamente

## Instrucciones de Uso

- No usar números negativos  
- Emplear números entre 0 y 82 para la coordenada x  
- Emplear números entre 0 y 42 para la coordenada y
- Emplear tíldes para las instrucciones. Sólo escribir en minúscula.

## Descripción del Programa

El programa construye figuras geométricas dentro de una matriz ya definida, empleando las ecuaciones de la línea y el círculopara hacerlo. En el caso de la línea, solicita las coordenadas de dos puntos, entre los cuales se dibujará una línea, ya que se puede obtener la pendiente m y la traslación b a partir de estos. El programa también contempla la construcción de líneas verticales, las cuales no son consideradas funciones.

Tanto el triángulo como el rectángulo son combinaciones de líneas. Ambas funciones solicitan las coordenadas del punto izquierdo inferior de la figura y su base y altura. 

Para el círculo se emplea también la ecuación matemática. Se solicitan las coordenadas del centro y el radio y se emplean ambas raíces para construir el círculo. Se empleó una función propia llamada redondeo para convertir el valor float al int más cercano.

