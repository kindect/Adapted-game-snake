# This is the main entry of kindect/Adapted-game-snake
The project is written in Python, and currently it is used for the contest.

Using MulanPSL-2 lisense which is required for the contest.

Futher info about the code can be found in wiki.

Dependencies: Pygame sys time random threading

## Pictures on Windows:
![1](https://images.gitee.com/uploads/images/2020/0802/144029_0eec6591_6537938.png "Screenshot (4).png")
![2](https://images.gitee.com/uploads/images/2020/0802/144046_36e1e283_6537938.png "Screenshot (5).png")
## Latest Release:
https://gitee.com/kindect/Adapted-game-snake/releases

can also download from:

https://gitee.com/kindect/Adapted-game-snake/raw/master/Tsnake/dist/Tsnake.zip

Also on github:

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

Default refresh rate is 60fps.(can change it)

Multi-food(default is 3)

Multi-poisonous-food(default is 3)

## Bugs:
If you find a bug, please bring up a issue, or better, PR
* [x] ~~The release version sometimes bring up a runtime error that the food in foods is a NoneType and raise a error(need to reproduce)~~

***Fixed in 1.0.1-alpha***

* [ ] Low contrast in posionous food
![Low contrast](https://images.gitee.com/uploads/images/2020/0802/150242_ec74553b_6537938.png "Capture.PNG")

## TODO:
* [ ] Multi-player?(Might use a server so might have security issues.)

* [ ] Robots.(This is rather easy to achieve since no internet connection is required)

* [x] Posionous food

* [ ] Score showing

* [ ] dead screen