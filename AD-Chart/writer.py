import json
import os

counter = 0


def hugo_create(dict_obj, ceo):
    with open('orgchart.txt', "w"):
        pass
    writer = open('orgchart.txt', "a")
    recurse_travel(dict_obj[ceo], writer)


def recurse_travel(cur_obj, writer):
    global counter
    concat = "-" * counter
    if counter > 0:
        concat = "-" * counter + " "
    counter += 1
    writer.write(str(concat + cur_obj.getFn() + " " + cur_obj.getLn() + "," + cur_obj.getTitle() + "\n"))
    for items in cur_obj.getChilds():
        recurse_travel(items, writer)
    counter -= 1


def json_create(FormattedArr, root):
    tmpFile = open(os.path.join('res/json/', 'voss.json'), "w")
    tmpFile.write(json.dumps(FormattedArr[root].__dict__, indent=4, separators=(',', ': ')))
    tmpFile.close()
