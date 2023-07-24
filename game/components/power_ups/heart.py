from game.components.power_ups.power_up import PowerUp

from game.utils.constants import HEART_TYPE, HEART_RED

class Heart(PowerUp):
    def __init__(self):
        super().__init__(HEART_RED, HEART_TYPE)