from target import TargetType
from cv import UIMatcher
import uiautomator2 as u2
import time
import random


class Automator:
    def __init__(self, device: str, targets: dict):
        """
        device: 如果是 USB 连接，则为 adb devices 的返回结果；如果是模拟器，则为模拟器的控制 URL 。
        """
        self.d = u2.connect(device)
        self.targets = targets

    def start(self):
        """
        启动脚本，请确保已进入游戏页面。
        """
        while True:
            # 判断是否出现货物。
            self._match_target()

            # 简单粗暴的方式，处理 “XX之光” 的荣誉显示。
            # 当然，也可以使用图像探测的模式。
            self.d.click(439, 1092)

            # 滑动屏幕，收割金币。
            # self._swipe()

    def _swipe(self):
        """
        滑动屏幕，收割金币。
        """
        for i in range(3):
            # 横向滑动，共 3 次。
            sx, sy = self._get_position(i * 3 + 1)
            ex, ey = self._get_position(i * 3 + 3)
            self.d.swipe(sx, sy, ex, ey)

    @staticmethod
    def _get_position(key):
        """
        获取指定建筑的屏幕位置。
        """
        positions = {
            1: (200, 800),
            2: (358, 711),
            3: (536, 627),
            4: (200, 628),
            5: (371, 544),
            6: (529, 454),
            7: (205, 462),
            8: (361, 391),
            9: (527, 307)
        }
        return positions.get(key)

    def _get_target_position(self, target: TargetType):
        """
        获取货物要移动到的屏幕位置。
        """
        return self._get_position(self.targets.get(target))

    def _match_target(self):
        """
        探测货物，并搬运货物。
        """
        for x in range(9):
            for j in range(3):
                # time.sleep(random.uniform(0.1, 0.3))
                sx, sy = self.positions_train.get(j + 1)
                ex, ey = self.positions_location.get(x + 1)
                self.d.swipe(sx, sy, ex, ey)

    positions_location = {
        1: (200, 790),
        2: (355, 705),
        3: (360, 620),
        4: (200, 620),
        5: (360, 540),
        6: (525, 450),
        7: (200, 460),
        8: (360, 350),
        9: (525, 260)
    }
    positions_train = {
        1: (440, 1105),
        2: (540, 1065),
        3: (640, 995)
    }
