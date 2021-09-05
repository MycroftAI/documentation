# Mycroft Python Style Guide

## 1 Background

Python is the main programming language used at Mycroft. This style guide is a list of 
dos and don’ts for Python code.  The [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) 
was used as a starting point.


## 2 Python Language Rules

### 2.1 Lint
Run Pylint over your code using this pylintrc.

#### 2.1.1 Definition
Pylint is a tool for finding bugs and style problems in Python source code. It finds problems 
that are typically caught by a compiler for less dynamic languages like C and C++. 
Because of the dynamic nature of Python, some warnings may be incorrect; however, spurious 
warnings should be fairly infrequent.

#### 2.1.2 Pros
Catches easy-to-miss errors like typos, using variables before assignment, etc.

#### 2.1.3 Cons
Pylint isn’t perfect. To take advantage of it, sometimes we’ll need to write around it, 
suppress its warnings or fix it.

#### 2.1.4 Decision
Make sure you run Pylint on your code.

Suppress warnings if they are inappropriate so that other issues are not hidden. To suppress 
warnings, you can set a line-level comment:

```python
dict = 'something awful'  # Bad Idea... pylint: disable=redefined-builtin
```

Pylint's warnings are each identified by symbolic name (`redefined-builtin` in the above example).

If the reason for the suppression is not clear from the symbolic name, add an explanation.

Suppressing in this way has the advantage that we can easily search for and revisit them.

You can get a list of Pylint warnings by doing:

`pylint --list-msgs`

To get more information on a particular message, use:

`pylint --help-msg=C6409`

Prefer `pylint: disable` to the deprecated older form `pylint: disable-msg`.

Unused argument warnings can be suppressed by deleting the variables at the beginning of the 
function. Always include a comment explaining why you are deleting it. “Unused.” is sufficient. 
A common example at Mycroft is a message bus event handler that does not need the event
message passed to all handlers:

```python
def event_handler(message: Message):
    del message  # Unused by handler.
    print("In this event handler")
```

Other common forms of suppressing this warning include using `_` as the identifier for 
the unused argument or prefixing the argument name with `unused_`, or assigning them to `_`. 
These forms are allowed but no longer encouraged. These break callers that pass arguments 
by name and do not enforce that the arguments are actually unused.

### 2.2 Global variables
Avoid global variables.

#### 2.2.1 Definition
Variables that are declared at the module level or as class attributes.

#### 2.2.2 Pros
Occasionally useful.

#### 2.2.3 Cons
Has the potential to change module behavior during the import, because assignments to 
global variables are done when the module is first imported.

#### 2.2.4 Decision
Avoid global variables.

While they are technically variables, module-level constants are permitted and encouraged. 
For example: `_MAX_HOLY_HANDGRENADE_COUNT = 3`. Constants must be named using all caps with 
underscores. See Naming below.

If needed, globals should be declared at the module level and made internal to the module 
by prepending an _ to the name. External access must be done through public module-level 
functions. See Naming below.

### 2.3 Nested/Local/Inner Functions
Nested local functions or classes are fine when used to close over a local variable.

#### 2.3.1 Definition
A function can be defined inside a method or function. Nested functions have read-only 
access to variables defined in enclosing scopes.

#### 2.3.2 Pros
Allows definition of utility functions that are only used inside a very limited 
scope. Very ADT-y. Commonly used for implementing decorators.

#### 2.3.3 Cons
Nested functions cannot be directly tested. Nesting can make the outer function 
longer and less readable.

#### 2.3.4 Decision
They are fine with some caveats. Avoid nested functions except when closing over a 
local value other than self or cls. Do not nest a function just to hide it from users of a 
module. Instead, prefix its name with an _ at the module level so that it can still be accessed 
by tests.

### 2.4 Comprehensions & Generator Expressions
Okay to use for simple cases.

#### 2.4.1 Definition
List, Dict, and Set comprehensions as well as generator expressions provide a concise and 
efficient way to create container types and iterators without resorting to the use of traditional 
loops, map(), filter(), or lambda.

#### 2.4.2 Pros
Simple comprehensions can be clearer and simpler than other dict, list, or set creation techniques. 
Generator expressions can be very efficient, since they avoid the creation of a list entirely.

#### 2.4.3 Cons
Complicated comprehensions or generator expressions can be hard to read.

