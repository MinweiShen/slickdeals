from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='slickdeals',
      version='1.0',
      description='Slickdeals command line tool',
      long_description=readme(),
      url='https://github.com/MinweiShen/slickdeals',
      author='Minwei Shen',
      author_email='minweishen1991@gmail.com',
      packages=['slickdeals'],
      install_requires=[
          'requests',
          'beautifulsoup',
      ],
      entry_points={
          'console_scripts': ['slickdeals=slickdeals.slickdeals:main'],
      },
      zip_safe=False
      )