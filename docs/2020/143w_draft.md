# 怼周刊_v143
~ 预定 200113 2042 发布

-----------------------------------------
...TODO


-----------------------------------------

- 主编: [大妈](http://du.zoomquiet.io/2014-02/ac0-zq/)
- 责编: 所有怼员

## Activity 活性
> 社区当前嗯哼程度


::.

~ PoDU 图表注入区

.::


## propose 号召

- [|蠎周刊 |汇集全球蠎事儿 !-)](http://weekly.pychina.org/archives.html)
    + 俺私人嗯哼了5年了
    + 邀请大家一起来, 每周嗯哼
- 每周例怼后, 无论是否列席, 大家都在 `故事->怼印象` 中追加当周 top3 感触



## Achievements 成果 
~ 各种成品/半成品 内部知识作品

      
## Stories 故事 
~ 收集各自无法雷同的怼圈真人故事...

### 熊本 -> 为 pysrc/fractal 配置合适环境
- 背景
    - 因聚会主题演讲所需,得现场演示 [pysrc/fractal: Draw fractal image by python.](https://github.com/pysrc/fractal).
    - 俺的配置
        + macOS Mojave/ 10.14.4.
    - 前置条件
        + 已成功安装 pyenv, 并检验过.
- 分析
    - pysrc/fractal github 上只有 15 个 stars,直接装到环境里,觉得不稳定...
    - 希望复制出 1 个专属环境,以玩赏该 module.
- 分解
    - 查一下自己已经有的工程环境
        + 是否有 1 个纯净的版本环境可供复制?
    - 查一下 pysrc/fractal 使用 python3 还是 2
    - 创建适合 pysrc/fractal 的版本环境
- 记录
    - `$ pyenv versions`
        + 判断: 似乎有 1 个纯净环境 -> `3.7.4`,那么接下来就是复制该环境...

```
$ pyenv versions
* system (set by /Users/zsy/.pyenv/version)
  3.7.4
  3.7.4/envs/374blog
  374blog
```

- `$pyenv virtualenv 3.7.4`
    + 判断: 原来 `3.7.4` 是俺曾经建好的纯净环境,那么直接复制即可...

```
$ pyenv virtualenv 3.7.4
pyenv-virtualenv: `/Users/zsy/.pyenv/versions/3.7.4' already exists.
```

- `$pyenv local 3.7.4` vs `$pyenv local 环境别称`
    + 判断: 似乎先做前半步,再做后半步,但是为啥要 2 次 local?

```
待补...
```

- `$ pip install fractal`

```
待补...
```

- Refer
    - [debuguself.github.io/2018-07-30-pyenv101.md at master · DebugUself/debuguself.github.io](https://github.com/DebugUself/debuguself.github.io/blob/master/_posts/scm4du/2018-07-30-pyenv101.md)
    - [TS3: Pyenv 最终介绍 — Blogging 蟒营™ 博客](https://blog.101.camp/TS/190919-pyenv-finally-intro/)
    - [191006_pyenv-usage_20-00-50_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili](https://www.bilibili.com/video/av77693412?from=search&seid=6335516483445440874)


### impression 怼印象 
~ 例怼中感触最嗯哼的 top3 感想

- `(￣▽￣)`:
    + ...

### live 怼生活
~ 生活中带有怼范的各种 (投稿后可同时沉淀到 [wiki 的2.5 怼生活](https://github.com/DebugUself/du4proto/wiki/How2Live)下)


`熊本`:


- 200106 .5h 排版 TS 05
- 200105 .5h 瑶台镜 BP 再试;

`(￣▽￣)`:

- 200106 JKV+ 恢复 Elixir 开发,感觉回到大学用 C++ 感觉...
- 200105 JKV+ 101camp过往 BP 收集, 才发觉, 真心不少, 产品级的都有4个了...


## Recommedations 推荐 
~ 嗯哼各种怼路上发现的嗯哼...

- 是也乎:
    + [Issue 368 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-368.html)


## Postscript 后记 
~ 怼周刊是什么以及为什么和能怎么...

大妈曰过: `参差多态 才是生机`
问题在 `参差` 的行为是无法形成团队的

    Coming together is a beginning; 
    Keeping together is progress; 
    Working together is success!

<--- [Henry Ford](https://www.brainyquote.com/quotes/quotes/h/henryford121997.html)

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

<--- [Henry Ford](https://www.brainyquote.com/quotes/quotes/h/henryford121997.html)

That's why Dama keeps on debugging.
However, as time goes by, maybe you would not remember these days clearly and spread your experience difficultly.
What a pity!
The valuable should have a fixed form to be recorded.
That's why we make the Weekly for DU.

