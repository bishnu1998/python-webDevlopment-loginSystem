import mysql.connector as connector
""" 
con = connector.connect(host='localhost',
                        user='root',
                        password='',
                        database='login_system'
                        )
#coursor is use to fire the query 

"""


class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     user='root',
                                     password='',
                                     database='login_system'
                                     )

        query = 'create table if not exists user(id int primary key,name varchar(50),password varchar(50))'
        cursor = self.con.cursor()
        cursor.execute(query)
        print('table created.')

        # insertion operation
    def insert_user(self,id,name, password):
        query = "insert into user(id,name,password) values({},'{}','{}')".format(
            id, name, password)
        print(query)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("inserted successfully!!")
    
    #fetch operation
    def fetch_all(self,id):
        query = "select*from user where id={}".format(id)
        cursor = self.con.cursor()
        cursor.execute(query)
        for row in cursor:
            print("id:",row[0])
            print("name:",row[1])
            print("password:",row[2])
            print()
        print("fetch successfully!!")
    
    #delete operation
    def delete_user(self,id):
            query = "delete from user where id={}".format(id)
            print(query)
            cursor=self.con.cursor()
            cursor.execute(query)
            self.con.commit()
     
            print("successfully deleted")
    
    #update operation
    def update_user(self,name,id):
        query = "update user set name ='{}' where id={}".format(name,id)
        print(query)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("updated successfully!!")


# main:
helper = DBHelper()
#helper.insert_user(2,'min12', 'kkaa12')
#helper.fetch_all(2)
#helper.delete_user(2)
helper.update_user("ram",1)

