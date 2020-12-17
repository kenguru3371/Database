import pymysql.cursors

db = pymysql.connect('localhost','root','3413900ALp','mydb')

cursor = db.cursor()
while True:
    print('''Введите действие: Просмотреть-1, Добавить-2, Редактировать-3, Удалить-4, Выход-5''')
    a = input(": ")
    if a == '1':\

        cursor.execute("SELECT * FROM `mydb`.`students`;")
        data = cursor.fetchall()
        print(*data, sep="\n")

    elif a == '2':
        number = input ("Введите номер человека по списку : ")
        surname = input("Введите фамилию человека: ")
        name = input("Введите имя человека: ")
        skill = input("Введите навыки человека: ")

        cursor.execute("INSERT INTO `mydb`.`students` (`номер`, `фамилия`, `имя`, `навыки`) VALUES (%s, %s, %s, %s);", (number,surname,name,skill))
        cursor.execute("SELECT * FROM mydb.students;")

        print("Товарищ занесен в таблицу!Ура!")

    elif a == '3':
        number = input("Введите номер человека которого хотите изменить: ")
        surname = input("Введите фамилию человека: ")
        name = input("Введите имя человека: ")
        skill = input('Введите навыки человека: ')

        sql = "UPDATE `mydb`.`students` SET `фамилия` = '%s', `имя` = '%s', `навыки` = '%s' WHERE (`номер` = '%s');"% (surname,name,skill,number)

        cursor.execute(sql)
        cursor.execute("SELECT * FROM mydb.students;")
        print("Товарищ изменен!Ура!")

    elif a == '4':
        number = input("Введите номер человека которого хотите удалить: ")
        sql = "DELETE FROM `mydb`.`students` WHERE (`номер` = '%s');"%(number)

        cursor.execute(sql)
        cursor.execute("SELECT * FROM mydb.students;")
        print("Товарищ удален!")

    elif a == '5':
        break
db.commit()

db.close()
