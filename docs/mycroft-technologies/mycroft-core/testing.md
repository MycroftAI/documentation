---
description: An overview of the test frameworks used by mycroft-core.
---

# Testing

## Unit Tests

Mycroft-core unit tests are located in `mycroft-core/test/unittests`

These are created using the [`unittest`](https://docs.python.org/3/library/unittest.html) package from the Python standard library.

### Test runner

A helper command is provided in `mycroft-core/bin` to enable quick and simple access to the test runner. It is assumed that this directory is on your `$PATH` . 

If that is not the case, prepend all `mycroft-*` commands with the path to your `mycroft-core/bin` directory or run the tests manually. 

#### Execute all tests

To execute all tests run:

```text
mycroft-start unittest
```

#### Execute single test

To execute a single test file run:

```text
mycroft-start singlueunittest path/to/test/file.py
```

The second argument points to the test file you wish to execute. Note that this is relative to your `mycroft-core` installation.

If I was working on the audio utilities, I might run:

```text
mycroft-start singlueunittest test/unittests/audio/test_utils.py
```

#### Manually run tests

The `mycroft-start` helper commands are a convenience wrapper. They activate the Python virtual environment and run pytest.

The equivalent commands to run all tests would be:

```shell
cd ~/mycroft-core
source .venv/bin/activate
pytest
```

## Integration Tests

The Mycroft integration test suite is called Voight Kampff. Currently this does explicitly cover mycroft-core, however Skills are tested, which indirectly tests a range of Mycroft's technologies.

For more detail on Voight Kampff see:

{% page-ref page="../../skill-development/voight-kampff/" %}



