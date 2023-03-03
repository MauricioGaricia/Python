def Num_conso():
    for i in range(1, 101):
        print(i)

def multi_3():
    for i in range(1, 101):
        if i % 3 == 0:
            print('Fizz')
        else:
            print(i)

def multi_5():
    for i in range(1, 101):
        if i % 5 == 0:
            print('Buzz')
        else:
            print(i)
def multi_3_5():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        else:
            print(i)


def main():
    while True:
        menu = '''          MENU
        1. imprimir Numeros pór consola del 1 al 100 por consola 
        2. Multiplos de 3 cambiarlos por la palabra Fizz
        3. Multiplos de 5 cambiarlos por la palabra Buzz
        4. Multiplos de 3 y de 5 a la vez cambiarlos por la palabra FizzBuzz
        5. Salir 
        
        Elige Una Opcion : '''

        opcion = input(menu)
        if opcion == '1':
            print(Num_conso())

        elif opcion =='2':
            print(multi_3())

        elif opcion == '3':
            print(multi_5())

        elif opcion == '4':
            print(multi_3_5()) 
            
        elif opcion == '5':
            break 

if __name__ == '__main__':
    main()


