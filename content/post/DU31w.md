---
title: "DU31w"
date: 2017-11-13T20:20:00+08:00
---

# 怼周刊\_v31
\~ 预定 17.11.13 20:20 发布

Release time - 22:45, November 20th, 2017

---- 

本周定场诗 无

---- 



- 主编: [大妈][1]
- 责编:
	+ [xpgeng][2]
	+ [sunoonlee][3]
	+ [Zoe][4]
	+ [bambooom][5]

# 进度 Timelines
\~ 记录当周关键事件日期+证据链接

- [42h\[TASK]20171111 怼周会迎新及纪要][6]

# 任务 Tasks
\~ 记述关键共怼任务 (如果没有, 留空)


# 进展 Progress
\~ 整体上圈内部活跃指标情况

- 提交: 5 人,
  + @zhangshiyinrunwithcc 
  + @leilayanhui 
  + @liguanghe 
  + @ZoomQuiet
  + @zoejane  

- 引发的作品:
	+ NIL
- 状态:

由于统计接口问题,本次没有统计表...

[72h\[DUW]怼周刊进展Progess状态chk4st.py运行报错JSONDecodeError][7]

- 在线(测试ing..):
	+ `curl du.zoomquiet.us`
	+ `curl du.zoomquiet.us/v0/all/cic/rank/5/`
	+ `curl du.zoomquiet.us/v0/all/cil/rank/5/`
	+ `curl du.zoomquiet.us/v0/week/cic/rank/5/`
	+ `curl du.zoomquiet.us/v0/week/cil/rank/5/`
	+ ...


# 成果 Achievements
\~ 各种成品/半成品 内部知识作品

## @zoejane - 怼周刊网页版

- 链接 - [DU Weekly 怼周刊][8]
- Issue - [72h \[DUW]怼周刊网页版送上 · Issue #288][9]
- 快速翻阅往期怼周刊,手机上也可以快乐的阅读怼周刊啦


# 故事 Stories
\~ 收集各自无法雷同的怼圈真人故事...

- [关乎社群:1 自怼圈的由来 | DebugUself with DAMA ;-)][10]

## 熊本🐻-\>怼圈感受:泽鱼与溪鱼

```
渔父词 唐.储光羲

泽鱼好鸣水,溪鱼好上流.
渔梁不得意,下渚潜垂钩.
乱荇时碍楫,新芦复隐舟.
...
素发随风扬,远心与云游.
逆浪还极浦,信潮下沧洲.
非为徇形役,所乐在行休.

注:渔梁为捕鱼工程,古时在上流建木闸,可诱捕进出闸门的鱼.
```

- 怼圈与开智不同,花样繁多.本熊在自怼圈第1期招新时来到自怼圈.第1期怼员大体有3种玩法:
	+ 1.立刻启动自己小项目,比如AI作音乐,统计怼员commit次数等作品;
	+ 2.尝试参与小组项目
	+ 3.参与维护,运营怼圈
- 本文记录了本熊加入自怼圈来30w的3个阶段,3个阶段本熊参与的项目各有不同,且角色不同.从摸索git的小白,到参与小队项目,再到参与怼圈维护.
- 每个角色有各自的乐趣,即使同为怼员,也有泽鱼与溪鱼之分.泽鱼喜好平静湖水,溪鱼喜好热闹溪流.愿大家都能体验怼圈不同角色带来的乐趣.


### 第一阶段:神秘的Git!
- 本熊的背景
	+ 0 \~ 10w
	+ 刚加入自怼圈时,还不会使用git,github将本地diff推送到远程库.
	+ 进入自怼圈干得第一件大事是,学习用git和github将本地目录与远程库进行ssh配置,连接;学习将本地diff推送到远程库.
