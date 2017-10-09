import sqlite3
from sqlite3 import Error
import os

DIR = './model/'


def create_connection():
    db_file = os.path.join(DIR, 'errordbv2.db')

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)


def create_table(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)


def add_error(conn, error):
    sql = """ INSERT INTO errors(description, cause, user, found_time, fixed_time)
              VALUES(?,?,?,?,?) """

    cur = conn.cursor()
    cur.execute(sql, error)

    return cur.lastrowid


def delete_error(conn, id):
    sql = """ DELETE FROM errors WHERE id=? """
    cur = conn.cursor()
    cur.execute(sql, (id,))


def load_all_errors(conn):
    sql = """ SELECT * FROM errors """
    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()

    return rows


def find_error_by_id(conn, id):

    sql = """ SELECT * FROM errors WHERE id=? """
    cur = conn.cursor()
    cur.execute(sql, (id,))

    rows = cur.fetchall()

    return rows


def update_error(conn, error):

    sql = """ UPDATE errors
              SET description = ?,
                  cause = ?,
                  user = ?,
                  fixed_time = ?
              WHERE id = ? """

    cur = conn.cursor()
    cur.execute(sql, error)
