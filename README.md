# Implementation of system commands: cp and ps

~~ *This project was implemented in April 2015* ~~

To launch the scripts, assign first the execute permission to them.

## cp

*mycopy.py* equals the **cp** command and takes two arguments *from* and *to* for copying repertories and regular files from the *from* folder into the *to* folder:
```
python mycopy.py frome to
```

## ps

To launch the *ps* script, execute the bash script:
```
./test.sh
```
Then follow the instructions in the terminal.


This script only manages the following options and does not currently allow to combine them:
* **-u** (does not yet manage all the information to be displayed)
* **-a**
* **-x**
