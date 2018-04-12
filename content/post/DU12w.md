---
title: "DU12w"
date: 2017-07-01T20:20:00+08:00
---

# 怼周刊\_v12
\~ 预定 17.7.1 20:20 发布

---- 

时差

	天圆地方自古曰
	其实正好反过来
	夜晩却为地自影
	时区穿梭有差异
	身体老实跟不上
	总算归来查log
	又是七天暗进步
	迎新筹备还缺嘛
	再启新四周项目
	自怼小圈稳心气

---- 

- 主编: [大妈][1]
- 责编:
	+ [xpgeng][2]
	+ [sunoonlee][3]
	+ [Zoe][4]
	+ [bambooom][5]

# 进度
\~ 记录当周关键事件日期+证据链接

- 170624 [72h \[ANN] 170624 怼周会及会议纪要][6]
- 170401 关闭报表和入密
- 170331 om103py 毕业

# 任务
\~ 记述关键共怼任务 (如果没有, 留空)

- 170624 [S04E51 启动][7]
- 170603 [怼圈的二次开放 筹备中][8]


# 进展
\~ 整体上圈内部活跃指标情况

- 提交(S04E051): 7 人 (6人延续上期 + 1 个新项目)
   - 小组 @zoomquiet 时间帐单:效能分析小队
	   - @zoomquiet 
	   - @zsy
	   - @liguanghe
	   - @simpleowen 
	   - @mxclover 
   - @hetao Deep Learning 自学计划
   - @zoejane 进入 Web 世界
- 引发的作品:
	+ @hetao - Deep Learning 学习笔记
	+ @zoejane - Demo 网页
- 状态:

<table>
<tr><th>allcic Commit</th><th> times</th><th>weekly Commit</th><th> times</th></tr>
<tr><td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>255</td>
        <td>
            <a href='http://github.com/zoejane'>zoejane</a></td><td>25</td>
            
<tr><td>
            <a href='http://github.com/zoejane'>zoejane</a></td><td>239</td>
        <td>
            <a href='http://github.com/mxclover'>mxclover</a></td><td>10</td>
            
<tr><td>
            <a href='http://github.com/liguanghe'>liguanghe</a></td><td>117</td>
        <td>
            <a href='http://github.com/zhangshiyinrunwithcc'>zhangshiyinrunwithcc</a></td><td>2</td>
            
<tr><td>
            <a href='http://github.com/mxclover'>mxclover</a></td><td>113</td>
        <td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>1</td>
            
<tr><td>
            <a href='http://github.com/bambooom'>bambooom</a></td><td>107</td>
        <td>
            <a href='http://github.com/livingworld'>livingworld</a></td><td>1</td>
            
<tr><th>all Commit </th><th>Comments times</th><th>weekly Commit</th><th>Comments times</th></tr>
<tr><th>all Issue </th><th>Comments times</th><th>weekly Issue</th><th>Comments times</th></tr>
<tr><td>
            <a href='http://github.com/ZoomQuiet'>ZoomQuiet</a></td><td>307</td>
        <td>
            <a href='http://github.com/zhangshiyinrunwithcc'>zhangshiyinrunwithcc</a></td><td>8</td>
            
<tr><td>
            <a href='http://github.com/zhangshiyinrunwithcc'>zhangshiyinrunwithcc</a></td><td>168</td>
        <td>
            <a href='http://github.com/zoejane'>zoejane</a></td><td>3</td>
            
<tr><td>
            <a href='http://github.com/liguanghe'>liguanghe</a></td><td>129</td>
        <td>
            <a href='http://github.com/mxclover'>mxclover</a></td><td>1</td>
            
<tr><td>
            <a href='http://github.com/zoejane'>zoejane</a></td><td>70</td>
        <td>
            <a href='http://github.com/livingworld'>livingworld</a></td><td>1</td>
            
</table>

\<- 170701 16:22

- 在线(测试ing..):
	+ `curl du.zoomquiet.us`
	+ `curl du.zoomquiet.us/v0/all/cic/rank/5/`
	+ `curl du.zoomquiet.us/v0/all/cil/rank/5/`
	+ `curl du.zoomquiet.us/v0/week/cic/rank/5/`
	+ `curl du.zoomquiet.us/v0/week/cil/rank/5/`


