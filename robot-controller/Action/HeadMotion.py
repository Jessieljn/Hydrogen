from Definitions import Direction
from BaseAction import BaseAction


class HeadMotion(BaseAction):
    def __init__(self, direction):
        super(HeadMotion, self).__init__()
        self._direction = direction
    #END __init__()

    def execute(self, nao):
        if self._direction == Direction.Up:
            nao.tiltHeadUp()
        elif self._direction == Direction.Down:
            nao.tiltHeadDown()
        elif self._direction == Direction.Left:
            nao.turnHeadLeft()
        elif self._direction == Direction.Right:
            nao.turnHeadRight()
        else:
            pass
        #END if
    #END execute()

    def actionToString(self):
        return "Head Motion"
    #END actionToString()

    def paramToString(self):
        if self._direction == Direction.Up:
            return "Up"
        elif self._direction == Direction.Down:
            return "Down"
        elif self._direction == Direction.Left:
            return "Left"
        elif self._direction == Direction.Right:
            return "Right"
        else:
            return "Neutral"
        #END if
    #END paramToString()
#END HeadMotion.py