#### 2.4.4 Decision
Okay to use for simple cases. Each portion must fit on one line: mapping expression, for clause, 
filter expression. Multiple for clauses or filter expressions are not permitted. Use loops instead 
when things get more complicated.

Yes:
```python
result = [mapping_expr for value in iterable if filter_expr]

result = [
    {'key': value} for value in iterable
    if a_long_filter_expression(value)
]

result = [
    complicated_transform(x)
    for x in iterable if predicate(x)
]

descriptive_name = [
    transform({'key': key, 'value': value}, color='black')
    for key, value in generate_iterable(some_input)
    if complicated_condition_is_met(key, value)
]

result = []
for x in range(10):
    for y in range(5):
        if x * y > 10:
            result.append((x, y))

return {
    x: complicated_transform(x)
    for x in long_generator_function(parameter)
    if x is not None
}

squares_generator = (x**2 for x in range(10))

unique_names = {user.name for user in users if user is not None}

eat(
    jelly_bean for jelly_bean in jelly_beans
    if jelly_bean.color == 'black'
)
```

No:
```python
result = [
    complicated_transform(
        x, some_argument=x+1
    )
    for x in iterable if predicate(x)
]

result = [(x, y) for x in range(10) for y in range(5) if x * y > 10]

return (
    (x, y, z)
    for x in range(5)
    for y in range(5)
        if x != y
        for z in range(5)
            if y != z
)
```
### 2.5 Conditional Expressions
Okay for simple cases.

#### 2.5.1 Definition
Conditional expressions (sometimes called a “ternary operator”) are mechanisms that provide a 
shorter syntax for if statements. For example: x = 1 if cond else 2.

#### 2.5.2 Pros
Shorter and more convenient than an if statement.

#### 2.5.3 Cons
May be harder to read than an if statement. The condition may be difficult to locate if the expression is long.

#### 2.5.4 Decision
Okay to use for simple cases. Each portion must fit on one line: true-expression, if-expression, 
else-expression. Use a complete if statement when things get more complicated.

Yes:
```python
one_line = 'yes' if predicate(value) else 'no'
slightly_split = (
    'yes' if predicate(value) else 'no, nein, nyet'
)
the_longest_ternary_style_that_can_be_done = (
        'yes, true, affirmative, confirmed, correct'
        if predicate(value)
        else 'no, false, negative, nay'
)
```

No:
```python
bad_line_breaking = (
    'yes' if predicate(value) else
    'no'
)
portion_too_long = (
    'yes'
    if some_long_module.some_long_predicate_function(
        really_long_variable_name
    )
    else 'no, false, negative, nay'
)
```

### 2.6 Default Argument Values
Okay in most cases.

#### 2.6.1 Definition
You can specify values for variables at the end of a function’s parameter list, e.g., def foo(a, b=0):. 
If foo is called with only one argument, b is set to 0. If it is called with two arguments, b has the 
value of the second argument.

#### 2.6.2 Pros
Often you have a function that uses lots of default values, but on rare occasions you want 
to override the defaults. Default argument values provide an easy way to do this, without 
having to define lots of functions for the rare exceptions. As Python does not support overloaded 
methods/functions, default arguments are an easy way of “faking” the overloading behavior.

#### 2.6.3 Cons
Default arguments are evaluated once at module load time. This may cause problems if the 
argument is a mutable object such as a list or a dictionary. If the function modifies the 
object (e.g., by appending an item to a list), the default value is modified.

#### 2.6.4 Decision
Okay to use with the following caveat:

Do not use mutable objects as default values in the function or method definition.

Yes: 
```python
def foo(a, b=None):
    if b is None:
        b = []

def foo(a, b: Optional[Sequence] = None):
    if b is None:
        b = []

def foo(a, b: Sequence = ()):  # Empty tuple OK since tuples are immutable
         ...
```

No:  
```python
def foo(a, b=[]):
         ...

def foo(a, b=time.time()):  # The time the module was loaded???
         ...

def foo(a, b=FLAGS.my_thing):  # sys.argv has not yet been parsed...
         ...

def foo(a, b: Mapping = {}):  # Could still get passed to unchecked code
         ...
```

### 2.7 Properties
Use properties for accessing or setting data where you would normally have used simple, 
lightweight accessor or setter methods.

#### 2.7.1 Definition
A way to wrap method calls for getting and setting an attribute as a standard attribute access 
when the computation is lightweight.

