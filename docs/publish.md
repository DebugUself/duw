# 发布怼周刊
> 一个长长的小故事

## 背景
> 170401 自怼圈启动

作为 `自学习型社区` 以作品为驱动,
那么, 作为社区整体应该有什么通用作品以便所有成员可以参与?

## 开始
> 自然, 是内部刊物了

- 目的: 节奏小结社区的嗯哼
- 作用: 作为仪式所有成员可参与
- 内容: [DebugUself/du4proto at DUW](https://github.com/DebugUself/du4proto/tree/DUW)
    + 专用分支中
    + 以周数为名 .md 文档
    + 编辑期间 `XXX_draft.md`
    + 发布后 -> `XXX.md`
- 操作: 完全人工进行
    + 值班主编整合好内容:
        * 定场诗
        * 一周进展
        * 怼故事
        * ...
    + 本地打印为 .pdf
        * 一般使用 chrome 打开
        * 利用插件完成 GFM 渲染
        * 再用内置 PDF 打印机输出
    + 利用 github 仓库的 release 功能
        * 给分支作一个 weekly 标签
        * 包含周刊期数, 比如: [Release DU101w · DebugUself/du4proto](https://github.com/DebugUself/du4proto/releases/tag/v19.03.25)
        * 并附件上 .pdf
    + 同时将此消息通过 ggoups 通告全体

## 然后
> 内容得和社区现状更加紧密的结合

- 毕竟, 社区是以 github 协作为核心来嗯哼的
- 那么, github 中各种协作行为本身的数据就应该是周刊的客观内容
- 虽然, 官方给了越来越多的可视化统计
- 但是, 和社区关注的并不吻合:
    + 当周 top5 commit 提交是谁?
    + 当周 top5 commit-comments 点评是谁?
    + 当周 top5 issue 创建是谁?
    + 当周 top5 issue-comments 回复是谁?
    + 全历史累计 top5 ...
- 所以, 根据 github API 开发了 [st](https://github.com/DebugUself/du4proto/tree/DU_tools/st) ~ 活性统计工具
    + 其中 [heroku](https://github.com/DebugUself/du4proto/tree/ZQ4mDjango/heroku) 版本, 部署在 PaaS 中
    + 通过 github 事件激发 web hook, 来持续记录各种事件到 Redis 中
    + 这样就能通过 RESTful 接口随时返回当前的统计数据
    + 并格式化到 周刊中
    + 而怼员们甚至于随手写了 chrome 插件:
        * [bambooom/crx-intro-demo: a little tutorial about the first chrome extension](https://github.com/bambooom/crx-intro-demo)
        * 可以通过点击就自动获得报表

>> 然而, 其它主要周刊发布行为, 还是要人工来...

## 后来
> 180412 @zoejane [init(hugo site) with theme jane · DebugUself/duw@23be3a1](https://github.com/DebugUself/duw/commit/23be3a1b8fc76fe59946d9b1972e5d55b29334c2)


著名的 Zoe 教练, 为了学习 SSG(静态网站生成器),

- 想将内部 怼周刊, 变成外部可访问的网站
- 自主创建仓库:
    + github.com/DebugUself/duw/
- 使用: [gohugoio/hugo: The world's fastest framework for building websites.](https://github.com/gohugoio/hugo) 完成自动构建
- 发布: du.zoomquiet.io/duw
- 问题:
    + [DUW](https://github.com/DebugUself/du4proto/tree/DUW) 分支中的文稿都是纯净版 .md
    + 没有任何头部 meta 信息
    + 而类似 hugo 的 [Static-Site-Generators: A definitive list of tools for generating static websites.](https://github.com/pinceladasdaweb/Static-Site-Generators) 多数是面向 blog 的
    + 都要求有一定 meta 信息列在头部
    + 以便引擎提取并自动化处理
    + 所以, Zoe 自行完成了基本的头信息追加
    + 但是, 整个过程, 暂时只能人工在本地构建好环境来进行转换
    + 进一步的, hugo 本身是 golang 构建的:
        * 而 golang 运行环境在本地的构建
        * 或是利用 CI/CD 服务来远程构建
        * 都不是件容易的事儿
    + 而且, 和自怼圈默认的 Python 技术桟也不吻合

>>> 所以,就停止了...


## 现在
> 是也乎,(￣▽￣) 方法有三...

怼圈第三年, 大家都感觉怼周刊已经连载超过 100 期, 值得真正变成社区作品:

- 完全自动化发布
- 自动化统计数据
- 自动收集各种来源内容
- 自动合成 .md
- 自动发布为 .pdf 以及 release + ggroups
- ...

### @Vwan
<~ [1m [Task] 怼周刊自动化发布流程进展 · Issue #626 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/626)

叕一位伟大的怼员, 直接撸袖子开始:

- 分支: [duw_pub](https://github.com/DebugUself/du4proto/tree/duw_pub)
- 尝试:
    + md -> pdf 
    + release 自动提交
    + email 自动发布
    + ...
- 但是:
    + 核心自动化 => 将 [DUW](https://github.com/DebugUself/du4proto/tree/duw_pub) 分支内容
        * 合理发布为友好访问的网站
        * 一直没进展


### DAMA
> 那么作为可展开的基础, 得提供一个完整的思路和过程哈?... 

#### MVP
> 从简化目标开始

- 既然决定自动化发布了
- 那么, 所有对内的人工发布行为, 能忽略就忽略:
    + pdf 打印
    + release 标签附件
    + ggroups 邮件
    + ... 都先搁置
- 单单完成:
    + 将文稿从
        * 分支:[DUW](https://github.com/DebugUself/du4proto/tree/duw_pub)
    + 发布到
        * 仓库:[duw](github.com/DebugUself/duw/)
    + 访问为: du.101.camp
    + 自动化过程工具在:
        * 分支:[duw_pub](https://github.com/DebugUself/du4proto/tree/duw_pub)

#### [Markdoc](https://pypi.org/project/Markdoc/#history)
> 11年停止开发的优秀类 wiki SSG

- 非常小
- 功能也非常单一
    + 就是将约定目录中所有 .md 以原样目录结构发布为 wiki 
- 一直有在用:
    + [华蠎 维基 | PyChina.org Static Wiki](http://wiki.pychina.org/)
    + [珠海GDG 维基 | ZHGDG Static Wiki](http://wiki.zhgdg.org/)
    + [Index | Zoom.Quiet Personal Static Wiki](http://wiki.zoomquiet.io/)
    + [Index _ 101Camp Static Wiki](http://wiki.101.camp/)
    + ...
- 所以, 快速重构:
    + 仓库:[duw](github.com/DebugUself/duw/) 切换为 Markdoc 发布
    + 配置 ghihub-pages 用指定域名发布

>> 但是, 开始自动化时遇到历史问题

[2d[Help] pip install Markdoc 出错 · Issue #635 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/635)

由于年代久远, Python 也早已进入 3.0 时代, 

Markdoc 依赖的几个模块也都放弃了 py2 环境升级到 py3 了,

导致即便使用 Pyenv 等手段, 将所有环境降级到当前,

也难以安装...


#### [Mkdocs](https://pypi.org/project/mkdocs/#history)
> 唯二的不需要 meta 额外信息支持的 SSG 

好在很早也用过另外一种静态网站生成引擎: [Mkdocs](https://pypi.org/project/mkdocs/#history)

- 不象 Markdoc 是类似 wiki 样, 自动根据原有目标结构输出
- 而是一种标准文档网站思路, 由 `mkdocs.yml` 逐一声明发布结构来构建
- 而且, 一直勤劳的维护并良好兼容 py3
- 进一步的, 有丰富的样式可以选择
- 唯一要解决的就是自动生成吻合自然目录结构的 `mkdocs.yml`

>> 操作文本, 这可是 Python 的强项哪...


def gen4idx(c):

    ...

    for root, dirs, files in os.walk(DOC):
        _exp = ''
        _idx = ''
        if not dirs:
            _sub = root.split('/')[1]
            _idx = _sub#[:-5]
            _exp += '# {} \n'.format(_sub)
            _exp += '> {} weekly report\n\n'.format(_sub[2:6])
            for md in files:
                if '_draft' in md: pass
                elif 'md' == md.split('.')[-1]:
                    _exp += '- [{}]({})\n'.format(md[:-3],md[:-3])
        print(_exp)

果然, 10多行就完成了自动索引构建.


#### CI/CD
> 在本地可以一键完成所有自动化发布操作后, 如何真正无人值守完成发布?

这在业界当然是标准 -> 持续集成/部署 而已,

但是, 先 MVP 定义一下:

- 用 [invoke](https://pypi.org/project/invoke/) 构建自动指令
- 用 shell 脚本包装
- 用 crontab 自动定期执行
- 将以上部署到一台主机中即完成最间 CI/CD
    + 当然, 这台主机最好是外网可访问
    + 7x24 小时稳定运行
    + 空间/计算能力足够
    + ...

[invoke](https://pypi.org/project/invoke/) 是 fabric 1.0 的升级版,

- 拆分为专注本地指令执行管理的模块, 
- 写自然的 Python 代码, 但是, 可以自由调用系统各种指令,
- 所以, 很快完成关键行为的定义和构建
- 因为, 都可以在本地快速调试而已

> ༄  inv -l

    Available tasks:

      bu    build all local doc -> site
      gh    jump into ln -s -> site push all bulited static pages
      pl    pull all necessary change AT FIRST...
      pu    push all local fix into content rep.
      pub   MAIN COMMAND -> SEQUENCE RUN ALL NEED ACTS PUBLISH SITE

发布行为:

    crontab -e 声明定期事务:

        */20 5-23 * * * /PATH/2/cron4duw.sh >> /dev/null 2>&1

    cron4duw.sh ~> 定期事务脚本
        +- 初始化日志目录 => ghbr_logging_duw
        +- 合理执行 inv pub
        +- 将最新处理日志 push 到 github

    inv pub 
        === +- pl -> 先同步所有仓库/分支
            |       +- br_DUW
            |       +- br_duw_pub
            |       +- ghp_duw
            +- bu -> 用 Mkdocs 构建网站
            |       +- br_duw_pub/site 链接到 ghp_duw
            |       +- mkdocs build 时自动输出所有网页到 site 中
            +- pu -> 将 br_duw_pub 变化检入仓库
            +- gh -> 将 最终成果 push 给 github-pages 发布


其中平行部署的几个目录:

- br_DUW ~> orphan 分支:[DUW](https://github.com/DebugUself/du4proto/tree/duw_pub)
    + 周刊底稿
    + 成员通过 git 自由编程
- br_duw_pub ~> orphan 分支:[duw_pub](https://github.com/DebugUself/du4proto/tree/duw_pub)
    + 周刊发布工程
    + 理论上只应该由机器人/管理员嗯哼
- ghp_duw ~> 独立 仓库:[duw](github.com/DebugUself/duw/)
    + 周刊 github-pages 发布仓库
    + 使用 master 发布策略, 利用 github 的空间/流量完成免费发布
- ghbr_logging_duw ~> orphan 分支:[logging](https://github.com/DebugUself/duw/tree/logging)
    + 收集自动化过程中关键处置信息
    + 由自动化脚本完成 git 操作, 追加新日志到仓库中
    + 这样所有成员, 就可以不用登录主机也知道周刊发布进行了什么过程/操作

### pipenv+conda
> python 运行时环境的科学管理

- Miniconda3 完成基本隔离运行时
- 然后, 在其中安装 pipenv
- 并通过 pipenv install 来自动化构建项目专用虚拟环境

### crontab
> 特殊的无一切环境变量加持的 shell 运行时

最终, 部署环境是 aliyun 最小 VPS

- Ubuntu 16.04.3 LTS
    + 4.4.0-105-generic #128-Ubuntu SMP 
    + Thu Dec 14 12:42:11 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
- 单核
- 256M 内存
- 50G 空间


> 开始调试

[duw/190418_215045.log at logging · DebugUself/duw](https://github.com/DebugUself/duw/blob/logging/2019/04/190418_215045.log)

各种找不到


> git 失常

[duw/190419_122501.log at logging · DebugUself/duw](https://github.com/DebugUself/duw/blob/logging/2019/04/190419_122501.log)

因为相对路径在 crontab 中是被嫌弃的...


> 路径出问题

[duw/190419_162001.log at logging · DebugUself/duw](https://github.com/DebugUself/duw/blob/logging/2019/04/190419_162001.log)

最终想来想去, 还是通过 env 临时声明个全局变量完成路径的统一.

> 就是不发布

[duw/190419_210001.log at logging · DebugUself/duw](https://github.com/DebugUself/duw/blob/logging/2019/04/190419_210001.log)


关键失常:

    ...

    /opt/www/debuguself/br_duw_pub
        ERROR   -  Config value: 'theme'. Error: Unrecognised theme name: 'simplex'. The available installed themes are: mkdocs, readthedocs 

        Aborted with 1 Configuration Errors!

才想起来, 即使有定制 theme, 在具体编译时, 也一定要事先安装好对应 theme:


    $ pr pip install mkdocs-bootswatch


再检验一下:

> $ pr pip show mkdocs-bootswatch

    Name: mkdocs-bootswatch
    Version: 1.0
    Summary: Bootswatch themes for MkDocs
    Home-page: http://www.mkdocs.org
    Author: Dougal Matthews
    Author-email: dougal@dougalmatthews.com
    License: BSD
    Location: /home/du19/.local/share/virtualenvs/br_duw_pub-XOQ-Lz1N/lib/python3.7/site-packages
    Requires: mkdocs

>> 这下应该都好了...


### 可用
> 经过大约 10几轮调试, 终于开始定期嗯哼了

[duw/190419_170001.log at logging · DebugUself/duw](https://github.com/DebugUself/duw/blob/logging/2019/04/190419_170001.log)

每天 5点~23点, 每隔 20 分钟, 自动构建一次.



### TODO

- 将定期变成指定仓库事务响应
    + 190420 快速通过仓库约定文件来触发
- 使用 ChatOps 将运维对话化
- 追加内容撰写渠道:
    + 通过 Issue 指定标题/首行 来完成提交?
    + 通过 Slack 指定频道指定 /commands ?
    + 通过微信动作号指定前缀对话?
    + 通过 ggoups 指定标题前缀来嗯哼?
    + 通过...
- 是的, 可以也应该通过各种不受限定的场景高速为周刊贡献嗯哼


## 嗯哼

- 190419 DUr init.
    + 1300 debug full auto public
    + 1642 fix path chaos
    + 1842 main story publish 



