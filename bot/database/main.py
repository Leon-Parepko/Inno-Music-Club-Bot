import logging
from logging import log

import psycopg2
from bot.misc.env import PG
from bot.database.models import models

ConnectionDB: psycopg2.connect

dns = "dbname=%s user=%s host='%s' password='%s' port='%s'" % \
      (PG.dbname, PG.user, PG.host, PG.password, PG.port)


def register_db():

    try:
        global ConnectionDB
        ConnectionDB = psycopg2.connect(dns)
    except psycopg2.OperationalError as e:
        # if ConnectionDB: ConnectionDB.rollback()
        raise type(e)(str(e).rstrip() + ': happens when tried to connect to DB server')

    if not PG.tables_created:
        try:
            createDB()
        except psycopg2.OperationalError as e:
            raise type(e)(str(e).rstrip() + ' happens at %s' % 'createDB')


def createDB():
    for model in models:
        # print(model, ':', model().getCreateTableQuery())
        try:
            createTableQuery = model().getCreateTableQuery()
            if createTableQuery == '':
                raise Exception(('Model %s' % model) + ' is empty')
            cur = ConnectionDB.cursor()
            cur.execute(createTableQuery)
            ConnectionDB.commit()
            cur.close()
            # records = cur.fetchall()
            # print(records)
        except psycopg2.errors.DuplicateTable as e:
            log(logging.WARNING, str(e).rstrip() + f': with Model {model} happens at %s' % 'createDB')
        except Exception as e:
            raise type(e)(str(e) + ': happens at %s' % 'createDB')
    pass
