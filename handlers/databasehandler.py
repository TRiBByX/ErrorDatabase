import sqlite3
from sqlite3 import Error

DIR = '../model/'


def create_connection(db_file):

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)


def create_table(conn):

    sql = """ CREATE TABLE IF NOT EXISTS errors (
                                id integer PRIMARY KEY,
                                description text,
                                comment text,
                                discovery_date text,
                                last_work_date text,
                                fixed_date text NOT NULL,
                                cause text NOT NULL,
                                discovered_by text,
                                fixed_by text
                            );
          """

    try:
        c = conn.cursor()
        c.execute(sql)
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
                  comment = ?,
                  fixed_date = ?
              WHERE id = ? """

    cur = conn.cursor()
    cur.execute(sql, error)
