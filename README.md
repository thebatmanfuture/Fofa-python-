## 使用介绍

UP的b站主页：https://space.bilibili.com/692997880?spm_id_from=333.337.0.0

欢迎加UP的qq一起交流

![](/img/lightning.png)

这是一个有关fofa爬虫的脚本，作者会持续更新

#### 第一版（2022-3-12）

使用方式：

使用前请先配置好你的`Authorization`，该`Authorization`可以在fofa中抓包获取，如图

这里在搜索命令之后，点击切换页数，抓包

![](/img/fofa.png)

发送到repeater模块发现了`Authorization`，把它放进脚本里（脚本里有标注位置）

![](/img/burp.png)

![](/img/python.png)

当你输入fofa命令之后，url会写入到同级的urls.txt里

~~~python
>>> python fofa.py
请输入fofa命令:
>>> body="74cms"	#  这里就是你输入的fofa查询命令 
~~~

第二版会增加多线程，以及优化界面和命令行形式