# Tacit (generation 3) <a href="https://tacit-lang.github.io/"><img width="30" height="30" src="art/favicon.svg?raw=true"/></a>

## About

Tacit is a friendly programming language that uses **ergonomics**, **determinism**, and **efficiency** to help you express your creativity.

- With powerful features like **significant whitespace** and **functional programming**, the Tacit language works together with you and helps you out at every step.

- The Tacit community is here to help too! We know how tough coding can be, and we do our best to make this a safe space where **kindness** and **empathy** are the norm.

### The code here

The code here in this Git repo is a temporary interpreter (in Python), created to help bootstrap a self-recursive Tacit compiler.

## Developing

### Prerequisites

You'll need [Python 3.7.2](https://www.python.org/downloads/release/python-372/) and [Pipenv](https://pipenv.readthedocs.io/en/latest/).

### Initial setup

These commands will get the code and get you into a running Python environment:

```bash
git clone https://github.com/tacit-lang/tacit-gen3-python.git
cd tacit-gen3-python
pipenv install
pipenv shell
```

### Workflow

- `pytest-watch` to start testing code changes
- `pipenv install package==version` to install new packages

## License

This project is released under the MIT License (see [LICENSE.md](LICENSE.md) for details).