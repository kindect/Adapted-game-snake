devoted to zxx.
# This is the main entry of kindect/Adapted-game-snake
Chinese version(中文版本):https://gitee.com/kindect/Adapted-game-snake/blob/master/README.md

### Original intention:
When I designed this project, in fact, if I had to say something, my thinking was actually about to solidify, but the ideas under the main project were still good, including poison (this idea came from there)

Of course, I have to thank many, many people, many, many projects

The main computer is a PC, and the code is written in Visual Studio. Many people say that it is too bulky, and it takes more than 20G for one installation. I want to tell these people, (I installed a partition (about 120G)), and the bulky may not be A bad thing, stability is a good thing, compilation efficiency is extremely high

I may solve the problem of PyInstaller. There are too many problems with PyWin32. An old version of the dependent library usually leads to program instability.

Pygame is actually such a framework. The library files written in SDL are slightly more efficient than PyQt, but they all need runtime, so the efficiency is actually = fart. There are many useless files in pygame, but I still chose it. The reason It is, programming in python is actually for the sake of time. C# programs are written in the same way, and the efficiency will be much higher, but since Python is used, efficiency must be guaranteed

The program itself only took a day when it was written. I wrote it secretly during the online class. The efficiency is not bad. It takes up 1-3% of the CPU (i9-9900K, yes, that is the shell i7). Later, I want to package the class. I don’t think much, but the bug comes from here. I don’t want to comment on this kind of thing, but too many bugs will definitely affect the user experience. I think the existing bugs are okay.

I think that as a game, the playability must be the lowest standard. It is currently playable but it is playable, with special emphasis on user experience. I despised the design of the square from the beginning, so I drew the body of the snake in Photoshop. There is not much creativity to say, but it should be good to take this project magically
![Snake Body](https://images.gitee.com/uploads/images/2020/0806/171536_c88950d8_6537938.png "example.png")
Then came the PEP specification. This specification is simply outrageous, but for readability, I also added a lot of comments (I hate writing comments, but for the principle that the code is read more often than written, I I wrote notes, and explained these principles in detail')

![comment](https://images.gitee.com/uploads/images/2020/0806/174719_c34bbe4e_6537938.png "comment.png")

![comment](https://images.gitee.com/uploads/images/2020/0806/174749_383bdf0c_6537938.png "comment.png")

Whoever wants to say that I don't write notes, I will be anxious with someone :D

For a program, the most important thing is to give the user the right to choose. Of course, open source programs are one of them. The code written before is "open source is a virtue and strength", but the code written before is all about stitching. Supplement, never encapsulate classes, now open source is a requirement, but open source without comments is not as good as not open source.

The embodiment of the concept of giving the right of choice to the user is to take out the files (pictures, audio, fonts) and put them outside to source/go. Other warehouses\projects may be able to directly take these files away, but it must also be implemented. A spirit (if you want to close the source)

The number of visits to the repo is very high, as evidenced by the picture, but the download volume is not high, and the number of Download Zip is not high. There are only 4 Stars, one of which is my own

![access page](https://images.gitee.com/uploads/images/2020/0806/171213_02815615_6537938.png "Screenshot")

Some people brush stars, just look at the person who clicked the star and you will find that new registration, no repo, just clicked a like, and then ran away

If you suspect that I am not serious about the project, you can look at the number of commits: D

### Technical specs
The project is written in Python, and currently it is used for the contest.

Using MulanPSL-2 license which is required for the contest.

Further info about the code can be found in wiki.(and inside the code)

Dependencies: Pygame sys time random threading

~~Current version is not stable, go to release for stable version~~

## This is the end of supporting PyInstaller, All the users must exec using runtime

Mac OS tested, but installing pygame is so much trouble especially in Big Sur, so still not recommended

## Pictures on Windows:
![1](https://images.gitee.com/uploads/images/2020/0802/144029_0eec6591_6537938.png "Screenshot (4).png")
![2](https://images.gitee.com/uploads/images/2020/0802/144046_36e1e283_6537938.png "Screenshot (5).png")
## Latest Release:
https://gitee.com/kindect/Adapted-game-snake/releases/v1.0.2


## Build:
### Using Visual Studio
1. Clone the repo:
> git clone https://gitee.com/kindect/Adapted-game-snake.git
2. Open Visual Studio, select open a project or solution(or choose to clone from remote directory, which means to skip step 1, but you need to do some settings afterwards.)
3. Choose Tsnake.sln
4. Press F5 to start debug, Ctrl+F5 to run without debug

###  Others:(Like PyCharm, or Vi :D)
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

* [x] ~~Low contrast in poisonous food~~

![Low contrast](https://images.gitee.com/uploads/images/2020/0802/150242_ec74553b_6537938.png "Capture.PNG")

***Fixed in 1.0.2***

* [ ] dead screen cause the program to freeze.

## TODO:
* [ ] ~~~Multi-player(offline)~~~(abondoned)

* [ ] Robots.

* [x] Poisonous food

* [x] Score showing

* [x] dead screen(with bug)