- 本熊的行动
	+ [DU2w故事:惨案:难以push到master][11]
	+ [[ASK]git push origin master报错refusing to merge unrelated histories应该搜索关键词是?](https://github.com/DebugUself/du4proto/issues/27)
- 本熊的感受
	+ **大妈常言:用之弗学**.在本阶段,花费接近1个月时间,只为学习git push等5行简单基本命令.为何耽误良久?
		* 特殊原因:由于一开始使用Github时,身在特殊部门,网络连接经过特殊设置,导致git push等命令无法执行.后转移至其他网络环境,git push 成功.
		* 常规原因:花费较多时间试图明白ssh和git push原理,而非真正探索 **如何使用git**.
	- **认知负荷无处不在**
		* 这种负荷主要来自2方面:一方面是,老怼员已经构建起基本的怼圈规则,而新怼员需要服从于该规则,学习新规则已经导致新怼员的 **认知负荷** ;
		* 另一方面,老怼员熟悉怼圈规则是因为其创造/撰写了规则(截止目前怼圈已有56篇wiki),而新怼员熟悉怼圈规则却要依靠阅读文档/wiki来熟悉怼圈.老怼员靠 **动手** 来学习规则,新怼员却要依靠 **看书** 来学习规则.**动手明显优于看书** .
- 本熊的改变
	+ 从试图明白它是什么,转向先不管它是什么,先明白怎么用它?
	+ 然而,此阶段,本熊还尚未形成 **记录习惯**,所以学习git过程中很多细节都没有可以追查的记录

### 第二阶段:进击的时间账单小队
- 本熊的背景
	+ 10 \~ 20w
	+ 加入自怼圈第1个小队项目,时间账单小队atl4dama
	+ 时间账单项目的目标是,通过分析大妈8年的时间记录数据,衡量大妈效能
- 本熊的行动
	+ [DU13w故事:熊本🐻-\>atl4dama见闻录1:从零开始才放心][12]
	+ [DU14w故事:熊本🐻-\>atl4dama见闻录2: good csv可能长啥样(上)?][13]
	+ [DU14w故事:熊本🐻-\>atl4dama见闻录2: good csv可能长啥样(下)?][14]
	+ [DU15w故事:熊本🐻-\>atl4dama见闻录4:自学, 病在哪里?][15]
	+ [DU16w故事:熊本🐻-\>怼圈放弃录1:5个42分钟][16]
	+ [DU17w故事:熊本🐻-\>atl4dama见闻录5:以功能/管道为线索拆解代码][17]
	+ [DU17w故事:熊本🐻-\>小熊42分钟开发手册之狗六的魔像][18]
	+ [DU20w故事:熊🐻本来稿-\>时间账单效能小队duwk20进展][19]
	+ [DU28w故事:熊本🐻-\>atl4dama使用手册1:微小的不幸][20]
	+ [DU28w成果:atl4dama4UserManual][21]
	+ [DU30w成果:alt4dama2MakeSET4][22]
- 本熊的感受
	+ **一定要对探索过程形成可追查的记录**
		* 1. 发布issue
		* 2. 怼周会例行怼
		* 3. 怼周刊文章沉淀
	+ **记录,控制探索怼圈的成本,风险**
		* 自怼圈不少探索,是需要付出 **更高的时间,精力成本,以及承担作品很可能失败的风险.** 倘若只凭着对创造的喜爱,就随意指定目标,处处播散种子,很容易陷入一事无成且自信全无的困局.(参见怼周刊[DU24w故事:熊本🐻-\>0902怼周会:探索之'江湖险恶'][23])
- 本熊的改变
	+ 从不记录到,形成了 **记录的习惯**
	+ 将atl4dama探索过程,形成了11篇文档,并投稿怼周刊

### 第三阶段:最爱的怼周刊
- 本熊的背景
	+ 20 \~ 30w
	+ 编辑,发布5期怼周刊
- 本熊的行动
	+ [DU26w成果:熊本🐻-\>怼周刊发布手册][24]
	+ [DU30w成果:熊本🐻-\>如何在怼周刊任务,成果2个版块形成固定投稿节奏?][25]
- 本熊的感受
	+ **自运营**
		* 自怼圈与开智课程显著区别是 **怼圈具备自运营的性质** .在开智,课程运营人员会帮助组织多学员对一教练的答疑,而学员的沉淀笔记也往往是由开智运营人员审定发布在开智app里.**使用一个平台与构建一个平台是两种完全不同的体验.** 在怼圈,怼员自行编辑审定发布怼周刊,自行组织筹办怼周会.由 **使用平台人员升级为构建,维护平台人员, 被赋予更多创造的机会.** 参与的目标由 **完成任务** 到 **制定任务** ,自由性更多,目标也更为多样性.
	+ **写自己个儿的使用手册**
		* 不要太过在乎老怼员的文档,建议,操作流程,一定要亲身体会,亲手测试.因为
		老怼员与新怼员之间,**天然存在预期偏差** :老怼员认为文档中理所应当需要记录的事,可能新怼员从来没有注意过.而新怼员认为老怼员在文档里应该给予的提示,老怼员却认为可有可无.久而久之,怼员会发现,**研究怼圈文档不如自己动手撰写新文档好**.
- 本熊的改变
	+ 从依赖别人的文档企图尽快完成功能,转变至多问别人当时为什么这样写
	+ 然后再写一篇基于自己个儿测试体验的新文档(参见[DU28w故事:熊本🐻-\>atl4dama使用手册1:微小的不幸][26])






# 推荐 Recommedations
\~ 嗯哼各种怼路上发现的嗯哼...

- 是也乎:
	+ [蠎加载 150 \|蠎周刊 \|汇集全球蠎事儿 \!\-\)][27]
	+ [用问题对话虚无 --- HackYourself 大哉问系列][28]


