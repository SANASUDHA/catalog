from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from model import *

engine = create_engine('sqlite:///mybook.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete Books if exisitng.
session.query(Book).delete()
# Delete BookItem if exisitng.
session.query(BookItem).delete()
# Delete Users if exisitng.
session.query(User).delete()

# Create sample users
FirstUser = User(name="Sana Sudha",
                 email="sudha139k@gmail.com",
                 picture='https://plus.google.com/u/0/photos/'
                 '101854936676654161549/albums/profile/'
                 '6626186901972038082?iso=false')
session.add(FirstUser)
session.commit()
print "Done to add FU"
# Create sample books of novel
Book1 = Book(name="Mysteries",
             user_id=1, date=datetime.datetime.now())
session.add(Book1)
session.commit()

Book2 = Book(name="Thrillers",
             user_id=1, date=datetime.datetime.now())
session.add(Book2)
session.commit()

Book3 = Book(name="Historical Fiction",
             user_id=1, date=datetime.datetime.now())
session.add(Book3)
session.commit()

# Populate a bookitems with author for testing
# Using different users for novel book author also
BookItem1 = BookItem(name="Romantic Suspense",
                     author="Robyn Carr",
                     poster='https://images.gr-assets.com/'
                     'books/1529762242l/40392262.jpg',
                     price="200",
                     btype="NovelBook",
                     date=datetime.datetime.now(),
                     book_id=1,
                     user_id=1)
session.add(BookItem1)
session.commit()

BookItem2 = BookItem(name="Crime Thriller",
                     author="Tess Gerritsen",
                     poster='https://images.huffingtonpost.com/'
                     '2013-09-12-gunmoney.JPG',
                     price="150",
                     btype="NovelBook",
                     date=datetime.datetime.now(),
                     book_id=2,
                     user_id=1)
session.add(BookItem2)
session.commit()

BookItem3 = BookItem(name="The Twentieth Wife",
                     author="Margaret George",
                     poster='https://s3-us-west-2.amazonaws.com/'
                     'tabs.web.media/3/9/3907/3907-square-1536.jpg',
                     price="250",
                     btype="NovelBook",
                     date=datetime.datetime.now(),
                     book_id=3,
                     user_id=1)
session.add(BookItem3)
session.commit()

print("Data has been inserted Successfully!")
