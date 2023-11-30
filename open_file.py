import os


def reader_files(path_to_file):
    list_data = []
    with open(path_to_file, encoding='utf-8') as f:
        current_len = len(f.readlines())
        f.seek(0)
        list_data.append([current_len])
        list_data.append(f.read())
        return list_data


def folder_loop():

    path = r'C:\Users\adada\Desktop\Python GIT\pyTEST\files'
    os.chdir(path)
    first_part = {}
    second_part = {}
    for file in os.listdir():
        if file.endswith('.txt'):
            path_to_file = f'{path}\{file}'
            m = reader_files(path_to_file)
            first_part[file] = m[0][0]
            second_part[file] = m[1]

    sorted_list = sorted(first_part.items(), key=lambda x: x[1])
    for i in sorted_list:
        with open('result.txt', 'a', encoding='utf-8') as result:
            result.write(i[0]+'\n')
            result.write(str(i[1])+'\n')
            result.write(second_part[i[0]]+'\n')


folder_loop()
