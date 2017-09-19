# Python Standard Library
The Python Standard Library as a very big set of programming tools that you can use to help you to program in Python. 
It provides new types of objects and functions for a range of common and specialised tasks, from networking to mathematical statistics. Other people have already written this code and put it into useful "modules" for you to access and use in your own code.

# Importing Modules

The Python Standard Library is organised into parts called modules. Many modules are simply Python files, like the Python scripts you've already used and written. 
In order to be able to use the code contained in a module we must import it, either in the interactive interpreter or in a Python script of our own.

The syntax for importing a module is simply import package_name.

>>> import math

Put 'import' statements at the top of your file (each one on a separate line). Importing a module runs the code in that file. It will typically contain a lot of definitions, and usually doesn't show any output. Running the code will make all of the module's functions and types of objects available to use.

For example, math has a factorial function. (It finds the product of a positive integer with all of the integers smaller than it; so the factorial of 4 is 24 because 4 × 3 × 2 × 1 = 24.) 
We have already used import math to import the math module. Now, in order to use the factorial function, we can call it, starting with the module name math, then a dot (.) and then the function name factorial().

>>> print(math.factorial(3))
6

# Other ways to import, and naming

There are some other variants of importing that are useful in other situations.

- To import an individual function or class from a module use

>>> from module_name import object_name

for example:

>>> from collections import defaultdict

This gives access only to defaultdict from the module collections. defaultdictwill be accessible with its own name (without the module name before it) and trying to access collections or even call collections.defaultdict() will give a NameError.

    >>> collections
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'collections' is not defined
    >>> collections.defaultdict()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'collections' is not defined
    >>> defaultdict()
    defaultdict(None, {})

Importing individual objects from a module means you only take what you need, and you don't need to use dot notation to access them.

You can import multiple individual objects from a module by separating them with commas:

    >>> from collections import defaultdict, namedtuple

This technique is very common when importing pieces from large libraries.

- To import a module and give it a different (usually shorter) name

To rename a module, you can use as:

>>> import module_name as different_name

for example

>>> import multiprocessing as mp

If the name of a module is particularly long, or if there is a clash with something with the same or similar name, you can rename a module.

You will then access objects from the module via the alternative name that you specified, and the usual dot notation:

>>> mp.cpu_count()
4

- Import an individual item from a module and give it a different name

You can combine the previous two pieces of syntax to import an item from a module and change its name:

from module_name import object_name as different_name

For example:

from csv import reader as csvreader

Again, you'll be able to access only that individual item directly via its newly specified name: no dot notation needed. This can be useful if you have multiple objects with similar names from different packages in your namespace. 
For example, perhaps you want a csv reader and a json reader - you could import them from their respective modules and give them descriptive names.

- One technique that you should NOT use for importing

Another way of importing that you may see in other people's code but that you should not use is

from module_name import *

For example:
from random import *

This will import every object from the random module individually, and allow you to access each of them directly via its name. 
The real problem with this is that modules may contain many objects, each of which has a name. Including all of these names may overwrite (or may be overwritten by) other names you are using in your program. 
import * also makes it impossible for collaborators to find where an imported object was defined. A reader can search for the definition of a function and not find it, and they won't know which import * statement introduced the function. These problems can lead to a lot of confusion. Do NOT use from module_name import *!!

If you really want to use all of the objects from the random module, use the standard import random instead and access each of the objects via the dot notation.

- Modules, packages and names

Some of the Python Standard Library modules have a lot in them! In order to manage the code better, they are split down into sub-modules that are contained within a package. A package is simply a module that contains sub-modules. A sub-module is specified with the usual dot notation.

For example, the os module (useful for dealing with filesystems, works the same for every operating system) has a submodule, os.path which is used specifically for dealing with pathnames. Modules that are submodules are specified by the package name and then the submodule name separated by a dot.

You can import the submodule os.path using

>>> import os.path

You can then use the objects from the submodule in the usual way:

>>> os.path.isdir('my_path')
False

However, this syntax for importing will only work for submodules - you cannot import a function from a module in this way.

>>> import os.path.isdir
ImportError: No module named 'os.path.isdir'; 'os.path' is not a package

Sometimes naming can be a point of confusion when working with modules. For example, a module might be named after one of the important classes or functions within it. 

In this case, you'll need to think carefully about your import statements:

>>> from datetime import datetime

imports the datetime class from the datetime module. Note that, after this, using datetime will refer to the datetime class, not the module.

- Importing and accessing from modules

Once you've imported something, it will remain imported until you exit the interactive interpreter with exit() or ctrl-D (or if you are working on Windows ctrl-Z).

- Our favourie modules

The Python Standard Library has a lot of modules. Some of them are listed below:


csv: very convenient for reading and writing csv files

collections: useful extensions of the usual data types including OrderedDict, defaultdict and namedtuple

random: generates pseudo-random numbers, shuffles sequences randomly and chooses random items

string: more functions on strings. This module also contains useful collections of letters like string.digits (a string containing all characters with are valid digits).

re: pattern-matching in strings via regular expressions

math: some standard mathematical functions

os: interacting with operating systems

os.path: submodule of os for manipulating path names

sys: work directly with the Python interpreter

json: good for reading and writing json files (good for web work)
