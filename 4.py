#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('text_source.txt', 'w') as file:
    file.write(input('Напишите текст необходимый для сжатия на латинице: '))
with open('text_source.txt', 'r') as file:
    my_txt = file.readline()

def file_encod(txt):
    encond = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                encond += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encond += str(count) + prev_char
        return encond

txt_compr = file_encod(my_txt)

with open('text_compressed.txt', 'w') as file:
    file.write(f'{txt_compr}')
print(txt_compr)