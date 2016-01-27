class Json:

    first_name = ''
    last_name = ''
    title = ''
    email = ''
    mobile = ''
    tel = ''
    skype = ''
    location = ''
    manager = ''
    IPtel = ''
    data = {}

    def __init__(self, fname, lname, email, title=None, mobile=None, tel=None, skype=None, location=None, manager=None,
                 ip=None):
        self.first_name = fname
        self.last_name = lname
        self.title = title
        self.email = email
        self.mobile = mobile
        self.tel = tel
        self.skype = skype
        self.location = location
        self.manager = manager
        self.ip = ip

