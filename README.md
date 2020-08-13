# j2logo Exercise #13

## General data
* Author: Jorge Luis Piña González
* Email: jpinagonzalez@gmail.com
* Url: https://j2logo.com/ejercicios/ejercicio-13-acumulado/

## Description:
Implementa una función siguiente_mayor(lista), a la que se le pase como argumento una lista de números enteros 
y reemplace cada número por el siguiente más grande de la lista.

## Considerations:
* La función debe devolver una nueva lista con el resultado.
* Los elementos en la lista serán únicos.
* El elemento mayor se sustituye por el número -1.

## Examples output:
````
>>> siguiente_mayor([5, 7, 3, 2, 8])
[7, 8, 5, 3, -1]
````
````
>>> siguiente_mayor([2, 3, 4, 5])
[3, 4, 5, -1]
````
````
>>> siguiente_mayor([1, 0, -1, 8, -72])
[8, 1, 0, -1, -1]
````

## Command execute
````
python exercise14.py
````
## Command output
````
Execute: acumulado([5, 7, 3, 2, 8])
[7, 8, 5, 3, -1]
Right answer: True
````
````
Execute: acumulado([2, 3, 4, 5])
[3, 4, 5, -1]
Right answer: True
````
````
Execute: acumulado([1, 0, -1, 8, -72])
[8, 1, 0, -1, -1]
Right answer: True
````