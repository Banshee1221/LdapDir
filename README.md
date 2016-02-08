# AD-Chart
AD-Chart is an LDAP parser and formatter written in Python 2. 
It is used to pull information from a company AD server and use this to build a hierarchy tree.

# Requirements
The application was built in Python 2 and also requires the following packages:
- [docopt](http://docopt.org/)
- [python-ldap](http://www.python-ldap.org/index.html)

# Usage
Create a file called creds.dat in the AD-Chart folder and put your LDAP auth credentials in it. Example:
```bash
("cn=readonlyuser,ou=this,ou=that,dc=example,dc=com", "readonlyuserpassword")
```
You can then execute either
```bash
python main.py --json
```
OR
```bash
python main.py --goog
```

--json will create a json file under AD-Chart/res/json with all the information needed to generate a tree using the D3js method,
while using --goog will generate a Google charts API compatable index.html.

**Using the --goog flag is not recommended at this stage.**

# Credits
- Mike Bostock for [D3js](https://github.com/mbostock/d3)
- Ilya Yakubovich for his [Descendant Tree](https://github.com/Yakubovich/descendant_tree)
