# Introduction
This file explains how to contribute work to this project.

# Development setup

1. Install [Git](https://git-scm.com/).
1. Install [Python 2.7](https://www.python.org/downloads/). It's strongly recommended to use
[virtualenv](https://virtualenv.pypa.io/en/stable/) to manage your Python environments, to prevent different Python
projects on your machine from interfering with each other (because they use different versions of Python or different
versions of the same library).
1. Install the required packages, e.g. Mockito, by running `pip install -r requirements.txt` from the project directory.

# Getting the source code

1. Create a [GitHub](https://github.com/) account if you don't already have one.
1. [Create your own fork](https://help.github.com/articles/fork-a-repo/) of the [lwotai project](https://github.com/tharkad/lwotai).
1. Clone your fork onto your development machine.

# Coding style

This section provides guidance about how to structure and format the code.

## Formatting

In general, try to adhere to the industry-standard [PEP 8](https://www.python.org/dev/peps/pep-0008/) style. This will
make it easy for experienced Python developers to understand the code.

## Testing

* Write unit tests for the code you are adding or changing. This allows other developers to refactor the code without
fear of breaking it.
* Where code seems untestable (e.g. it selects a country at random), refactor that code to remove the randomness, e.g.
change the method to accept a mock randomizer whose behaviour you can control.
* Use [Mockito](https://github.com/kaste/mockito-python) as the mocking library.

# Submitting changes

When your change is done, e.g. fully covered by unit tests and properly formatted,
[create a pull request](https://help.github.com/articles/creating-a-pull-request/) on GitHub. Mike (the project owner)
will review your change and merge it into his fork if he's happy with it.