#### 2.7.2 Pros
Readability is increased by eliminating explicit get and set method calls for simple attribute '
access. Allows calculations to be lazy. Considered the Pythonic way to maintain the interface of a 
class. In terms of performance, allowing properties bypasses needing trivial accessor methods 
when direct variable access is reasonable. This also allows accessor methods to be added in the 
future without breaking the interface.

#### 2.7.3 Cons
Can hide side effects much like operator overloading. Can be confusing for subclasses.

#### 2.7.4 Decision

Use properties in new code to access or set data where you would normally have used lightweight 
accessor or setter methods. Properties should be created with the @property decorator.

Inheritance with properties can be non-obvious if the property itself is not overridden. 
Thus, one must make sure that accessor methods are called indirectly to ensure methods overridden '
in subclasses are called by the property (using the template method design pattern).

Yes: 
```python
import math

class Square:
    """A square with two properties: a writable area and a read-only perimeter.

    To use:
        >>> sq = Square(3)
        >>> sq.area
        9
        >>> sq.perimeter
        12
        >>> sq.area = 16
        >>> sq.side
        4
        >>> sq.perimeter
        16
    """
    def __init__(self, side: float):
        self.side = side

    @property
    def area(self) -> float:
        """Area of the square."""
        return self._get_area()

    @area.setter
    def area(self, area: float):
        self._set_area(area)

    def _get_area(self) -> float:
        """Indirect accessor to calculate the 'area' property."""
        return self.side ** 2

    def _set_area(self, area: float):
        """Indirect setter to set the 'area' property."""
        self.side = math.sqrt(area)

    @property
    def perimeter(self) -> float:
        return self.side * 4
```

### 2.8 True/False Evaluations
Use the “implicit” false if at all possible.

#### 2.8.1 Definition
Python evaluates certain values as `False` when in a boolean context. A quick “rule of thumb” 
is that all “empty” values are considered false, so `0`, `None`, `[]`, `{}`, `''` all evaluate as 
`False` in a boolean context.

#### 2.8.2 Pros
Conditions using Python booleans are easier to read and less error-prone. In most cases, they’re also faster.

#### 2.8.3 Cons
May look strange to C/C++ developers.

#### 2.8.4 Decision
Use the “implicit” false if possible (e.g. `if foo:` rather than `if foo != []:`). There are a 
few caveats that you should keep in mind though:

* Always use `if foo is None:` (or `is not None`) to check for a `None` value. Foe example,
when testing whether a variable or argument that defaults to `None` was set to some other value. The other 
value might be a value that’s `False` in a boolean context!
* Never compare a boolean variable to `False` using `==`. Use `if not x:` instead. If you need to
distinguish `False` from `None` then chain the expressions, such as `if not x and x is not None:`.
* For sequences (strings, lists, tuples), use the fact that empty sequences are false, 
so `if seq:` and `if not seq:` are preferable to `if len(seq):` and `if not len(seq):` respectively.

When handling integers, implicit false may involve more risk than benefit (i.e., accidentally 
handling `None` as `0`). You may compare a value which is known to be an integer (and is not 
the result of `len()`) against the integer `0`.

Yes: 
```python
if not users:
    print('no users')

if foo == 0:
    self.handle_zero()

if foo % 10 == 0:
    self.handle_multiple_of_ten()

 def foo(bar=None):
    if bar is None:
        bar = []
```

No:  
```python
if len(users) == 0:
    print('no users')

if foo is not None and not foo:
    self.handle_zero()

if not foo % 10:
    self.handle_multiple_of_ten()

def foo(bar=None):
    bar = bar or []
```

Note that `'0'` (i.e. zero as string) evaluates to `True`.

### 2.9 Function and Method Decorators
Use decorators judiciously when there is a clear advantage. Avoid `staticmethod` and limit use of `classmethod`.

#### 2.9.1 Definition
Decorators for functions and methods (a.k.a. “the @ notation”). One common decorator is @property, 
used for converting ordinary methods into dynamically computed attributes. However, the decorator 
syntax allows for user-defined decorators as well. Specifically, for some function my_decorator, this:

```python
class C:
    @my_decorator
    def method(self):
        # method body ...
```

is equivalent to:

```python
class C:
    def method(self):
        # method body ...
    method = my_decorator(method)
```

#### 2.9.2 Pros
Elegantly specifies some transformation on a method; the transformation might eliminate 
some repetitive code, enforce invariants, etc.

