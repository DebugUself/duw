---
title: "DU11w"
date: 2017-06-24T20:20:00+08:00
---

# 怼周刊\_v11
\~ 预定 17.6.24 20:20 发布

---- 

i am backing...

	魂未离兮 往时差
	身将返兮 此周六
	例会行兮 空客中
	wifi渺兮 请自治
	归兮归兮 自怼圈
	敢不止兮 debug

---- 

- 主编: [大妈][1]
- 责编:
	+ [xpgeng][2]
	+ [sunoonlee][3]
	+ [Zoe][4]
	+ [bambooom][5]

# 进度
\~ 记录当周关键事件日期+证据链接

- 170617 [[TASK]2017-06-17 怼周会及纪要 · Issue #147 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/147)
- 170401 关闭报表和入密
- 170331 om103py 毕业

# 任务
\~ 记述关键共怼任务 (如果没有, 留空)

- 170603 [怼圈的二次开放 筹备中][6]
- 170527 [S03E51 启动][7]


# 进展
\~ 整体上圈内部活跃指标情况

- 提交(S03E051): 12 人 (1个5人小组 + 7 个个人项目)
   - 小组 @zoomquiet 时间帐单:效能分析小队
	   - @zoomquiet 
	   - @zsy
	   - @liguanghe
	   - @simpleowen 
	   - @mxclover 
   - @bambooom chrome 插件 & Vue 学习
   - @fatfox2016 分析当前政府招标市场信息,生成市场情况报告
   - @livingworld Deep Learning自学计划
   - @sunoonlee 机器学习
   - @xpgeng 深度学习
   - @yuanchunrong 使用Django搭建个人博客计划
   - @zoejane 体验如何能让计算机作曲 (Google Magenta)
- 引发的作品:
	+ @zoejane - AI 作曲一首 Magenta\_03
- 状态:

<table>
<tr><th>allcic Commit</th><th> times</th><th>weekly Commit</th><th> times</th></tr>
<tr><td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>254</td>
        <td>
            <a href='http://github.com/zoejane'>zoejane</a></td><td>9</td>
            
<tr><td>
            <a href='http://github.com/zoejane'>zoejane</a></td><td>212</td>
        <td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>7</td>
            
<tr><td>
            <a href='http://github.com/liguanghe'>liguanghe</a></td><td>116</td>
        <td>
            <a href='http://github.com/simpleowen'>simpleowen</a></td><td>3</td>
            
<tr><td>
            <a href='http://github.com/bambooom'>bambooom</a></td><td>106</td>
        <td>
            <a href='http://github.com/mxclover'>mxclover</a></td><td>2</td>
            
<tr><th>all Issue </th><th>Comments times</th><th>weekly Issue</th><th>Comments times</th></tr>
<tr><td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>307</td>
        <td>
            <a href='http://github.com/zoejane'>zoejane</a></td><td>6</td>
            
<tr><td>
            <a href='http://github.com/zhangshiyinrunwithcc'>zhangshiyinrunwithcc</a></td><td>154</td>
        <td>
            <a href='http://github.com/Zxlon'>Zxlon</a></td><td>1</td>
            
<tr><td>
            <a href='http://github.com/liguanghe'>liguanghe</a></td><td>127</td>
        <td>
            <a href='http://github.com/NBR-hugh'>NBR-hugh</a></td><td>1</td>
            
</table>

-\> 17.06.124 17:41

- 在线(测试ing..):
	+ `curl du.zoomquiet.us`
	+ `curl du.zoomquiet.us/v0/all/cic/rank/5/`
	+ `curl du.zoomquiet.us/v0/all/cil/rank/5/`
	+ `curl du.zoomquiet.us/v0/week/cic/rank/5/`
	+ `curl du.zoomquiet.us/v0/week/cil/rank/5/`


# 成果
\~ 各种成品/半成品 内部知识作品

## zoejane - AI 作曲 (Magenta 03)

* [Project Plan][8]
* Magenta 写的第三首音乐
	* [magenta\_03(improv\_rnn) @SoundCloud][9]

## 时间帐单:效能分析小队 推进中

- 组员
	* `(￣▽￣)` -\> 大妈
	* 🐻 `熊` =\> @zhangshiyinrunwithcc
	* 🐣 `鹤` =\> @李广鹤
	* 🐈 `猫` =\> @simpleowen
	* 🐴 `mx` =\> @mxclover
-  目标
	- 通过分析大妈和剑飞, 两人5年以上持续时间帐单的数据
	- 获得数据化的行为效能结论
	- 对自身行为给出几点优化策略
- [Github 项目链接][10]
- [Project Plan][11]    

# 故事
\~ 收集各自无法雷同的怼圈真人故事...

## @simpleowen - 案例:如何定位与解决问题

### 背景

时间账单小分队进行数据清洗中...  

@mxclover: 
> 14年3月5号之后的数据类型 都变成chaos 了... ..

### 分析
* 重现现象
	* 使用同一脚本 zq1actype.py
	* 任意取一份3月5号之后的数据 aTLer\_140901-141001\_report.csv
	* 执行 cat ../raw/zoomquiet/1302--report/aTLer\_140901-141001\_report.csv | python3 zq1actype.py
	* 获得重现确认
	* 每个活动分类都变成了 chaos
* 观察数据
	* 快速查看3月5号前后的原始数据
	* 对比异同
	* 发现3月5号后的数据,每个数据项都被双引号包围
	* "GDG","01:46","2014-03-10 10:43","2014-03-10 12:30",
	* 而3月5号之前的数据则没有双引号
	* 用餐,1.0,02/27/14 19:15,02/27/14 20:17,
* 调试代码
	* 观察代码逻辑流程
	* 在关键位置放置 print
	* 屏蔽 print 以后的代码
	* 观察输出
	* 重复 print -\> 屏蔽 -\> 观察 的过程,直到定位到问题的源头
	* 找到原因以后修复问题就比较快了

### 结论

面对纠结局面时,应将问题切片,设法创建一些单纯的场景,以单纯化解复杂

### 大妈提点

观察出问题... 就去调通哪...  这就是机会... 

异同是肉眼看出来的, 问题是怎么看 ,以及用什么问题过滤技巧来看 代码检测, 则包含了更多的技巧: 怎么追加代码? 在哪儿? 或是另外重新写代码?运行?检验数据准备? 怎么设计代码? 怎么不触动以往的即有代码? ...  每个点都是习惯

所以, 看起来清洗是整个项目中最简单的 因为目标相对最简单 但是, 作起来才知道有多少事儿要作

从现象到定位问题再解决, 这个过程的无阻碍自主进行, 就是编程基本功之一

所以,无论多小心, 面对长期数据时,总是有意外发生 虽然具体问题都不复杂 问题是纠结在一起时, 现象是千变万化的 导致很难判定... 

快速设计出单纯的场景隔离其它问题,捕获指定问题, 才能进一步快速解决

这就是流水线的原理哪... . 将复杂的制造过程, 分解为每个工位上简单的行为 降低工人的培训成本, 同时提高可替代性... . 对于代码而言... .就是每次只用尽可能少的代码处理尽可能单纯的运算

编程, 就两种模式 复杂到看不出问题 简单到无法容纳问题... 

## @zoejane - 怼圈三个月体验分享

### S03E51 小结 - 状态不好也不影响去做

- 缘起
	- 这个月觉得状态并不好,除了月初那几天真的是很投入,后来大部分都比较打酱油. 
	- 但是当自己整理这个月做的东西的时候,又觉得没有那么糟糕. 三首音乐,一段视频,几篇笔记,居然感觉也还挺充实的. 
- 体验
	- 即使状态不好,也不影响自己做一件事情. 
		- 因为有时候做着做着状态就来了. 
		- 即使没有状态,好歹也是练个手熟,混个眼熟,也算是在积累和练习了. 做得烂也比光想不做好. 
	- 更清楚的认识了自己的时间和精力. 
		- 以为自己有时间又状态好只是一种幻觉. 之前订计划时总把自己的状态想得很好,然后以为总是有意外打乱了我的节奏. 
		- 真正体验过后发现大部分时间都会是面临临时加班,临时哄娃,睡眠不足,心情不好等状态. 这才是我生活中的常态. 
		- 订计划时要充分考虑自己没有时间,精力不足的日常情况. 让自己可以在这种情况下也能完成任务,而不是老是订不切实际的计划打击自己. 
	- 以作品为导向订计划更容易完成. 
		- 把东西都学完很难. 基本看到中途就打瞌睡了. 
		- 但是做出一个简单的作品还是比较容易的,总是会多少做多少. 而且也更有成就感一些. 
		- 做出作品后,自己才更能体会自己之前学习的东西,更愿意去学,也更愿意学得进去,因为有实际的问题要去解决.  
		- 以作品为导向也更容易衡量本周是否完成任务了. 不然看的东西很杂,学习进度不好衡量. 

### 三个月的收获 - 我居然可以每月探索一个自己喜欢的主题

- 我居然也可以完成计划了. 
	 - 这三个月最让我震惊的,莫过于我居然可以给自己订月计划,并且真的完成了大部分了. 要知道,我原来这么多年订的计划就从来没有完成过,长期处于临时抱佛脚,担当各种事情救火队员的状态.
- 给自己营造一个环境. 
	- 自己做基本上自律不起来,但是在一个社群里,感觉又不同了,还是更有前进动力一些. 总之了解了自己一个人不自律的弱点后,就不要去挑战自己这个弱点,而是给自己创造好环境,自己只要懒懒的被动前进就好,哈哈.
- 我居然还可以探索那么多的事情. 
	- 另一个让我震惊的就是,我居然可以每个月探索一些不同的好玩的事情. 
	- 以前我总觉得我很多事情都来不及做. 工作和家庭的双重压力,让我觉得几乎没有自我的时间了. 
	- 现在我发觉,即使正常上班和哄娃,一年居然可以挤出一点时间,探索十二件我觉得有意思的事,我又觉得生活变得好玩了起来. 

### 三个月的困难 - 总是碰到低谷想放弃

- 低潮比我想象的还多. 
	- 常常觉得走不下去了,觉得自己是不是有问题. 后来发现,也不是自己有问题,大部分人都是这样的. 基本上我低谷的时候,整个怼圈也是低谷,所以自己也不用太过自责,要学会更坦然一点.
- 低谷也不见得就要停下来. 
   - 想想自己连不喜欢的工作都能做下来,也没见出什么大的问题啊. 为什么面对自己喜欢的事情,反而要那么轻易说放弃. 哪怕心情麻木,哪怕感觉自己原地踏步,总之还是
- 有波谷也会有波峰,只是正常的交替. 
	- 走过去了,就会见到下一次波峰,当然,也还会遇到下一次波谷. 
	- 总之不管是什么样的节奏,能做点自己喜欢的事情,能认识一些自己欣赏的人,不也挺好嘛. 




# 推荐
\~ 嗯哼各种怼路上发现的嗯哼...

# 后记
\~ 怼周刊是什么以及为什么和能怎么...

大妈曰过: `参差多态 才是生机`
问题在 `参差` 的行为是无法形成团队的

	Coming together is a beginning; 
	Keeping together is progress; 
	Working together is success!

\<--- [Henry Ford][12]

- 所以, 有了 大妈 随见随怼的持续嗯哼...
- 但是, 想象一年后, 回想几十周前自己作的那些 `图样图森破` 
- 却没现成的资料来出示给后进来嗯哼?
- 不科学, 值得记录的, 就应当有个形式固定下来
- 所以,有了这个 `怼周刊` (Weekly 4 DU)


[1]:	http://du.zoomquiet.io/2014-02/ac0-zq/
[2]:	http://du.zoomquiet.io/2017-04/about-xpgeng/
[3]:	http://du.zoomquiet.io/2017-04/about-sunoonlee/
[4]:	http://du.zoomquiet.io/2017-04/about-zoe/
[5]:	http://du.zoomquiet.io/2017-04/about-bambooom/
[6]:	https://github.com/DebugUself/du4proto/issues/135
[7]:	https://github.com/DebugUself/du4proto/blob/master/S03E51/README.md
[8]:	https://github.com/DebugUself/du4proto/blob/master/S03E51/du_s03e51_zoejane_plan.md
[9]:	https://soundcloud.com/zoezoejane/magenta_03
[10]:	https://github.com/DebugUself/du4proto/tree/atl4dama
[11]:	https://github.com/DebugUself/du4proto/blob/master/S03E51/du_s03e51_zoomquiet_plan.md
[12]:	https://www.brainyquote.com/quotes/quotes/h/henryford121997.html