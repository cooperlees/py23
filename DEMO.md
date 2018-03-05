# Instructor Demo Plan

Just some notes to print for a presenter to have a plan for demos of this code.

## Unit testing

- Lets see if unit tests pass with Python 2
```
python2 setup.py test -v
```

- Lets run the program with Python 2
```
python2 py23/py23.py
```

- Lets run Python 3 unit tests
```
python3 setup.py test -v
```

- Run unit test - show they fail
```
python3 setup.py test -v
```
- Lets fix code to allow unit tests to pass
1) encode subprocess output (Gate with six.PY2)
2) s/iteritems/items/g

- Run the program - Make program run
```
python3 py23/py23.py
```

- Run unit tests - show they pass
```
python3 setup.py test -v
```


## mypy

```
mypy --py2 py23/py23.py
```
