> (优先级别标定-> XXXL|XXL|XL|L|M|S 参考: [TEE-style](https://github.com/DebugUself/du4proto/wiki/RlShortNames#%E4%BC%98%E5%85%88%E7%BA%A7))

## 背景
~ 阐述 记录/问题/事件/... 发生的背景

感谢 @Vwan 独立启动嗯哼:

- [3w[WIP] DUW 自动化发布优化 · Issue #634 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/634)
- [1m [Task] 怼周刊自动化发布流程进展 · Issue #626 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/626)
    + [DUW2Autopub · DebugUself/du4proto Wiki](https://github.com/DebugUself/du4proto/wiki/DUW2Autopub)

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

## 分析
~ 先给出自己的态度以及尝试

参考: [Publish - Debug Uself Weekly](https://du.101.camp/duw/publish/)

- 当前通过组合两个仓库(4个分支)+github-pages+aliyun VPS 
- 可以自动完成定期发布:
    + 每周6/0/1, 5~23点,每趁42分,集成发布一次

### TODO
> pubDUW 作为独立社区作品应该考虑的是

- 周刊自动化, 是否可以泛化为任意类型的自动化出版?
    + 通过约定的渠道
        * 指定仓库分支中对应文件的撰写
        * Slack 中指定频道的片段注入
        * 微信群中指定前缀的随时嗯嗯嗯
        * 公众号对话消息中输入指定前缀
        * ...
    + 输入文字, 即有后台系统自动化完成:
        * 内容收集
        * 拼合
        * 网站 输出
        * Slack/ggroup/wechat/... 通知
        * ...
- 在周刊自动化出版的基础上
    + 我们还可以/应该嗯哼什么?

## 方案
~ 给出可以追踪进展的行为追踪顺序

- [x] 合理触发周刊自动发布:
    + [x] :+1: 约定 trigger 文件提交(指定分支特殊文件创建)
        * 指定分支 -> [DUW](https://github.com/DebugUself/du4proto/tree/duw_pub)
        * 指定目录 -> [du4proto/_trigger at DUW](https://github.com/DebugUself/du4proto/tree/DUW/_trigger)
        * 指定文件 -> `deploy.txt`
        * [x] 感知 ~ 53c3974
        * [x] 复原 ~ eba5e99
        * [x] 联调 ~ e4481f4
    + [ ] ? ChatOps 远程触发
    + [ ] ? SlackBot 触发
    + [ ] ? 邮件触发(指定列表, 持续标题邮件发送)
    + [X] :o: 文件改名触发( XXX_draft.md -> XXX.md)
        * 发布后修订就难以触发了
- [x] github hooks 关联
    + [x] 评估渠道
        * [x] :+1: github-webhook
        * [x] :o: [opsdroid/opsdroid: 🤖 An open source chat-ops bot framework](https://github.com/opsdroid/opsdroid)
        * [x] :o: [errbotio/errbot: Errbot is a chatbot, a daemon that connects to your favorite chat service and bring your tools and some fun into the conversation.](https://github.com/errbotio/errbot)
    + [x] 实验触发
        * [x] ngrok...4527a8f
        * [x] 配置为临时 hook ~ 1ca418d
    + [x] hooks 开发
        * [x] 识别 `_tragger/delpoy.md` ~ d93e61d
        * [x] 生成 `_trigger4deploy.log` 作为 crontab 本地感知触发器 ~ 3112743
        * [x] 本地触发器 -> crontab ~ 4ac2aaf
    + [x] hooksrv 部署
        * [x] pipenv 环境准备
        * [x] bottle + gunicorn ~ 861abfb
            - `gunicorn -c gunicorn_cfg.py --capture-output hooksrv:app`
            - [有没有办法在gunicorn中记录python打印语句？ \| landcareweb\.com](http://landcareweb.com/questions/36553/you-mei-you-ban-fa-zai-gunicornzhong-ji-lu-pythonda-yin-yu-ju)
        * [x] +supervisor ~ 5c8aed8
        * [x] nginx 代理
        * [x] 部署域名 -> hook.duw.101.camp
    + [x] hooks 测试
        * [x] 测试 域名
        * [x] 测试 /alive
        * [x] 测试触发 ~ ff4f80c
            - ztop:/opt/www/debuguself/_trigger4deploy.log
            - 通过 hooksrv 生成
    + [x] hooks 关联具体行为
        * [x] 测试 cron4trig2duw.sh ~ 28b7198
        * [x] 替换 crontab
        * [x] 提高 定期频率
            - `*/5 8-23 * * * /opt/www/debuguself/br_duw_pub/cron4trig2duw.sh >> /opt/log/cron/duw_hook.log 2>&1`
        * [x] 检验 触发全程 ~ c29b293,7b142c7
        * [x] 追加间隔信息给定时事务记要 ~ 6b9d50a
- [x] hooksrv 生产运行
    + [x] gunicorn 运行/检验 ~ ccd746f
    + [x] supervisor 监察 gunicorn ~ 71924b5
        * [x] cba57ee ~ 文件不存在解决
        * [x] `child process was not spawned` -> 使用系统级**监察器**
            - `$ sudo apt install supervisor`
            - `$ supervisord -c supervisor.conf`
            - `$ $ supervisorctl -c supervisor.conf status`
                + `hooksrv   RUNNING   pid 15866, uptime 0:00:01`
    + [x] gunicorn 不能以 deamon 形式运行 ~ eafdb17

> $ pr supervisord -c supervisor.conf

    Error: The directory named as part of the path '/opt/log/httpd/supervisord.log' does not exist in section 'program:hooksrv' (file: 'supervisor.conf')
    For help, use /home/du19/.local/share/virtualenvs/br_duw_pub-XOQ-Lz1N/bin/supervisord -h

>> 用 pipenv 中的 supervisord, 环境太限制;
>> 使用系统级别

/opt/www/debuguself/br_duw_pub

        通过配置文件启动supervisor
    supervisord -c supervisor.conf
        察看supervisor的状态
    supervisorctl -c supervisor.conf status
        重新载入 配置文件
    supervisorctl -c supervisor.conf reload
        启动指定/所有 supervisor管理的程序进程
    supervisorctl -c supervisor.conf start [all]|[appname]
        关闭指定/所有 supervisor管理的程序进程
    supervisorctl -c supervisor.conf stop [all]|[appname]

![ScreenShot 2019-05-17 16 37 40](https://user-images.githubusercontent.com/22494/57914911-37ffa480-78c2-11e9-9664-827d50553e17.jpg)

>> 101.camp 不可能备案...

- 快速配置 DNSpod 使用 zoomquiet.top 备案域名
- 追加配置 nginx 代理新域名接口
- 配置 github-webhook 使用新服务

> ༄  http http://hook.duw.zoomquiet.top/alive

    HTTP/1.1 200 OK
    Connection: keep-alive
    Content-Length: 186
    Content-Type: application/json
    Date: Fri, 17 May 2019 08:46:59 GMT
    Server: nginx/1.10.3 (Ubuntu)

    {
        "error": 0,
        "link": {
            "href": "/alive",
            "title": "GET+POST echo",
            "type": "application/json"
        },
        "message": "i am livin",
        "method": "GET",
        "state": 200,
        "version": "hooksrv v.190517.1542"
    }


>>> 当前关系图谱: [怼周刊_v108 ~ pubDUW 阶段故事](https://du.101.camp/duw/108w/#achievements)

对应日志:

- Nginx -> ztop:/var/log/nginx/
    + access.log
    + error.log
- Crontab -> /opt/log/cron/
    + duw_hook.log
- Hooksrv -> /opt/log/httpd
    + Supervisord:
        * supervisord.log
        * error 合并
    + gunicorn:
        * gunicorn_access.log
        * gunicorn_error.log




- [x] st 社区活性统计~> [3w[MVP] st 社区活性统计器 · Issue #651](https://github.com/DebugUself/du4proto/issues/651)
- [ ] MVP 多渠道采写: ~> ...

### VPS
> aliyun 上 Ubuntu 环境自动化过程

- [ ] 持续集成/部署:
    + [ ] CI/D 工具评估 [Topic: ci-cd](https://github.com/topics/ci-cd)
        * [ ] Circle CI
        * [ ] Travis CI
    + [x] MVP 持续过程
        * [x] 指定仓库指定分支指定变化
        * [x] 可感知 ~ `_trigger/deploy.md`
        * [x] 可触发 ~ `/opt/www/debuguself/br_duw_pub/_trigger4deploy.log`
        * [x] 可记录 
            - [x] 可 指定仓库 [DebugUself/duw at logging](https://github.com/DebugUself/duw/tree/logging)
        * [ ] 可 slack 回响
- [ ] 使用文档
    + [x] SCMlog
    + [x] 配置过程
    + [x] 管理手册
    + [ ] 开发指南


## refer:

- [Deploy flask app with nginx using gunicorn and supervisor](https://medium.com/ymedialabs-innovation/deploy-flask-app-with-nginx-using-gunicorn-and-supervisor-d7a93aa07c18)


```
 o
  o
ooo
```
参考: [禁止事项清单](https://github.com/DebugUself/du4proto/wiki/HbNotDoIt)

