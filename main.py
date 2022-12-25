
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             port = 3306,
                             user='root',
                             password='12345',
                             database='tech',
                             cursorclass=pymysql.cursors.DictCursor)




def create_blogs_table():
    with connection.cursor() as cursor:
        sql = """
              
            create table blogs( 
                id int, 
                title varchar(50), 
                description varchar(255) 
                );
            """
        cursor.execute(sql)
    connection.commit()

def insert_blogs_table (title, description):
    with connection.cursor() as cursor:
            sql = """

                    insert into blogs (title, description) values (%s,%s);

                  """
            cursor.execute(sql, (title, description))
    connection.commit()

create_blogs_table()
insert_blogs_table("Card title", "This card has supporting text below as a natural lead-in to additional content.")
