'''Assignment
Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

  235
+  52
-----
  235
+  52
-----
Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.
Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:
If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
If the user supplied the correct format of problems, the conversion you return will follow these rules:
There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
Numbers should be right-aligned.
There should be four spaces between each problem.
There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
'''

def num(numero):
    try:
        int(numero)
        return True
    except:
        return False


def arithmetic_arranger(lista, result=False):
    arranged_problems = ''
    funcao = []
    # Checking Errors
    if len(lista) > 5:
        return "Error: Too many problems."
    for item in lista:
        item = item.split()
        if not num(item[0]) or not num(item[2]):
            return "Error: Numbers must only contain digits."
        elif len(item[0]) > 4 or len(item[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        elif item[1] not in '-+':
            print(item[1])
            return "Error: Operator must be '+' or '-'."
        elif not int(item[0]) or not int(item[2]):
            return "Error: Numbers must only contain digits."
        # New List to iterat
        funcao.append(item)

    # First Line
    for i, c in zip(funcao, range(len(funcao))):
        if int(i[0]) < int(i[2]):
            arranged_problems += f"{i[0]:>{(len(i[2]) + 2)}}"
        else:
            arranged_problems += f"{i[0]:>{(len(i[0]) + 2)}}"
        # separate the problems if not the last problem
        if (c + 1) != len(funcao):
            arranged_problems += '    '
    arranged_problems += '\n'

    # Second Line
    for j, c in zip(funcao, range(len(funcao))):
        if int(j[0]) < int(j[2]):
            arranged_problems += f"{j[1]} {j[2]}"
        else:
            arranged_problems += f"{j[1]} {j[2]:>{len(j[0])}}"
        # separate the problems if not the last problem
        if (c + 1) != len(funcao):
            arranged_problems += '    '
    arranged_problems += '\n'

    for k, c in zip(funcao, range(len(funcao))):
        if int(k[0]) < int(k[2]):
            arranged_problems += f'{"-" * (len(k[2]) + 2)}'
        else:
            arranged_problems += f'{"-" * (len(k[0]) + 2)}'
        # separate the problems if not the last problem
        if (c + 1) != len(funcao):
            arranged_problems += '    '

    if result == True:
        arranged_problems += '\n'
        for item, c in zip(funcao, range(len(funcao))):
            resultado = 0
            if item[1] == '-':
                resultado = int(item[0]) - int(item[2])
            else:
                resultado = int(item[0]) + int(item[2])

            if int(item[0]) < int(item[2]):
                arranged_problems += f" {resultado:>{(len(item[2]) + 1)}}"
            else:
                arranged_problems += f" {resultado:>{((len(item[0])) + 1)}}"
            # separate the problems if not the last problem
            if (c + 1) != len(funcao):
                arranged_problems += '    '
    return arranged_problems
