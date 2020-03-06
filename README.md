# About project
Small tool for aggregating and grouping data. Written in Python, mimicking functionality of my older C++ data-explorer project. Created to refresh Python skills, have some fun, exercise TDD and compare speed of C++/Go/Python versions.

# Usage: 
data_explorer.py [-h] file {avg,min,max} aggregation grouping  
Where:  
+ file - name of file with data to load,  
+ {avg,min,max} - type of operation, use one of those,  
+ aggregation - name of column used for aggregating data,  
+ grouping - name of column used for grouping data.

# Input data format
Input data need tgo have following structure:  
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