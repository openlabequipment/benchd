from setuptools import setup

setup(
	name='benchctl',
	version='0.1',
	py_modules=['benchctl'],
	install_requires=[
		'Click'
	],
	entry_points='''
		[console_scripts]
		benchctl=benchctl:cli
	''',
)