import math

def is_prime(num):

    if num <= 1:
        return False
    
    if num == 2:
        return True
    
    if num % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False 
    return True 


def get_primes(number_list):
    primes = []
    
    for number in number_list:
        
        if is_prime(number):
            primes.append(number) 
    return primes

example_list = [1, 4, 6, 7, 13, 9, 67]
prime_list = get_primes(example_list)

print(f"The original list is: {example_list}")
print(f"The prime numbers from the list are: {prime_list}")


# 7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#    A. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#    B. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
#    C. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*
