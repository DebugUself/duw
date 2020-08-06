> (优先级别标定-> XXXL|XXL|XL|L|M|S 参考: [TEE-style](https://github.com/DebugUself/du4proto/wiki/RlShortNames#%E4%BC%98%E5%85%88%E7%BA%A7))

## 背景
~ 阐述 记录/问题/事件/... 发生的背景

- 工程: [DU.support](https://github.com/DebugUself/du4proto/projects/8?add_cards_query=is%3Aopen)
- 分支: [DebugUself/du4proto at duw_pub](https://github.com/DebugUself/du4proto/tree/duw_pub)
- IDD: [du4proto/IDD3.md at duw_pub · DebugUself/du4proto](https://github.com/DebugUself/du4proto/blob/duw_pub/IDD3.md)
- HOOK: 
    + 触发器: http://hook.duw.zoomquiet.top/ 
    + st 感应:
        * golang : https://playload.herokuapp.com/playload 
- 发布: 
    + 仓库: [DebugUself/duw: 怼周刊 -> 自怼圈社区电子周刊](https://github.com/DebugUself/duw)
    + 访问: du.101.camp/duw
- 关联:
    + 意见: [2w\[讨论\] 怼周刊 Progress 部分意见征集 · Issue #612 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/612)
        * [1m \[Task\] 怼周刊自动化发布流程进展 · Issue #626 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/626)
    + 问题: [2d\[Help\] pip install Markdoc 出错 · Issue #635 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/635)
    + 推进: [3w\[WIP\] DUW 自动化发布优化 · Issue #634 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/634)
        * [3w\[MVP\] pubDUW 实用化 · Issue #652 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/652)
    + 内容: [2m\[DU_tools\]使用手册公募使用手册 · Issue #328 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/328)
        * [2w\[WIP\] DUPoW ~ 怼力通证 · Issue #645 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/645)
        * [3w\[MVP\] st 社区活性统计器 · Issue #651 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/651)
        * [3W\[MVP\]社区活性统计 Golang 版 · Issue #687 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/687)
        * [2w\[WIP\] DUPoW ~ 怼力通证 · Issue #645 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/645)

## 目标

令怼周刊的编辑和发布越来越`三有`

## 分析

- DONE: 周刊自身自动化发布
- TODO:
    + ? 自动化远程监察/控制
    + 周刊内容自动化采集/生成

## 追踪

> 活性内容准备

- [ ] [2w\[WIP\] DUPoW ~ 怼力通证 · Issue #645 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/645)
- [ ] [3w\[MVP\] st 社区活性统计器 · Issue #651 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/651)
    + [ ] [3W\[MVP\]社区活性统计 Golang 版 · Issue #687 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/687)

> 自动化合并

- [ ] 模板选择
    + [ ] 评估
    + [ ] 试用
    + [ ] 决定
- [ ] st 数据准备
- [ ] 自动化合并

## VPS
> aliyun 上 Ubuntu 环境自动化过程

- [ ] 持续集成/部署:
    + [ ] CI/D 工具评估 [Topic: ci-cd](https://github.com/topics/ci-cd)
        * [ ] Circle CI
        * [ ] Travis CI
    + [ ] 可 slack 回响
- [ ] 文档
    + [ ] 开发指南
    + [ ] 运维指南


## refer:

- [Deploy flask app with nginx using gunicorn and supervisor](https://medium.com/ymedialabs-innovation/deploy-flask-app-with-nginx-using-gunicorn-and-supervisor-d7a93aa07c18)


## refer
> 当前关系图谱: [怼周刊_v108 ~ pubDUW 阶段故事](https://du.101.camp/duw/108w/#achievements)

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






```
 o
  o
ooo
```
参考: [禁止事项清单](https://github.com/DebugUself/du4proto/wiki/HbNotDoIt)