# 成果
\~ 各种成品/半成品 内部知识作品

## @hetao - Deep Learning学习笔记

- [DebugUself/du4proto at hetao][9]
- @hetao 童鞋近期在 GitHub 更新了自己这几周以来对于 Depp Learning 非常详细的学习笔记,推荐!

### 20170626 Skip-gram word2 笔记

Skip-Gram主要是给定input word来预测上下文,区别于CBOW给定上下文预测input word. 

Word2Vec模型实际上分为了两个部分,第一部分为建立模型,第二部分是通过模型获取嵌入词向量. 

### 第一部分:模型
#### Fake Task

- 印象:训练模型的真正目的是获得模型基于训练数据学得的隐层权重. 为了得到这些权重,我们首先需要构建完整的神经网络作为我们的"Fake Task". 
- 例子:以一个句子`"The dog barked at the mailman"`的输入为例. 
	+ 首选选择,单词"dog"作为input word. 
	+ 其次,定义一个叫做**skip\_window**的参数,它代表着我们从当前input word的一侧(左边或右边)选取词的数量. 如果我们设置`skip_window=2`,那么我们最终获得窗口中的词(包括input word在内)就是['The', 'dog','barked', 'at']. `skip_window=2`代表着选取左input word左侧2个词和右侧2个词进入我们的窗口,所以整个窗口大小span=2x2=4. 
	+ 另一个参数叫**num\_skips**,它代表着我们从整个窗口中选取多少个不同的词作为我们的output word,当`skip_window=2`,`num_skips=2`时,我们将会得到两组 (input word, output word) 形式的训练数据,即 ('dog', 'barked'),('dog', 'the'). 
	+ 神经网络基于这些训练数据将会输出一个概率分布,这个概率代表着我们的词典中的每个词是output word的可能性. 例如我们先拿一组数据 ('dog', 'barked') 来训练神经网络,那么模型通过学习这个训练样本,会告诉我们词汇表中每个单词是"barked"的概率大小. 
	+ 模型的输出概率代表着到我们词典中每个词有多大可能性跟input word同时出现. 
	+ **window\_size=2**表示选择输入词前后各两个词和输入词进行组合,如图蓝色代表input word,方框内代表位于窗口内的单词,由图可知,可以统计词汇组合出现概率高低. 
		* ![][image-1]
#### 模型细节

- 首选构建自己的词汇表(vocabulary)再对单词进行one-hot编码. 
- 假设从我们的训练文档中抽取出10000个唯一不重复的单词组成词汇表. 我们对这10000个单词进行one-hot编码,得到的每个单词都是一个10000维的向量,向量每个维度的值只有0或者1,假如单词ants在词汇表中的出现位置为第3个,那么ants的向量就是一个第三维度取值为1,其他维都为0的10000维的向量($ants=[0, 0, 1, 0, ..., 0]$). 
- 还是上面的例子,"The dog barked at the mailman",那么我们基于这个句子,可以构建一个大小为5的词汇表(忽略大小写和标点符号):("the", "dog", "barked", "at", "mailman"),我们对这个词汇表的单词进行编号0-4. 那么"dog"就可以被表示为一个5维向量[0, 1, 0, 0, 0]. 
- 模型的输入如果为一个10000维的向量,那么输出也是一个10000维度(词汇表的大小)的向量,它包含了10000个概率,每一个概率代表着当前词是输入样本中output word的概率大小. 
- ![][image-2]
- 隐层没有使用任何激活函数,但是输出层使用了sotfmax. 
- 我们基于成对的单词来对神经网络进行训练,训练样本是 ( input word, output word ) 这样的单词对,input word和output word都是one-hot编码的向量. 最终模型的输出是一个概率分布. 

#### 隐层

用300个特征节点表示一个单词,即用300维向量表示,则隐藏层权重矩阵为10000x300维度. 
看下面的图片,左右两张图分别从不同角度代表了输入层-隐层的权重矩阵. 左图中每一列代表一个10000维的词向量和隐层单个神经元连接的权重向量. 从右边的图来看,每一行实际上代表了每个单词的词向量. 

