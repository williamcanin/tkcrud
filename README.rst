==============
TkCrud
==============

Python crud using MVC-style Tkinter.

Requirements
------------

- Python >=3.8
- Setuptools >= 42.0.2
- Wheel >= 0.33.6
- MariaDB(MySQL)>= 10.4.11-1
- SqLite >= 3.30

Using
-----

**Developer:**


This project was created with `PyCharm`_ 2019.3, so we would recommend using the project with PyCharm.
If you do not want to, you can start the project as follows:

.. code-block:: shell

    $ git clone https://github.com/snakypy/snakypy-tkcrud.git
    $ cd tkcrud
    $ python -m venv venv
    $ . venv/bin/activate
    $ pip install -r requirements.txt
    $ pip install -r requirements-dev.txt
    $ bin/setup -i
    $ tkcrud-run

**User:**

.. code-block:: shell

    $ pip install snakypy-tkcrud --user
    $ tkcrud-run

When you run the project for the first time, it will create database access settings in the **"$HOME/.config/tkcrud/config/config.json"** directory.
Open this file with any text editor, and choose between MySQL and SQLite for database.
Example:

**For SQLite:**

.. code-block:: json

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


**For MySQL:**

.. code-block:: json

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

Donation
--------

If you liked my work, buy me a coffee <3

.. image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
    :target: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YBK2HEEYG8V5W&source

License
-------

The gem is available as open source under the terms of the `MIT License`_ © William Canin

Stored in the organization: `Snakypy`_

Credits
-------

* Name: William C. Canin
* Country: Brazil - SP
* E-Mail: william.costa.canin@gmail.com
* Personal page: `William Canin`_

Links
-----

* Code: https://github.com/snakypy/snakypy-tkcrud
* Documentation: https://github.com/snakypy/snakypy-tkcrud/README.md
* Releases: https://pypi.org/project/snakypy-tkcrud
* Issue tracker: https://github.com/snakypy/snakypy-tkcrud/issues

.. _Snakypy: https://github.com/snakypy
.. _PyCharm: https://www.jetbrains.com/pycharm/
.. _MIT License: https://github.com/snakypy/snakypy-tkcrud/blob/master/LICENSE
.. _William Canin: http://williamcanin.github.io
