# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО,
# значения — данные о хобби. Сохранить словарь в файл users_hobby.txt.
# Фрагмент файла с данными о пользователях (users.txt): Иванов Иван Иванович
#                                                       Петров Петр Петрович 
# Фрагмент файла с данными о хобби (hobby.txt):         скалолазание, охота, 
#                                                       горные лыжи

def fill_user(users):
    file_users = open('users.txt', 'w')
    file_users.write(users)
    file_users.close()
    path = './users.txt'
    data = open(path, 'r')
    # content = data.read()
    # print(content)
    data.close

def fill_hobby(hobby):
    file_hobby = open('hobby.txt', 'w')
    file_hobby.write(hobby)
    file_hobby.close()
    path = './hobby.txt'
    data = open(path, 'r')
    # content = data.read()
    # print(content)
    data.close()

def fill_new_dict():
    user = []
    path = './users.txt'
    data = open(path, 'r')
    line = data.readline()
    while line:
        user.append(line)
        line = data.readline()
    user = [line.rstrip() for line in user]
    data.close()
    # print(user)
    hobbys = []
    path1 = './hobby.txt'
    data1 = open(path1, 'r')
    line1 = data1.readline()
    while line1:
        hobbys.append(line1)
        line1 = data1.readline()
    hobbys = [line.rstrip() for line in hobbys]
    data1.close()
    # print(hobbys)
    new_dict = dict(zip(user, hobbys))
    print(new_dict)

users = 'Иванов Иван Иванович\nПетров Петр Петрович'
hobby = 'скалолазание, охота\nгорные лыжи'
fill_user(users)
fill_hobby(hobby)
fill_new_dict()
