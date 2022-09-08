# Tipagem dinamica
variavel_string = "Oi sophia"  # Texto
variavel_double = 1.10  # Valores com ponto flutuante
variavel_int = 124352  # Valores numericos inteiros
variavel_array_int = [1, 2, 3, 4]  # Vetores podem ser uni ou bi dimensionais
# Array = Vetor unidimensional
# Matriz = Vetor bidimensional
matriz_int_str = [[1, 2, 3, 4], ['a', 'b', 'c', 'd']]
variavel_array_string = ["Sophia", "Cruz", "Sodre"]



print(variavel_string)
print(variavel_double)
print(variavel_int)

print(variavel_array_int[1])
print(variavel_array_string[0])



variavel_string = 10

print(f'Variavel string com numero {variavel_string}')


variavel_array = []

# ==========================================================================================

for i in variavel_array_int:
    print(f'{i=}')



for numero1 in range(1, 11):
    print(f'{numero1=}')
    print(f"TABOADA DO {numero1}\n========================================")
    for numero2 in range(1, 11):
        print(f'{numero2} x {numero1} = {numero1 * numero2}')
        print(f'{numero2=}')

print('tchau')

"""
Fortemente Tipado

int variavelInteira = 10;

String variavelString = "oi sophia"

static int main(){
  system.out.print("oi");
  return 10;
}

variavelInteira = main();

"""
