with open('orgchart.txt', "w"):
        pass
writer = open('orgchart.txt', "a")
counter = 0


def json_parse(dict_obj, ceo):

    recurse_travel(dict_obj[ceo])


def recurse_travel(cur_obj):
    global counter
    concat = "-" * counter
    if counter > 0:
        concat = "-" * counter + " "
    counter += 1
    writer.write(str(concat+cur_obj.getFn() + " " + cur_obj.getLn() + "," + cur_obj.getTitle() + "\n"))
    for items in cur_obj.getChilds():
        recurse_travel(items)
    counter -= 1

    """
    for items in FO.getChilds():
        print " - " + items.getFn(), items.getLn()
        for items2 in items.getChilds():
            print " -- " + items2.getFn(), items2.getLn()
            for items3 in items2.getChilds():
                print " --- " + items3.getFn(), items3.getLn()
    """