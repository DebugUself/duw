---
title: "About"
date: 2017-08-20T21:38:52+08:00
lastmod: 2017-08-28T21:41:52+08:00
menu: "main"
weight: 50

# you can close something for this content if you open it in config.toml.
comment: false
mathjax: false
---
# 怼周刊

> 莫私怨

	莫怨莫愁 暗自神伤
	当真动手 越怼越快
    嗯哼不乱 是谓逍遥

## 缘起
进入 `玻璃花园` 大家相互观察, 才能感受到自学的参差多态, 是多么欢乐.

- 如此欢乐的事, 当然应该记录下来, 内部发行, 以励前行,
- 54 周后, 结集成册即成佳话 ;-)


## 协议
![CC BY-NC-SA 3.0](https://licensebuttons.net/l/by-nc-sa/3.0/80x15.png)

[Creative Commons — 署名-非商业性使用-相同方式共享 3.0 中国大陆 — CC BY-NC-SA 3.0 CN](https://creativecommons.org/licenses/by-nc-sa/3.0/cn/)

## 编辑
~ 既然故事都是大家自己嗯哼出来的, 当然的, 周刊也应该是大家的

只是为了协同,得有所约定, 以免乱了章法 -> 暂定:

- 发行: 每周一期
    
    一般 周一 20:20 发布,分三个渠道发布:

    + [release](https://github.com/DebugUself/du4proto/releases)
    + [Debug Uself 自怼圈](https://groups.google.com/forum/#!forum/debuguself)
    + 再分享 pdf 到 小密圈

- 节奏: 
    + 筹稿两周, 和合一周
    + <-- [DebugUself/du4proto at DUW](https://github.com/DebugUself/du4proto/tree/DUW) 分支进行
    + 如遇不可抗力, 将跳过当周,继续下一期的编辑发行

- 容器:
    + 分支中 `.md` 文本
    + `*_draft.md` 为筹稿状态文稿(自由分栏追加内容)
    + `*_TUV.md` 为和合编辑状态文稿(禁止追加新内容)
    + `*w.md` 为正式发布文稿(原则上不应该再修订)
    + `*_tpl.md` 为周刊版式, 作为模板, 指导新周刊的组织

详细文件名规约:

    DU(No.)w[_state].md
     |  |  | |  |    +- 统一为 Markdown 格式纯文本文件 
     |  |  | |  +- 文稿状态 tpl->draft->TUV->正稿
     |  |  | +- 连接符 [] <- 为可选区域内容
     |  |  +- week 周
     |  +- 从0开始的 怼周数一年,如果不中断的话,将出到 53w
     +- DebugUself 缩写


PS:

- 参考:
    + [Chinese Union Version - Wikipedia](https://en.wikipedia.org/wiki/Chinese_Union_Version)
    + [好中文的样子第四讲:聆听"和合本""圣经" - 简书](http://www.jianshu.com/p/0172f0ca359b)
    + [好中文的样子第七讲: "圣经"和合本与白话文 - 简书](http://www.jianshu.com/p/a1fae605b006)
- 所以, **TUV** --> `The Union Version` 和合版本
    + 通过和合技, 快速多人联合完成文稿迭代的过程
    + 以上.

## 投稿
~ 试刊号由大妈和3位义务教练联合出品

接下来自己动手才更加快乐 -> 投稿渠道:

+ 仓库 [_draft](https://github.com/DebugUself/du4proto/tree/master/_draft) 目录,发布文稿:
    * 文件名格式 `DU[总周数]_[github id]_[内容简述 英文,小写单词,用-连接].md`
        - 比如: `DU3w_zoomquiet_how-2-make-me-coding.md`
    * 然后在 [Issues · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues) 
    * 创建`[Weekly] ` 前缀的 Issue 来通告
    * 一定要包含文稿的 仓库链接
    * 并 `@DebugUself/du0mana`
+ 列表发送 `[Weekly] ` 前缀的邮件, 并附 .md 格式的文稿
+ 没了.

### 收录标准
~ 同 自怼圈 所有行为指标

- 有用 ~ 解决真实问题的, 非常虚构内容, 体裁不限制, 尽量提供客观证据/数据/代码...
- 有趣 ~ 形式上流畅, 大家看的下去, 也学的上手
- 有种 ~ 一定的挑战性, 如果是大家都知道的事儿, 再怎么嗯哼, 也算不上带种,一定要尽力作自己20年后说起来也非常赞的事儿...



## 记录

- 17.4.10 规范编辑流程, 发布:
    + DU_w_tpl.md
    + DU1w_draft.md
    + DU2w_draft.md
    + DU3w_draft.md
- 17.4.8 DU0w.md
- 17.5.5 re-orphan br clone

:

    ༄  mkdir DUWeekly
    ༄  cd DUWeekly
    ༄  git init
    Initialized empty Git repository in /opt/data/Sites/DU.xmq/br/.git/
    ༄  git remote add -t DUW -f origin git@github.com:DebugUself/du4proto.git
    Updating origin
    remote: Counting objects: 183, done.
    remote: Compressing objects: 100% (5/5), done.
    remote: Total 183 (delta 3), reused 3 (delta 3), pack-reused 175
    Receiving objects: 100% (183/183), 73.27 KiB | 11.00 KiB/s, done.
    Resolving deltas: 100% (106/106), done.
    From github.com:DebugUself/du4proto
     * [new branch]      DUW        -> origin/DUW
     * [new tag]         17.4.15    -> 17.4.15
     * [new tag]         17.4.8     -> 17.4.8
    ༄  git checkout DUW
    Branch DUW set up to track remote branch DUW from origin.
    Switched to a new branch 'DUW'

