# 0x00. AirBnB clone - The console

<p align="center">
  <img src='./utils/HBNB.png' border='0' alt='Air-Bn-B-Project'/>
</p>


## [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=28&pause=1000&repeat=false&width=435&lines=Table+of+Contents%3A)](https://git.io/typing-svg)


* [Project Description](#Project-Description)
* [Description of the command interpreter](#Description-of-the-command-interpreter)
* [How to start it, How to use it](#How-to-start-it,-How-to-use-it)
* [Contributors](#Contributors)
* [Usage](#Usage)

## <!-- ubuntu -->
<a href="https://ubuntu.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A" alt="Suite CRM"></a> <!-- python--> <a href="https://www.python.org" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Python&color=FFD43B&logo=python&logoColor=3776AB&labelColor=2F333A" alt="python"></a> </a> <!-- vim --> <a href="https://www.vim.org/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A" alt="Suite CRM"></a>
<!-- vs code --> <a href="https://code.visualstudio.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=5C2D91&logo=Visual%20Studio%20Code&logoColor=5C2D91&labelColor=2F333A" alt="Suite CRM"></a> </a> <!-- git --> <a href="https://git-scm.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Git&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A" alt="git distributed version control system"></a> <!-- github --> <a href="https://github.com" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github"></a>

<br />

## Description of the command interpreter
* Its exactly the same as the shell but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

	- Create a new object (ex: a new User or a new Place)
	- Retrieve an object from a file, a database etc
	- Do operations on objects (count, compute stats, etc)
	- Update attributes of an object
	- Destroy an object


<br />

## How to start it, How to use it
* **Execution**
	- Your shell should work like this in interactive mode:

```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  all    create   help  show
BaseModel  EOF   Review  User   count  destroy  quit  update

(hbnb)
(hbnb)
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project(simple shell) in C)

```sh
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  all    create   help  show
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

All tests should also pass in non-interactive mode:
```sh
$ echo "python3 -m unittest discover tests" | bash
```
<br />

## Usage

* Start the console in interactive mode:

```bash
$ ./console.py
(hbnb)
```

* Use help to see the available commands:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

* Quit the console:

```bash
(hbnb) quit
$
```
<br />

## Contributors
* The following people contributed to this repository.
1. Hillary Awanga <hillarymarvince@gmail.com>
2. Alukwe Jones Terah <jtalukwe@kabarak.ac.ke># AirBnB_clone
