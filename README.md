# 这是 kindect/Adapted-game-snake 的主页面
英文版本(English version):https://gitee.com/kindect/Adapted-game-snake/blob/master/README-en.md

### 初衷:
当我设计这个项目的时候, 其实如果要说的话, 我的思维其实已经快要固化了, 但是主项目下点子还是不错的, 包括毒药(这个点子就是从那里来的)

当然还要感谢很多很多人, 很多很多项目

主力机是PC, 写代码用的是Visual Studio, 很多人说它太笨重, 一次安装要占用20多G, 我想告诉这些人,(我安装了一个分区(大概120G左右)), 笨重也许不是一件坏事, 稳定才是好事, 编译效率奇高

Pyinstaller的问题我也许会解决吧, pywin32的问题太多了, 一个老版本的依赖库通常就会导致程序不稳定

Pygame其实就是这样一个框架, 用SDL写的库文件, 效率能稍微比PyQt高那么一点吧, 但是都需要runtime, 所以效率其实=fart, pygame中很多没用的文件, 但是还是选择了它, 原因在于, 使用python编程, 其实就是为了时间来的, C#程序一样写, 效率也会高不少, 但是既然使用了Python, 效率就一定要有保障

程序本身开始写的时候只花了一天, 网课的时候偷摸写的, 效率还行, 占用1-3%的CPU(i9-9900K, 对, 就是那个套壳i7), 后来说要封装class, 觉得没什么, 但是bug就是从这里出来的, 我不想对这种事情做什么评价, 但是bug太多肯定影响用户体验, 已有的bug我觉得还行

我觉得, 作为一款游戏, 那么可玩性一定是最低标准, 目前可玩倒是可玩, 尤其注重用户体验, 我从一开始就很鄙视方块的设计, 所以自己用Photoshop画了蛇的身体, 创意要说的话其实也不多, 倒是拿这个项目魔改应该不错

后来就是PEP规范, 这个规范简直离谱, 但是为了可读性, 我也加了不少注释(我本人很讨厌写注释, 但是, 对于'代码被阅读的次数总比编写的次数多的原则, 我还是写了注释, 而且详细解释了这些原则')

一个程序, 最重要的就应该是, 把选择权交给用户, 开源程序当然是其中的一种, 之前写代码都是"开源是一种美德, 也是实力", 但是之前写代码都是缝缝补补, 从来不封装class, 现在开源是要求, 但是不写注释的开源还不如不开源.

把选择权交给用户的理念的体现便是, 把文件(图片, 音频, 字体)都拿出来放在外面resouce/去, 其它仓库\项目也许可以直接把这些文件拿走, 但是也务必贯彻这一种精神(如果你要闭源的话)

repo的访问量很高, 有图为证, 但是下载量不高, Download Zip的人也不高, Star也只有4个, 其中一个还是我自己

有些人刷star的, 看看点star的人你就能发现, 新注册, 没有repo, 就点了一个赞, 然后就跑了

如果你怀疑我不认真搞项目, 你可以看看commit数量:D

### 愿景:

1. 发到pypi上面, 以后直接pip install tsnake
2. 这辈子没有bug
3. 拿到奖品(:D)

### 技术参数:
程序使用Python编写, 仅供参赛使用

使用要求的木兰-2开源协议(MulanPSL-2)

关于本项目代码的更多信息可以在wiki上找到

依赖: Pygame sys time random threading

~~注意 当前版本并不稳定 release都是稳定的~~

## 对Pyinstaller的支持走到尽头, 所有用户麻烦runtime

Mac OS 已通过测试, 但是尤其是在Big Sur上安装编译Pygame太困难了, 所以不推荐

## 在Windows上运行情况:
![展示图片1](https://images.gitee.com/uploads/images/2020/0802/144029_0eec6591_6537938.png)
![展示图片2](https://images.gitee.com/uploads/images/2020/0802/144046_36e1e283_6537938.png)
## 最新发行版
https://gitee.com/kindect/Adapted-game-snake/releases/v1.0.2


## 编译:
### 使用Visual Studio编译
1. 下载repo
> git clone https://gitee.com/kindect/Adapted-game-snake.git
2. 打开Visual Studio, 选择打开项目或解决方案(或者跳过第一步, 从远程仓库clone)
3. 选择repo里面Tsnake.sln
4. 按下F5开始调试, 按下Ctrl+F5来运行(不调试)

### 其它(PyCharm, 或者Vi硬汉)
> git clone https://gitee.com/kindect/Adapted-game-snake.git
> cd Tsnake/
> python3 -m pip install pygame
> python3 Tsnake.py

## 目前的功能
> 实现方法可参考wiki, 图片可在这里下载:

![2](https://images.gitee.com/uploads/images/2020/0803/145912_a12be9ca_6537938.png)

![2](https://images.gitee.com/uploads/images/2020/0803/145925_33a0d83a_6537938.png)

Just to show a bit

* [x] 丝滑的移动(不再是方块)
* [x] 默认刷新频率60fps(可以更改)
* [x] 多食物(默认是3个)
* [x] 多毒药(默认是3个)
* [x] 音效(buttercup by Jack Stauber(握紧我的抱枕~~))

## Bugs:
如果你发现一个bug, 请提出Issue或者更好, PR
* [x] ~~发行版有时提出一个runtimeError并指出foods中food是一个NoneType(需要复现)~~
* [ ] 毒药分辨率低

![低分辨率](https://images.gitee.com/uploads/images/2020/0802/150242_ec74553b_6537938.png)

* [ ] 死亡屏幕导致程序宕机(目前的解决办法是停掉这个功能, 代码在注释里面)

## TODO:
* [ ] ~~~多人模式(脱机)~~~(已抛弃该方案)

* [ ] 机器人

* [x] 毒药

* [x] 显示分数

* [x] 死亡显示(with bugs)