# socket code skeleton comes from
# https://realpython.com/python-sockets/

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR #need to pip install sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import socket
import json
#[(War and Peace y  124326)]
class server:

    def __init__(self):
        self.HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
        self.PORT = 65430  # Port to listen on (non-privileged ports are > 1023)
        self.data = 0
        self.x = 0
        self.disp = ""

    def runSocket(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("SOCKET 1?")
            s.bind((self.HOST, self.PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:
                    # receiving message from the client
                    data = conn.recv(1024)
                    if not data:
                        break
                    # sends the data back to the client?

                    self.data = data
                    #conn.sendall(data)
                    book_result = self.sql(data) #results. book_res <list>
                    byte_result = bytes(book_result, 'utf-8') #create bytestring
                    print("byte result is ", type(byte_result))
                    conn.sendall(byte_result )
    #for future expansion
    def query_result(self, booksObj, Book):
        # sqlalchemy.orm.Query.select_from(*from_obj)
        #
        return booksObj.query(Book).filter(Book.id == 1)

        if self.data ==  b'SELECT * FROM users':
            return booksObj.query(Book).all()

    def sql(self, query_data):
        print("2?")
        Base  = declarative_base()

        class Book(Base): #book is instantiated later to add to table
            __tablename__ = "bookes"#users
           # __table_args__ = {'mysql_engine': 'SQLite'}


            #columns
            id = Column("id", Integer, primary_key=True, autoincrement=True)
            title = Column("title", String)
            fiction = Column("fiction", CHAR)
            isbn = Column("isbn", Integer)


            def __init__(self, id,  title, fiction, isbn):
                self.id = id
                self.title = title
                self.fiction = fiction
                self.isbn = isbn


            def __repr__(self): #used for printing
                return f"({self.id} {self.title} {self.fiction}  {self.isbn})"


        engine = create_engine("sqlite:///mydb.db", echo = True)
        Base.metadata.create_all(bind=engine)

        Session = sessionmaker(bind=engine)
        booksObj = Session()


        #fill table
        #title fiction isbn

        """ 
        p0 = Book(0,"War and Peace", "y", 124326)
        booksObj.add(p0) #create vook but not in database
        booksObj.commit() #sends data to database
        """

        """ 
        p1 = Book(1,"Of human bondage", "y", 435743)
        booksObj.add(p1)  # create vook but not in database
        booksObj.commit()  # sends data to database
        """

        #prints query to screen
        #results = booksObj.query(Book).all()
        print("")
        print("query passed is ", self.data)
        print("")
        results = booksObj.query(Book).all()
        #results = self.query_result(booksObj, Book)



        strResults = str(results)

        """ 
        result = connection.execute(
            table.insert().
            values(name='foo').
            returning(table.c.col1, table.c.col2)
        )
        """




        print("%#$%#^#$^", type(strResults))
        print(results)
        #print(result.all())
        return strResults