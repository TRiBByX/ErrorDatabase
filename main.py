from handlers import databasehandler
import os

'''
def main():
    database = os.path.join('model/', 'errordb.db')

    sql_create_table = """ CREATE TABLE IF NOT EXISTS errors (
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
    conn = databasehandler.create_connection(database)

    if conn is not None:
        databasehandler.create_table(conn, sql_create_table)
    else:
        print('An error occured with the creation of the error table')
'''


def main():

    database = os.path.join('model/', 'errordb.db')

    conn = databasehandler.create_connection(database)

    with conn:
        error = ('Something went wrong', 'commenting on this',
                 '04-10-2017', '04-10-2017', '05-10-2017',
                 'Weird Casue', 'Christoffer', 'Christoffer')

        databasehandler.add_error(conn, error)


if __name__ == '__main__':
    main()
