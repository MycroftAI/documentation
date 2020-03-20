# Test Runner

## Setup the tests
Voight Kampff is designed to test not only your Skill in isolation, but also ensuring Skills operate as expected when co-existing with different sets of Skills from the Marketplace.

Parameters for this testing can be set through a YAML configuration or using flags when running the tests.

### YAML Configuration
The configuration of these tests consists of three main settings:
* Platform (string) - the platform or device type that the tests are being run on. This must be one of [default, mycroft_mark_1, mycroft_mark_2, mycroft_mark_2pi, picroft, kde, respeaker]
* Test Skills (list) - the testrunner will execute the tests for these Skills
* Extra Skills (list) - additional Skills that will be installed prior to the test. Tests from these Skills will not be executed.

```YAML
platform: mycroft_mark_1
tested_skills:
- mycroft-hello-world
- mycroft-personal
extra_skills:
- cocktails
```

The example above shows that this tests suite:
- is being run on a Mark 1 device
- the tests from the Hello World and Personal Skills will be included
- before running the tests, the Cocktails Skill be installed if it isn't already on the system.

By default the test runner will use the configuration stored at: `mycroft-core/test/integrationtests/voight_kampff/default.yml`.

You can specify an alternate file when running the tests using the `-c` flag. As described in [Running the tests](#running-the-tests)


### Manually running the Test Setup
This step will happen automatically when you run the tests. However if you want to trigger this independently, you can call the Python Module from within the Mycroft virtual environment.
```bash
cd ~/mycroft-core
source .venv/bin/activate
python -m test.integrationtests.voight_kampff.test_setup
deactivate # to exit the virtual environment
```

## Running the tests
If the Mycroft helper commands (located in `mycroft-core/bin/`) have been included on your `$PATH` you can initiate the test runner using either:
```bash
mycroft-start vktests
```
or
```bash
mycroft-skill-testrunner vktests
```

### Commandline options
Commandline flags can be used to set or override configuration and runtime options.

```
  -p PLATFORM, --platform PLATFORM            
        Set the PLATFORM or device type, must be one of:[default, kde,
        mycroft_mark_1, mycroft_mark_2, mycroft_mark_2pi, picroft, respeaker].
  -t SKILL,SKILL, --test-skills SKILL,SKILL
        Test the provided comma-separated list of SKILLS.
  -e PATTERN, --exclude PATTERN
        Don't run feature files matching regular expression PATTERN.
  -i PATTERN, --include PATTERN
        Only run feature files matching regular expression PATTERN.
  -s SKILL,SKILL, --extra-skills SKILL,SKILL
        Ensure the provided comma-separated list of SKILLS are installed.
  -r INT, --random-skills INT
        Install INT random Skills before the test is run.
        WARNING: These Skills will be installed and not automatically removed.
  -d DIR, --skills-dir
        Set the directory for Skills on this system.
  -c FILE, --config FILE
        Use the provided YAML configuration file for the test parameters.
  -o FILE, --outfile FILE
        Write to specified file instead of stdout.
  -f FORMAT, --format FORMAT
        Specify a formatter. If none is specified the default formatter is used.
        Pass "--format help" to get a list of available formatters.
  --stop
        Stop running tests at the first failure.
  --tags TAG_EXPRESSION
        Only execute features or scenarios with tags matching TAG_EXPRESSION.
        Pass "--tags-help" for more information.
  -w, --wip
        Only run scenarios tagged with "wip". Additionally: use the "plain"
        formatter, do not capture stdout or logging output and stop at the
        first failure.
  -h, --help
        Display this help message
```


Examples:
```bash
mycroft-skill-testrunner vktests -c /path/to/your/configuration.yml
```

### Manually running the Test Runner
You can alternatively run the test suite using the provided Shell script:
```
cd ~/mycroft-core/test/integrationtests/voight_kampff
./run_test_suite.sh
```
