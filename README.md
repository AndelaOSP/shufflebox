Shufflebox v0.0.1
===============================

**Author:** Andela Kenya

<img src="https://andela.com/wp-content/uploads/2016/01/Andela-logo-landscape-blue-400px.png" alt="" width="200">

Overview
--------

A randomizer package for shuffling.

Installation / Usage
--------------------

To install use pip: [COMING SOON]

     $ pip install shufflebox


Or clone the repo:

    $ git clone https://github.com/Habu-Kagumba/shufflebox.git

Install locally:

    $ python setup.py install

Or install in project environment:

```sh
# Inside environment, navigate to shufflebox directory
$ pip install -e .
```

Contributing
------------

TBD

Example
-------

```python
from shufflebox import Randomizer

# create the dataset
items = range(90)

rand = Randomizer(items)

# get random item
rand.get_random()

# create groups of 4 items
rand.create_groups(4)
```