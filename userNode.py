class userNode:

    def __init__(self, fname, lname, email, title=None, mobile=None, tel=None, skype=None, location=None, manager=None,
                 ip=None):
        self.parent = None
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
        self.children = []

    def getFn(self):
        return self.first_name

    def getLn(self):
        return self.last_name

    def getTitle(self):
        return self.title

    def getMail(self):
        return self.email

    def getMobile(self):
        return self.mobile

    def getTel(self):
        return self.tel

    def getSkype(self):
        return self.skype

    def getLoc(self):
        return self.location

    def getMan(self):
        return self.manager

    def getIP(self):
        return self.ip

    def setParent(self, parentNode):
        self.parent = parentNode

    def addChild(self, childNode):
        self.children.append(childNode)

    def getPar(self):
        return self.parent

    def getChilds(self):
        return self.children

    def prettyPrint(self):
        print "==========\nName: %s %s\nTitle: %s\nEmail: %s\nTelephone: %s\nMobile: %s\nIP Tel: %s\nSkype Name: %s\n" \
              "Manager: %s\nLocation: %s\nManages: %s\n==========\n" % (self.first_name, self.last_name, self.title, self.email,
                                                          self.tel, self.mobile, self.ip, self.skype, self.manager,
                                                          self.location, str(self.children))
