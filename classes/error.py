from handlers import databasehandler


class Error(object):
    """Error class"""
    def __init__(self, description, cause, user, found_time, fixed_time):
        super(Error, self).__init__()
        self.description = description
        self.cause = cause
        self.user = user
        self.found_time = found_time
        self.fixed_time = fixed_time

    def add_to_db(self):
        conn = databasehandler.create_connection()

        error = (self.description, self.cause, self.user,
                 self.found_time, self.fixed_time)

        databasehandler.add_error(conn, error)

        return conn

    def __str__(self):
        string = (
            'ID : {0}\nDescription : {1}\Cause : '
            '{2}\nUser : {3}\nFound time : {4}\nF'
            'ixed time : {5}').format(
                self.id,
                self.description,
                self.cause,
                self.user,
                self.found_time,
                self.fixed_time
        )
        print(type(string))
