box = []
for i in input().split():
    if i in '/*-+':
        a = box[-2]
        b = box[-1]
        box.pop()
        box.pop()
        if i == '+':
            answer = a + b
        elif i == '-':
            answer = a - b
        elif i == '*':
            answer = a * b
        else:
            answer = a / b
        box.append(answer)
    else:
        box.append(int(i))
print(box[0])
