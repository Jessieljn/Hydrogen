from Definitions import Direction
from Action import Action


class HeadMotion(Action):
    def __init__(self, param):
        super(HeadMotion, self).__init__()
        self.parameter = param
    #END __init__()

    def execute(self, nao):
        if self.parameter == Direction.Up:
            nao.tiltHeadUp()
        elif self.parameter == Direction.Down:
            nao.tiltHeadDown()
        elif self.parameter == Direction.Left:
            nao.turnHeadLeft()
        elif self.parameter == Direction.Right:
            nao.turnHeadRight()
        else:
            pass
    #END execute()

    def actionToString(self):
        return "Head Motion"
    #END actionToString()

    def paramToString(self):
        if self.parameter == Direction.Up:
            return "Up"
        elif self.parameter == Direction.Down:
            return "Down"
        elif self.parameter == Direction.Left:
            return "Left"
        elif self.parameter == Direction.Right:
            return "Right"
        else:
            return "Neutral"
    #END paramToString()
#END class