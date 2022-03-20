expression = input("enter expression:  ")
output = 0
i = -1
for ch in range(len(expression)):
    if i == ch:
        continue
    if expression[ch] in ['-', '+', '/', '', '*','^','%',"(",")"]:
        next_value = int(expression[ch+1])
        if expression[ch] == '-':
            output -= next_value
            i = ch+1
        elif expression[ch] == '+':
            output += next_value
            i = ch+1
        elif expression[ch] == '*':
            output *= next_value
            i = ch+1
        elif expression[ch] == '/':
            output /= next_value
            i = ch+1
        elif expression[ch] == '^':
            output **= next_value
            i = ch+1
        elif expression[ch] == '%':
            output %= next_value
            i = ch+1
    else:
        output = int(expression[ch])

print(output)