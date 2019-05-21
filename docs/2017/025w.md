# 怼周刊_v25
~ 预定 17.10.2 20:20 发布

Release time - 20:20, October 2th, 2017

-----------------------------------------

Shooting self  ---by DAMA

    袁门射戟 望其运行结果
    集速射击 闻其执行输入
    自怼射己 问其设计思路
    输出射辑 切其过程变化


Shooting self  ---by mxclover
    
    Shooting the halberd    Looking the result of operation
    Shooting speed fire     Listening the input of execution 
    Shooting debug self     Asking the ideas of design
    Shooting output log     Switching the change of process
    
-----------------------------------------

- 主编: [大妈](http://du.zoomquiet.io/2014-02/ac0-zq/)
- 责编:
    + [xpgeng](http://du.zoomquiet.io/2017-04/about-xpgeng/)
    + [sunoonlee](http://du.zoomquiet.io/2017-04/about-sunoonlee/)
    + [Zoe](http://du.zoomquiet.io/2017-04/about-zoe/)
    + [bambooom](http://du.zoomquiet.io/2017-04/about-bambooom/)

# 进度 Timelines
~ 记录当周关键事件日期+证据链接

- 170930 [42h[TASK]2017-09-30 怼周会会 ](https://github.com/DebugUself/du4proto/issues/245)


# 任务 Tasks
~ 记述关键共怼任务 (如果没有, 留空)

- 170923 [6d[TASK] 立项: 程序员能力树可视化, 又是一个有意思的项目啦](https://github.com/DebugUself/du4proto/issues/237)


# 进展 Progress
~ 整体上圈内部活跃指标情况

- 提交: 9 人,
    - 小组 @zoomquiet 时间帐单:效能分析小队
        - 成员: @zsy @liguanghe @simpleowen @mxclover 
    - @draachen Py104 学习
    - @hetao 深度学习
    - @liguanghe 域外生活录
    - @OMlalala 投资学习
    - @zsy 编程与写作
    - @zoejane 日常节奏形成
    - @leilayanhui Py103复习
    - @Wangjunyu 编程与工作相结合
- 引发的作品:
    + NIL
- 状态:

<table>
<tr><th>allcic Commit</th><th> times</th><th>weekly Commit</th><th> times</th></tr>
<tr><td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>359</td>
        <td>
            <a href='http://github.com/leilayanhui'>leilayanhui</a></td><td>17</td>

<tr><td>
            <a href='http://github.com/liguanghe'>liguanghe</a></td><td>315</td>
        <td>
            <a href='http://github.com/liguanghe'>liguanghe</a></td><td>12</td>

<tr><td>
            <a href='http://github.com/zoejane'>zoejane</a></td><td>301</td>
        <td>
            <a href='http://github.com/zhangshiyinrunwithcc'>zhangshiyinrunwithcc</a></td><td>8</td>

<tr><td>
            <a href='http://github.com/mxclover'>mxclover</a></td><td>186</td>
        <td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>4</td>

<tr><td>
            <a href='http://github.com/zhangshiyinrunwithcc'>zhangshiyinrunwithcc</a></td><td>158</td>
        <td>
            <a href='http://github.com/mxclover'>mxclover</a></td><td>1</td>

<tr><th>all Commit </th><th>Comments times</th><th>weekly Commit</th><th>Comments times</th></tr>
<tr><th>all Issue </th><th>Comments times</th><th>weekly Issue</th><th>Comments times</th></tr>
<tr><td>
            <a href='http://github.com/liguanghe'>liguanghe</a></td><td>501</td>
        <td>
            <a href='http://github.com/zhangshiyinrunwithcc'>zhangshiyinrunwithcc</a></td><td>16</td>

<tr><td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>417</td>
        <td>
            <a href='http://github.com/liguanghe'>liguanghe</a></td><td>13</td>

<tr><td>
            <a href='http://github.com/zhangshiyinrunwithcc'>zhangshiyinrunwithcc</a></td><td>348</td>
        <td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>5</td>

<tr><td>
            <a href='http://github.com/zoejane'>zoejane</a></td><td>107</td>
        <td>
            <a href='http://github.com/vanxv'>vanxv</a></td><td>4</td>

<tr><td>
            <a href='http://github.com/mxclover'>mxclover</a></td><td>81</td>
        <td>
            <a href='http://github.com/leilayanhui'>leilayanhui</a></td><td>3</td>

</table>

- 在线(测试ing..):
    + `curl du.zoomquiet.us`
    + `curl du.zoomquiet.us/v0/all/cic/rank/5/`
    + `curl du.zoomquiet.us/v0/all/cil/rank/5/`
    + `curl du.zoomquiet.us/v0/week/cic/rank/5/`
    + `curl du.zoomquiet.us/v0/week/cil/rank/5/`

- [文档->du4proto/st at DU_tools · DebugUself/du4proto](https://github.com/DebugUself/du4proto/tree/DU_tools/st)

# 成果 Achievements
~ 各种成品/半成品 内部知识作品

##  Wiki: python 操作环境指南
### 背景
- 越来越多.ipynb 形式,有怼员直觉的想尝试一切运行都在 Jupyter 中, 将 代码文本/系统环境/运行时环境/交互环境/... 各种 Python 可以运行的环境当成同一类对象了.

### 意义
了解 python 运行环境, 并知晓在开发和运行时分别选用什么环境, 可快速推进开发效率.  

### 现象
- 现象1
    + atl4dama 大妈在 ipynb 中开发完了整个脚本. 其中包括读取文件, 并操作.
    + 我git pl 仓库后, 打开大妈的 .ipynb文件, 直接 shift + enter, 诶? 报错显示文件不存在
- 现象2
    + 直接复制大妈的系列管道命令: ༄ find ../../raw/zoomquiet/weekly/*.csv |
xargs -I{} python zq7SET4.py {} > atl2SET4dama_all.csv
    + 报错说文件夹不存在?
- 现象3
    + 命令行直接运行含有```import matplotlib.pyplot as plt```内容的 .py 文本, 报错 命令行不能显示图片.


### python 运行环境
#### 软件运行环境的层次

当我们从零开始一个软件项目的时候,会考虑的问题有:
- 需要什么样的服务器?
   - 系统:Win or Linux
   - 配置:CPU 16核 8核?内存 16G?
   - 虚拟还是实体小机
   - 用途是什么?用于跑应用还是放数据库等等
- 需要什么样的权限配置?
   - 一般不给Root用户
- 需要什么样的网络配置?
   - 是否需要访问外网,需要访问哪些地址
   - 是否需要外网访问,开放哪些端口
- 需要什么样的(服务器架构)拓扑结构
   - 是否需要进行负载均衡
   - 和其他服务器的联通关系

- 服务器上需要安装的应用或者依赖包?

这是我们普遍理解的运行环境. 需要注意的是,以上的问题一般只有在生产环境申请服务或者部署应用的时候才会问的这么细,如果是开发环境申请服务器,基本上只要搞清楚网络配置,剩下的都交给开发自己搞. 因为开发人员会有各种自己需要的东西的安装,甚至做一些技术的尝试和创新等等. 

以上的部分应该作为广义的软件运行环境下的比较偏向操作系统,网络环境的层次

#### Python 程序运行在哪儿


在前面的运行环境的问题都搞定后,才是到安装python. 当我们在shell 里输入 python XXX.py 的时候,首先shell 会去环境变量对应的地址去寻找这一条命令如何执行,找到了python的可执行程序后,才知道如何理解这一条命令. 之后才会根据python 的方式执行py脚本. 其实执行的时候也会先通过解释器把py脚本做一轮解释,之后才继续执行. 

python和操作系统的关系,在写脚本的时候感受不深,不过[15.1. os — Miscellaneous operating system interfaces](https://docs.python.org/2/library/os.html)这里就会有感觉,通过os的包的函数,获取到操作系统层面的一些信息,甚至执行相关的操作. 如果利用shell交互,则会在操作系统和python程序间通过shell进行传递. 

#### Python 运行环境及类别

- 1.命令行:用文本编辑器写好 .py 为扩展名的文本文件,打开命令行窗口,把当前目录切换到 .py 文件所在目录,然后用 python 解释器执行. terminal cli python .py
```
xxx(path)$ python xxx.py
```
- 2. 交互环境运行: 使用 python 自带的 IDLE(terminal cli python)
```
$ python
>>> 
>>> 
...
...
```
- 3. 集成开发环境(IDE)
    - IPython: 基于CPython之上的一个交互式解释器, Cpython 是官方版本. 
```
$ cd xxx(path)
$ jupyter notebook
```

or 
```
$ jupyter notebook
in1: cd
ot1: xxx(path)
```
同样需要在当前脚本所在的路径下, 才可以执行当前脚本. 

#### 选择哪种环境(操作)
- 不同的运行时环境都分别解决了什么问题?   
- 开发和运行环境是相同的嘛?
- 当前, 哪种运行环境最适合我们的日常自怼?

仍以 [DebugUself/du4proto at atl4dama](https://github.com/DebugUself/du4proto/tree/atl4dama) 为例, 回答以上问题.

- 开发: 在 3.集成开发环境(IDE)IPython 中进行尝试, 因为所见即所得, 大量减少输入 print() 的时间. 
- 形成连续代码后, 另存为 .py, 保存在固定文件夹, 并撰写调用文档. 
- 运行: 1. 命令行 cd 进 .py脚本所在文件夹, $ python .py
```
                  /> .md(doc/)
    .ipynb(ipynb/) -> .py(try/) -> moudle(src/) -> readme.md
         ^                             |
         +-----------------------------+    
```

- 以上本地的 .ipynb 和 .py 脚本 会推送到远程仓库, 生成的最终 .py脚本 沉淀在 src/ 文件夹里面. 期间过程中的 .csv 或 .html 文件不应上传到远程仓库. 原因及过程在这里: [HbUsageRepositoryFile · DebugUself/du4proto Wiki](https://github.com/DebugUself/du4proto/wiki/HbUsageRepositoryFile)

- 另: 2.交互式环境 可以使用 os 模块, 与系统交互时, 直接使用. 

### 参考
- [Jupyter and the future of IPython — IPython](https://ipython.org/)


### 增补
- 可在本 wiki 上持续增补
- 可在 [4d[BC]究竟 Python 都有什么运行姿势? 何时应用哪种? · Issue #227 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/227) 中持续讨论


### Changelog
- 20170926 lgh wiki 初稿 60 min 

## @liguanghe 
- [Part Achievement in Python Project named atl4dama 时间账单项目阶段成果 | Li Guanghe's blog](https://liguanghe.github.io/2017/09/25/lgh8html/)

# 故事 Stories
~ 收集各自无法雷同的怼圈真人故事...
## 熊本🐻->友情怼:怼员小鹤的3个优点

今早slack<br>
大妈指导**如何给怼友点赞**<br>
特成此文<br>

```
以下对话发生于slack#atl4dama

zoomquiet [8:35 AM] 
@zhangshiying 忘记密圈第一法则啊啊啊啊啊啊?
别轻易点赞
要赞也得言之有物
戳心戳肺
所以... 为毛你作不到?和广鹤差了什么?
又~你比她强在哪儿
好习惯之养成成份成因过程... 也在自怼射程啊啊啊啊啊啊
```

### 小鹤事迹

- 克服时差
    + 小鹤持续近20周,每周六晚新西兰时间凌晨00:42-02:42(北京时间8:42-10:42)参加周会并录音
        * 小鹤能够主动将自己生活节奏调节至与怼圈一致
            - 我也在努力,我的节奏是`北京时间晚上10点30要睡`,我会尽量10点左右完成怼会

- 时间记录
    + 小鹤持续6个月的时间记录,且发布在其博客上,见[6个月时间报告](https://liguanghe.github.io/2017/09/25/TimeReport0924/)
        * 小鹤能够做到,让别人看得懂她的时间记录,别人可以很方便得了解她
            - 我也有时间记录,但贪图方便,都用我自己的简写/暗号/指数,别人要花费比较多成本才能看懂

- 提交plan
    + 小鹤每季都提交plan,且s07e51第1个提交[du4proto/S07E51](https://github.com/DebugUself/du4proto/tree/master/S07E51)
        * 这又让我方便了解她,又挑拨起我动笔写plan的欲望了

- pandas折腾折线图
    + 小鹤在不到1个月时间内,折腾出一张折线图,且形成成果发布在其博客上,见[Part Achievement in Python Project namedatl4dama 时间账单项目阶段成果](https://liguanghe.github.io/2017/09/25/lgh8html/)
        * 我上次也折腾1个月,但没有折腾出折线图,也没有记录过程的博文发布
            - 今后我可能更加注重积累`可用记录`

- 声音
    + 小鹤好听+甜甜的
        * 我在录音里听起来像踢馆的...

### 3个优点

小鹤在以下三个方面,明显优于我<br>
1. 规律性形成`可用记录`
2. 投入怼圈时间
3. 先天声音

timelog<br>
42mins<br>
~ 现场 [3d[DUW]友情怼:怼员小鹤的3个优点](https://github.com/DebugUself/du4proto/issues/239)<br>

## @liguanghe -> 队员熊本的四个优点
- 胆子大, 不纠结. 不给自己预设牛人的牛. 
比如 是怼圈最早跟大妈有良好交流的人. 我在整个 py103课程里都不敢跟大妈说话, 也不敢麻烦大妈呢. 先自己预设牛人都比较难相处. 预设别人先会不喜欢我. 
- 执行力强
想到就去做, 目前还没什么没实现吧.
- 积极/热心/不玻璃心(诶, 这点我也有, 所以是一样强, 233)
- 还相信爱情. (已婚多年的我表示, 过往不究啊.)

### 最后,我们都要做像大妈一样的人
- 完美的老师
- 自信, 耐心和善意的看待整个世界
- 处理信息的数量级超出咱们好多0
- 会写诗
- 会说相声
- ...



# 推荐 Recommedations
~ 嗯哼各种怼路上发现的嗯哼...

- 是也乎:  
    + [Python Data Analysis with pandas · The Morning Data](https://mubaris.com/2017-09-25/python-data-analysis-with-pandas)
    + [Jupyter Notebook Viewer](http://nbviewer.jupyter.org/gist/wrobstory/1eb8cb704a52d18b9ee8/Up%20and%20Down%20PyData%202014.ipynb) 配色以及思路...
    + [hcchengithub/peforth: A Forth programming language in python](https://github.com/hcchengithub/peforth)
    + [蠎加载 144 |蠎周刊 |汇集全球蠎事儿 !-)](http://weekly.pychina.org/importpython/importpython-144.html)
    + [法国"乔布斯"砸1亿造的这所"野鸡"大学,没老师没文凭,毕业生却被一流大公司抢着要](https://mp.weixin.qq.com/s/S0gMh-y0UUeL6POE5QU9FQ)
    + [Teaching People Git, Emma Jane Hogbin Westby - Git Merge 2015-xYhHi8yK-Is.mp4](https://pan.baidu.com/s/1gf1phq7)




# 后记 Postscript
~ 怼周刊是什么以及为什么和能怎么...

大妈曰过: `参差多态 才是生机`
问题在 `参差` 的行为是无法形成团队的

	Coming together is a beginning; 
	Keeping together is progress; 
	Working together is success!

<--- [Henry Ford](https://www.brainyquote.com/quotes/quotes/h/henryford121997.html)

- 所以, 有了 大妈 随见随怼的持续嗯哼...
- 但是, 想象一年后, 回想几十周前自己作的那些 `图样图森破` 
- 却没现成的资料来出示给后进来嗯哼?
- 不科学, 值得记录的, 就应当有个形式固定下来
- 所以,有了这个 `怼周刊` (Weekly 4 DU)

What is DUW?
Why we make DUW?
What are the possibilities of DUW?

Dama said, variety brings vitality.
But various behaviors may make us hard to cooperate as a team.

	Coming together is a beginning; 
	Keeping together is progress; 
	Working together is success!

<--- [Henry Ford](https://www.brainyquote.com/quotes/quotes/h/henryford121997.html)

That's why Dama keeps on debugging.
However, as time goes by, maybe you would not remember these days clearly and spread your experience difficultly.
What a pity!
The valuable should have a fixed form to be recorded.
That's why we make the Weekly for DU.