#### 2.9.3 Cons
Decorators can perform arbitrary operations on a function’s arguments or return values, 
resulting in surprising implicit behavior. Additionally, decorators execute at import time. 
Failures in decorator code are pretty much impossible to recover from.

#### 2.9.4 Decision
Use decorators judiciously when there is a clear advantage. Decorators should follow the same 
import and naming guidelines as functions. Decorator pydoc should clearly state that the function 
is a decorator. Write unit tests for decorators.

Avoid external dependencies in the decorator itself (e.g. don’t rely on files, sockets, 
database connections, etc.), since they might not be available when the decorator runs 
(at import time, perhaps from pydoc or other tools). A decorator that is called with valid 
parameters should (as much as possible) be guaranteed to succeed in all cases.

Never use `staticmethod` unless forced to in order to integrate with an API defined in an 
existing library. Write a module level function instead.

Use `classmethod` only when writing a named constructor or a class-specific routine 
that modifies necessary global state such as a process-wide cache.

### 2.10 Type Annotated Code
You can annotate Python 3 code with type hints according to PEP-484, and type-check the 
code at build time with a type checking tool like pytype.

Type annotations can be in the source or in a stub pyi file. Whenever possible, annotations 
should be in the source. Use `.pyi` files for third-party or extension modules.

#### 2.10.1 Definition
Type annotations (or “type hints”) are for function or method arguments and return values:

```python
def func(foo: int) -> List[int]:
    ...
```

You can also declare a variable's type using similar PEP-526 syntax:

```python
foo: SomeType = some_func()
```

#### 2.10.2 Pros
Type annotations improve the readability and maintainability of your code. The type checker 
will convert many runtime errors to build-time errors.

#### 2.10.3 Cons
You will have to keep the type declarations up to date. You might see type errors that you 
think are valid code.

#### 2.10.4 Decision
You are strongly encouraged to enable Python type analysis when updating code. When adding 
or modifying public APIs, include type annotations and enable checking via pytype in the build 
system. As static analysis is relatively new to Python, we acknowledge that undesired side effects 
(such as wrongly inferred types) may prevent adoption by some projects. In those situations, 
authors are encouraged to add a comment with a TODO or link to a bug describing the issue(s) 
currently preventing type annotation adoption in the BUILD file or in the code itself as appropriate.

## 3 Python Style Rules

### 3.1 Black
Consistently formatted code promotes readability. Black is a third-party Python formatting 
tool self-described as "the uncompromising code formatter". It takes decisions about how code 
is formatted away from both Mycroft and its contributors by applying a predefined set of formatting 
rules to the code.  This provides freedom from minutiae, such as using single or double quotes, 
when writing and reviewing code.

Code repositories in the MycroftAI GitHub organization will have pre-commit hooks defined
that "black" the code before committing it.  This will prevent extra commits that do nothing
but reformat code.

Black makes opinionated decisions about:
* Line length
* Line wrapping
* White space (i.e. indentation, blank lines, etc.)
* Comments
* Call chains
* Parentheses

