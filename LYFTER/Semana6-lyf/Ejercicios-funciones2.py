
# A
x = 10
print(f"The value of x before the function call is: {x}")

def change_global():
   
    global x
    x = 15  

change_global()

print(f"The value of x after the function call is: {x}")



#B

MESSAJE = "Hi"

def Carlos():

    print(MESSAJE, "Carlos")
    return MESSAJE + " Carlos" 

Carlos() 


#    2. Experimente con el concepto de scope:
#    A. Intente accesar a una variable definida dentro de una función desde afuera.
#    B.  Intente accesar a una variable global desde una función y cambiar su valor.