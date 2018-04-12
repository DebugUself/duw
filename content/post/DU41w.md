---
title: "DU41w"
date: 2018-01-22T20:20:00+08:00
---

# 怼周刊\_v41
\~ 预定 18.1.22 20:20 发布

---- 

参数好

	好参数 步长小
	多指标 可检验
	多组合 可测试
	千测百验参数好
	
	What Is The Good Parameters?
	
	Take the smallest steps 
	Inspect multiple indicators 
	Test all possible combinations
	After thousands of modifications 
	There stands the good parameters 
	
	                        —— ZoomQuiet, 熊本

---- 

- 主编: [大妈][1]
- 本期责编:
	+ 张诗颖

# 进度 Timelines
\~ 记录当周关键事件日期+证据链接

- [42h\[TASK]20180120 怼周会 分享及纪要][2]

# 任务 Tasks
\~ 记述关键共怼任务 (如果没有, 留空)

- 排查自己的分支, 减少浪费的空间. [6d\[TASK]主仓库文件容量将突破免费空间限额, 如何应对? (请怼友们都来回答)][3] 在这个 issue 下记录过程.
- 追踪管理自己的分支, 在 [怼圈指北][4] 和 wiki 怼作品 两处登记.
- [8w\[TASK]怼周会主持人轮值登记][5] 
- [10w\[TASK]怼周刊责编轮值登记][6]

# 进展 Progress
\~ 整体圈内活跃指标情况([st][7] 专用服务, 尚少使用手册)

<table>
<tr><th>allcic Commit</th><th> times</th><th>weekly Commit</th><th> times</th></tr>
<tr><td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>484</td>
        <td>
            <a href='http://github.com/leilayanhui'>leilayanhui</a></td><td>23</td>

<tr><td>
            <a href='http://github.com/liguanghe'>liguanghe</a></td><td>480</td>
        <td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>14</td>

<tr><td>
            <a href='http://github.com/zhangshiyinrunwithcc'>zhangshiyinrunwithcc</a></td><td>421</td>
        <td>
            <a href='http://github.com/OMlalala'>OMlalala</a></td><td>7</td>

<tr><td>
            <a href='http://github.com/zoejane'>zoejane</a></td><td>306</td>
        <td>
            <a href='http://github.com/liguanghe'>liguanghe</a></td><td>6</td>

<tr><td>
            <a href='http://github.com/leilayanhui'>leilayanhui</a></td><td>304</td>
        <td>
            <a href='http://github.com/zhangshiyinrunwithcc'>zhangshiyinrunwithcc</a></td><td>4</td>

<tr><th>all Commit </th><th>Comments times</th><th>weekly Commit</th><th>Comments times</th></tr>
<tr><th>all Issue </th><th>Comments times</th><th>weekly Issue</th><th>Comments times</th></tr>
<tr><td>
            <a href='http://github.com/liguanghe'>liguanghe</a></td><td>791</td>
        <td>
            <a href='http://github.com/liguanghe'>liguanghe</a></td><td>11</td>

<tr><td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>500</td>
        <td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>9</td>

<tr><td>
            <a href='http://github.com/zhangshiyinrunwithcc'>zhangshiyinrunwithcc</a></td><td>410</td>
        <td>
            <a href='http://github.com/leilayanhui'>leilayanhui</a></td><td>5</td>

<tr><td>
            <a href='http://github.com/mxclover'>mxclover</a></td><td>115</td>
        <td>
            <a href='http://github.com/livingworld'>livingworld</a></td><td>4</td>

<tr><td>
            <a href='http://github.com/zoejane'>zoejane</a></td><td>112</td>
        <td>
            <a href='http://github.com/Hugo1030'>Hugo1030</a></td><td>2</td>

</table>

# 成果 Achievements
\~ 各种成品/半成品 内部知识作品

- @OMlalala 翻译工程: [DebugUself/leo-editor-cn: Leo docs in Chinese | Leo 中文文档翻译][8]
- @leilayanhui [TLS eqan?提问][9]
[win10 安装 ubuntu 虚拟机][10]
- @Hugo1030[Kaggle:本周总结][11]
- @livingworld[Python in Hydrology][12]
- @熊本[Git远程库操作1:取回远程库分支更新并与本地分支merge][13]

# 故事 Stories
\~ 收集各自无法雷同的怼圈真人故事...
## 熊本-\>DUW本地修改规则1:merge前先取回最新

#### 问题
- 本地修改怼周刊DU\_draft文件后,再push到远程库时,经常出现non fast forward情境.
- 这是因为远程库DU\_draft文件为多人协作文件,远程库随时有更新.
- 如何减少non fast forward事故？

