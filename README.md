## TianBot-Mini

### 任务

基于ROS to GO控制Tianbot迷你机器人完成以下任务：

* [ ] **topic发布**：控制小车速度，不考虑避障到达终点(25')
* [ ] **topic监听**：保存小车实时位置，画出轨迹图(10')
* [ ] **topic发布&控制第三方包|访问action服务器**：
  * [ ] 运行`demo_slam.launch`，通过鼠标选取目标点，感受见图和避障过程(5')
  * [ ] 发布`move_base_simple/goal`话题或访问`move_base`的action服务器指定目标点，达到同样效果(15')
  * [ ] 确定几个目标点依次发送，尝试在地上走一个几何图案，运行过程**实时避障**

---

### Quickstart

