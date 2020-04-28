# Hello pip

Before you do anything, make sure you create an account oon pypi.org. It's important to constantly share your code and ideas with others as it'll imrpove the quality over time. It's very easy to convince yourself that some piece of code is useful and well written if noone is using it.

## Installing the right packages

Before you get started I'll assume you've went ahead and downloaded the Python Anaconda distribution


Then you want to go

```
conda create -n hello-pip
conda install setuptools wheel twine tqdm
```

## Project Setup

Then setup your directories in the same way as this repo
* README: Is this document, your chance to pitch your product. Most people will skim this before they read the rest of your code so take particular care in writing it
* LICENSE: Pick whatever works for your usecase - check out tldrlegal.com if you're not sure what to pick
* setup.py: Will contain all your package metadata
* hello.pip: is an executable we need to make runnable by typing ```chmod +x hello-pip```

## Compiling Package

Run ```python setup.py bdist_wheel``` which will create 3 new folders in your directory
1. Build/
2. dist/
3. hello_pip.egg.info/

The dist folder contains your package in wheel format so if you'd like to run your package locally you can run
```
pip install dist/hello_pip-0.1-py3-none-any.whl
```

## Upload to PyPi

# Next steps
1. Build a more complete tutorial, instad of echo, upload a class others can import
2. Build a package people use and love