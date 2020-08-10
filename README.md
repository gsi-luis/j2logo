# j2logo Exercise #13

## General data
* Author: Jorge Luis Piña González
* Email: jpinagonzalez@gmail.com
* Url: https://j2logo.com/ejercicios/ejercicio-13-acumulado/

## Description:
Implementa una función acumulado(lista), a la que se le pase como argumento una lista de
números enteros y devuelva una lista de la suma acumulada.

## Considerations:
* Si se pasa como argumento una lista vacía ([]), la función devolverá una lista vacía.
* Imagina la siguiente lista [1, 2, 3, 4]. La función acumulado([1, 2, 3, 4]) devolverá [1, 3, 6, 10].
* Como ves, cada elemento de la lista devuelta es [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4].

## Examples output:
````
>>> acumulado([1, 5, 7])
[1, 6, 13]
````
````
>>> acumulado([1, 0, 1, 0, 1])
[1, 1, 2, 2, 3]
````
````
>>> acumulado([])
[]
````

## Command execute
### Solution #1:
````
python3 exercise13.py
````
### Solution #2:
````
python3 exercise13a.py
````

## Command output
````
Execute: acumulado([1, 5, 7])
[1, 6, 13]
Right answer: True
````
````
Execute: acumulado([1, 0, 1, 0, 1])
[1, 1, 2, 2, 3]
Right answer: True
````
````
Execute: acumulado([])
[]
Right answer: True
````