上面我们提到,input word和output word都会被我们进行one-hot编码. 如果我们将一个1 x 10000的向量和10000 x 300的矩阵相乘,它会消耗相当大的计算资源,为了高效计算,它仅仅会选择矩阵中对应的向量中维度值为1的索引行(这句话很绕),看图就明白. 

上面的例子中,左边向量中取值为1的对应维度为3(下标从0开始),那么计算结果就是矩阵的第3行(下标从0开始)--- [10, 12, 19],这样模型中的隐层权重矩阵便成了一个"查找表"(lookup table),

#### 输出层

经过神经网络隐层的计算,ants这个词会从一个1 x 10000的向量变成1 x 300的向量,再被输入到输出层. 输出层是一个softmax回归分类器,它的每个结点将会输出一个0-1之间的值(概率),这些所有输出层神经元结点的概率之和为1. 
下面是一个例子,训练样本为 (input word: "ants", output word: "car") 的计算示意图. 
![][image-3]

#### 直觉上的理解

针对上下文相似的情况,进行词干话(stemming),就是去除词缀得到词根的过程. 

### 第二部分 基于skip-gram模型的高效训练

针对权重矩阵过大的问题,Word2Vec做出了如下优化:

- 将常见的单词组合(word pairs)或者词组作为单个"words"来处理. 
- 对高频次单词进行抽样来减少训练样本的个数. 
- 对优化目标采用"negative sampling"方法,这样每个训练样本的训练只会更新一小部分的模型权重,从而降低计算负担. 

