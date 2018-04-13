# DU Weekly 小站

DU Weekly 小站正式迁移至怼圈内部啦, 欢迎小伙伴一起来更新, 探索更多玩法 
@DebugUself/du4all 

- [DU Weekly 小站](http://duw.zooomquiet.io/)
- [Github 仓库](https://github.com/DebugUself/duw)
- [Issue](https://github.com/DebugUself/du4proto/issues/380)

## Usage

- 提交最新一期周刊方式
master 分支 -> content/post 目录 ->  复制 [du4proto/DUW](https://github.com/DebugUself/du4proto/tree/DUW) 分支里 相应的 `DU--w.md` -> 在最前面处添加标题和时间信息, 如

    ```
    ---
    title: "DU52w"
    date: 2018-04-09T20:20:00+08:00
    ---
    ```
    
- 还可以添加任何你喜欢的内容(`content` 目录下)
- 或者修订成你喜欢的显示界面(`themes` 目录下) 
- :)
- ...

## 背景

- 怼周刊到现在已经累计到 50 多期了，希望能为它建立一个小站，能让我们更方便的查询和阅读，也让它后续能有更多的发展空间
- [[RDD]DU Weekly 怼周刊小站 项目，自述原案 · Issue #365 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/365)
- [[RDD]DU_tools ~ 怼圈运营工具箱](https://github.com/DebugUself/du4proto/issues/368)


## 分析

- 之前尝试在私人仓库中试用了不同的建立怼周刊小站的方式, 包括
    - Hugo + Netlify 
    - Travis CI + Github Pages + Hugo
    - Jekyll + GitHub Pages 
- 最后觉得最方便也最美观的方式还是 Hugo + Netlify
    - 使用方式上, 和 Github Pages 支持的 Jekyll 一样方便, 只需要 push 相应的文件, 网站会自动更新
    - 界面上, 感觉 Hugo 的 Janes 主题还比较适合怼周刊的展示
- 当然, 希望小伙伴们如果有更好的方案的话, 一起来这个仓库里一起试验,共同玩耍
- 未来, 希望能慢慢做到 @ZoomQuiet  [提到的](https://github.com/DebugUself/du4proto/issues/368) `规划自动发布到 7niu 等其它 CDN 中
并提供全文搜索功能,在对应微信号/Slack 频道`


## 进展

- 180413 DU Weekly 小站 启用新域名 http://duw.zoomquiet.io
- 180412 [DU Weekly 小站](https://duw.zoejane.net/) 迁移至 [怼圈内部 repo](https://github.com/DebugUself/duw), 并启用新域名 https://duw.zoejane.net
- 180329 DU Weekly 小站 上线
- 180329 在 du.zoomquiet.io 右上角添加了 怼周刊 小站链接
- 180329 测试了将 duw 的文章直接放入 du.zoomquiet.io ，显示有错位，需要进一步调整模板了才能用这种方式
