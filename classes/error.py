class Error(object):
    """Error class"""
    def __init__(self, id, description, comment, disc_date, last_work_date,
                 cause, fixed_by, fixed_when, disc_by):
        super(Error, self).__init__()
        self.id = id
        self.description = description
        self.comment = comment
        self.disc_date = disc_date
        self.last_work_date = last_work_date
        self.cause = cause
        self.fixed_by = fixed_by
        self.fixed_when = fixed_when
        self.disc_by = disc_by

    def __str__(self):
        return 'ID : {0}\nDescription : {1}\nComment : {2}\nDate Discovered : {3}\nLast known working date : {4}\nCause : {5}\nFixed by : {6}\nFixed when : {7}\nDiscovered by : {8}'.format(
            self.id,
            self.description,
            self.comment,
            self.disc_date,
            self.last_work_date,
            self.cause,
            self.fixed_by,
            self.fixed_when,
            self.disc_by
            )