#### 方法
- 在本地建立2个分支issue1和issue2:issue1分支用于随时与远程库分支保持更新同步,issue2分支用于本地DU\_draft文件修改.
- 每次在issue2修改后(状态C1,见图1)
	+ 先checkout到issue1分支,取回远程库分支最新更新(状态C2)
	+ 然后再在issue1分支上,merge issue2分支上所作的修改(状态C3)
	+ 最后把issue1(状态C3)的更新推送到远程库分支上(状态C3)

#### 图示

- 图1.先更新issue1再merge issue2
<img src="https://user-images.githubusercontent.com/19412465/35215487-5dad05e4-ff9f-11e7-81db-cfe434d5e63d.jpg" width = "500" height = "300" alt="图片1" text-align=center />

#### 命令行
- 在本地分支issue2上作本地修改,并提交这些修改
- `$ git checkout issue2`
- `$ git add #更新的文件`
- `$ git commit #更新的文件`

- 取回远程库DUW分支更新
- `$ git fetch origin DUW`

- 在本地分支issue1上merge取回的远程库更新
- `$ git checkout issue1`
- `$ git merge origin/DUW`

- 将issue2提交的修改merge到issue1上
- **注意:此处是危险步骤,最好先确认issue1和当前的远程库DUW分支是一模一样的**
- `$ git checkout issue1`
- `$ git merge issue2`

- 将issue1的修改推送到远程库的DUW分支上
- `$ git push origin issue1:DUW`

- 取回远程库DUW分支更新
- `$ git fetch origin DUW`

#### 时间消耗
- 2hr实验
- 1hr备料
- 30ms成文

# 推荐 Recommedations
\~ 嗯哼各种怼路上发现的嗯哼...

- 是也乎:
	+ [蠎加载 159 |蠎周刊 |汇集全球蠎事儿 !-)][14]
	+ [the0demiurge/Python-Scripts: My testing, learning, minor projects, and interesting things.][15] 分享的正确姿态...
		* [免费爬墙网站项目\(ShadowSocksShare\)开发简记][16]
	+ [Learn X in Y Minutes: Scenic Programming Language Tours][17] 速成教程集中窝点...
		* \<\~ [adambard/learnxinyminutes-docs: Code documentation written as code! How novel and totally my idea!][18] 必然可以参与的了...
	+ [Pure Danger Tech][19] \~ 隔壁大叔的努力痕迹...

## 号召

- [|蠎周刊 |汇集全球蠎事儿 !-)][20]
	+ 俺私人嗯哼了5年了
	+ 邀请大家一起来, 每周嗯哼

# 后记 Postscript
\~ 怼周刊是什么以及为什么和能怎么...

大妈曰过: `参差多态 才是生机`
问题在 `参差` 的行为是无法形成团队的

	Coming together is a beginning; 
	Keeping together is progress; 
	Working together is success!

\<--- [Henry Ford][21]

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

\<--- [Henry Ford][22]

That's why Dama keeps on debugging.
However, as time goes by, maybe you would not remember these days clearly and spread your experience difficultly.
What a pity!
The valuable should have a fixed form to be recorded.
That's why we make the Weekly for DU.



[1]:	http://du.zoomquiet.io/2014-02/ac0-zq/
[2]:	https://github.com/DebugUself/du4proto/issues/340
[3]:	https://github.com/DebugUself/du4proto/issues/338
[4]:	https://github.com/DebugUself/du4proto/wiki/How2PubHandBook
[5]:	https://github.com/DebugUself/du4proto/issues/325
[6]:	https://github.com/DebugUself/du4proto/issues/319
[7]:	https://github.com/DebugUself/du4proto/tree/DU_tools/st
[8]:	https://github.com/DebugUself/leo-editor-cn
[9]:	https://github.com/DebugUself/du4proto/issues/339
[10]:	https://github.com/DebugUself/du4proto/blob/YHarticles/2018-01-16-install-ubuntu-in-virtualbox-win10.md
[11]:	https://github.com/DebugUself/du4proto/blob/kaggle/doc/lichuan_log.md
[12]:	https://github.com/DebugUself/du4proto/tree/hetao/Translation/Python-in-Hydrology
[13]:	https://github.com/DebugUself/du4proto/blob/1d9c744996936dece2dd06d857c6afd26dd57d57/git/1.md
[14]:	http://weekly.pychina.org/importpython/importpython-159.html
[15]:	https://github.com/the0demiurge/Python-Scripts
[16]:	https://the0demiurge.blogspot.jp/2017/10/shadowsocksshare.html
[17]:	https://learnxinyminutes.com/
[18]:	https://github.com/adambard/learnxinyminutes-docs
[19]:	http://puredanger.github.io/tech.puredanger.com/
[20]:	http://weekly.pychina.org/archives.html
[21]:	https://www.brainyquote.com/quotes/quotes/h/henryford121997.html
[22]:	https://www.brainyquote.com/quotes/quotes/h/henryford121997.html