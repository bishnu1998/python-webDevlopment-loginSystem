import mysql.connector as connector


class DBConnector:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     user='root',
                                     password='',
                                     database='login_system'
                                     )

    # insertion operation
    def insert_user(self, id, name, password):
        query = "insert into user(id,name,password)values({},'{}','{}')".format(
            id, name, password)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("insertion successful!!")

    # deletion operation
    def delete_user(self, id):
        query = "delete from user where id={}".format(id)
        print(query)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("user deleted successfully")

    # update operation
    def update_user(self, password, id):
        query = "update user set password='{}' where id={}".format(
            password, id)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("user successfully updated")

    # fetch all data
    def fetch_all(self):
        query = "select*from user"
        cursor = self.con.cursor()
        cursor.execute(query)
        for i in cursor:
            print("id:", i[0])
            print("name:", i[1])
            print("password:", i[2])
            print()


if __name__ == "__main__":
    d = DBConnector()
    # d.insert_user(1,'kaji','kaji')
    # d.delete_user(3)
    # d.update_user("password1",1)
    # d.fetch_all()
    while True:
        x = int(input(
            "1 for insertion \n2 for delete\n3 for update\n4 for fetch\n5 from exit\nenter the choice:"))
        if x == 1:
            id = int(input("id:"))
            name = input("name:")
            password = input("password:")
            d.insert_user(id, name, password)
        elif x == 2:
            id = int(input("id:"))
            d.delete_user(id)
        elif x == 3:
            id = int(input("id:"))
            password=input("password")
            d.update_user(password,id)
        elif x == 4:
            d.fetch_all()
        elif x == 5:
            exit()
        else:
            print("choose correct choice")
