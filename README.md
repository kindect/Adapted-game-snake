# this is the main entry of kindect/Adapted-game-snake
The project is written in Python, and currently it is used for the contest.

using MulanPSL-2 lisense which is required for the contest.

Futher info about the code can be found in wiki.

Dependencies: Pygame sys time random threading

## Latest Release:
https://gitee.com/kindect/Adapted-game-snake/releases

also on github:

https://github.com/kindect/Adapted-game-snake/releases

Notice that the Github repo is forked from Gitee, so might have delay, check Gitee for the newest version

Only provide release in Windows Platform, other platform see Build:

## Build:
### Using Visual Studio(>=2017, commuinty or Professional(Enterprise version not tested) with Python3.7 support installed)
1. Clone the repo:

	git clone https://gitee.com/kindect/Adapted-game-snake.git

2. Open Visual Studio, select open a project or solution
3. Choose Tsnake.sln
4. Press F5 to start debug, Ctrl+F5 to run without debug

###  Others:
1. Clone the repo:

	git clone https://gitee.com/kindect/Adapted-game-snake.git

2. change dir

	cd Tsnake

3. Now there's two thing you need to notice: one is the Tsnake.py, which of course is the main Python program. The other is pics/ dir, which contains the pictures required.

## Features by now:
Regular snake features: moving around.(using module threading)

default refresh rate is 60fps.(can change it)

multi-food(default is 3)

## Bugs:
If you find a bug, please bring up a issue, or better, PR
* The release version sometimes bring up a runtime error that the food in foods is a NoneType and raise a error(need to reproduce)

## TODO:
[ ] multi-player?(might use a server so might have security issues.)

[ ] robots.(this is rather easy to achieve since no internet connection is required)

[ ] posionous food(remain dicussing)