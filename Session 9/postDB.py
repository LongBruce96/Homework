import pymongo

client = pymongo.MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")
db = client.c4e

my_feelings={
    'title': 'From C4E30 with Love',
    'author': 'Long Bruce',
    'content': 'Khóa học mang lại rất nhiều kiến thức bổ ích mới về thế giới công nghệ cũng như đã đem lại cơ hội cho m kết nối vs những ng bạn mới.'
    }

db.posts.insert_one(my_feelings)
