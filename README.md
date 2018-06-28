## T3: Todo List Time Tracker

T3 is a simple, CLI based todo list that also tracks how long you have been working on your various projects.

T3 was started in Spring 2018 and was originally developed by a group from an Open Source Computing class at Loyola University Chicago.

Keep up to date with release announcements and updates by joining our IRC channel on Freenode: ##T3Comp412

<b>Mission Statement: </b>
To assist those who struggle with time management through a simple, easy to use, to do list time tracker.


## Visit our Website:
[![T3-Todo-List-Time-Tracker](https://user-images.githubusercontent.com/31542650/39339677-b3bd5cec-498f-11e8-9167-66b48bba2208.png)](https://j-adamski.github.io/T3-Todo-List-Time-Tracker/)

## Installation/Compiling:
Full Instructions can be found in [our Getting Started Guide](https://github.com/j-adamski/T3-Todo-List-Time-Tracker/blob/master/GettingStarted.md)
```
sudo python3 setup.py install
```
Tar.gz file is available [here](https://github.com/j-adamski/T3-Todo-List-Time-Tracker/blob/master/archive/t3-1.2.0.tar.gz)

Binary Distribution is available [here](https://github.com/j-adamski/T3-Todo-List-Time-Tracker/blob/master/archive/t3-1.2.0-dev1-py3-none-any.whl)

For ArchLinux users, PKGBUILD is available [here](https://github.com/j-adamski/T3-Todo-List-Time-Tracker/blob/master/archive/PKGBUILD) 

## Quick Intro:
Add your first project:
```
    python3 t3.py --add FirstProject
```

Start timing the project:
```
    python3 t3.py --start FirstProject
```

Mark Project as completed:
```
    python3 t3.py --complete FirstProject
```

Delete Project:
```
    python3 t3.py --delete FirstProject
```


Print report of completed projects:
```
    python3 t3.py --report completed
```

Print help dialog: 
```
    python3 t3.py --help
```


## Usage:

When you run t3.py with the help flag, the help message will be displayed, listing all of the available command options.
Available Options:
* `--add` - Will add a Project to your list
* `--complete` - Will mark a Project on your list as completed
* `--delete` - Removes Project from list
* `--report` - Prints out basic report of the week by default. Active prints out current Projects. Completed prints out only completed Projects. All prints out the entire json file
* `--start` - Starts Timing the Project, will overwrite existing tracking time if project is already being tracked.
* `--stop` - Stops timing of project, updates total run time
* `--edit` - Edits the time spent on a project in minutes


## Wiki/FAQ:
FAQ can be located in the [wiki](https://github.com/j-adamski/OSC-Project-2/wiki)


## Contribution Guidelines

If you want to contribute to T3, review the [contribution guidelines.](https://github.com/j-adamski/T3-Todo-List-Time-Tracker/blob/master/Contribution.md) This project also adhere's to the T3 [code of conduct.](https://github.com/j-adamski/T3-Todo-List-Time-Tracker/blob/master/CODE_OF_CONDUCT.md) All contributers are expected to adhere to this code at all times.

## Authors
* Thomas Hatzopoulos
* Prachi Patel
* Eunice Montenegro
* Julia Adamski
* Iri Bandas

## License:

This project is licensed under the [GPL 3.0](LICENSE) License
