
import re





archivo = open("ceylon.txt")
archivo=archivo.read()


palabra_reservada_print=re.findall('print',archivo)

palabra_reservada_input=re.findall('input',archivo)

palabra_reservada_for=re.findall('^for',archivo)

palabra_reservada_if=re.findall('if',archivo)



print("Encontro las palabras reservadas " , palabra_reservada_for,palabra_reservada_if,palabra_reservada_print,palabra_reservada_input)

print("\n")
print("\n")
print("\n")
print("\n")


sentencia_for=re.findall('\([a-z]+\sin\s[a-z]+\)',archivo)

print("La sentencia del for es ",sentencia_for)

sentencia_if=re.findall('if.+\(.+\)',archivo)

print("La sentencia del if es ",sentencia_if)

sentencia_print=re.findall('print\(.+\)',archivo)

print("La sentencia del print es ",sentencia_print)

sentencia_input=re.findall('input\(.+\)',archivo)

print("La sentencia del input es ",sentencia_input)















            
          

          

            


