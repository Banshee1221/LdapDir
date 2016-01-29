import json

counter = 0
json_obj = {}


def json_create(dict, head):
    CEO = dict[head]
    json_obj[head] = {"first_name": CEO.getFn(), "last_name": CEO.getLn(), "email": CEO.getMail(),
                      "title": CEO.getTitle(), "mobile": CEO.getMobile(), "tel": CEO.getTel(), "skype": CEO.getSkype(),
                      "location": CEO.getLoc(), "manager": CEO.getMan(), "ip": CEO.getIP(), "manages": {}}
    creator(CEO)


def creator(dict_obj):

    global counter
    counter += 1

    fname = dict_obj.getFn()
    lname = dict_obj.getLn()
    email = dict_obj.getMail()
    title = dict_obj.getTitle()
    mobile = dict_obj.getMobile()
    tel = dict_obj.getTel()
    skype = dict_obj.getSkype()
    location = dict_obj.getLoc()
    manager = dict_obj.getMan()
    ip = dict_obj.getIP()

    print counter,
    print dict_obj.getFn() + " " + dict_obj.getLn() + "," + dict_obj.getTitle()
    for items in dict_obj.getChilds():
        creator(items)
    counter -= 1