For more information about Black, see the [documentation](https://black.readthedocs.io/en/stable/).

### 3.2 Semicolons
Do not terminate your lines with semicolons, and do not use semicolons to put two statements on the same line.

### 3.3 License boilerplate
Every file should contain license boilerplate at the top of the file. Choose the appropriate  
boilerplate for the license used by the project (for example, Apache 2.0, BSD, LGPL, GPL).

### 3.3 Docstrings
Python uses docstrings to document code. A docstring is a string that is the first statement 
in a package, module, class or function. These strings can be extracted automatically through 
the __doc__ member of the object and are used by pydoc. (Try running pydoc on your module to 
see how it looks.). 

[PEP257](https://www.python.org/dev/peps/pep-0257/) dictates much of the formatting rules
for module, function, and method docstrings.

#### 3.3.2 Module level docstrings
Each module must have a docstring describing the contents and usage of the module.  This
docstring appears immediately following the licence boilerplate. 

Example:
```python
"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
```
#### 3.3.3 Functions and Methods
In this section, “function” means a method, function, or generator.

All functions must have a docstring.  It should give enough information to write a call 
to the function without reading the function’s code. The docstring should describe the 
function’s calling syntax and its semantics, but generally not its implementation details, 
unless those details are relevant to how the function is to be used. For example, a function 
that mutates one of its arguments as a side effect should note that in its docstring. Otherwise, 
subtle but important details of a function’s implementation that are not relevant to the caller 
are better expressed as comments alongside the code than within the function’s docstring.

The docstring should be descriptive-style (`"""Fetches rows from a Bigtable."""`) rather than 
imperative-style (`"""Fetch rows from a Bigtable."""`). The docstring for a @property data descriptor 
should use the same style as the docstring for an attribute or a function argument 
(`"""The Bigtable path."""`, rather than `"""Returns the Bigtable path."""`).

A method that overrides a method from a base class may have a simple docstring sending 
the reader to its overridden method’s docstring, such as `"""See base class."""`. The rationale 
is that there is no need to repeat in many places documentation that is already present in the 
base method’s docstring. However, if the overriding method’s behavior is substantially different 
from the overridden method, or details need to be provided (e.g., documenting additional side effects), 
a docstring with at least those differences is required on the overriding method.

Certain aspects of a function should be documented in special sections, listed below. 
Each section begins with a heading line, which ends with a colon. All sections other than 
the heading should maintain a hanging indent of two or four spaces (be consistent within a file). 
These sections can be omitted in cases where the function’s name and signature are informative 
enough that it can be aptly described using a one-line docstring.

##### Arguments
The `Args:` section lists each parameter by name. A description should follow the name, 
and be separated by a colon followed by either a space or newline. If a function accepts *foo 
(variable length argument lists) and/or **bar (arbitrary keyword arguments), they should 
be listed as *foo and **bar.

##### Return Value
The `Returns:` (or `Yields:` for generators) section describes the type and semantics of the return value. 
If the function only returns None, this section is not required. It may also be omitted if the 
docstring starts with Returns or Yields (e.g. `"""Returns row from Bigtable as a tuple of strings."""`) 
and the opening sentence is sufficient to describe return value.

##### Raised Exceptions
The `Raises:` section lists all exceptions that are relevant to the interface followed by a description. 
Use a similar exception name + colon + space or newline and hanging indent style as described in 
`Args:`. You should not document exceptions that get raised if the API specified in the docstring 
is violated (because this would paradoxically make behavior under violation of the API part of the API).

##### Example
```python
def fetch_small_table_rows(
    table_handle: smalltable.Table, keys: Sequence[Union[bytes, str]],
    require_all_keys: bool = False,
) -> Mapping[bytes, Tuple[str]]:
    """Fetches rows from a Smalltable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by table_handle.  String keys will be UTF-8 encoded.

    Args:
        table_handle: An open small_table.Table instance.
        keys: A sequence of strings representing the key of each table
          row to fetch.  String keys will be UTF-8 encoded.
        require_all_keys: Optional; If require_all_keys is True only
          rows with values set for all keys will be returned.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {b'Serak': ('Rigel VII', 'Preparer'),
         b'Zim': ('Irk', 'Invader'),
         b'Lrrr': ('Omicron Persei 8', 'Emperor')}

        Returned keys are always bytes.  If a key from the keys argument is
        missing from the dictionary, then that row was not found in the
        table (and require_all_keys must have been False).

    Raises:
        IOError: An error occurred accessing the small_table.
    """
```
#### 3.3.4 Classes
Classes should have a docstring below the class definition describing the class. If your 
class has public attributes, they should be documented here in an Attributes section and 
follow the same formatting as a function’s Args section.

Example:
```python
class SampleClass:
    """Summary of class here.

    More class information....
    Even more class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam: bool = False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""
```

### 3.4 Comments

#### 3.4.1 Block and Inline Comments
The final place to have comments is in tricky parts of the code. If you’re going to have 
to explain it at the next code review, you should comment it now. 

Complicated operations get a few lines of comments before the operations commence. 

```python
# We use a weighted dictionary search to find out where i is in
# the array.  We extrapolate position based on the largest num
# in the array and the array size and then do binary search to
# get the exact number.
```

Non-obvious operations get comments at the end of the line. To improve legibility, these 
comments should start at least 2 spaces away from the code with the comment character #, 
followed by at least one space before the text of the comment itself.

```python
if foo & (foo - 1) == 0:  # True if foo is 0 or a power of 2.
```

Never describe the code. Assume the person reading the code knows Python (though not what 
you’re trying to do) better than you do.

```python
# BAD COMMENT: Now go through the array and make sure whenever foo occurs
# the next element is foo + 1
```

#### 3.4.2 TODO Comments
Use TODO comments for code that is temporary, a short-term solution, or a placeholder for 
a enhancement that will break backwards compatibility.

A TODO comment begins with the string TODO in all caps followed by a colon. If the comment
is regarding a breaking change, the major version it will appear in.  This is followed by an explanation of what there is to do.

The purpose is to have a consistent TODO format that can be searched to find out how to get more details. 
A TODO is not a commitment that the person referenced will fix the problem. Thus, when you create a TODO, 
it is almost always your name that is given.

```python
# TODO: 21.08 Remove in favor of new way.

# TODO: Replace this hack with...
```

### 3.5 Imports

Imports should be on separate lines; there are exceptions for typing imports.

Yes: 
```python
import os
import sys
from typing import Mapping, Sequence
```

No:  
```python
import os, sys
```

Imports are always put at the top of the file, just after any module comments and docstrings 
and before module globals and constants. Imports should be grouped as follows:

* Python `__future__` imports
* Python standard library imports
* Blank line
* Third party library imports
* Blank line
* Application specific imports
* Imports from within the current package

Within each grouping, imports should be sorted lexicographically, ignoring case, according 
to each module’s full package path (the path in from path import ...).

Example:
```python
import collections
import queue
import sys

from absl import app
from absl import flags
import bs4
import cryptography
import tensorflow as tf

from book.genres import scifi
from myproject.backend import huxley
from myproject.backend.hgwells import time_machine
from myproject.backend.state_machine import main_loop
from otherproject.ai import body
from otherproject.ai import mind
from otherproject.ai import soul
```

### 3.6 Naming
Function names, variable names, and filenames should be descriptive; eschew abbreviation. 
In particular, do not use abbreviations that are ambiguous or unfamiliar to readers outside 
your project, and do not abbreviate by deleting letters within a word.

* Use `snake_case` for module, package, function, variable and parameter names
* Use `TitleCase` for class and exception names.
* Use `CAPS_WITH_UNDERSCORES` for global constants.

#### 3.6.1 Names to Avoid 
* Single character names (except for `i` for an index in a loop or iterator or `e` as an 
exception identifier in try/except statements). Please be mindful not to abuse single-character naming. 
Generally speaking, descriptiveness should be proportional to the name’s scope of visibility. 
For example, `i` might be a fine name for 5-line code block but within multiple nested scopes,
it is likely too vague.
* Dashes (-) in any package/module name
* `__double_leading_and_trailing_underscore__` names (reserved by Python)
* Iffensive terms
* Names that needlessly include the type of the variable (for example: id_to_name_dict)

#### 3.6.2 Naming Conventions=
“Internal” means internal to a module, or protected or private within a class.

Prepending a single underscore (`_`) has some support for protecting module variables and 
functions (linters will flag protected member access).

Prepending a double underscore (`__` a.k.a. “dunder”) to an instance variable or method 
effectively makes the variable or method private to its class (using name mangling); 
we discourage its use as it impacts readability and testability, and isn’t really private. 
Prefer a single underscore.

Place related classes and top-level functions together in a module. Unlike Java, there is 
no need to limit yourself to one class per module.

### 3.6.3 File Naming

Python filenames must have a .py extension and must not contain dashes (`-`). This allows 
them to be imported and unit tested. If you want an executable to be accessible without the 
extension, use a symbolic link or a simple bash wrapper containing exec "$0.py" "$@".

### 3.7 Main
In Python, pydoc as well as unit tests require modules to be importable. If a file is meant 
to be used as an executable, its main functionality should be in a main() function, and your 
code should always check `if __name__ == '__main__'` before executing your main program, 
so that it is not executed when the module is imported.

Example:
```python
def main():
    ...

if __name__ == '__main__':
    main()
```

All code at the top level will be executed when the module is imported. Be careful not to call 
functions, create objects, or perform other operations that should not be executed when the file is being imported.

### 3.8 Function Length
Prefer small and focused functions.

We recognize that long functions are sometimes appropriate, so no hard limit is placed on 
function length. If a function exceeds about 30 lines, think about whether it can be broken 
up without harming the structure of the program.

Even if your long function works perfectly now, someone modifying it in a few months may 
add new behavior. This could result in bugs that are hard to find. Keeping your functions 
short and simple makes it easier for other people to read and modify your code.

You could find long and complicated functions when working with some code. Do not be intimidated 
by modifying existing code: if working with such a function proves to be difficult, you find 
that errors are hard to debug, or you want to use a piece of it in several different contexts, 
consider breaking up the function into smaller and more manageable pieces.

### 3.9 Type Annotations

#### 3.9.1 General Rules
* Familiarize yourself with [PEP-484](https://www.python.org/dev/peps/pep-0484).
* If any other variable or a returned type should not be expressed, use Any.
* You are not required to annotate all the functions in a module. At least annotate your public APIs.
* Use judgment to get to a good balance between safety and clarity on the one hand, and flexibility on the other.
* Annotate code that is prone to type-related errors (previous bugs or complexity).
* Annotate code that is hard to understand.
* Annotate code as it becomes stable from a typing perspective. In many cases, you can annotate 
all the functions in mature code without losing too much flexibility.

#### 3.9.2 Default Values
As per PEP-008, use spaces around the = only for arguments that have both a type annotation and a default value.

Yes:
```python
def func(a: int = 0) -> int:
  ...
```

No:
```python
def func(a:int=0) -> int:
  ...
```

#### 3.9.3 NoneType
In the Python type system, NoneType is a “first class” type, and for typing purposes, 
None is an alias for NoneType. If an argument can be None, it has to be declared! You can 
use Union, but if there is only one other type, use Optional.

Use explicit Optional instead of implicit Optional. Earlier versions of PEP 484 allowed 
`a: str = None` to be interpreted as `a: Optional[str] = None`, but that is no longer 
the preferred behavior.

Yes:
```python
def func(a: Optional[str], b: Optional[str] = None) -> str:
  ...

def multiple_nullable_union(a: Union[None, str, int]) -> str:
  ...
```

No:
```python
def nullable_union(a: Union[None, str]) -> str:
  ...
def implicit_optional(a: str = None) -> str:
  ...
```

#### 3.9.4 Conditional Imports
Use conditional imports only in exceptional cases where the additional imports needed for 
type checking must be avoided at runtime. This pattern is discouraged; alternatives such 
as refactoring the code to allow top level imports should be preferred.

Imports that are needed only for type annotations can be placed within an `if TYPE_CHECKING:` block.

Conditionally imported types need to be referenced as strings, to be forward compatible with 
Python 3.6 where the annotation expressions are actually evaluated.

Only entities that are used solely for typing should be defined here; this includes aliases. 
Otherwise, it will be a runtime error, as the module will not be imported at runtime.

The block should be right after all the normal imports.

There should be no empty lines in the typing imports list.

Sort this list as if it were a regular imports list.

Example: 
```python
import typing
if typing.TYPE_CHECKING:
  import sketch

def f(x: "sketch.Sketch"): 
    ...
```

#### 3.9.5 Circular Dependencies
Circular dependencies that are caused by typing are code smells. Such code is a good candidate 
for refactoring. Although technically it is possible to keep circular dependencies, various 
build systems will not let you do so because each module has to depend on the other.

Replace modules that create circular dependency imports with `Any`. Set an alias with a meaningful 
name, and use the real type name from this module (any attribute of `Any` is `Any`). Alias definitions 
should be separated from the last import by one line.

Example: 
```python
from typing import Any

some_mod = Any  # some_mod.py imports this module.
...

def my_method(self, var: "some_mod.SomeType") -> None:
  ...
```

#### 3.9.6 Generics
When annotating, prefer to specify type parameters for generic types; otherwise, the generics’ 
parameters will be assumed to be `Any`.

Examples:
```python
def get_names(employee_ids: List[int]) -> Dict[int, Any]:
  ...

# These are both interpreted as get_names(employee_ids: List[Any]) -> Dict[Any, Any]
def get_names(employee_ids: list) -> Dict:
  ...

def get_names(employee_ids: List) -> Dict:
  ...
```

## 4 Parting Words
BE CONSISTENT.

If you’re editing code, take a few minutes to look at the code around you and determine its 
style. If they use spaces around all their arithmetic operators, you should too. If their 
comments have little boxes of hash marks around them, make your comments have little boxes 
of hash marks around them too.

The point of having style guidelines is to have a common vocabulary of coding so people can 
concentrate on what you’re saying rather than on how you’re saying it. We present global style 
rules here so people know the vocabulary, but local style is also important. If code you add 
to a file looks drastically different from the existing code around it, it throws readers out 
of their rhythm when they go to read it. Avoid this.
