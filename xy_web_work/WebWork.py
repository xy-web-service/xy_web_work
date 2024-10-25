# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "WebWork"
"""
  * @File    :   WebWork.py
  * @Time    :   2023/04/26 12:35:27
  * @Author  :   余洋
  * @Version :   1.0
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, Ship of Ocean
  * @Desc    :   None
"""
from pathlib import Path
import xy_web_work
from .Work import Work


class WebWork(Work):
    prog: str = xy_web_work.__name__
    description: str = f""">>>>>>>>>>>> {xy_web_work.__name__} - v{xy_web_work.__version__} <<<<<<<<<<<<<"""
    parser_key = "xy_web_parser"
    config_relative_path: Path = Path("config/xy_web.toml")