---
description: >-
  Skills have access to both persistent and temporary namespaced filesystems
  independent of the Skill's root directory.
---

# Filesystem access

Many Skills may want access to parts of the filesystem. To account for the many different platforms that can run Mycroft there are three locations that a Skill can utilize.

* Persistent filesystem
* Temporary cache
* Skill's own root directory

## Persistent Files

When your Skill needs to store some data that will persist over time and cannot easily be rebuilt, there is a persistent filesystem namespaced to your Skill.

### Reading and writing to files

This uses the standard Python `open()` method to read and write files. It takes two parameters:

* filename \(str\) - a path relative to the namespace. subdirs not currently supported.
* mode \(str\) – a file handle mode \[r, r+, w, w+, rb, rb+, wb+, a, ab, a+, ab+, x\]

Example:

```python
    def write_line_to_file(self, filename, line):
        """Write a single line to a file in the Skills persistent filesystem."""
        with self.file_system.open(filename, "w") as my_file:
            my_file.write(line)

    def read_file(self, filename):
        """Read the contents of a file in the Skills persistent filesystem."""
        with self.file_system.open(filename, "r") as my_file:
            return my_file.read()
```

### Check if a file exists

Quick method to see if some file exists in the namespaced directory.

Example:

```python
        filename = "example.txt"
        with self.file_system.open(filename, "w") as my_file:
            my_file.write("Hello world")
        self.log.info(self.file_system.exists(filename))
        # True
        self.log.info(self.file_system.exists("new.txt"))
        # False
```

### Get the path of the namespaced directory.

`self.file_system.path` is a member value containing the root path of the namespace. However it is recommended that you use the `self.file_system.open()` method to read and write files.

Example:

```python
from mycroft import MycroftSkill, intent_handler

class FileSystemSkill(MycroftSkill):

    def initialize(self):
        """Log the path of this Skills persistent namespace."""
        self.log.info(self.file_system.path)

def create_skill():
    return FileSystemSkill()
```

### Example Skill

```python
from mycroft import MycroftSkill, intent_handler

class FileSystemSkill(MycroftSkill):

    def initialize(self):
        """Perform initial setup for the Skill.

        For this example we do four things:
        1. Log the path of this directory.
        2. Write to a file in the directory.
        3. Check that our file exists.
        4. Read the contents of our file from disk.
        """
        filename = "example.txt"
        self.log.info(self.file_system.path)
        self.write_line_to_file(filename, "hello world")
        self.log.info(self.file_system.exists(filename))
        self.log.info(self.read_file(filename))

    def write_line_to_file(self, filename, line):
        """Write a single line to a file in the Skills persistent filesystem."""
        with self.file_system.open(filename, "w") as my_file:
            my_file.write(line)

    def read_file(self, filename):
        """Read the contents of a file in the Skills persistent filesystem."""
        with self.file_system.open(filename, "r") as my_file:
            return my_file.read()

def create_skill():
    return FileSystemSkill()
```

## Temporary Cache

Skills can create a directory for caching temporary data to speed up performance.

This directory will likely be part of a small RAM disk and may be cleared at any time. So code that uses these cached files must be able to fallback and regenerate the file.

### Example Skill

```python
from os.path import join
from mycroft import MycroftSkill, intent_handler
from mycroft.util import get_cache_directory

class CachingSkill(MycroftSkill):

    def initialize(self):
        """Perform initial setup for the Skill.

        For this example we do four things:
        1. Get a cache directory namespaced for our Skill.
        2. Define a file path for the cache_file.
        3. Write some data to the cache_file
        4. Log the path of the cache_file
        4. Log the contents of the cache_file.
        """
        cache_dir = get_cache_directory('CachingSkill')
        self.cache_file = join(cache_dir, "myfile.txt")
        self.cache_data()
        self.log.info(self.cache_file)
        self.log.info(self.read_cached_data())

    def cache_data(self):
        with open(self.cache_file, "w") as cache_file: 
            cache_file.write("Some cached data") 

    def read_cached_data(self):
        with open(self.cache_file, "r") as cache_file: 
            return cache_file.read()

def create_skill():
    return CachingSkill()
```

## Skill Root Directory

```python
self.root_dir
```

This member variable contains the absolute path of a Skill’s root directory e.g. `~.local/share/mycroft/skills/my-skill.me/`.

Generally Skills should not modify anything within this directory. Modifying anything in the Skill directory will reload the Skill. This will also prevent the Skill from updating as we do not want to overwrite changes made during development. It is also not guaranteed that the Skill will have permission to write to this directory.

