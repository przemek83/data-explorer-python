from setuptools import setup, find_packages

setup(name="data_explorer",
      version='0.0.1',
      description='Small tool for aggregating and grouping data.',
      packages=find_packages(),
      install_requires=['pytest'],
      python_requires='>=3.7',
      url="https://github.com/przemek83/data-explorer-python")
