matrix = [
    ['7', 'i', 'i'],
    ['T', 's', 'x'],
    ['h', '%', '3'],
    ['i', '^', '#'],
    ['s', 'M', '$'],
    ['$', 'a', '^'],
    ['%', 't', '%'],
    ['^', 'r', '!'],
]
message = ""
for x in range(len(matrix[0])):
    for y in range(len(matrix)):
        if matrix[y][x].isalpha():
            message += matrix[y][x]
        else:
            try:
                if message[-1] != ' ':
                    message += ' '
            except:
                pass
print(message)