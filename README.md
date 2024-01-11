# Analizador léxico básico. Teoria de lenguajes Formales
El lenguaje utilizado para construir el analizador es Python
## Funcionamiento
El programa lee el archivo, luego se utilizan expresiones regulares para encontrar las partes requeridas, en este caso palabras reservadas del lenguaje cylon
Para encontrar los elementos buscados se usan diferentes tipos de expresiones algunas de ellas son:
. ^ $ * + ? { } [ ] \ | ( )

## El resultado es :
- La sentencia del for es  ['(nombre in nombres)', '(p in people)']
- La sentencia del if es  ['if (x > 1000)', 'if (p.age>=18)']
- La sentencia del print es  ['print("Hola mundo!\\n")', 'print("really big")']
- La sentencia del input es  ['input("Ingrese sus datos\\n")']


