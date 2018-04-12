---
title: "DU23w"
date: 2017-09-18T20:20:00+08:00
---

# 怼周刊\_v23
\~ 预定 17.9.18 20:20 发布

Release time - 20:20, September 18th, 2017

---- 

变量之墙

	入秋广鹤燥
	熊猫截取用变量
	须数塞串囧


The wall of variable

	Guanghe being flippancy in the fall
	Pandas selected by variable 
	Must be int but into string
	o(╯□╰)o

小鹤译版

	Spring or Autumn rightnow
	String or int in Pandas variable
	Alice confused all

p.s. 小鹤所在新西兰是春天, 英文也要跟中文的 短-长-短 一致, 末尾押韵[au]

小鹤德语

	Frühling oder Herbst jetzt
	String oder int im Pandas Variable
	Alice verwirrt alle


---- 

- 主编: [大妈][1]
- 责编:
	+ [xpgeng][2]
	+ [sunoonlee][3]
	+ [Zoe][4]
	+ [bambooom][5]

# 进度 Timelines
\~ 记录当周关键事件日期+证据链接

- 170916 [42h\[TASK]20170916 怼周会 分享及纪要][6]


# 任务 Tasks
\~ 记述关键共怼任务 (如果没有, 留空)

- 170911 [4d\[BC]究竟 Python 都有什么运行姿势? 何时应用哪种?][7]



# 进展 Progress
\~ 整体上圈内部活跃指标情况

- 提交: 10 人,
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
	- @mxclover 自怼就业跃迁录
- 引发的作品:
	+ NIL
- 状态:

<table>
<tr><th>allcic Commit</th><th> times</th><th>weekly Commit</th><th> times</th></tr>
<tr><td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>348</td>
        <td>
            <a href='http://github.com/liguanghe'>liguanghe</a></td><td>19</td>

<tr><td>
            <a href='http://github.com/zoejane'>zoejane</a></td><td>301</td>
        <td>
            <a href='http://github.com/Wangjunyu'>Wangjunyu</a></td><td>13</td>

<tr><td>
            <a href='http://github.com/liguanghe'>liguanghe</a></td><td>266</td>
        <td>
            <a href='http://github.com/mxclover'>mxclover</a></td><td>9</td>

<tr><td>
            <a href='http://github.com/mxclover'>mxclover</a></td><td>173</td>
        <td>
            <a href='http://github.com/vanxv'>vanxv</a></td><td>7</td>

<tr><td>
            <a href='http://github.com/zhangshiyinrunwithcc'>zhangshiyinrunwithcc</a></td><td>138</td>
        <td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>2</td>

<tr><th>all Commit </th><th>Comments times</th><th>weekly Commit</th><th>Comments times</th></tr>
<tr><td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>149</td>
        <td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>3</td>

<tr><th>all Issue </th><th>Comments times</th><th>weekly Issue</th><th>Comments times</th></tr>
<tr><td>
            <a href='http://github.com/liguanghe'>liguanghe</a></td><td>460</td>
        <td>
            <a href='http://github.com/liguanghe'>liguanghe</a></td><td>37</td>

<tr><td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>402</td>
        <td>
            <a href='http://github.com/zhangshiyinrunwithcc'>zhangshiyinrunwithcc</a></td><td>8</td>

<tr><td>
            <a href='http://github.com/zhangshiyinrunwithcc'>zhangshiyinrunwithcc</a></td><td>310</td>
        <td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>7</td>

<tr><td>
            <a href='http://github.com/zoejane'>zoejane</a></td><td>107</td>
        <td>
            <a href='http://github.com/OMlalala'>OMlalala</a></td><td>6</td>

<tr><td>
            <a href='http://github.com/mxclover'>mxclover</a></td><td>76</td>
        <td>
            <a href='http://github.com/Wangjunyu'>Wangjunyu</a></td><td>5</td>

</table>

- 在线(测试ing..):
	+ `curl du.zoomquiet.us`
	+ `curl du.zoomquiet.us/v0/all/cic/rank/5/`
	+ `curl du.zoomquiet.us/v0/all/cil/rank/5/`
	+ `curl du.zoomquiet.us/v0/week/cic/rank/5/`
	+ `curl du.zoomquiet.us/v0/week/cil/rank/5/`

- [文档-\>du4proto/st at DU\_tools · DebugUself/du4proto][8]

