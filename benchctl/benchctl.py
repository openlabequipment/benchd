import click

import repl as benchrepl


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--debug/--no-debug', default=False)
def cli(debug):
	"""Benchctl is a utility for interacting with benchd and benchd-aggregator
	servers to fetch data, program experiments, and control instruments.

	It is additionally used to configure and administrate benchd instances.
	"""

@cli.command(short_help='start a repl to interact with benchd servers')
def repl():
	"""Starts a REPL which can be used to interact with and administrate
	both benchd and benchd-aggregator servers."""
	benchrepl.run()