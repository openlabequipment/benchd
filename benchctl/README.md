# benchctl
Benchctl is a utility for interacting with benchd and benchd-aggregator servers to:
* fetch data
* program experiments
* control instruments.

Benchctl is also used to configure and administrate benchd instances.

## Developing
Do `virtualenv venv` in the root of the project (the `benchd/` directory); activate it with `. venv/bin/activate`.

In the `benchctl/` directory, `pip install -r requirements.text` and then `pip install --editable .`; you can now develop new code and simply run `benchctl`.
