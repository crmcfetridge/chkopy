from setuptools import setup, find_packages

setup(
	name='chkopy',
	version='1.2.0b1',
	description='A colleciton of checksum functions and a command line tool.',
	author='Christopher McFetridge',
	author_email='cmcfetri@willamette.edu',
	classifiers=[
		'Development Status :: 4 - Beta',
		'Programming Language :: Python :: 2.7',
		],
	keywords='checksum copy recusive',
	scripts=['bin/chkopy'],
	install_requires=[
		'argparse',
		'hashlib',
		'os',
		'shutil'
		],
)