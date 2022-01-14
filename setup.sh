[ -d angledat ] && rm -rf angledat

git clone https://github.com/Ccode-lang/angledat.git

mkdir ~/.strawberry &>/dev/null
mkdir ~/.strawberry/main &>/dev/null
mkdir ~/.strawberry/bin &>/dev/null
mkdir ~/.strawberry/lib &>/dev/null
mkdir ~/.strawberry/pakbin &>/dev/null


cp package.py ~/.strawberry/main
chmod +x strawberry
cp strawberry ~/.strawberry/bin
cp angledat/angledat.py ~/.strawberry/lib

cd ~/.strawberry
git clone https://github.com/Ccode-lang/pmlist


printf "    \e[32m\e[42m&\e[0m \e[32m\e[42m&\e[0m\n"
printf "     \e[32m\e[42m&\e[0m\n"
printf "    \e[31m\e[41m@@@\e[0m\n"
printf "  \e[31m\e[41m@@@@@@@\e[0m\n"
printf "   \e[31m\e[41m@@@@@\e[0m\n"
printf "     \e[31m\e[41m@\e[0m\n\n\n"

echo Install is done
echo Add both ~/.strawberry/bin and ~/.strawberry/pakbin to path.
