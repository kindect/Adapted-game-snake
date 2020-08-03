# 这是 kindect/Adapted-game-snake 的主页面
程序使用Python编写, 仅供参赛使用

使用要求的木兰-2开源协议(MulanPSL-2)

关于本项目代码的更多信息可以在wiki上找到

依赖: Pygame sys time random threading

## 在Windows上运行情况:
![展示图片1](https://images.gitee.com/uploads/images/2020/0802/144029_0eec6591_6537938.png)
![展示图片2](https://images.gitee.com/uploads/images/2020/0802/144046_36e1e283_6537938.png)
## 最新发行版
https://gitee.com/kindect/Adapted-game-snake/releases

作为源码的一部分下载(只有最新版):

https://gitee.com/kindect/Adapted-game-snake/raw/master/Tsnake/dist/Tsnake.zip

也可以从Github上下载:

https://github.com/kindect/Adapted-game-snake/releases

注意到Github的项目是从Gitee上Fork的, 所以可能会有延迟, 查看Gitee来看最新版

另外, release只提供Windows版本

## 编译:
### 使用Visual Studio编译(版本>=2017, 社区版或专业版, 未测试企业版, 安装Python3.7支持)
1. 下载repo
> git clone https://gitee.com/kindect/Adapted-game-snake.git
2. 打开Visual Studio, 选择打开项目或解决方案
3. 选择repo里面Tsnake.sln
4. 按下F5开始调试, 按下Ctrl+F5来运行(不调试)
### 其它
> git clone https://gitee.com/kindect/Adapted-game-snake.git
> cd Tsnake/
> python3 -m install pygame
> python3 Tsnake.py

## 目前的功能
> 实现方法可参考wiki, 图片可在这里下载:

![1](https://gitee.com/kindect/Adapted-game-snake/blob/master/Tsnake/pics/body/1.png)

![2](https://gitee.com/kindect/Adapted-game-snake/blob/master/Tsnake/pics/body/2.png)

![3](https://gitee.com/kindect/Adapted-game-snake/blob/master/Tsnake/pics/body/3.png)

![12](https://gitee.com/kindect/Adapted-game-snake/blob/master/Tsnake/pics/body/12.png)

![13](https://gitee.com/kindect/Adapted-game-snake/blob/master/Tsnake/pics/body/13.png)

![23](https://gitee.com/kindect/Adapted-game-snake/blob/master/Tsnake/pics/body/23.png)

1. 丝滑的移动(不再是方块)
2. 默认刷新频率60fps(可以更改)
3. 多食物(默认是3个)
4. 多毒药(默认是3个)

## Bugs:
如果你发现一个bug, 请提出Issue或者更好, PR
* [x] ~~发行版有时提出一个runtimeError并指出foods中food是一个NoneType(需要复现)~~
* [ ] 毒药分辨率低

![低分辨率](https://images.gitee.com/uploads/images/2020/0802/150242_ec74553b_6537938.png)

## TODO:
* [ ] 多人模式(脱机)
* [ ] 机器人
* [x] 毒药
* [ ] 显示分数
* [ ] 死亡显示