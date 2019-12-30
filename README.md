# Tkcrud

Python crud using MVC-style Tkinter.


## Features

- Using [mysql-connect-python](https://pypi.org/project/mysql-connector-python/) and [Tkcalendar](https://pypi.org/project/tkcalendar) of non-native libraries, the rest all on the nail.
- Option to choose between MySQL and SQLite.
- Records search field by Name and ID.

## Requirements

- Python >=3.8
- Setuptools >= 42.0.2
- Wheel >= 0.33.6
- MariaDB(MySQL)>= 10.4.11-1
- SqLite >= 3.30

## Using

This project was created with [PyCharm](https://www.jetbrains.com/pycharm/) 2019.3, so we would recommend using the project with PyCharm.
If you do not want to, you can start the project as follows:

**Developer:**

```
$ git clone https://github.com/snakypy/snakypy-tkcrud.git
$ cd tkcrud
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ pip install -r requirements-dev.txt
$ bin/setup -i
$ tkcrud-run
``` 

**User:**

```
$ pip install snakypy-tkcrud --user
$ tkcrud-run
```

When you run the project for the first time, it will create database access settings in the "$ HOME / .config / tkcrud / config / config.json" directory.
Open this file with any text editor, and choose between MySQL and SQLite for database.
Example:

**For SQLite:**

```json
{
    "connection": {
        "dbname": "sqlite",
        "mysql": {
            "user": "",
            "password": "",
            "host": "",
            "database": "",
            "raise_on_warnings": true
        },
        "sqlite": {
            "filename": "database.sqlite"
        }
    }
}
```

**For MySQL:**

```json
{
    "connection": {
        "dbname": "mysql",
        "mysql": {
            "user": "root",
            "password": "123",
            "host": "localhost",
            "database": "tkcrud",
            "raise_on_warnings": true
        },
        "sqlite": {
            "filename": ""
        }
    }
}
```

## Donation

If you liked my work, buy me a coffee :coffee: :smiley:

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YBK2HEEYG8V5W&source)

## License

The project is available as open source under the terms of the [MIT License](https://github.com/williamcanin/tkcrud/blob/master/LICENSE) © William Canin

Stored in the organization: [Snakypy](https://github.com/snakypy)

## Credits

* Name: William C. Canin
* Country: Brazil - SP
* E-Mail: william.costa.canin@gmail.com
* GitHub: [William Canin](http://github.com/williamcanin)
* Personal page: [William Canin](http://williamcanin.github.io)