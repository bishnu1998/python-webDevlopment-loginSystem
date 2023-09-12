import mysql.connector as connector
con = connector.connect(host="localhost",
                        user="root",
                        password="",
                        database="login_system"
                        )

if con.is_connected:
    print("connectoin successful!!")

    cursor = con.cursor()

    while True:
        id = int(input("id:"))
        name = input("name:")
        password = input("password:")

        query = "insert into login values({},'{}','{}')".format(
            id, name, password)
        #query ="insert into login(id,name,password)values(12,'ram','shysm')"
        cursor.execute(query)
        con.commit()

        #to break the loop
        x = int(input("Enter,\n 2 for exit! and any other number to continue: "))
        if x == 2:
            break
        print("successfully inserted!!")
