from game.components.power_ups.power_up import PowerUp

from game.utils.constants import OBLIQUE, OBLIQUE_TYPE

class ObliqueMovement(PowerUp):
    def __init__(self):
        super().__init__(OBLIQUE, OBLIQUE_TYPE)