这是一个[模型词汇表][10],及[vocabulary][11],相应的论文有[Distributed Representations of Words and Phrases
and their Compositionality](https://arxiv.org/pdf/1310.4546.pdf),[代码][12]. 

#### 对高频词抽样

如下图所示,对于"the"这种常用高频单词,既无意义,又的比重大. 对于我们在训练原始文本中遇到的每一个单词,它们都有一定概率被我们从文本中删掉,而这个被删除的概率与单词的频率有关. 
![][image-4]

#### 抽样率
在语料库中,该词出现概率越低,越有可能被保留. $P(w\_i)=1-\sqrt{\frac{t}{f(w\_i)}}$. 在代码中还有一个参数叫"sample",这个参数代表一个阈值,默认值为0.001,这个值越低,越不容易保留,即$P(w\_i)$越大. 

#### 负采样(negative sampling)

- 印象:用来提高训练速度并且改善所得到词向量的质量的一种方法. 不同于原本每个训练样本更新所有的权重,负采样每次让一个训练样本仅仅更新一小部分的权重,这样就会降低梯度下降过程中的计算量. 
- 例子:
	+ 当我们用训练样本 ( input word: "fox",output word: "quick") 来训练我们的神经网络时,"fox"和"quick"都是经过one-hot编码的. 如果我们的vocabulary大小为10000时,在输出层,我们期望对应"quick"单词的那个神经元结点输出1,其余9999个都应该输出0. 在这里,这9999个我们期望输出为0的神经元结点所对应的单词我们称为"negative" word. 
	+ 如果使用了负采样的方法我们仅仅去更新我们的positive word-"quick"的和我们选择的其他5个negative words的结点对应的权重,共计6个输出神经元,相当于每次只更新$300x 6=1800$个权重. 
	+ 在论文中,作者指出指出对于小规模数据集,选择5-20个negative words会比较好,对于大规模数据集可以仅选择2-5个negative words. 

#### 如何选择negative words

我们使用"一元模型分布(unigram distribution)"来选择"negative words". 要注意的一点是,一个单词被选作negative sample的概率跟它出现的频次有关,出现频次越高的单词越容易被选作negative words. 
代码公式如下:
$P(w\_i)=\frac{f(w\_i)^{3/4}}{\sum\_{j=0}^n(f(w\_j)^{3/4})}$
每个单词被赋予一个权重,即$f(w\_i)$, 它代表着单词出现的频次. 公式中开3/4的根号完全是基于经验的,论文中提到这个公式的效果要比其它公式更加出色. 

- [c语言实现代码][13]
- [Word2Vec Resources教程][14]

### 第三部分:基于TensorFlow实现Skip-Gram模型

分为四部分:

- 数据预处理
- 训练样本构建
	+ 采样
	+ 构造batch
		* 找到每个input word的上下文:如果我们固定skip\_window=2的话,那么fox的上下文就是[quick, brown, jumps, over]. 
			- 我在实际选择input word上下文时,使用的窗口大小是一个介于[1, window\_size]区间的随机数. 这里的目的是让模型更多地去关注离input word更近词.
		* 基于上下文构建batch:如果我们的batch\_size=1的话,那么实际上一个batch中有四个训练样本. 

- 模型构建
	+ 输入层到嵌入层
		* 输入层到隐层的权重矩阵作为嵌入层要给定其维度,一般embeding\_size设置为50-300之间.
	+ 嵌入层到输出层
		* TensorFlow中的sampled\_softmax\_loss,由于进行了negative sampling,所以实际上我们会低估模型的训练loss. 
			- 有点儿费解.
- 模型验证


#### 参考资源

- [A really good conceptual overview of word2vec from Chris McCormick][15]
- [First word2vec paper from Mikolov et al.][16]
- [NIPS paper with improvements for word2vec also from Mikolov et al.][17]
- [An implementation of word2vec from Thushan Ganegedara][18]
- [TensorFlow word2vec tutorial][19]
- [知乎专栏][20]

### 零碎卡片
#### Word embeddings

- 印象:one-hot encode效率太低,浪费计算资源. 为了解决这个问题,采用了所谓embeddings,通过直接从权重矩阵中获取隐藏层值来跳过嵌入层的乘法,即使用权重矩阵作为查找表. 
- 例子:例如"heart"被编码为958,"mind"为18094.然后为了获取"heart"的隐藏层值,只需要嵌入矩阵的第958行. 这个过程称为嵌入式查找,隐藏单元的数量是嵌入维度. 
	+ ![][image-5]
	+ ![][image-6]

#### Word2Vec

- 印象:两种实现Word2Vec的结构:
	+ CBOW (Continuous Bag-Of-Words)
	+ Skip-gram
	![][image-7]

#### Preprocessing

印象:根据词频排序,频率最高的为0,其次为1,依次排序. 最终,输入一段words,输出的是一段文字中单词对应的序列位置. 

#### Subsampling

- 印象:去除一些无意义的词汇. 公式表达式为:
$P(w\_i)=1-\sqrt{\frac{t}{f(w\_i)}}$
其中,t是惩罚参数,$f(w\_i)$是$w\_i$在数据集中的频率,$P(w\_i)$是丢弃word的概率
- 例子:将一些无意义的词汇,例如"the","of"等去除.

#### Making batches

- 印象:获取一段话前后的word个数. 
- 例子:

```
def get_target(words, idx, window_size=5):
    ''' Get a list of words in a window around an index. '''
    R = np.random.randint(1, window_size+1)
    start = idx - R if (idx - R) > 0 else 0
    stop = idx + R
    target_words = set(words[start:idx] + words[idx+1:stop+1]) # 切片之后打乱了顺序

    # Your code here
    return list(target_words)
```

## zoejane - Demo 网页

* [Project Plan][21]
* [Demo 网页][22]

## 时间帐单:效能分析小队 推进中

- 组员
	* `(￣▽￣)` -\> 大妈
	* 🐻 `熊` =\> @zhangshiyinrunwithcc
	* 🐣 `鹤` =\> @李广鹤
	* 🐈 `猫` =\> @simpleowen
	* 🐴 `mx` =\> @mxclover
-  目标
	- 通过分析大妈和剑飞, 两人5年以上持续时间帐单的数据
	- 获得数据化的行为效能结论
	- 对自身行为给出几点优化策略
- [Github 项目链接][23]
- [Project Plan][24]  

# 故事
\~ 收集各自无法雷同的怼圈真人故事...

# 推荐
\~ 嗯哼各种怼路上发现的嗯哼...


# 后记
\~ 怼周刊是什么以及为什么和能怎么...

大妈曰过: `参差多态 才是生机`
问题在 `参差` 的行为是无法形成团队的

	Coming together is a beginning; 
	Keeping together is progress; 
	Working together is success!

\<--- [Henry Ford][25]

- 所以, 有了 大妈 随见随怼的持续嗯哼...
- 但是, 想象一年后, 回想几十周前自己作的那些 `图样图森破` 
- 却没现成的资料来出示给后进来嗯哼?
- 不科学, 值得记录的, 就应当有个形式固定下来
- 所以,有了这个 `怼周刊` (Weekly 4 DU)


[1]:	http://du.zoomquiet.io/2014-02/ac0-zq/
[2]:	http://du.zoomquiet.io/2017-04/about-xpgeng/
[3]:	http://du.zoomquiet.io/2017-04/about-sunoonlee/
[4]:	http://du.zoomquiet.io/2017-04/about-zoe/
[5]:	http://du.zoomquiet.io/2017-04/about-bambooom/
[6]:	https://github.com/DebugUself/du4proto/issues/148
[7]:	https://github.com/DebugUself/du4proto/blob/master/S04E51/README.md
[8]:	https://github.com/DebugUself/du4proto/issues/135
[9]:	https://github.com/DebugUself/du4proto/tree/hetao
[10]:	http://mccormickml.com/2016/04/12/googles-pretrained-word2vec-model-in-python/
[11]:	https://github.com/chrisjmccormick/inspect_word2vec/tree/master/vocabulary
[12]:	https://code.google.com/archive/p/word2vec/
[13]:	https://github.com/chrisjmccormick/word2vec_commented
[14]:	https://github.com/chrisjmccormick/word2vec_commented
[15]:	http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/
[16]:	https://arxiv.org/pdf/1301.3781.pdf
[17]:	http://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf
[18]:	http://www.thushv.com/natural_language_processing/word2vec-part-1-nlp-with-deep-learning-with-tensorflow-skip-gram/
[19]:	https://www.tensorflow.org/tutorials/word2vec
[20]:	https://zhuanlan.zhihu.com/zhaoyeyu
[21]:	https://github.com/DebugUself/du4proto/blob/master/S04E51/du_s04e51_zoejane_plan.md
[22]:	http://blog.zoejane.net/learn-web
[23]:	https://github.com/DebugUself/du4proto/tree/atl4dama
[24]:	https://github.com/DebugUself/du4proto/blob/master/S03E51/du_s03e51_zoomquiet_plan.md
[25]:	https://www.brainyquote.com/quotes/quotes/h/henryford121997.html

[image-1]:	https://raw.githubusercontent.com/DebugUself/du4proto/hetao/week8/note/images/window_size.png?token=ABQhvBWcLwFRicNJ1heHDKnP-yo3GPRRks5ZYEqlwA==
[image-2]:	https://raw.githubusercontent.com/DebugUself/du4proto/hetao/week8/note/images/neural_network.png?token=ABQhvNCC06XQfJwEMwBAZufGtntBrecgks5ZYEq5wA==
[image-3]:	https://raw.githubusercontent.com/DebugUself/du4proto/hetao/week8/note/images/input_output.png?token=ABQhvPeeIv6dMuE67Lo4hj5LYmjB2MnWks5ZYErMwA==
[image-4]:	https://raw.githubusercontent.com/DebugUself/du4proto/hetao/week8/note/images/window_size.png?token=ABQhvLEjfwZz2EuoVM_DN8ZqQCWUNtrZks5ZYErdwA==
[image-5]:	https://raw.githubusercontent.com/DebugUself/du4proto/hetao/week8/note/images/lookup_matrix.png?token=ABQhvOms5WWP6LWu8qx0iukDk9CYQ4Ouks5ZYEtMwA==
[image-6]:	https://raw.githubusercontent.com/DebugUself/du4proto/hetao/week8/note/images/tokenize_lookup.png?token=ABQhvLHc3PWG3nLblV-ZTa1gk5jGDxpPks5ZYEtzwA==
[image-7]:	https://raw.githubusercontent.com/DebugUself/du4proto/hetao/week8/note/images/word2vec_architectures.png?token=ABQhvNFrrnOwVj9uK9LSkao02U8ZSecoks5ZYEuKwA==