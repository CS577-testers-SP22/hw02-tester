# hw02-tester

Additional tests for CS577 Spring 2022 HW02: Asymptotic Analysis & Graphs

## Changes

### V1.4
 - Add second sample input from Canvas

### V1.3
 - Add explicit test for following input order instead of sorting again

### V1.2
 - Check for whitespace since Gradescope cares about that

### V1.1
 - Add sample input on Canvas as test0
 - Show difference between expected and user output
 - Run `make build` before running tests

### V1.0
 - Initial commit

## Usage

Download [tests.json](tests.json) and [hw02-test.py](hw02-test.py) into the directory that contains your `Makefile` and code. Your need to be able to run your code using `$ make build && make run` in that directory.

The contents of your directory should look like this:

```shell
.
├── Makefile
├── DFS.py | DFS.class | DFS | etc
├── tests.json
└── hw02-test.py
```

To run the tests, do

```shell
$ python3 hw02-test.py
```

`tqdm` is used to track progress. If you don't have it installed, you'll need to do `$ pip install tqdm`.

## Additional Information

 - If you want to see how the tests were generated, or generate your own, see [generate_tests.py](generate_tests.py)
 - These are not the actual tests Gradescope uses. I just generated random graph inputs, and made sure the outputs matched for a Java version and a Python version that each passed all Gradescope tests.

## Disclaimer

These tests are not endorsed or created by anyone working in an official capacity with UW Madison or any staff for CS577. The tests are make by students, for students.

By running any of the code in this repository, you are executing code you downloaded from the internet. Back up your files and take a look at what you are running first.

If you have comments / questions / suggestions, create an issue at [https://github.com/CS577-testers-SP22/hw02-tester/issues](https://github.com/CS577-testers-SP22/hw02-tester/issues) or ask in the Discord at [https://discord.gg/CTFKYaUePf](https://discord.gg/CTFKYaUePf). If you want to contribute, submit a pull request or ask to join the organization in Discord.
