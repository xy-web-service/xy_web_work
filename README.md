<!--
 * @Author: yuyanget 845262968@qq.com
 * @Date: 2024-10-18 13:02:23
 * @LastEditors: yuyanget 845262968@qq.com
 * @LastEditTime: 2024-10-23 20:51:38
 * @FilePath: /xy_web_work/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_web_work

- [简体中文](readme/README_zh_CN.md)
- [繁体中文](readme/README_zh_TW.md)
- [English](readme/README_en.md)

## 说明

xy-web-service服务设置模块.

## 源码仓库

- <a href="https://github.com/xy-web-service/xy_web_work.git" target="_blank">Github地址</a>  
- <a href="https://gitee.com/xy-web-service/xy_web_work.git" target="_blank">Gitee地址</a>

## 安装

```bash
pip install xy_web_work
```

## 使用

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
```

## 捐赠

如果小伙伴们觉得这些工具还不错的话，能否请咱喝一杯咖啡呢?  

![Pay-Total](./readme/Pay-Total.png)


## 联系方式

```
微信: yuyangiit
邮箱: 845262968@qq.com
```