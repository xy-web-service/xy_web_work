# -*- coding: UTF-8 -*-
__doc__ = "Runner.py"
__version__ = "0.0.1"

import xy_work
from xy_work.Work import Work


class Runner:
    @property
    def __version__(self) -> str:
        return "0.0.1"

    def get_name(self) -> str:
        return "xy_web_work_demo"

    @property
    def parser_key(self) -> str:
        return Work().parser_key

    def __init__(self, *args, **kwargs) -> None:
        parser = kwargs.get(self.parser_key)
        xy_work_argparser_description: str = f""">>>>>>>>>>>> {self.get_name()} - v{xy_work.__version__} <<<<<<<<<<<<<"""
        if not parser:
            parser = Work().argparser_make(
                self.get_name(), xy_work_argparser_description
            )
        self.parser = parser

        print(xy_work_argparser_description)
        print("")
        print("Hello World!!!")
