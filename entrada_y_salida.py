# Este programa muestra la forma de recoger información desde el teclado
# 20 de septiembre

print('Hola! como te llamas?')
miNombre = input() # input() recibe texto desde el teclado
print('Hola', miNombre, 'espero que lo estés pasando genial')
print('Qué edad tienes?')
edad = int(input())

if edad > 13:
  print('Ok, puedes entrar')
else: 
  print('mmm no, aquí no se permiten niños')


  