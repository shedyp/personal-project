import pyodbc as py

# Trusted Connection to Named Instance
conn = py.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQLEXPRESS;DATABASE=CRUD;Trusted_Connection=yes;')

cursor = conn.cursor()


""" cursor.execute('''
		CREATE TABLE products (
			product_id int primary key,
			product_name nvarchar(50),
			price int
			)
               ''')
 """

conn.commit()
