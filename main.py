from handlers import databasehandler
from classes import error
from datetime import datetime

'''
def main():
    sql_create_table = """ CREATE TABLE IF NOT EXISTS errors (
                                id integer PRIMARY KEY,
                                description text NOT NULL,
                                cause text,
                                user text NOT NULL,
                                found_time datetime,
                                fixed_time datetime
                            );
                       """
    conn = databasehandler.create_connection()

    if conn is not None:
        databasehandler.create_table(conn, sql_create_table)
    else:
        print('An error occured with the creation of the error table')
'''

'''
def main():

    database = os.path.join('model/', 'errordb.db')

    conn = databasehandler.create_connection(database)

    with conn:
        error = ('Something went wrong', 'commenting on this',
                 '04-10-2017', '04-10-2017', '05-10-2017',
                 'Weird Casue', 'Christoffer', 'Christoffer')

        databasehandler.add_error(conn, error)

'''


def main():
    newerror = error.Error('network went dark, hacking attack by lizard squad',
                           'hack', 'Christoffer', datetime.today(), None)

    conn = newerror.add_to_db()

    rows = databasehandler.load_all_errors(conn)

    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
