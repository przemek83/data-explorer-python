# About project
Small tool for aggregating and grouping data. Written in Python, mimicking functionality of my older C++ data-explorer project. Created to refresh Python skills, have some fun, exercise TDD and compare speed of C++/Go/Python versions.

# Usage 
`data_explorer.py [-h] file {avg,min,max} aggregation grouping`  
Where:  
+ `file` - name of file with data to load,  
+ `{avg,min,max}` - type of operation, use one of those,  
+ `aggregation` - name of column used for aggregating data,  
+ `grouping` - name of column used for grouping data.

Example usage:  
`python data_explorer.py sample.txt avg score first_name`  

Example output:
```
Data loading completed in 0.000227s
Operation completed in 0.000011s
Results:  {'tim': 8.0, 'tamas': 5.5, 'dave': 8.0}
```

# Input data format
Input data need to have following structure:  
```
<column 1 name>;<column 2 name>;<column 3 name>  
<column 1 type>;<column 2 type>;<column 3 type>  
<data 1 1>;<data 2 1>;<data 3 1> 
...  
<data 1 n>;<data 2 n>;<data 3 n> 
```
Where column type can be `string` or `integer`.  

Example data:
```
first_name;age;movie_name;score
string;integer;string;integer
tim;26;inception;8
tim;26;pulp_fiction;8
tamas;44;inception;7
tamas;44;pulp_fiction;4
dave;0;inception;8
dave;0;ender's_game;8
```
Such simple and strict format of data was used for simplicity of parsing.

# Tox
I've used Tox for static analysis and testing. Following tools are used:  
+ flake8  
+ mypy  
+ pylint  
+ prospector  
+ bandit
+ cov-report

To launch tox sequence of checks install it and type `tox` in project dir.