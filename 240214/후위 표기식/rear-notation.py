N = int(input())
formula = input()
numbers = {chr(ord('A')+i):int(input()) for i in range(N)}
stack = [numbers[formula[0]]]
for i in range(1, len(formula)):
    element = formula[i]
    if element.isalpha():
        stack.append(numbers[element])
    else:
        num2 = stack.pop()
        num1 = stack.pop()
        if element == '*':
            stack.append(num1*num2)
        elif element == '/':
            stack.append(num1/num2)
        elif element == '-':
            stack.append(num1-num2)
        else:
            stack.append(num1+num2)

print(f'{stack[0]:.2f}')