# 成果 Achievements
\~ 各种成品/半成品 内部知识作品

## @atl4damaAll 时间账单阶段成果
-  SET4 效能指数
	- 算法: 参考网络流量的收费统计: 次峰计费原则
```
    可以尝试用: 输出峰值平均时长 (TOTa ~ Top Output Time average) 为间接效能指标
        统计一周内所有输出行为
        以每次输出用时排序
        取前 20% 为当周有效输出
        取平均时长,计为 xx.xTOTa
    配合对应的: 低产峰值平均时长 (LOTa ~ Low Output Time average) 为对比效能指标
        统计一周内所有 沟通/输入 行为
        以每次用时排序
        取前 20% 为当周输出低产峰值总量
        取平均时长,计为 xx.xLOTa
    以及每天的: 中断指数 (TBI ~ Totle Broken Index) 为加权
        TBT ~ 中断总时长
        TBC ~ 中断次数
        设每天有效工作时间为8小时
        (TBT/TBC)/(86060) -> 平均中断时长 占有效工作时间比例 -> TBI
        即,每天平均中断时长占有效工作时间的比例, 记为: xx.xTBI

    SET4 (Simple Efficiency Time for DU)指标
    ~=
    (TOTa/LOTa)*(1-TBI)
```
	- 数据: 时间账单原始数据 -> 数据清洗 -> SET4 算法
```
2013,10,0.7680911558109835
2013,11,1.189180055912261
2013,12,1.39789172884749
2013,13,1.3416940789473684
2013,14,0.35046302012594144
...
```
	- 可视化: 通过 pandas 在 jupyter notebook 中实现
```
tr = pd.read_csv('/Users/liguanghe/du4proto/src/_atl2log/atl2SET4dama_all.csv')
tr.columns = ['year','week','set4']
ax = tr.plot.line(x='week',y='set4')
ax
plt.show()
```
![][image-1]

