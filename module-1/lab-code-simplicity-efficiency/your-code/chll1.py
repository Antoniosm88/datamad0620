print('Welcome to this calculator!')

a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')

operacion=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven"]
operacion3=["zero","one","two","three","four","five","six","minus five","minus four","minus three","minus two","minus one"]
operacion2=["plus","minus"]
numeros = {'zero': 0,
            'one': 1,
            'two': 2,
            'three':3,
            'four':4,
            'five': 5}

if(not a in operacion) or (not c in operacion) or (not b in operacion2):
    print("I am not able to answer this question. Check your input.")
    
elif b == 'plus':
    
    print(a,b ,c, 'equals' ,operacion[(numeros[a]+numeros[c])], 'goodbye :)')
        
        
elif b == 'minus':
    
     print(a,b ,c, 'equals', operacion3[(numeros[a]-numeros[c])], 'goodbye :)')
