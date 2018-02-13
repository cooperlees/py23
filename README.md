# py23
Code used for a Python 2 to Python 3 tutorial to be presented at Scaleconf 2018.
- http://scaleconf.org/

The goal of this tutorial is to show *Pythonistas* how to use `Unit Testing`
and `type analysis` to allow a smooth Python 2 to Python 3 conversion
of existing code bases.


## Tutorial Steps
Create virtualenvs or install py23 into your Python installation.

### Python 2 unit test run

```
python2 ./setup.py test
```
- This should grab all the dependencies and run our unit tests

### Run py23
Lets run the super exciting program in Python 2!

```
python2 py23/py23.py --help
python2 py23/py23.py

Sample Output:
cooper-mbp:py23 cooper$ python2 py23/py23.py
I am writing lame Python 2 code
I read in /etc/hosts as <type 'str'>
echo of "Hello World!" match as they are both <type 'str'>
```

### Python 3 unit test Run
Since we're awesome and have unit tests lets pretend we want to move this
awesome code to Python 3.
- If you're using virtualenvs create a Python 3 venv. If you didn't know
  Python 3 includes the `venv` module by defaults

```
python3 -m venv --help

e.g.
python3 -m venv /path/to/venv/base
```
- You can then activate it or access the python and pip binaries in the `bin`
  directory within that virtual environment.


```
python3 ./setup.py test
```

One test (test_iteritems_fun) will fail:

```
======================================================================
ERROR: test_iteritems_fun (py23.tests.base.TestPy23)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/cooper/repos/py23/py23/tests/base.py", line 49, in test_iteritems_fun
    actual_output = iteritems_fun(self.important_data, version)
  File "/Users/cooper/repos/py23/py23/py23.py", line 53, in iteritems_fun
    for version, message in data.iteritems():  # noqa: B301,T484
AttributeError: 'dict' object has no attribute 'iteritems'
```

- Lets uncomment out the Py23 example in 'iteritems_fun' to allow the tests to pass_context

```
test_binary_file (py23.tests.base.TestPy23) ... ok
test_iteritems_fun (py23.tests.base.TestPy23) ... ok
test_subprocess_echo (py23.tests.base.TestPy23) ... ok
```

### Run py23
Lets rerun the awesome program now in Python 3. The output should be
slightly different.

```
python3 py23/py23.py

Sample Output:
cooper-mbp:py23 cooper$ python3 py23/py23.py
I am writing the future, aka, Python 3
I read in /etc/hosts as <class 'str'>
echo of "Hello World!" match. They are both <class 'str'>
```
- Do you see the difference?
- Python 3 no longer calls 'str' a "type"

### Read py23.py
Take note of the py23 compliant code in some of the functions.

- In `binary_file_open` we use `six.PY2` to work out if we require decoding
  (Yes, you would normally just not open the file in binary mode)
- In `iteritems_fun` `.iteritems()` is left on purpose to have a test fail
- In `subprocess_echo` we also use `six.PY2` to see if we need to tell
  subprocess to decode the output via the encoding perameter. In Python 3
  subprocess defaults to returning byte arrays (b'')
- `click` is Python 2 / 3 friendly so main needs no changes


### Type Checking
- Extra Credit

If you read the code closely you can see `# type:` annotations scattered
throughout the code. This is Python 2 type annotating.
In Python 3 we have actual PEP484 typing support so it does not need to be comments.

- To run mypy and check this file's typing:

```
# mypy is Python 3 only ...
pip3 install mypy
# Make sure you run it in Py2 mode or you will get an error :)
mypy --py2 py23/py23.py
```

- For extra points once you go to Python 3 you can retype this code using the
much cleaner and nicer Python 3 type annotating:
- http://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html


### pytest + tox
`tox` (https://tox.readthedocs.io/), using `pytest` (https://pytest.org/) help automate running code in different
versions of the Python runtime. This is fantastic to ensure new features and
more importantly bug fixes work in all required versions of Python.

To run tox run the following:
```
pip install tox
tox

Sample Output:
TBA
```

### CI and Unit Tests
Github allows Travis CI and WINDOWS CI environments to run your code on each
diff put up. I have included a sample `.travis.yml` file that runs our test suite
in both Python 2 and 3.

Travis + Github: https://docs.travis-ci.com/user/getting-started/


# Questions etc.
**Cooper Ry Lees** <me@cooperlees.com>
- https://twitter.com/cooperlees
