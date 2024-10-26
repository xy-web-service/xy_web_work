<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:52:22
 * @FilePath: /xy_web_work/readme/README_en.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_web_work

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

## Description

xy-web-service Service settings module.

## Source Code Repositories

- <a href="https://github.com/xy-web-service/xy_web_work.git" target="_blank">Github</a>  
- <a href="https://gitee.com/xy-web-service/xy_web_work.git" target="_blank">Gitee</a>

## 安装

```bash
pip install xy_web_work
```

## How to use

```python
# main.py
from xy_web_work.WebWork import WebWork as xyWebWork
from xy_web_work.Settings.Settings import Settings

class WebServerWork(xyWebWork):
    settings: Settings | None = Settings()

    prog: str = "xy_test_demo"
    description: str = f""">>>>>>>>>>>> xy_test_demo - v1.0.0 <<<<<<<<<<<<<"""

if __name__ == "__main__":
    web_server_work = WebServerWork()
    web_server_work.main()
```

```bash
python main.py -c project -n xy_web_work_demo
# 创建项目 [ xy_web_work_demo ] 成功!!!
# 项目路径 ==>>> /mnt/bs-media/Workspace/project/opensource/xy-web-service/xy_web_work/test/xy_web_work_demo

cp main.py xy_web_work_demo
cd xy_web_work_demo
python main.py
# >>>>>>>>>>>> xy_web_work_demo - v1.0.1 <<<<<<<<<<<<<
# Hello World!!!
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