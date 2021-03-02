usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright [current year] the Melange authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from multiprocessing import Pool, Process
from datetime import datetime
import boto3
import sys
import os
import argparse
import logging
import logging.config
from bottle import route, run
from boto.cloudformation.stack import Output
import json
import socket
import sqlite3 as lite

def connect_db():
    con = None
    con = lite.connect('master.db')
    cur = con.cursor() 
    objects = []
    objects.append(con)
    objects.append(cur)
    return objects

def create_chatroom(name, tagline, cur, conn):
        #create the message room for the name of the room you are creating.
        try:
            cur.execute("""CREATE TABLE %s (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                           ROOM_ID INT, 
                           ROOM_MESSAGE TEXT, 
                           USER_ID INT,
                           DATE DATE)""" % name)
        except Exception as e:
            logger.info('%s already exist' % name)

        creation_date = datetime.now()
        #insert id,name,tagline,date
        cur.execute("""INSERT INTO ROOMS 
                        VALUES(?,?,?)""" , ( name, tagline, str(creation_date) ))
        conn.commit()
        logger.info('created room %s!' % name) 

def init_tables (conn, cur):
    try:
        cur.execute("""CREATE TABLE ROOMS(ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                           NAME TEXT, 
                           TAGLINE TEXT,
                           DATE DATE)""")

        cur.execute("""CREATE TABLE USERS(ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                           FIRSTNAME TEXT, 
                           LASTNAME TEXT,
                           HEADLINE TEXT,
                           PHONE TEXT,
                           EMAIL TEXT,
                           PASSWORD TEXT,
                           DATE DATE)""")

        cur.execute("""CREATE TABLE FRIENDS(ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                           IDFIRST INT, 
                           IDSECOND INT,
                           DATE DATE)""")  
        conn.commit()
        logger.info('Successfully Created Tables!') 
    except:
        logger.info('Tables already exist!')    

def setup_db(logger):
    try:
        logger.info('Building Database Tables.') 
        init_db = connect_db()

        con = init_db[0]
        cur = init_db[1]
        #inital tables
        try:
            init_tables (con, cur)
        except Exception as e:
            logger.info('Tables Exist.')

        try:
            create_chatroom('Lobby', 'Insight is the future', cur, con)
        except Exception as e:
            logger.info('Lobby already exist %s ' % e)

        try:    
            cur.execute('SELECT ID FROM ROOMS WHERE NAME="Lobby"')   
            id = cur.fetchone() 
            welcome_date = datetime.datetime
            cur.execute("INSERT INTO Lobby VALUES(?,?,?,?)" , (id, 'Welcome to the Insight Lobby!', '1',str(welcome_date),))  
        except Exception as e:
            logger.info('%s' % e)

        con.commit()
        con.close()
    except Exception as e:
        logger.info(str(e))
        pass

@route('/get_chat/<name>')
def get_status( name="Get Loading Status"):
    values = name.split('&')
    room = values[0]
    init_db = connect_db()

    con = init_db[0]
    cur = init_db[1] 
    cur.execute('SELECT * FROM %s' % str(room))
    values = cur.fetchall()   
    return values


if __name__ == '__main__':
    url = os.path.dirname(os.path.realpath(__file__)) + '/logging.ini'
    logging.config.fileConfig(url)
    logger = logging.getLogger('root')    
    setup_db(logger)
    #ip_address = socket.gethostbyname(socket.gethostname())
    run(host='127.0.0.1', port=8001, debug=True)