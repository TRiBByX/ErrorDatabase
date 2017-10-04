import sqlite3
from sqlite3 import Error

DIR = '../model/'


def create_connection(db_file):

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def add_error(conn, error):
    sql = """ INSERT INTO errors(description,
                                 comment, discovery_date,
                                 last_work_date, fixed_date,
                                 cause, discovered_by, fixed_by)
              VALUES(?,?,?,?,?,?,?,?) """

    cur = conn.cursor()
    cur.execute(sql, error)

    return cur.lastrowid


def delete_error(conn, id):
    sql = """ DELETE FROM errors WHERE id=? """
    cur = conn.cursor()
    cur.execute(sql, (id,))
