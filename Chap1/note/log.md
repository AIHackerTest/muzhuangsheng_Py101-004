## Ch1d2

- **探索记录**

今天尝试完成本周任务：   
【X】查看卡包里关于任务的要求   
【X】查看卡包里相关官方文档   
【X】完成天气查询编程  

探索技能点：   
【X】with open('filename') as f: 用with方式来写可以省去最后f.close()那一步，调用完会自动close，而close file是个好习惯。    
【X】for i in k： 小循环语句    
【X】a, b= f.split(',') 将逗号/空格/等前后元素分割赋值给a,b，若('', 1)表示分割一次，即将字符串分割成两个部分。    
【X】dict = {key: value, key: value} 其中key要unhashable，相当于字典，直接查询相应key的value。可以用dict[key]=value为dict添加元素。    
【X】str.replace('\n', '') 用空格取代\n
【X】Python3中格式化的新方法，‘{}{}’.format('hello','world'), 还可以'{1}, {0}'.format('world','hello')指定顺序，或者‘{i}{j}'.format(i = 'hello', j = 'world')     
【X】git add添加修改至stage, git commit添加修改至respitory, git push至远程GitHub库。    



- **复盘 & 改进**   

今日收获：    
 1. 用更优雅的方法写代码，先将任务拆解成4个部分，分别def函数，结构比上周好看，每个部分的检验也更加便捷。
 2. 再次使用try except语句接受异常输入。    

哪些地方做得不好？打算如何改进？    
 1. 练习的当下没有及时记录，导致时间记录非常粗略    
 2. 探索技能是基于本周任务，边查询边敲代码，不够体系化，在考虑如何将琐碎知识点纳入教程的大体系里。或许可以尝试先写出一个提纲，一点点填入？
 还是以输出倒逼输入本来就是正确的学习方法，无所谓体系化不体系化？  


## Ch1d4【2.5h】
- [x] 看Ch0加油卡包【1:9】【0.5h】
- yield  **待查**
- 推荐《流畅的Python》 *reference for advanced stage*
- 看书时可以好几本对照着看，互相解释  →  *主题阅读*
- YouGlish(English in YouTube) native教读法

- [x] [PEP8](https://www.python.org/dev/peps/pep-0008/#maximum-line-length)
学习
【:Comments】【1h】
- improve **readability** of your code
- indentation 为4个空格(少用tab)，跨行时可以纵向对齐，或进一步缩进，例如：
```
  foo = long_function_name(var_one, var_two,
                           var_three, var_four)

  def long_function_name(
          var_one, var_two, var_three,
          var_four):
      print(var_one)
```  
- maximum-line-length: 79 characters   
- 算法的跨行，在运算符前面break
- 空格用法
- **不要背！每次敲完代码利用文档自检就记住了！**

- [x]看自评互评参考&大妈演示视频 【1h】
- 小步迭代快跑，只要可运行，马上git commit -m "改动简介"
- 善用pass占位符
- 善用print来查看新增功能，运行成功，即可commit；第二版中#print
- 历史输入数据存储open('filename','a').write('\n'+d)，其中d = input()
- 历史数据输出print(open('filename').read)
- terminal中touch filename新建文档，cat filename显示文档
- KM = (P+K)<sup>S</sup>  (KM: Knowledge management, P: People,
  +: Information Tech, K: Knowledge, **S: Sharing**)
  
  
## Ch1d5【2h】

- [x]看[如何掌握所有的程序语言](http://www.yinwang.org/blog-cn/2017/07/06/master-pl)
[如何学习一门新的编程语言](http://www.yangzhiping.com/tech/learn-program-psychology.html)
【20'】
- 不要试图掌握整个语言，而是去掌握 **语言特性**。
- **语言特性** 包括变量定义、算数运算、for/while循环语句等
- 不要一上来就读书读书读书，快速浏览语言手册，然后直接拿一段例子代码开始捣鼓，把它改成自己想解决的问题
- 在学习区可以练习，**少看书，多练习**

- [x] 看Ch0加油卡包【9:】【1h】
- 写代码三步走：先 **运行** 起来，然后从用户的角度思考，最后readability
- **函数** 的本质是有输入和输出，封装起来是为了可调用可重复，而不是把代码打包起来。
查阅廖雪峰教程函数那节：
  > 当代码出现有规律的重复的时候，可以写成更有意义的函数调用。
  这样函数本身只需写一次就可以多次调用。

- 【Q】为什么while后要**return**
【A】查询后知定义函数时，如果没有return，函数结果会是None，而None表示没有任何值。
- git commit -am "" 可以直接将tracked的文件加入stage的同时加入repository；等于git add之后再git commit -m ""

- [x]看Ch0进阶任务讲解【0.5h】
- 拆分任务，每写一步可以print来查看效果
- 边写猜数字游戏的教程大纲
 1. random.randint(a,b) Return a random integer N such that a <= N <= b.
 2. Python3中input()得到字符串
 3. int() 将...变为integer
 4. for in, while循环
 5. if判断
 6. break跳出循环，continue跳过下面的语句进入下一个循环，refer to 晓峰 循环那章
 7. try except接受错误   


- [x]修改Ch1作业代码，增加退出前输出历史信息的功能，参考昨天看的PEP8提高可读性【10'】
