---
title: "DU70w"
date: 2018-08-13T20:20:00+08:00
---

# 怼周刊\_v70
\~ 预定 18.8.13 20:20 发布
  实际 18.8.13 20:50 发布
---- 

...TODO


---- 

- 主编: [大妈][1]
- 责编:


# 进度 Timelines
\~ 记录当周关键事件日期+证据链接
- [42h\[TASK]20180811 怼周会 分享及纪要][2]


# 任务 Tasks
\~ 记述关键共怼任务 (如果没有, 留空)
- [6d\[TASK]新老怼友的测评报告, 来分析异同吧][3]

## 号召

- [|蠎周刊 |汇集全球蠎事儿 !-)][4]
	+ 俺私人嗯哼了5年了
	+ 邀请大家一起来, 每周嗯哼
- 每周例怼后, 无论是否列席, 大家都在 `故事->怼印象` 中追加当周 top3 感触



# 进展 Progress
\~ 整体圈内活跃指标情况([st][5] 专用服务, 尚少使用手册)

- PS: 获取不到 weekly Commit / times 数据，结果均为NIL

> 参考 [4w\[ASK] 怼周刊 进展 Progress/状态 统计方法 get不到数据 ][6]

# 成果 Achievements
\~ 各种成品/半成品 内部知识作品

- @izhangshiying
	+ 项目名称:用pandas做hist图
	+ 项目内容:用pandas对5个整数数据进行简单运算，并将运算结果可视化(matplotlib)
	+ 分支地址:[DebugUself/du4proto at zsy][7]
	+ ipynb地址:[du4proto/pandas-seriers-division-hist-pic.ipynb at zsy · DebugUself/du4proto][8]
- @liguanghe
	+ [我的怼圈1.0和2.0][9]
	+ [25d\[LOG]种一棵事业树(2) · Issue #433 · DebugUself/du4proto][10]
	+ [lghFL][11]
# 故事 Stories
\~ 收集各自无法雷同的怼圈真人故事...

## 熊本🐻 -\> 下载github远程库中的specific branch
#### 0.缘由
- 自己去年在du4proto增创建了属于自己的分支zsy
- 一年过去整个du4proto协同仓库已有53个branch
- 目标 -\> 只下载du4proto协同仓库自己主管的那1个分支

#### 1.资源
- [How to clone a specific Git branch? - Stack Overflow][12]

#### 2.命令行

	git init
	git remote add -t $BRANCH -f origin $REMOTE_REPO
	git pull origin $BRANCH_REMOTE:$BRANCH_LOCAL 

#### 3.结果

- 本地master分支成功与du4proto远程库zsy分支建立联系。
- 且只git clone了zsy分支内容到本地目录中。

![git-github-remote-specific-branch][image-1]

## 熊本🐻 -\> 怼圈的「乞食」精神

作为怼圈小白，本熊也经常感到自己的技术水平「饥寒相逼」。
一会儿出现conflict，一会儿kernel不能work，还经常弄错目录。
当陷入如此「饥寒窘境」时，本熊也曾暗自苦恼，期待「田螺姑娘」转世，「缸中」突然有米。

请教挨饿老师傅，陶潜大师。
师傅赠我「乞食」一诗，谓遵从此诗方可获救。
此诗如下

	乞食 陶潜
	饥来驱我去，不知竟何之。
	行行至斯里，叩门拙言辞。
	主人解馀意，遗赠岂虚来。
	谈谐终日夕，觞至辄倾杯。
	情欣新知欢，言咏遂赋诗。
	感子漂母惠，愧我非韩才。
	衔戢知何谢，冥报以相贻。

师傅的诗句大意为：饥饿来了驱赶我出门，我也不知道去向何方。
一路走走停停，在邻村门口叩响了一户人家的门扉，笨拙得解释着自己的窘境。
主人并没有因为我的愚笨而嫌弃，而是通解我的心意，馈赠给我丰富的食物。
我和主人相谈甚欢，把酒言诗。
我心中感怀这户主人慷慨的恩惠，像汉朝「漂母」一般(典故，见注释)。
但可惜我并非韩信之才，无法报答。
只希望日后若泉下相见，能有机会报答这户主人的恩情。
注释:[「漂母韩信」典故][13]

师傅智慧便是，「走出门，拙言辞，期遗赠，报相贻」。
- 对应到怼圈便是
	+ 存疑问 -\> 留心怼圈
	+ 提问题 -\> 发issue
	+ 期待回复 -\> 发issue
	+ 总结问题并回馈他人 -\> 存wiki

## 怼印象
\~ 例怼中感触最嗯哼的 top3 感想

- `lgh`
	+ 几位新怼都提到了发言会紧张, 不用紧张啦, 干啥都行. 
	+ 好几位怼友提到了要做前端, 可以一起组队打怪啊.
	+ 几位新怼介绍了自己, 也开始了怼圈的行动, 是个很好的开始. 加油\\~

# 推荐 Recommedations
\~ 嗯哼各种怼路上发现的嗯哼...

- [Welcome to Python cheatsheet!][14] 各种 python 代码片段的小抄，了解一下

# 后记 Postscript
\~ 怼周刊是什么以及为什么和能怎么...

大妈曰过: `参差多态 才是生机`
问题在 `参差` 的行为是无法形成团队的

	Coming together is a beginning; 
	Keeping together is progress; 
	Working together is success!

\<--- [Henry Ford][15]

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

\<--- [Henry Ford][16]

That's why Dama keeps on debugging.
However, as time goes by, maybe you would not remember these days clearly and spread your experience difficultly.
What a pity!
The valuable should have a fixed form to be recorded.
That's why we make the Weekly for DU.



[1]:	http://du.zoomquiet.io/2014-02/ac0-zq/
[2]:	https://github.com/DebugUself/du4proto/issues/445
[3]:	https://github.com/DebugUself/du4proto/issues/446
[4]:	http://weekly.pychina.org/archives.html
[5]:	https://github.com/DebugUself/du4proto/tree/DU_tools/st
[6]:	https://github.com/DebugUself/du4proto/issues/411#issuecomment-408895253
[7]:	https://github.com/DebugUself/du4proto/tree/zsy
[8]:	https://github.com/DebugUself/du4proto/blob/zsy/dataSci/pandas-seriers-division-hist-pic.ipynb
[9]:	https://liguanghe.github.io/2018/08/11/ReDu1.0/
[10]:	https://github.com/DebugUself/du4proto/issues/433
[11]:	https://github.com/DebugUself/du4proto/tree/lghFL
[12]:	https://stackoverflow.com/questions/1911109/how-to-clone-a-specific-git-branch
[13]:	https://www.slkj.org/c/38681.html
[14]:	https://www.pythonsheets.com/
[15]:	https://www.brainyquote.com/quotes/quotes/h/henryford121997.html
[16]:	https://www.brainyquote.com/quotes/quotes/h/henryford121997.html

[image-1]:	http://p3gjd3dx2.bkt.clouddn.com/2018-08-10-git-github-remote-specific-branch.png