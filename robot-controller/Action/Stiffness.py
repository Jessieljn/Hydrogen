from BaseAction import BaseAction


class Stiffness(BaseAction):
    def __init__(self, value):
        super(Stiffness, self).__init__()
        self._value = float(value)
    #END __init__()

    def execute(self, nao):
        nao.setStiffness(self._value)
    #END execute()

    def actionToString(self):
        return "Stiffness"
    #END actionToString()

    def paramToString(self):
        return str(self._value)
    #END paramToString()
#END class
