# TianBot-Mini

## 任务

基于ROS to GO控制Tianbot迷你机器人完成以下任务：

* [ ] **topic发布**：控制小车速度，不考虑避障到达终点(25')
  * 发送`/tianbot_mini/cmd_vel` topic控制*线速度，角速度*(运行时开启`bringup.launch`)
* [ ] **topic监听**：监听`/tianbot-mini/odom`话题，保存小车实时位置，画出轨迹图(10')
* [ ] **topic发布&控制第三方包|访问action服务器**：
  * [ ] 运行`demo_slam.launch`，通过鼠标选取目标点，感受见图和避障过程(5')
  * [ ] 发布`move_base_simple/goal`话题或访问`move_base`的action服务器指定目标点，达到同样效果(15')
  * [ ] 确定几个目标点依次发送，尝试在地上走一个几何图案，运行过程**实时避障**

## Quickstart

1. Fork项目:

![](http://118.24.109.65/photo_db/233_Markdown_IMG_tianbot1.png)

2. 将fork的项目克隆到本地：

```shell
# 注意将@YOUR_NAME换成你的用户名
git clone https://github.com/@YOUR_NAME/TianBot-Mini-Dev
```

3. 添加我的远程仓库：

```shell
git remote add master https://github.com/qiaopengju/TianBot-Mini-Dev
# 可以通过git remote -v 查看有几个远程仓库，origin是你Fork的，master是刚刚创建的我的仓库
```

3. **跳转到自己的分支(一定要在自己的分支底下开发修改)**:

```shell
git checkout mengqiuting	# 秋婷跳转到这个
git checkout xuhuiqing		# 慧卿跳转到这个
```

4. 进行开发，add & commit，建议用git桌面版，可以看有哪些修改

* 建议每加一个功能点就commit一下，写清楚做了哪些修改

```shell
# git add 添加你想加入的文件，建议用GUI
# git commit -m "你对哪些做了修改，建议经常commit"
git push -u origin mengqiuting | xuhuiqing # 将修改推到你fork的github仓库分支中，一定不要推送到main
```

5. pull request

![](http://118.24.109.65/photo_db/233_Markdown_IMG_tianbot2.png)

7. pull request通过后，及时拉取我做的修改:

```shell
git pull master main
```

8. 跳转到第4步，继续开发
