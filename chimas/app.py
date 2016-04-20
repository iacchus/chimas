import cherrypy

import sqlite3
import json

cmx_conf = cherrypy.config.update({'server.socket_port': 41345})

USERNAME = "user1"
PASSWORD = "pass1"

# DB TEST

def list_boards():
    boards = []

    conn = sqlite3.connect('dummy.sqlite3')
    c = conn.cursor()

    c.execute("SELECT * FROM boards")

    row = c.fetchone()
    while row:
        boards.append({'name':row[0], 'desc':row[1]})

        row = c.fetchone()

    return boards

def list_thread():
    pass

# self.posts_thread = self.fetch_thread(cursor, 0, 5, self.topic_id, self.topic_id, posts_thread)
# self.posts_list = self.fetch_thread_linear(cursor, 0, 5, self.topic_id, self.topic_id, posts_list)

def num_of_replies(cursor, post_id):

    cursor.execute("SELECT * FROM posts WHERE reply_to_id='{}'".format(post_id))
    row = cursor.fetchone()

    if row:
        csize = len(row)

        if csize > 0:
            return csize
        else:
            return False

    else:
        return False

def fetch_thread(cursor, thread_num=0, thread_max=5, topic_id='1', post_id='1', posts=[]):
   
    if thread_num==0: # OP

        cursor.execute("SELECT * FROM posts WHERE id='{}'".format(post_id))
        row = cursor.fetchone()

        post = {
            'id'            : row[0],
            'topic_id'      : row[1],
            'reply_to_id'   : row[2],
            'board_id'      : row[3],
            'date'          : row[4],
            'author_id'     : row[5],
            'title'         : row[6],
            'post_text'     : row[7],
            'hash_id'       : row[8],
            'replies'       : [],
            'thread_num'    : thread_num+1
        }

        posts.append(post)

        if (thread_num+1 < thread_max) and num_of_replies(cursor, post_id) > 0:
            thread_num +=1
            fetch_thread(cursor, thread_num, thread_max, topic_id, post_id, post['replies'])

    else: # when recursively called to fetch replies

        cursor.execute("SELECT * FROM posts WHERE reply_to_id='{}'".format(post_id))
        data_replies = cursor.fetchall()

        while len(data_replies) > 0:

            cur_reply = data_replies.pop(0)

            reply = {
                'id'            : cur_reply[0],
                'topic_id'      : cur_reply[1],
                'reply_to_id'   : cur_reply[2],
                'board_id'      : cur_reply[3],
                'date'          : cur_reply[4],
                'author_id'     : cur_reply[5],
                'title'         : cur_reply[6],
                'post_text'     : cur_reply[7],
                'hash_id'       : cur_reply[8],
                'replies'       : [],
                'thread_num'    : thread_num+1
            }

            posts.append(reply)
	    
            if (thread_num+1 < thread_max) and num_of_replies(cursor, reply['id']) > 0:
                #thread_num +=1 WRONG AS IT INCREMENTS EVERY LOOP
                fetch_thread(cursor, thread_num+1, thread_max, topic_id, reply['id'], reply['replies'])

    return posts

# this function avoids using another recursion when presenting data

def fetch_thread_linear(cursor, thread_num=0, thread_max=5, topic_id='1', post_id='1', posts=[]):
   
    if thread_num==0: # OP

        cursor.execute("SELECT * FROM posts WHERE id='{}'".format(post_id))
        row = cursor.fetchone()

        post = {
            'id'            : row[0],
            'topic_id'      : row[1],
            'reply_to_id'   : row[2],
            'board_id'      : row[3],
            'date'          : row[4],
            'author_id'     : row[5],
            'title'         : row[6],
            'post_text'     : row[7],
            'hash_id'       : row[8],
            'replies'       : [],
            'thread_num'    : thread_num+1
        }

        posts.append(post)

        if (thread_num+1 < thread_max) and num_of_replies(cursor, post_id) > 0:
            thread_num +=1
            fetch_thread_linear(cursor, thread_num, thread_max, topic_id, post_id, posts)

    else: # when recursively called to fetch replies

        cursor.execute("SELECT * FROM posts WHERE reply_to_id='{}'".format(post_id))
        data_replies = cursor.fetchall()

        while len(data_replies) > 0:

            cur_reply = data_replies.pop(0)

            reply = {
                'id'            : cur_reply[0],
                'topic_id'      : cur_reply[1],
                'reply_to_id'   : cur_reply[2],
                'board_id'      : cur_reply[3],
                'date'          : cur_reply[4],
                'author_id'     : cur_reply[5],
                'title'         : cur_reply[6],
                'post_text'     : cur_reply[7],
                'hash_id'       : cur_reply[8],
                'replies'       : [],
                'thread_num'    : thread_num+1
            }

            posts.append(reply)
	    
            if (thread_num+1 < thread_max) and num_of_replies(cursor, reply['id']) > 0:
                fetch_thread_linear(cursor, thread_num+1, thread_max, topic_id, reply['id'], posts)

    return posts


class ChimasExtAuth:

    def __init__():
        self.exposed = True

    def validate_password(username,password):
        if username == USERNAME and password == PASSWORD:
            return True
        else:
            return False

class ChimasExtBBS:

    def __init__(self):
        pass

    @cherrypy.expose()
    @cherrypy.tools.json_out()
    def boards(self):
        #return "This is boards().."
        return list_boards()

    @cherrypy.expose()
    @cherrypy.tools.json_out()
    def topics(self):
        posts_list = []

        conn = sqlite3.connect('dummy.sqlite3')
        c = conn.cursor()

        #posts_list = fetch_thread_linear(c, 0, 5, 1, 1, posts_list)
        posts_list = fetch_thread(c, 0, 5, 1, 1, posts_list)

        return posts_list


class Chimas(object):
    def __init__(self):
        self.initExtensions()

    def initExtensions(self):
        self.bbs = ChimasExtBBS()


class App(object):
    def __init__(self):
        self.chimas = Chimas

    @cherrypy.expose
    def index(self):
        return "CHIMAS BBS SERVER, PLEASE USE A CLIENT."

if __name__ == '__main__':
    cherrypy.tree.mount(App().chimas(), '/', cmx_conf)

    cherrypy.engine.start()
    cherrypy.engine.block()
