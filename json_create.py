import json

counter = 0

def json_create(dict, head):

    global json_obj

    CEO = dict[head]
    #print json_obj[head]
    print "{'name': '%s', 'bio': '%s', 'image': '%s', 'children': [" % (str(CEO.getFn() + " " + CEO.getLn()),
            str(CEO.getFn() + " " + CEO.getLn() + "<br />Title: " + CEO.getTitle() + "<br />Email: " + CEO.getMail() +
                "<br />Mobile: " + CEO.getMobile() + "<br />Telephone: " + CEO.getTel() + "<br />Skype: " +
                CEO.getSkype() + "<br />Location: " + CEO.getLoc()+ "<br />IP No.: " + CEO.getIP()), "none")
    creator(CEO)


def creator(dict_obj):

    global counter
    global json_obj
    global tracker

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

    string = {"name": str(fname + " " + lname), "bio": str(fname + " " + lname + "<br />Title: " + title +
              "<br />Email: " + email + "<br />Mobile: " + mobile + "<br />Telephone: " + tel + "<br />Skype: " +
              skype + "<br />Location: " + location + "<br />IP No.: " + ip), "image": "none",
              "children": []}


    #print counter,
    counter += 1
    #print dict_obj.getFn() + " " + dict_obj.getLn() + "," + dict_obj.getTitle()
    #print string
    for items in dict_obj.getChilds():
        creator(items)
    counter -= 1
