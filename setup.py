from setuptools import setup, find_packages

setup(
	name="website",

	version="1.0.0",

	description="Flask project example.",

	author="lymagics",
	author_email="viacheslav.lymanskyi@nure.ua",

	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
	install_requires=['flask', 'sqlalchemy', 'requests'],

	package_data={'': ['static/*', 'templates/*']}
)