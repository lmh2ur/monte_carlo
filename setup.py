from setuptools import setup, find_packages

setup(
    name = 'monte_carlo_package',
    version = '1.0.0',
    url = 'https://github.com/lmh2ur/monte_carlo',
    author = 'Leah Hogenmiller',
    author_email = 'lmh2ur@virginia.edu',
    description='This package contains a monte carlo simulator',
    packages = find_packages(),
    install_requires = ['pandas', 'numpy'],
)