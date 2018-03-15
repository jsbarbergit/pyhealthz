pyhealthz
=========

Simple Python Web Server for Serving System Health Data

Development Environment Setup
-----------------------------

1. Ensure Python 3.x is installed
2. Ensure ``pip`` and ``virtualenv`` are installed
3. Clone git repo ``git clone git@github.com/jsbarbergit/pyhealthz``
4. ``cd pyhealthz`` and install dependencies: ``make install``
5. Start virtual environment ``pipenv shell``

Usage
-----

By default, pyhealthz will run on TCP/8080 and bind to all interfaces
Start pyhealthz by running the following:

::

    $ pyhealthz 

Optionally, specify ``--port`` and/or ``--address`` to override defaults

::
    $ pyhealthz --port 8181 --address 127.0.0.1

pyhealthz will run until terminated.

System resource usage data in JSON format via an HTTP call to:

::

    GET /healthz

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn’t active then use:

::

    $ pipenv run make