## @liguanghe
- 小鹤博客 | 域外生活录 | [Meals 吃了么 | Li Guanghe's blog][9]
- 小鹤博客 | 域外生活录 | [Single Room in Hostel 七夕搬单间][10]
- 小鹤博客 | python 基础 | [Basic Element and Grammer of Coding][11]


## @liguanghe
- 荔枝播客: 李广鹤
- 新增读书:
	- [集异璧 第九章 无门与哥德尔][12]
	- [集异璧 下篇异集璧 前奏曲][13]
	- [[集异璧 描述的层次和计算机系统1]在线收听\_李广鹤\_荔枝FM](https://www.lizhi.fm/2040956/2623781339466401798)
	- [[集异璧 第十章 描述的层次和计算机系统 2]在线收听\_李广鹤\_荔枝FM](https://www.lizhi.fm/2040956/2623923951707203078)
- 关联专辑: [[哥德尔 爱舍尔 巴赫]在线收听\_mp3下载\_荔枝FM](https://www.lizhi.fm/2040956/album/2614866758795105307)
- 英语分享: 
	- [[dunedin supermarket]在线收听\_李广鹤\_荔枝FM](https://www.lizhi.fm/2040956/2623943680638578182)
	- [[dunedin dinner for friendship]在线收听\_李广鹤\_荔枝FM](https://www.lizhi.fm/2040956/2624175737723394566)
	- [[dunedin he is coming]在线收听\_李广鹤\_荔枝FM](https://www.lizhi.fm/2040956/2624871245400072198)
- 关联专辑: [[Dunedin NZ]在线收听\_mp3下载\_荔枝FM](https://www.lizhi.fm/2040956/album/2613131869163763739)

# 故事 Stories
\~ 收集各自无法雷同的怼圈真人故事...

## 熊本🐻心语-\>有小队真好

自从怼圈s06e51以来<br>
atl4dama小队已连续举办3次会议<br>

每当周六上午不想起床逃避世界时候<br>
都会挣扎着打开zoom<br>
听到队友积极讨论项目细节的声音<br>

从争论pandas折线图是否有意义<br>
到看到队友把预想中的折线图做出来<br>
从深陷数据清洗细节无法推进进度<br>
到队友提醒先跟上小队节奏<br>

快要放弃时候<br>
耳边就会响起小明小鹤响亮的声音<br>
于是也不好意思再放弃下去<br>

虽说今后几个月依然风雨缥缈<br>
也不知道自己能为小队做什么<br>
但是有一个自己参与的小队<br>
不管做多做少<br>
每周每日都在叽叽喳喳的小队<br>
还是有种当下社会难以遇到的幸福感<br>

有小队真是幸福哇<br>
O(∩\_∩)O哈哈\~\_)<br>

## @liguanghe @atl4damaAll 血案故事: pandas variable int.

时间账单项目(branch: atl4dama), 尝试用 pandas 可视化的小鹤终于弄懂了想要的数据类型, 即一张 set4 的列表. 回头翻小明的尝试文档发现, 小明同学用时 6 小时, 手动生成2014年52周 set4 数据. 如何将其中手动部分转成自动生成表格呢? 小鹤再这里进行了尝试, 怼出pandas 的平均数代码等等. 只一处不过, 遇到报错:
```
TypeError: cannot do slice indexing on <class 'pandas.core.indexes.numeric.Int64Index'> with these indexers [otn] of <class 'str'>
```
因对 int 和 'str' 不敏感, (恩恩, 不知道 int 是什么), 便误以为是上位概念 variable 整个不支持, 在此处折腾两天, 遍查不到(google/github/slackflow), 差点要去 pandas官方 github 处开 issue, 留下污点. 好在大妈云, 自然查不到, 因为 pandas 支持 variable, 那里需要填的是个整数(int)而已. 于是 遂将 otn 改成 int(otn),即解决. 

这个故事告诉我们, bug不在别人在自己, 要相信模块是高手智慧的结晶, 错的一定是自己. 也告诉我们, 千万不要忽略报错信息, 详读报错信息, 了解每一个字的含义. 

(细节在此: [6h\[QUESTION]\[atl4dama]pandas 想选取的行数是个变量, 如何实现? ][14])

也经大妈提醒发现自己在编程的过程中, 没有建立调试习惯. 开 issue 以供讨论: [42h\[TASK]建立 dir type id help 等一系列内建自省函式][15]


# 推荐 Recommedations
\~ 嗯哼各种怼路上发现的嗯哼...


- 是也乎:
	+ [Octomender][16] 
	+ [蠎加载 142 |蠎周刊 |汇集全球蠎事儿 !-)][17]

# 后记 Postscript
\~ 怼周刊是什么以及为什么和能怎么...

大妈曰过: `参差多态 才是生机`
问题在 `参差` 的行为是无法形成团队的

	Coming together is a beginning; 
	Keeping together is progress; 
	Working together is success!

\<--- [Henry Ford][18]

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

\<--- [Henry Ford][19]

That's why Dama keeps on debugging.
However, as time goes by, maybe you would not remember these days clearly and spread your experience difficultly.
What a pity!
The valuable should have a fixed form to be recorded.
That's why we make the Weekly for DU.



[1]:	http://du.zoomquiet.io/2014-02/ac0-zq/
[2]:	http://du.zoomquiet.io/2017-04/about-xpgeng/
[3]:	http://du.zoomquiet.io/2017-04/about-sunoonlee/
[4]:	http://du.zoomquiet.io/2017-04/about-zoe/
[5]:	http://du.zoomquiet.io/2017-04/about-bambooom/
[6]:	https://github.com/DebugUself/du4proto/issues/231
[7]:	https://github.com/DebugUself/du4proto/issues/227
[8]:	https://github.com/DebugUself/du4proto/tree/DU_tools/st
[9]:	https://liguanghe.github.io/2017/09/16/Dunedinfoods/
[10]:	https://liguanghe.github.io/2017/09/08/DunedinSingleRoom/
[11]:	https://liguanghe.github.io/2017/09/11/BasicEementGrammerOfCoding/
[12]:	https://www.lizhi.fm/2040956/2622445417806639110
[13]:	https://www.lizhi.fm/2040956/2623745319720417286
[14]:	https://github.com/DebugUself/du4proto/issues/221
[15]:	https://github.com/DebugUself/du4proto/issues/230
[16]:	https://octomend.com/
[17]:	http://weekly.pychina.org/importpython/importpython-142.html
[18]:	https://www.brainyquote.com/quotes/quotes/h/henryford121997.html
[19]:	https://www.brainyquote.com/quotes/quotes/h/henryford121997.html

[image-1]:	https://ws2.sinaimg.cn/large/006tNc79gy1fjnd6x39l3j30mc0f4whb.jpg