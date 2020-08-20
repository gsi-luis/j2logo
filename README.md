# j2logo Exercise #13

## General data
* Author: Jorge Luis Piña González
* Email: jpinagonzalez@gmail.com
* Url: https://j2logo.com/ejercicios/ejercicio-15-el-final-comun-mas-largo/

## Description:
Implementa una función final_comun_mayor(str1, str2), a la que se le pase como argumento dos cadenas de caracteres y devuelva el final común a ambas más largo.

## Considerations:
* Si no existe un final común, la función debe devolver una cadena vacía.

## Examples output:
````
>>> final_comun_mayor('camión', 'ración')
'ión'
````
````
>>> final_comun_mayor('Python', 'PyCon')
'on'
````
````
>>> final_comun_mayor('Teclado', 'Mezclado')
'clado'
````
````
>>> final_comun_mayor('Harina', 'Arroz')
''
````

## Command execute
````
python exercise15.py
````
## Command output
````
Execute: final_comun_mayor(camión,ración )
ión
Right answer: True
````
````
Execute: final_comun_mayor(Python,PyCon )
on
Right answer: True
````
````
Execute: final_comun_mayor(Teclado,Mezclado )
clado
Right answer: True
````
````
Execute: final_comun_mayor(Harina,Arroz )

Right answer: True
````