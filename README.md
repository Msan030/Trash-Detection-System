# 楼道杂物检测系统

### 简介
一套针对图片、视频能够实时检测的楼道垃圾检测系统，包含垃圾识别算法和用户界面搭建两部分内容

### 实现方式
**前端：**
layui/html/css

**后端：**
Django+MySql+YoloV3

### 运行

1. 配置MySql
   * python manage.py makemigrations myApp
   * python manage.py migrate
   * 在project/settings.py文件中根据系统数据库设置修改数据库USER及PASSWORD条目
2. 下载模型参数：https://jbox.sjtu.edu.cn/l/61SYdh ，放在yolo/logs下
3. 配置Pytorch、Django、Opencv及其他项目依赖包，最好打开cuda
4. 服务端开启服务：python manage.py runserver
5. 客户端浏览器中输入服务器网址（由于条件限制，项目部署在本机）:http://127.0.0.1:8000/

### 页面功能
1. 注册和登录
2. 简介
3. 垃圾检测分类
   * 已替换YoloV3算法进行图片的识别与分类
   * 增加上传视频、图片进行检测的功能，并能实时显示新增数据与图像处理结果
4. 垃圾信息查询
   * 增加批量处理垃圾功能
5. 个人中心

### 分工
|  人员  |        分工        |
| :------: |:----------------:|
| 王蕾颖 |    个人中心、全局监控     |
| 仇雨恬 |  UI优化、注册页面、全局监控  |
| 陈予涵 | 数据查询、增加已处理-未处理属性 |
| 鲍奕凡 |     YoloV3算法     |
|  顾婧  |   数据库、后端Django   |

### Timeline

#### Week 10-11

更换选题，进行技术学习，细化项目框架；

发布问卷，收集数据，初步分工；

制作简介、个人中心页面；

实现登录、注册功能；

#### Week 12-13

前后端分离进行开发，拍摄素材；

实现垃圾信息查询功能；

使用遗留物检测与图片分类方法完成杂物分类；

初步实现YoloV3算法；

展示现有处理结果；

#### Week 14-15

前后端分别对项目进行优化；

增加上传图片、视频功能，实时处理上传数据，进行分类并将数据库存入数据库；

实现实时进行杂物分类，YoloV3算法效率更高，因此最终选用了YoloV3算法。
