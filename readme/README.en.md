<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:52:22
 * @FilePath: /xy_web_work/readme/README.en.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_web_work

| [简体中文](../README.md)         | [繁體中文](./README.zh-hant.md)        |                      [English](./README.en.md)          |
| ----------- | -------------|---------------------------------------|

## Description

xy-web-service Service settings module.

## Source Code Repositories

| [Github](https://github.com/xy-web-service/xy_web_work.git)         | [Gitee](https://gitee.com/xy-opensource/xy_web_work.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_web_work.git)          |
| ----------- | -------------|---------------------------------------|

## Installation

```bash
# bash
pip install xy_web_work
```

## How to use

###### 1. General

```bash
# 创建项目
xy_web_server -c project -n xy_web_demo
cd xy_web_demo
xy_web_server
# >>>>>>>>>>>> xy_web_demo - v0.0.1 <<<<<<<<<<<<<
# 
# xy_web_work Hello World!!!

```

###### 2. Extend or customize
```python
# main.py
from xy_web_work.WebWork import WebWork as xyWebWork
from xy_web_work.Settings.Settings import Settings


class WebServerWork(xyWebWork):
    settings: Settings | None = Settings()

    def __init__(self):
        self.prog = "xy_test_demo"
        self.description = f""">>>>>>>>>>>> xy_test_demo - v1.0.0 <<<<<<<<<<<<<"""


if __name__ == "__main__":
    web_server_work = WebServerWork()
    web_server_work.main()
```

```bash
# bash
python main.py -c project -n xy_web_work_demo
# 创建项目 [ xy_web_work_demo ] 成功!!!
# 项目路径 ==>>> /mnt/bs-media/Workspace/project/opensource/xy-web-service/xy_web_work/test/xy_web_work_demo

cp main.py xy_web_work_demo
cd xy_web_work_demo
python main.py -c runner
# >>>>>>>>>>>> xy_web_work_demo - v1.0.1 <<<<<<<<<<<<<
# xy_web_work Hello World!!!
```

## License
xy_web_work is licensed under the <Mulan Permissive Software License，Version 2>. See the [LICENSE](../LICENSE) file for more info.

## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?  

![Pay-Total](./Pay-Total.png)  


## Contact

```
WeChat: yuyangiit
Mail: yuyangit.0515@qq.com
```