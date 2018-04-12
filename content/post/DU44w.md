---
title: "DU44w"
date: 2018-02-12T20:20:00+08:00
---

# 怼周刊\_v44
\~ 预定 18.2.12 20:20 发布

---- 
喜迎春节辞旧岁

万家欢喜一相逢

年年岁岁奔相问

工资涨了有多少

@wuhuhu800





---- 

- 主编: [大妈][1]
- 责编:
	+ [xpgeng][2]
	+ [sunoonlee][3]
	+ [Zoe][4]

# 进度 Timelines
\~ 记录当周关键事件日期+证据链接

- [42h\[TASK]20180210 怼周会 分享及纪要 · Issue #346 · DebugUself/du4proto][5]

# 任务 Tasks
\~ 记述关键共怼任务 (如果没有, 留空)

# 进展 Progress
\~ 整体圈内活跃指标情况([st][6] 专用服务, 尚少使用手册)
<table>
<tr><th>allcic Commit</th><th> times</th><th>weekly Commit</th><th> times</th></tr>
<tr><td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>514</td>
        <td>
            <a href='http://github.com/leilayanhui'>leilayanhui</a></td><td>14</td>
            
<tr><td>
            <a href='http://github.com/liguanghe'>liguanghe</a></td><td>498</td>
        <td>
            <a href='http://github.com/OMlalala'>OMlalala</a></td><td>5</td>
            
<tr><td>
            <a href='http://github.com/zhangshiyinrunwithcc'>zhangshiyinrunwithcc</a></td><td>453</td>
        <td>
            <a href='http://github.com/wuhuhu800'>wuhuhu800</a></td><td>2</td>
            
<tr><td>
            <a href='http://github.com/leilayanhui'>leilayanhui</a></td><td>360</td>
        <td>
            <a href='http://github.com/zhangshiyinrunwithcc'>zhangshiyinrunwithcc</a></td><td>1</td>
            
<tr><th>all Commit </th><th>Comments times</th><th>weekly Commit</th><th>Comments times</th></tr>
<tr><th>all Issue </th><th>Comments times</th><th>weekly Issue</th><th>Comments times</th></tr>
<tr><td>
            <a href='http://github.com/liguanghe'>liguanghe</a></td><td>815</td>
        <td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>5</td>
            
<tr><td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>526</td>
        <td>
            <a href='http://github.com/zhangshiyinrunwithcc'>zhangshiyinrunwithcc</a></td><td>4</td>
            
<tr><td>
            <a href='http://github.com/zhangshiyinrunwithcc'>zhangshiyinrunwithcc</a></td><td>415</td>
        <td>
            <a href='http://github.com/wuhuhu800'>wuhuhu800</a></td><td>3</td>
            
<tr><td>
            <a href='http://github.com/mxclover'>mxclover</a></td><td>115</td>
        <td>
            <a href='http://github.com/leilayanhui'>leilayanhui</a></td><td>3</td>
            
<tr><td>
            <a href='http://github.com/zoejane'>zoejane</a></td><td>112</td>
        <td>
            <a href='http://github.com/liguanghe'>liguanghe</a></td><td>3</td>
            
</table>

# 成果 Achievements
\~ 各种成品/半成品 内部知识作品
- [hexo3:南辕北辙——从hexo主题丢失到手动添加submodule | 张诗颖的作品积累 - @zhangshiyinrunwithcc][7]
- [如何筹划旅游? 以新西兰游为例 - @liguanghe][8]
- [xgboost 官方文档参数的翻译 - @wuhuhu800][9] 

## @OMlalala 0204-0210 总结
- 释狮大会
	- 同步源仓库 Leo 5.7 版本
	- 成立专属 teams: [DU4leo][10]
		- 价值: 加入 teams 的怼友, 自动获得释狮大会的管理员权限
	- 大妈成立 slack 专用嗯哼频道: obp-leo
		- 寥寥数日, 发生消息 60+ (含提点/问题/建议等), 催生 [issue 4个][11], 欢迎一起嗯哼
	- 确定翻译总工作量, Leo 文档共 6.2 万字: [名留青狮][12]
- 人生第一个 PR
	- 给 Leo 官方仓库提交 [关于 License 的 PR][13], 顺利通过. 成为 25 个贡献者之一
	- 参考
		- [珍教 wiki][14]
		- [How getting into Open Source has been awesome for me][15]
- 个人博客
	- [2018年1月总结 - OMlalala.io][16]

# 故事 Stories
\~ 收集各自无法雷同的怼圈真人故事...

## 熊本-\>hexo3:南辕北辙——从hexo主题丢失到手动添加submodule

「摘要」本文记录了楼主遭遇hexo部署github后,url访问主题丢失，尝试了3个截然不同方向，最后用手动配置submodule脱离困境的故事。
「关键词」hexo;主题丢失;submodule;南辕北辙

## 0.hexo主题丢失
运用hexo和github构建博客。本地serve预览成功,配置了DNS后,安装了hexo-git-deployer,使用命令`hexo d`后,查看github 对应仓库页面,能够跳转到指定域名，但域名下的博客**主题样式丢失。**

## 1.尝试:修改config.yml的root目录
通过**bing搜索**，获得参考资源[Ubuntu下部署Hexo，本地serve预览成功，部署到网站却不能显示主题样式，如何解决？ - 知乎][17]。

文章说 **路径不对**。楼主将自己根目录下的\_config.yml`root: /Users/zsy/Documents/zsy.hexo`修改为`root: /Users/zsy/Documents/zsy.hexo/hexo`、`root: /`等。

重新部署后，主题样式在网页上依然都**没有显示**。看来并不是路径的问题。

## 2.尝试:使用submodule add返回already exists
通过**怼圈资源**，获得参考资源[重建Hexo的教训 | 浚宇的博客][18]和[Git的Hexo博客搭建和运维实例讲解-初级 | 浚宇的博客][19]

浚宇指出，如果用`git clone ...`下载主题，本地server虽然可以正常显示，但是部署到github上很可能引用出问题。应该使用`git submodule add`命令。

于是楼主在博客根目录下，添加博客主题 `git submodule add https://github.com/xing5/hexo-theme-codeland.git themes/codeland` 。结构返回的却是`'hexo/themes/codeland' already exists in the index`。主题不能添加submodule。

## 3.尝试:放弃使用`git rm ..`命令采用手动配置submodule
通过**bing搜索**，获得参考资源[基于Hexo的博客同步中的一些问题 - CSDN博客][20]、[hexo next主题保存 | Victor的博客][21]和[手动配置Git的Submodule | Strago's Corner][22]
。

这些文章提出解决submodule的**两种方案**。一种是，删除原来主题,然后再submodule新主题。另外一种是在已下载好的主题目录内，手动添加submodule。

其中第一种方案需要使用`git rm -r --cached theme/next`。好在之前先看了浚宇的博客，提醒了楼主如果使用`git rm`命令，可能导致之前配置好的主题文件全部丢失，即使新下载主题，也需要从头配置。

于是采用第二种手动配置方案。在hexo博客根目录下，新建文件名为`.gitmodules`的文件，并在该文件里配置主题信息，如下。

```
[submodule "themes/codeland"]
    path = themes/codeland
    url = git@github.com:xing5/hexo-theme-codeland.git
```

再次打开域名网页，主题样式成功显示。✧(≖ ◡ ≖✿)嘿嘿.

## 4.尝试:收集怼圈怼友博客地址
文章虽然阐述简单，但过程惊险又曲折。最让楼主不爽的是，如果不是先读怼友的博客，楼主仅仅通过bing搜索，是很难把主题样式问题从config的目录路径转向为submodule的配置上。如果不是先读怼友的博客，可能就会先尝试使用危险系数比较高的`git-rm`命令。

所以又回到zoom quiet提出的经典问题[∞h\[ASK]如何判定当前资料/图书靠谱度? ][23]

也许靠谱资料需要从收集靠谱人博客开始做起。本文最后将增添楼主曾经参考过或认为将来有参考价值的怼员博客地址。

## 5.怼员博客
- [Home | DebugUself with DAMA ;-)][24]
- [浚宇的博客][25]
- [Blah Blah Booooom - Bambooom][26]
- [sunoonlee][27]
- [Zoe Jane][28]
- [Li Guanghe's blog][29]
- [张诗颖的作品积累][30]

# 推荐 Recommedations
\~ 嗯哼各种怼路上发现的嗯哼...
- 是也乎:
	- [哪些思维方式是你刻意训练过的？][31] 
	- [不可错过的Python技术博客(网站)][32]

	- [张晓龙对微信产品的思考][33]

## 号召

- [|蠎周刊 |汇集全球蠎事儿 !-)][34]
	+ 俺私人嗯哼了5年了
	+ 邀请大家一起来, 每周嗯哼


# 后记 Postscript
\~ 怼周刊是什么以及为什么和能怎么...

大妈曰过: `参差多态 才是生机`
问题在 `参差` 的行为是无法形成团队的

	Coming together is a beginning; 
	Keeping together is progress; 
	Working together is success!

\<--- [Henry Ford][35]

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

\<--- [Henry Ford][36]

That's why Dama keeps on debugging.
However, as time goes by, maybe you would not remember these days clearly and spread your experience difficultly.
What a pity!
The valuable should have a fixed form to be recorded.
That's why we make the Weekly for DU.



[1]:	http://du.zoomquiet.io/2014-02/ac0-zq/
[2]:	http://du.zoomquiet.io/2017-04/about-xpgeng/
[3]:	http://du.zoomquiet.io/2017-04/about-sunoonlee/
[4]:	http://du.zoomquiet.io/2017-04/about-zoe/
[5]:	https://github.com/DebugUself/du4proto/issues/347
[6]:	https://github.com/DebugUself/du4proto/tree/DU_tools/st
[7]:	http://zhangshiying.in/2018/02/09/hexo3/
[8]:	https://liguanghe.github.io/2018/02/10/PlanTrip/
[9]:	https://github.com/wuhuhu800/debugself/blob/master/2018/xgboost_parameters.md
[10]:	https://github.com/orgs/DebugUself/teams/du4leo
[11]:	https://github.com/DebugUself/leo-editor-cn/issues?utf8=%E2%9C%93&q=0211
[12]:	https://github.com/DebugUself/leo-editor-cn/wiki/translate-log
[13]:	https://github.com/leo-editor/leo-editor/pull/709
[14]:	https://github.com/DebugUself/du4proto/wiki/How2PR
[15]:	https://blog.kentcdodds.com/how-getting-into-open-source-has-been-awesome-for-me-8480cd756a80
[16]:	http://omlalala.io/2018-02-04-summary-1801.html
[17]:	https://www.zhihu.com/question/29808864?sort=created
[18]:	http://blog.junyu.io/posts/0007-a-mistake-rebuilt-hexo-blog.html
[19]:	http://blog.junyu.io/posts/0012-hexo-git-apply-primary.html
[20]:	http://blog.csdn.net/u010873775/article/details/71303116
[21]:	http://www.victor123.cn/2017/11/30/error-next-submodule/
[22]:	http://strago.xin/2016/GitSubmodule/
[23]:	https://github.com/DebugUself/du4proto/issues/48
[24]:	http://du.zoomquiet.io/
[25]:	http://blog.junyu.io/
[26]:	https://bambooom.github.io/
[27]:	https://sunoonlee.github.io/
[28]:	http://blog.zoejane.net/
[29]:	https://liguanghe.github.io/
[30]:	http://zhangshiying.in/
[31]:	https://www.zhihu.com/question/23913984
[32]:	https://mp.weixin.qq.com/s/e0C_A32uWN9IQWZQX9DgHQ
[33]:	https://mp.weixin.qq.com/s/B0CrpLbVfnECatgwPES3fQ
[34]:	http://weekly.pychina.org/archives.html
[35]:	https://www.brainyquote.com/quotes/quotes/h/henryford121997.html
[36]:	https://www.brainyquote.com/quotes/quotes/h/henryford121997.html