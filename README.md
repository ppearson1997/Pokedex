# Pokedex

This is an app that records information of a certain pokemon.
This app was a part of a test.


## Instructions

First clone this repository.
```bash
$ git clone https://github.com/ppearson1997/Pokedex.git
```

Install dependencies. Make sure you already have [`python`](https://www.python.org/downloads/) & [`pipenv`](https://pypi.org/project/pipenv/#:~:text=Usage%20Examples%3A%20Create%20a%20new,%2D%2Dpre%20Show%20a%20graph) installed in your system.

```bash
$ pipenv shell
$ pipenv install
```

Migrate
```bash
$ python manage.py migrate
```

Load data from Pokeapi
```bash
$ python manage.py load_pokemons  # This is a management command
```

Run it
```bash
$ python manage.py runserver
```