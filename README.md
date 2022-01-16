# Strawberry PM
A package manager to install commands for raspberry pi.
# depends on...
* python3
* wget
* git
# TODO
* ~~Make only run on Rpi~~
* ~~Add packages (other than debug)~~
* Get some packages!!!
If you want to add your package file to the package list go to my [pmlist](https://github.com/Ccode-lang/pmlist) repo.
# Install
> ⚠️ The install will not work on systems other than linux and the command installed will crash on your system if it is not raspberry pi.  

First install the required packages. (They should already be installed)  
Next enter the folder and run the setup script.  Once this is done run `strawberry install debug`.  Then run `debug`.  
if you see three strawberries your installation works.
# If an install fails
* Run `strawberry uppak` and try again.
* If you still have problems replace `~/.strawberry/main/package.py` with the newest verion from github.
* If that still does not fix it report a bug.