# 后记 Postscript
\~ 怼周刊是什么以及为什么和能怎么...

大妈曰过: `参差多态 才是生机`
问题在 `参差` 的行为是无法形成团队的

	Coming together is a beginning; 
	Keeping together is progress; 
	Working together is success!

\<--- [Henry Ford][29]

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

\<--- [Henry Ford][30]

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
[6]:	https://github.com/DebugUself/du4proto/issues/286
[7]:	https://github.com/DebugUself/du4proto/issues/291
[8]:	https://duw.zoejane.net/
[9]:	https://github.com/DebugUself/du4proto/issues/288
[10]:	http://du.zoomquiet.io/2017-11/ac1-du4new/
[11]:	https://github.com/DebugUself/du4proto/blob/e56db1a41713e105c6b950c37ce3b299943fa461/DU2w.md#%E6%83%A8%E6%A1%88-%E9%9A%BE%E4%BB%A5-push-%E5%88%B0-master
[12]:	https://github.com/DebugUself/du4proto/blob/DUW/DU13w.md#zsy---%E7%86%8A%E6%9C%AC-atl4u-%E8%A7%81%E9%97%BB%E5%BD%951-%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%E6%89%8D%E6%94%BE%E5%BF%83
[13]:	https://github.com/DebugUself/du4proto/blob/DUW/DU14w.md#%E7%86%8A%E6%9C%AC--atl4dama%E8%A7%81%E9%97%BB%E5%BD%952-good-csv%E5%8F%AF%E8%83%BD%E9%95%BF%E5%95%A5%E6%A0%B7%E4%B8%8A
[14]:	https://github.com/DebugUself/du4proto/blob/DUW/DU14w.md#%E7%86%8A%E6%9C%AC--atl4dama%E8%A7%81%E9%97%BB%E5%BD%952-good-csv%E5%8F%AF%E8%83%BD%E9%95%BF%E5%95%A5%E6%A0%B7%E4%B8%8B
[15]:	https://github.com/DebugUself/du4proto/blob/DUW/DU15w.md#%E7%86%8A%E6%9C%AC--atl4dama%E8%A7%81%E9%97%BB%E5%BD%954%E8%87%AA%E5%AD%A6-%E7%97%85%E5%9C%A8%E5%93%AA%E9%87%8C
[16]:	https://github.com/DebugUself/du4proto/blob/DUW/DU16w.md#%E7%86%8A%E6%9C%AC---%E6%80%BC%E5%9C%88%E6%94%BE%E5%BC%83%E5%BD%951-5%E4%B8%AA42%E5%88%86%E9%92%9F
[17]:	https://github.com/DebugUself/du4proto/blob/DUW/DU17w.md#%E7%86%8A%E6%9C%AC-atl4dama%E8%A7%81%E9%97%BB%E5%BD%955%E4%BB%A5%E5%8A%9F%E8%83%BD%E7%AE%A1%E9%81%93%E4%B8%BA%E7%BA%BF%E7%B4%A2%E6%8B%86%E8%A7%A3%E4%BB%A3%E7%A0%81
[18]:	https://github.com/DebugUself/du4proto/blob/3f22c0c0cf523d9baff5139563e8371f47c66f20/DU17w_draft.md#%E7%86%8A%E6%9C%AC-%E5%B0%8F%E7%86%8A42%E5%88%86%E9%92%9F%E5%BC%80%E5%8F%91%E6%89%8B%E5%86%8C%E4%B9%8B%E7%8B%97%E5%85%AD%E7%9A%84%E9%AD%94%E5%83%8F
[19]:	https://github.com/DebugUself/du4proto/blob/DUW/DU20w.md#%E7%86%8A%E6%9C%AC%E6%9D%A5%E7%A8%BF-%E6%97%B6%E9%97%B4%E8%B4%A6%E5%8D%95%E6%95%88%E8%83%BD%E5%B0%8F%E9%98%9Fduwk20%E8%BF%9B%E5%B1%95
[20]:	https://github.com/DebugUself/du4proto/blob/DUW/DU28w.md#%E7%86%8A%E6%9C%AC-%E8%A7%86%E8%80%8C%E4%B8%8D%E8%A7%811%E5%BE%AE%E5%B0%8F%E7%9A%84%E4%B8%8D%E5%B9%B8
[21]:	https://github.com/DebugUself/du4proto/blob/atl4dama/try/bearManual/atl4dama4UserManual.md
[22]:	https://github.com/DebugUself/du4proto/blob/atl4dama/try/bearManual/alt4dama2MakeSET4.md
[23]:	https://github.com/DebugUself/du4proto/blob/DUW/DU24w.md#%E7%86%8A%E6%9C%AC-0902%E6%80%BC%E5%91%A8%E4%BC%9A%E6%8E%A2%E7%B4%A2%E4%B9%8B%E6%B1%9F%E6%B9%96%E9%99%A9%E6%81%B6
[24]:	https://github.com/DebugUself/du4proto/blob/DUW/DU26w.md#%E7%86%8A%E6%9C%AC-%E6%80%BC%E5%91%A8%E5%88%8A%E5%8F%91%E5%B8%83%E6%89%8B%E5%86%8C
[25]:	https://github.com/DebugUself/du4proto/blob/DUW/DU30w.md#%E7%86%8A%E6%9C%AC-%E5%A6%82%E4%BD%95%E5%9C%A8%E6%80%BC%E5%91%A8%E5%88%8A%E4%BB%BB%E5%8A%A1%E6%88%90%E6%9E%9C2%E4%B8%AA%E7%89%88%E5%9D%97%E5%BD%A2%E6%88%90%E5%9B%BA%E5%AE%9A%E6%8A%95%E7%A8%BF%E8%8A%82%E5%A5%8F
[26]:	https://github.com/DebugUself/du4proto/blob/DUW/DU28w.md#%E7%86%8A%E6%9C%AC-%E8%A7%86%E8%80%8C%E4%B8%8D%E8%A7%811%E5%BE%AE%E5%B0%8F%E7%9A%84%E4%B8%8D%E5%B9%B8
[27]:	http://weekly.pychina.org/importpython/importpython-150.html
[28]:	https://mp.weixin.qq.com/s/sAuFqaFtP3-0ars-3047Og
[29]:	https://www.brainyquote.com/quotes/quotes/h/henryford121997.html
[30]:	https://www.brainyquote.com/quotes/quotes/h/henryford121997.html