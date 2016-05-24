import requests
from requests.auth import HTTPBasicAuth

host = "http://127.0.0.1:5000"

#creds = ("","")

users = [
        {'login':'admin','email':'admin@ourhost.fqdn','password':'4dm1n'},
        {'login':'mercurio','email':'mercurioo@ourhost.fqdn','password':'4dmi11n'},
        {'login':'ouser','email':'ouser@ourhost.fqdn','password':'4dmi12n'},
        {'login':'h3ll0_user','email':'hell0@ourhost.fqdn','password':'4dmi331n'},
        {'login':'okayuser','email':'allk@ourhost.fqdn','password':'4dmi1JKn'},
        ]

boards = [
        {'title':'first board','description':'This is our first board'},
        {'title':'second board','description':'Yet another board'},
        {'title':'third board','description':'Third board here.'},
        {'title':'another board','description':'Yet still another board.'},
        {'title':'yet another board','description':'hello another board here'},
        ]
#    topic_id = Column(Integer)
#    reply_to_id = Column(Integer)
#    board_id = Column(String)
#    author_id = Column(String)
#    title = Column(String)
#    post_text = Column(String)
#    hash_id = Column(String)

posts = [
    {
#        'id' : '',
        'topic_id': '1',
        'reply_to_id': '0',
        'board_id': 'first board',
        'author_id': 'mercurio',
        'title': 'This is the title',
        'post_text': 'This is the post text.',
        'hash_id': 'deadd34d',
    },
    {
#        'id' : '',
        'topic_id': '1',
        'reply_to_id': '1',
        'board_id': 'first board', # maybe not necessary to replies
        'author_id': 'ouser',
        'title': 're: This is the title',
        'post_text': 'This is our second post and first reply',
        'hash_id': 'cafedead',
    },
    {
#        'id' : '',
        'topic_id': '1',
        'reply_to_id': '1',
        'board_id': 'first board',  # maybe not necessary to replies
        'author_id': 'admin',
        'title': 're: This is the title',
        'post_text': 'This is our third post and second reply.',
        'hash_id': 'b33fc4ke',
    },


]

for i in users:
    r = requests.post(host+'/users', data=i)

#    r = requests.post(host+'/users', auth=creds, data=i)

for i in boards:
    r = requests.post(host+'/boards', data=i)
