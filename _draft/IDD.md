# IDD
> Issue Drived Developping 

Issue 驱动的开发, 有可能高速增补正文时丢失关键变更,
所以, 用 repo. 来自然记录可追踪变化...

------------

> (优先级别标定-> XXXL|XXL|XL|L|M|S 参考: [TEE-style](https://github.com/DebugUself/du4proto/wiki/RlShortNames#%E4%BC%98%E5%85%88%E7%BA%A7))

## 背景
~ 阐述 记录/问题/事件/... 发生的背景

感谢 @Vwan 独立推进到现在基本可用:


- [1m [Task] 怼周刊自动化发布流程进展 · Issue #626 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/626)
- [DUW2Autopub · DebugUself/du4proto Wiki](https://github.com/DebugUself/du4proto/wiki/DUW2Autopub)

## 分析
~ 先给出自己的态度以及尝试

### 初衷

减少值班编辑的工作量, 以便保障周刊按时发布

### 追加

扩展周刊内容提供渠道, 以便丰富/日常化周刊内容聚合

### 所以

- 自动化, 是真正自动化, 任何编辑都不用本地安装专用组件以及进行程序性操作
    + 最好只通过约定的渠道
    + 输入文字, 即有后台系统自动化完成:
        * 内容采集
        * 拼合
        * PDF 输出
        * 网站 输出
        * tag 形成
        * ...
- 而全体怼员, 可以在各种熟悉的场景中进行周刊的撰写:
    + 指定仓库分支中对应文件的撰写
    + Slack 中指定频道的片段注入
    + 微信群中指定前缀的随时嗯嗯嗯
    + 公众号对话消息中输入指定前缀
    + ...
- 一切我们感觉可以复用的渠道都可以利用上
    + 即, 这都是 DUW 的自动化插件项目了... 


而以上都集成起来, 就一定需要一个可以在公网上响应所有需求的主机:

- 可以用自己家的 linux 服务暴露出来
- 也可以采购合理的 VPS 
- 也可以利害 heroku 之类免费 PaaS 空间
- ...


## 方案
~ 给出可以追踪进展的行为追踪顺序
为可视化进展状态使用如下形式:



- [x] XL 规划整体
- [x] 系统运行时评估
    + [x] :o: home server ~ 慢, 不安全
    + [x] :o: Heroku ~ 境外有关势力
    + [x] :question: Microsoft Azure ~ 可考虑备份
    + [x] :+1: aliyun ~ 勉强可用, 关键 抢域名时, 买了3年的可一直用
    + [x] :o: huaweicloud ~ 不专业
    + [x] :o: 腾讯云 ~ 不安全
- [x] MVP 撰写发布过程:
    + [x] 指定仓库 -> https://github.com/DebugUself/duw
    + [x] 指定目录 -> 
        * [x] 发布 https://github.com/DebugUself/duw/tree/master/docs
        * [ ] 稿件 https://github.com/DebugUself/duw/tree/master/wiki
    + [x] :o: push 即发布
        * [x] 权限限定
        * [x] 编译/发布 -> https://github.com/DebugUself/duw/blob/master/fabfile.py
        * [x] :o: 环境准备 .. markdoc 编译失败...#635
        * [x] 评估 SSG 方案
            - [x] :o: 调通 markdoc 核心功能 -> py3
            - [x] :+1: 基于 MkDocs 配置自动索引脚本
                + [x] 同 py.101.camp theme
                + [x] 恢复 uttrances 插件 ~ 406b7aa
                + [x] 自动指令脚本 ~ 1915ba3
            - [x] :o: 尝试其它 SSG 引擎: 没有可用的...
                + 支持 md
                    * [myles/awesome-static-generators: A curated list of static web site generators.](https://github.com/myles/awesome-static-generators)
                    * [Top Ten Static Website Generators | Netlify](https://www.netlify.com/blog/2016/05/02/top-ten-static-website-generators/)
                    * [StaticGen | Top Open Source Static Site Generators](https://www.staticgen.com/)
                    * [Static Site Generators](https://staticsitegenerators.net/)
                    * ...
                    * [tajmone/gh-themes-magick: GitHub Pages Themes Magick: https://tajmone.github.io/gh-themes-magick/](https://github.com/tajmone/gh-themes-magick)
                + 不用追加头部 meta 信息
                + 根据自然目录生成
                + 目录自动生成索引
                + :+1: theme 可定制, 追加 uttrances 插件
        * [x] TODO: Mkdoc 索引无法滚动,导致过长无法点选更多
            - [x] :o: 改造 HTML5 菜单?
            - [x] :+1:  自动生成索引页面 <- 菜单 [du4proto/tasks.py at duw_pub · DebugUself/du4proto](https://github.com/DebugUself/du4proto/blob/duw_pub/tasks.py)
            - [x] [DU2017Weekly](https://du.101.camp/duw/DU2017Weekly/) 不是自然排序...
                + [x] :o: 修改代码完成匹配
                + [x] :+1: 修改文件,变成 XXX 序号?
            - [x] 中山林峰📮: 应该可以直接访问:
                + [x] :+1: https://du.101.camp/duw/DU096w/
                + [x] :+1: https://du.101.camp/duw/2019/DU096w/
                + [x] 冗余发布, 问题是自动化? ~> [du4proto/tasks.py at duw_pub](https://github.com/DebugUself/du4proto/blob/duw_pub/tasks.py)
                    * [x] 自动同步多目录变化 ~ 3b32b22
                    * [x] 合理删除多余文件 ~ f4ed524
                    * [x] 自动下拉分支内容 ~ ca599df
- [ ] MVP 多渠道撰写:
    + [ ] 指定 Issue 回复聚合
    + [ ] 指定 Slack 频道聚合
    + [ ] 指定 公众号 回复聚合
    + [ ] 指定 邮箱 回复聚合
    + [ ] ...
- [ ] 持续集成/部署:
    + [ ] CI/D 工具评估 [Topic: ci-cd](https://github.com/topics/ci-cd)
        * [ ] Hudson
        * [ ] Circle CI
        * [ ] Travis CI
        * [ ] ...
    + [ ] ChatOps 工具评估
        * [ ] hubot
        * [ ] err
        * [ ] ...
    + [ ] MVP 持续过程
        * [ ] 指定仓库指定分支指定变化
        * [ ] 可感知
        * [ ] 可触发
        * [ ] 可追踪
        * [ ] 可记录
        * [ ] 可 slack 回报
        * [ ] 可 指定仓库 logging
        * [ ] ...


## 记录
~ 原始数据/过程/现象/...收集

- [x] 评估完成次序
- [x] 评估协同原则
- [ ] 明确团队成员
- [ ] 约定发布节奏
- [ ] ...

### VPS
> aliyun 上 Ubuntu 环境自动化过程

- [x] 初始化 ~ [LogAliyun](https://github.com/DebugUself/du4proto/wiki/LogAliyun)
    + [x] 专用用户 -> du19
    + [x] SSH 密匙 
        * -> /home/du19/.ssh/id_rsa.
        * -> /home/du19/.ssh/id_rsa.pub.
    + [x] 部署 github
    + [x] 检验可 push ~ 9765746
    + [x] 构建合理目录结构 -> opt
        * git@github.com:DebugUself/duw.git -> ghp_duw
        * DebugUself/du4proto/tree/DUW -> br_DUW
        * DebugUself/du4proto/tree/duw_pub -> br_duw_pub
            - br_duw_pub/site -> ln -s -> ghp_duw
    + [x] hg 统筹必要配置文件
    + [x] hg hooks 自动更新配置
    + [x] Miniconda3
        * [x] miniconda 虚拟环境 ~> Miniconda3-latest-Linux-x86_64.sh
        * [x] py 2.7 部署 ~> clone => py371
- [x] :+1: 定期 -> 20分钟 => [Publish - Debug Uself Weekly](https://du.101.camp/duw/publish/)
    + [x] 依赖模块部署
        * [x] pipenv
        * [x] Mkdocs
        * [x] invoke
    + [x] 定期事务 sh ~> 2789924 <~ [du4proto/cron4duw.sh at duw_pub](https://github.com/DebugUself/du4proto/blob/duw_pub/cron4duw.sh)
    + [x] crontab 部署
    + [x] 专用 logging 分支 ~> 
        * `git co --orphan logging`
        * `git remote add -t logging -f origin git@github.com:DebugUself/duw.git`
        * ==> [DebugUself/duw at logging](https://github.com/DebugUself/duw/tree/logging)
    + [x] 测试
- [ ] github hooks 关联
    + [ ] 评估渠道
        * [ ] github-webhook
            - [felixonmars/bottle-github-webhook: A very simple github post-receive web hook handler](https://github.com/felixonmars/bottle-github-webhook)
            - [carlos-jenkins/python-github-webhooks: Simple Python WSGI application to handle Github webhooks](https://github.com/carlos-jenkins/python-github-webhooks)
            - [datafolklabs/github-webhook-wrapper: Launch Custom Scripts For Any Repo/Branch From a Single Webhook Endpoint](https://github.com/datafolklabs/github-webhook-wrapper)
            - [post \- How do I receive Github Webhooks in Python \- Stack Overflow](https://stackoverflow.com/questions/14536992/how-do-i-receive-github-webhooks-in-python)
            - [How to Handle GitHub Webhooks Using Django](https://simpleisbetterthancomplex.com/tutorial/2016/10/31/how-to-handle-github-webhooks-using-django.html)
                + [django\-github\-webhook · PyPI](https://pypi.org/project/django-github-webhook/)
                + [用 Django 来响应 Github Webhook \| 博客 \| 安好](http://answ.me/post/github-webhook-with-django/)
                + [Django Packages : Webhooks](https://djangopackages.org/grids/g/webhooks/)
                    * [zapier/django\-rest\-hooks: Add webhook subscriptions to your Django app\.](https://github.com/zapier/django-rest-hooks)
            - ...
        * [ ] [opsdroid/opsdroid: 🤖 An open source chat-ops bot framework](https://github.com/opsdroid/opsdroid)
        * [ ] [errbotio/errbot: Errbot is a chatbot, a daemon that connects to your favorite chat service and bring your tools and some fun into the conversation.](https://github.com/errbotio/errbot)
    + [ ] 实验触发
    + [ ] hooks 开发
    + [ ] hooks 部署
    + [ ] hooks 测试
    + [ ] hooks 关联具体行为
- [ ] 使用文档
    + [ ] SCMlog
    + [ ] 配置过程
    + [ ] 管理手册
    + [ ] 开发指南


## 变更
~ 记录合并大家 建议/增补/.. 来的主要变动信息

- 190417 ZQ IDD 化 -> [du4proto/IDD.md at duw_pub](https://github.com/DebugUself/du4proto/blob/duw_pub/IDD.md)
- 190416 ZQ 完成 大索引自动生成
    + 2206 修改所有文件序列号, 完成顺序自动排序
- 190411 ZQ 完成 Markdoc -> Mkdocs 迁移和自动化
- 190402 ZQ init.
- ... 使用日期 作者 记要 <-- 这种行格式来嗯哼


```
 o
  o
ooo
```
参考: [禁止事项清单](https://github.com/DebugUself/du4proto/wiki/HbNotDoIt)

