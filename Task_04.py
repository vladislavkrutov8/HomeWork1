print("Введите первое значение: ")
num1 = float(input())
print("Введите второе значение: ")
num2 = float(input())
print("Введите действие +, -, /, *, mod, pow, div: ")
oper = input()
if num2 == 0 and oper == '/' or num2 == 0 and oper == 'mod' or num2 == 0 and oper == 'div':
    print('Деление на 0!')
elif oper == 'pow':
    print(num1 ** num2)
elif oper == 'div':
    print(num1 // num2)
elif oper == 'mod':
    print(num1 % num2)
elif oper == '*':
    print(num1 * num2)
elif oper == '/':
    print(num1 / num2)
elif oper == '+':
    print(num1 + num2)
elif oper == '-':
    print(num1 - num2)