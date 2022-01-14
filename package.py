import os
import sys
import requests
# import angledat
home = os.path.expanduser('~')
module = os.path.join(home, '.strawberry', 'lib')
sys.path.append(module)
import angledat as ang

args = sys.argv


def help():
    print("install : install a package")
    print("remove  : remove a package")
    print("uppak   : update package list")
    sys.exit()



if not os.name == "posix":
    print("Please run on a supported machine")
    sys.exit()

if len(args) == 1:
    help()

if args[1] == "install":
    try:
        filler = args[2]
    except:
        print("Second argument not given.")
        sys.exit()
    list = ang.read_dict(os.path.join(home, '.strawberry', 'pmlist', 'list.txt'))
    if args[2] in list:
        os.chdir(os.path.join(home, '.strawberry', 'pakbin'))
        package = list[args[2]]
        if not os.path.exists(args[2]):
            exit = os.system("wget " + package + " >~/.strawberry/wget.log 2>&1")
            if exit == 0:
                os.system("chmod +x " + args[2])
                print("Package installed")
            else:
                print("Failed to download package")
                sys.exit()
        else:
            print("Package is already installed")
            sys.exit()
    else:
        print("No package found")
elif args[1] == "uppak":
    os.chdir(os.path.join(home, '.strawberry', 'pmlist'))
    exit = os.system("git pull >~/.strawberry/uppack.log 2>&1")
    if not exit == 0:
        print("Error while pulling")
elif args[1] == "remove":
    os.chdir(os.path.join(home, '.strawberry', 'pakbin'))
    try:
        filler = args[2]
    except:
        print("Second argument not given.")
        sys.exit()
    if os.path.exists(args[2]):
        if not args[2] == "strawberry":
            exit = os.system("rm -rf " + args[2] + " >~/.strawberry/remove.log 2>&1")
            if not exit == 0:
                print("Could not remove package " + args[2])
        else:
            print("Package is protected cannot uninstall it.")
    else:
        print("No package called that exists")
else:
    print("Not a recognized command.")
    help()