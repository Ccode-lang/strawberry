import os
import io
import sys
import requests
# import angledat
home = os.path.expanduser('~')
module = os.path.join(home, '.strawberry', 'lib')
sys.path.append(module)
import angledat as ang

args = sys.argv


def help():
    print("install       : install a package")
    print("remove        : remove a package")
    print("uppak         : update package list")
    print("lsinstalled   : list installed packages")
    print("lsinstallable : list installable packages")
    print("search        : search for packages")
    sys.exit()
# from https://raspberrypi.stackexchange.com/questions/5100/detect-that-a-python-program-is-running-on-the-pi
def ispi():
    try:
        with io.open('/sys/firmware/devicetree/base/model', 'r') as m:
            if 'raspberry pi' in m.read().lower(): return True
    except Exception: pass
    return False


if not ispi():
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
        if not package.endswith(args[2]):
            print("Invalid link found for package.")
            sys.exit()
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
elif args[1] == "lsinstalled":
    installed = os.listdir(os.path.join(home, '.strawberry', 'pakbin'))
    for i in installed:
        print(i)
elif args[1] == "ver":
    print("Strawberry version 0.1")
elif args[1] == "lsinstallable":
    list = ang.read_dict(os.path.join(home, '.strawberry', 'pmlist', 'list.txt'))
    for name, val in list:
        print(name)
elif args[1] == "search":
    list = ang.read_dict(os.path.join(home, '.strawberry', 'pmlist', 'list.txt'))
    for name, val in list:
        if args[2] in name or args[2] in value:
            print(name)
else:
    print("Not a recognized command.")
    help()
