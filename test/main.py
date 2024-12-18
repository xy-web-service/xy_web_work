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
