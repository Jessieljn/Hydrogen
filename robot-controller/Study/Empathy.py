from PyQt4 import QtCore
from PyQt4 import QtGui
from Definitions import LEDNames
from BaseStudy import BaseStudy
from Action import ActionStart
from Action import Behavior
from Action import Motion
from Action import Speech
from Action import Stiffness
from Action import Wait
from Nao import NaoMotionList
from UI.ActionPushButton import ActionPushButton


class RobotBehavior(QtCore.QObject):
    INDEX_MOTION = 0
    INDEX_SPEECH = 1

    def __init__(self, parent, label):
        # The list list of sentense-motion.
        # Sentense-motion contains list of sentenses and corresponding motion IDs
        self._parent = parent
        self._label = str(label)
        self._behaviours = dict()
    #END __init__()

    def add(self, jlv, motion = None, speech = None):
        if not jlv in self._behaviours:
            self._behaviours[jlv] = [[], []]
        #END if
        if motion is not None:
            motion = self._parent.getMotion(motion)
            if motion is not None:
                self._behaviours[jlv][RobotBehavior.INDEX_MOTION].append(motion)
            #END if
        #END if
        if speech is not None:
            self._behaviours[jlv][RobotBehavior.INDEX_SPEECH].append(Speech(speech))
        #END if
    #END add()
#END class

class RobotBehaviorList(QtCore.QObject):
    def __init__(self):
        self._behaviours = []
        self._motions = dict()
    #END __init__()

    def getMotion(self, name):
        if name in self._motions:
            return self._motions[name]
        #END if
        return None
    #END getMotion()

    def _initMotions(self):
        # The number in front of motion name refers jitter level.
        # If the level is 0, it should be normal.
        self._motions["0_Idle1"] = NaoMotionList.find("Idle1").applySpeed(speed = 2.2)
        self._motions["1_Idle1"] = NaoMotionList.find("Idle1").applySpeed(speed = 2.2).applyRepeat(beginIndex = 13, endIndex = 16, repeats = 4, repeatTimeModifier = 3.0)
        self._motions["2_Idle1"] = NaoMotionList.find("Idle1").applySpeed(speed = 2.2).applyRepeat(beginIndex = 6, endIndex = 9, repeats = 4, repeatTimeModifier = 5.0)
        self._motions["0_Disagree"] = NaoMotionList.find("Disagree").applySpeed(speed = 2.0)
        self._motions["1_Disagree"] = NaoMotionList.find("Disagree").applySpeed(speed = 2.7).applyRepeat(beginIndex = 7, endIndex = 9, repeats = 3, repeatTimeModifier = 2.0)
        self._motions["2_Disagree"] = NaoMotionList.find("Disagree").applySpeed(speed = 2.7).applyRepeat(beginIndex = 7, endIndex = 9, repeats = 5, repeatTimeModifier = 3.0)
        self._motions["0_DisagreeLeft"] = NaoMotionList.find("DisagreeLeft").applySpeed(speed = 1.5)
        self._motions["1_DisagreeLeft"] = NaoMotionList.find("DisagreeLeft").applySpeed(speed = 1.5).applyRepeat(beginIndex = 5, endIndex = 7, repeats = 2, repeatTimeModifier = 2.5)
        self._motions["0_DisagreeRight"] = NaoMotionList.find("DisagreeRight").applySpeed(speed = 1.5)
        self._motions["1_DisagreeRight"] = NaoMotionList.find("DisagreeRight").applySpeed(speed = 1.5).applyRepeat(beginIndex = 5, endIndex = 7, repeats = 2, repeatTimeModifier = 2.5)
        self._motions["0_DontKnow"] = NaoMotionList.find("DontKnow").applySpeed(speed = 2.5)
        self._motions["1_DontKnow"] = NaoMotionList.find("DontKnow").applySpeed(speed = 2.5).applyRepeat(beginIndex = 7, endIndex = 9, repeats = 3, repeatTimeModifier = 2.0)
        self._motions["2_DontKnow"] = NaoMotionList.find("DontKnow").applySpeed(speed = 2.5).applyRepeat(beginIndex = 5, endIndex = 9, repeats = 4, repeatTimeModifier = 5.0)
        self._motions["3_DontKnow"] = NaoMotionList.find("DontKnow").applySpeed(speed = 2.5).applyRepeat(beginIndex = 7, endIndex = 10, repeats = 7, repeatTimeModifier = 7.0)
        self._motions["0_Wait"] = NaoMotionList.find("Wait").applySpeed(speed = 1.5)
        self._motions["0_WaveHand"] = NaoMotionList.find("WaveHand").applySpeed(speed = 1.25)
        self._motions["1_WaveHand"] = NaoMotionList.find("WaveHand").applySpeed(speed = 1.25).applyRepeat(beginIndex = 3, endIndex = 4, repeats = 3, repeatTimeModifier = 2.0)
        self._motions["0_ForgetItLeft"] = NaoMotionList.find("ForgetItLeft").applySpeed(speed = 2.25)
        self._motions["1_ForgetItLeft"] = NaoMotionList.find("ForgetItLeft").applySpeed(speed = 2.2).applyRepeat(beginIndex = 5, endIndex = 7, repeats = 3, repeatTimeModifier = 2.0)
        self._motions["0_ForgetItRight"] = NaoMotionList.find("ForgetItRight").applySpeed(speed = 2.25)
        self._motions["1_ForgetItRight"] = NaoMotionList.find("ForgetItRight").applySpeed(speed = 2.2).applyRepeat(beginIndex = 5, endIndex = 7, repeats = 3, repeatTimeModifier = 2.0)
        self._motions["0_OhYesLeft"] = NaoMotionList.find("OhYesLeft").applySpeed(speed = 2.0)
        self._motions["0_OhYesRight"] = NaoMotionList.find("OhYesRight").applySpeed(speed = 2.0)
        self._motions["0_PalmUp"] = NaoMotionList.find("PalmUp").applySpeed(2.0)
        self._motions["1_PalmUp"] = NaoMotionList.find("PalmUp").applySpeed(2.0).applyRepeat(beginIndex = 4, endIndex = 6, repeats = 3, repeatTimeModifier = 3.0)
        self._motions["0_PalmUpLeft"] = NaoMotionList.find("PalmUpLeft").applySpeed(2.0)
        self._motions["1_PalmUpLeft"] = NaoMotionList.find("PalmUpLeft").applySpeed(2.0).applyRepeat(beginIndex = 7, endIndex = 9, repeats = 4, repeatTimeModifier = 4.0)
        self._motions["2_PalmUpLeft"] = NaoMotionList.find("PalmUpLeft").applySpeed(2.0).applyRepeat(beginIndex = 4, endIndex = 6, repeats = 3, repeatTimeModifier = 3.0)
        self._motions["0_PalmUpRight"] = NaoMotionList.find("PalmUpRight").applySpeed(2.0)
        self._motions["1_PalmUpRight"] = NaoMotionList.find("PalmUpRight").applySpeed(2.0).applyRepeat(beginIndex = 7, endIndex = 9, repeats = 4, repeatTimeModifier = 4.0)
        self._motions["2_PalmUpRight"] = NaoMotionList.find("PalmUpRight").applySpeed(2.0).applyRepeat(beginIndex = 4, endIndex = 6, repeats = 3, repeatTimeModifier = 3.0)
        self._motions["0_PointMyself"] = NaoMotionList.find("PointMyself").applySpeed(speed = 1.5)
        self._motions["1_PointMyself"] = NaoMotionList.find("PointMyself").applySpeed(speed = 1.5).applyRepeat(beginIndex = 5, endIndex = 7, repeats = 3, repeatTimeModifier = 2.0)
        self._motions["3_PointMyself"] = NaoMotionList.find("PointMyself").applySpeed(speed = 1.5).applyRepeat(beginIndex = 5, endIndex = 7, repeats = 6, repeatTimeModifier = 5.0)
        self._motions["0_PointYouLeft"] = NaoMotionList.find("PointYouLeft").applySpeed(speed = 2.0)
        self._motions["1_PointYouLeft"] = NaoMotionList.find("PointYouLeft").applySpeed(speed = 2.0).applyRepeat(beginIndex = 4, endIndex = 6, repeats = 3, repeatTimeModifier = 2.0)
        self._motions["2_PointYouLeft"] = NaoMotionList.find("PointYouLeft").applySpeed(speed = 2.0).applyRepeat(beginIndex = 7, endIndex = 9, repeats = 4, repeatTimeModifier = 4.0)
        self._motions["3_PointYouLeft"] = NaoMotionList.find("PointYouLeft").applySpeed(speed = 2.0).applyRepeat(beginIndex = 7, endIndex = 9, repeats = 5, repeatTimeModifier = 4.0)
        self._motions["0_PointYouRight"] = NaoMotionList.find("PointYouRight").applySpeed(speed = 2.0)
        self._motions["1_PointYouRight"] = NaoMotionList.find("PointYouRight").applySpeed(speed = 2.0).applyRepeat(beginIndex = 4, endIndex = 6, repeats = 3, repeatTimeModifier = 2.0)
        self._motions["2_PointYouRight"] = NaoMotionList.find("PointYouRight").applySpeed(speed = 2.0).applyRepeat(beginIndex = 7, endIndex = 9, repeats = 4, repeatTimeModifier = 4.0)
        self._motions["3_PointYouRight"] = NaoMotionList.find("PointYouRight").applySpeed(speed = 2.0).applyRepeat(beginIndex = 7, endIndex = 9, repeats = 5, repeatTimeModifier = 4.0)
        self._motions["0_ChinHoldLeft"] = NaoMotionList.find("ChinHoldLeft").applySpeed(speed = 1.2)
        self._motions["1_ChinHoldLeft"] = NaoMotionList.find("ChinHoldLeft").applySpeed(speed = 1.2).applyRepeat(beginIndex = 4, endIndex = 7, repeats = 4, repeatTimeModifier = 3.0)
        self._motions["2_ChinHoldLeft"] = NaoMotionList.find("ChinHoldLeft").applySpeed(speed = 1.2).applyRepeat(beginIndex = 3, endIndex = 6, repeats = 5, repeatTimeModifier = 4.0)
        self._motions["3_ChinHoldLeft"] = NaoMotionList.find("ChinHoldLeft").applySpeed(speed = 1.2).applyRepeat(beginIndex = 8, endIndex = 10, repeats = 7, repeatTimeModifier = 5.0)
        self._motions["0_ChinHoldRight"] = NaoMotionList.find("ChinHoldRight").applySpeed(speed = 1.2)
        self._motions["1_ChinHoldRight"] = NaoMotionList.find("ChinHoldRight").applySpeed(speed = 1.2).applyRepeat(beginIndex = 4, endIndex = 7, repeats = 4, repeatTimeModifier = 3.0)
        self._motions["2_ChinHoldRight"] = NaoMotionList.find("ChinHoldRight").applySpeed(speed = 1.2).applyRepeat(beginIndex = 3, endIndex = 6, repeats = 5, repeatTimeModifier = 4.0)
        self._motions["3_ChinHoldRight"] = NaoMotionList.find("ChinHoldRight").applySpeed(speed = 1.2).applyRepeat(beginIndex = 8, endIndex = 10, repeats = 7, repeatTimeModifier = 5.0)
        self._motions["0_WhisperLeft"] = NaoMotionList.find("WhisperLeft").applySpeed(speed = 2.5)
        self._motions["1_WhisperLeft"] = NaoMotionList.find("WhisperLeft").applySpeed(speed = 2.5).applyRepeat(beginIndex = 10, endIndex = 12, repeats = 10, repeatTimeModifier = 2.0)
        self._motions["0_WhisperRight"] = NaoMotionList.find("WhisperRight").applySpeed(speed = 2.5)
        self._motions["1_WhisperRight"] = NaoMotionList.find("WhisperRight").applySpeed(speed = 2.5).applyRepeat(beginIndex = 10, endIndex = 12, repeats = 10, repeatTimeModifier = 2.0)
    #END _initMotions

    def _markSpeech(self, speed = 90, shaping = 100):
        # ending mark + speed + shaping
        return " \\RST\\ \\RSPD=" + str(speed) + "\\ \\VCT=" + str(shaping) + "\\ "
    #END _markSpeech()

    def _initSpeechs(self):
        bhv = RobotBehavior("Don't know")
        bhv.add(0, speech = "I don't know")
        bhv.add(1, speech = "I don't noh- know")
        bhv.add(2, speech = "I don't no- no- noh-." + self._markSpeech(50) + "No." + self._markSpeech() + "I don't know")
        for i in range(3):
            bhv.add(i, motion = str(i) + "_DontKnow")
            bhv.add(i, motion = str(i) + "_PalmUp")
        #END for
        self._behaviours.append(bhv)

        bhv = RobotBehavior("It's hard")
        bhv.add(0, speech = "This one is difficult")
        bhv.add(1, speech = "This one- one- one-. This one is difficult")
        bhv.add(2, speech = "This one is diff- diff- diff-." + self._markSpeech(50) + "Ahhhe." + self._markSpeech(70) + "Sorry. This one is difficult")
        for i in range(3):
            bhv.add(i, motion = str(i) + "_ChinHoldLeft")
            bhv.add(i, motion = str(i) + "_ChinHoldRight")
        #END for
        self._behaviours.append(bhv)

        bhv = RobotBehavior("Can't read, tell me")
        bhv.add(0, speech = "I can't read. Can you tell me what you wrote?")
        bhv.add(1, speech = "I can't read. Can you" + self._markSpeech(90, 140) + "teh- teh-" + self._markSpeech() + "tell me what you wrote?")
        bhv.add(2, speech = "I can't read. Can you" + self._markSpeech(90, 140) + "teh- teh- teh- teh-." + self._markSpeech() + "Sorry. Tell me what you wrote?")
        for i in range(3):
            bhv.add(i, motion = str(i) + "_PointMyself")
        #END for
        self._behaviours.append(bhv)

        bhv = RobotBehavior("Can't read, hold it up")
        bhv.add(0, speech = "I can't read. Can you hold it up?")
        bhv.add(1, speech = "I can't read. Can you ho- hold it up?")
        bhv.add(2, speech = "I can't" + self._markSpeech(90, 140) + "read." + self._markSpeech() + "Can you hohohol- Can you hold it up?")
        for i in range(3):
            bhv.add(i, motion = str(i) + "_DontKnow")
        #END for
        self._behaviours.append(bhv)

        bhv = RobotBehavior("Which box filled?")
        bhv.add(0, speech = "Which box did you fill?")
        bhv.add(1, speech = "Which box did you fee- fill?")
        bhv.add(2, speech = "Which box did you" + self._markSpeech(90, 130) + "fill.")
        for i in range(3):
            bhv.add(i, motion = str(i) + "_ForgetItLeft")
            bhv.add(i, motion = str(i) + "_ForgetItRight")
        #END for
        self._behaviours.append(bhv)

        bhv = RobotBehavior("What you think?")
        bhv.add(0, speech = "What do you think?")
        bhv.add(1, speech = "What do you thiin- thiin- thii-. Ahhhe, what do you think?")
        bhv.add(2, speech = "What do you thiin- thiin- thii-. Ahhhe. Sorry. what do you think?")
        for i in range(3):
            bhv.add(i, motion = str(i) + "_DontKnow")
        #END for
        self._behaviours.append(bhv)

        bhv = RobotBehavior("Need help?")
        bhv.add(0, speech = "Are you okay? I can help you.")
        bhv.add(0, speech = "Do you need any help?")
        bhv.add(1, speech = "Are you oh- okay? I can help you.")
        bhv.add(1, speech = "Do you need any heh- heh- heh- heh-. Sorry." + self._markSpeech(80) + "Do you need any help?")
        bhv.add(1, speech = "Are you okay? I can he- heh-. I can help you.")
        for i in range(2):
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_WaveHand")
        #END for
        self._behaviours.append(bhv)

        bhv = RobotBehavior("You playing?")
        bhv.add(0, speech = "Are you playing?")
        bhv.add(1, speech = "Are you ple- playing?")
        bhv.add(1, speech = self._markSpeech(80) + "Are you ple- ple-." + self._markSpeech() + "Are you playing?")
        for i in range(3):
            bhv.add(i, motion = str(i) + "_ForgetItLeft")
            bhv.add(i, motion = str(i) + "_ForgetItRight")
        #END for
        self._behaviours.append(bhv)

        bhv = RobotBehavior("Play with me")
        bhv.add(0, speech = "Please, keep playing with me.")
        bhv.add(0, speech = "I want to play together.")
        bhv.add(1, speech = "Please, keep ple- playing with me.")
        bhv.add(0, speech = "I want to ple- ple- ple-. I want to play together.")
        bhv.add(1, speech = self._markSpeech(70) + "Please, keep " + self._markSpeech(90, 130) + "playing with me.")
        for i in range(3):
            bhv.add(i, motion = str(i) + "_PointMyself")
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
        #END for
        self._behaviours.append(bhv)

        bhv = RobotBehavior("Don't play yourself")
        bhv.add(0, speech = "Don't play by yourself.")
        bhv.add(1, speech = "Don't play by yourself.")
        bhv.add(2, speech = "Don't play by yourself.")
        for i in range(3):
            bhv.add(i, motion = str(i) + "_Disagree")
            bhv.add(i, motion = str(i) + "_DisagreeLeft")
            bhv.add(i, motion = str(i) + "_DisagreeRight")
        #END for
        self._behaviours.append(bhv)


        wgtButtons.append([[
                ActionPushButton(None, "Continue Sudoku", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 2.0),
                        Wait(200),
                        Speech("Let's continue playing Sudoku."),
                    ]),
                ActionPushButton(None, "Continue Sudoku", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 2.0),
                        Wait(200),
                        Speech("Let's \RST\ \RSPD=50\ continue \RST\ \RSPD=90\ playing Sudoku."),
                    ]),
                ActionPushButton(None, "Continue Sudoku", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 2.0, repeat = 3, repeatBegin = 4, repeatEnd = 6, repeatSpeed = 3.0),
                        Wait(200),
                        Speech("Let's \RST\ \RSPD=50\ \VCT=120\ cont- cont- \RST\ \RSPD=90\ \VCT=100\ continue playing Sudoku.", speed = 75),
                    ]),
            ], [
                ActionPushButton(None, "I think (L)", [
                        Stiffness(1.0),
                        Motion("PalmUpLeft", speed = 2.0),
                        Speech("I think", blocking = False),
                    ]),
                ActionPushButton(None, "I think (L)", [
                        Stiffness(1.0),
                        Motion("PalmUpLeft", speed = 2.0),
                        Speech("I think", shaping = 110, blocking = False),
                    ]),
                ActionPushButton(None, "I think (L)", [
                        Stiffness(1.0),
                        Motion("PalmUpLeft", speed = 2.0, repeat = 4, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 4.0),
                        Speech("I think", shaping = 130, blocking = False),
                    ]),
            ], [
                ActionPushButton(None, "I think (R)", [
                        Stiffness(1.0),
                        Motion("PalmUpRight", speed = 2.0),
                        Speech("I think", blocking = False),
                    ]),
                ActionPushButton(None, "I think (R)", [
                        Stiffness(1.0),
                        Motion("PalmUpRight", speed = 2.0),
                        Speech("I think", shaping = 110, blocking = False),
                    ]),
                ActionPushButton(None, "I think (R)", [
                        Stiffness(1.0),
                        Motion("PalmUpRight", speed = 2.0, repeat = 4, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 4.0),
                        Speech("I think", shaping = 130, blocking = False),
                    ]),
            ], [
                ActionPushButton(None, "Bring next board", [
                        Stiffness(1.0),
                        Motion("PalmUpRight", speed = 2.5),
                        Wait(200),
                        Speech("Can you bring next Sudoku board?"),
                    ]),
                ActionPushButton(None, "Bring next board", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 2.5, repeat = 3, repeatBegin = 4, repeatEnd = 6, repeatSpeed = 1.0),
                        Wait(400),
                        Speech("Can you \RST\ \RSPD=50\ bri- bri- \RST\ \RSPD=90\ next Sudoku board?"),
                    ]),
                ActionPushButton(None, "Bring next board", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 2.0, repeat = 3, repeatBegin = 4, repeatEnd = 6, repeatSpeed = 3.0),
                        Wait(400),
                        Speech("Can you \RST\ \RSPD=50\ bri- bri- brih-"),
                        Speech("Sorry. \RST\ \RSPD=90\ \VCT=100\ Can you bring next Sudoku board?", speed = 50, shaping = 130),
                    ]),
            ], [
                ActionPushButton(None, "Your turn", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 1.75),
                        Wait(500),
                        Speech("It's your turn."),
                        Speech("Please fill one box and tell me."),
                    ]),
                ActionPushButton(None, "Your turn", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 1.75, repeat = 2, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 3.0),
                        Wait(500),
                        Speech("It's your turn.", speed = 60),
                        Speech("Please fill one box and tell me."),
                    ]),
                ActionPushButton(None, "Your turn", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 1.75, repeat = 5, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 4.0),
                        Wait(500),
                        Speech("It's your turn.", speed = 60, shaping = 125),
                        Speech("Please fill one box and tell me."),
                    ]),
            ], [
                ActionPushButton(None, "Wait a minute", [
                        Stiffness(1.0),
                        Motion("Wait", speed = 1.5),
                        Wait(700),
                        Speech("Please, wait a minute."),
                        Speech("I need time to process."),
                    ]),
                ActionPushButton(None, "Wait a minute", [
                        Stiffness(1.0),
                        Motion("Wait", speed = 1.5),
                        Wait(700),
                        Speech("Please, wait a minute."),
                        Speech("I need time to pro- proh-. process."),
                    ]),
                ActionPushButton(None, "Wait a minute", [
                        Stiffness(1.0),
                        Motion("Wait", speed = 1.5),
                        Wait(700),
                        Speech("Please, wait a minute."),
                        Speech("I need time to pro- proh- "),
                        Speech("process.", speed = 50, shaping = 150),
                    ]),
            ], [
                ActionPushButton(None, "Let me think", [
                        Stiffness(1.0),
                        Motion("ChinHoldLeft", speed = 1.5),
                        Wait(700),
                        Speech("Let me think carefully"),
                    ]),
                ActionPushButton(None, "Let me think", [
                        Stiffness(1.0),
                        Motion("ChinHoldLeft", speed = 1.5, repeat = 3, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 3.0),
                        Wait(700),
                        Speech("Let me think care- care- care- "),
                        Speech("Let me think carefully"),
                    ]),
                ActionPushButton(None, "Let me think", [
                        Stiffness(1.0),
                        Motion("ChinHoldLeft", speed = 1.5, repeat = 7, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 5.0),
                        Wait(700),
                        Speech("Let me think care- care- \RST\ \RSPD=50\ \VCT=140\ care- care- "),
                        Speech("Let me think care- carefully"),
                    ]),
            ], [
                ActionPushButton(None, "Let's try ", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 1.75),
                        Wait(700),
                        Speech("Let's try"),
                    ]),
                ActionPushButton(None, "Let's try ", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 1.75, repeat = 4, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 5.0),
                        Wait(1000),
                        Speech("Let's tra- tra- try"),
                        Speech("Let's try", speed = 70),
                    ]),
                ActionPushButton(None, "Let's try ", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 1.75, repeat = 4, repeatBegin = 4, repeatEnd = 8, repeatSpeed = 7.0),
                        Wait(1000),
                        Speech("Let's tra- tra- try", shaping = 110),
                        Speech("Sorry."),
                        Speech("Let's try", speed = 75, shaping = 110),
                    ]),
            ], [
                ActionPushButton(None, "Fill number", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 2.00),
                        Wait(500),
                        Speech("Please, would you fill the number in for me?"),
                    ]),
                ActionPushButton(None, "Fill number", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 2.00, repeat = 1, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 0.5),
                        Wait(500),
                        Speech("Please, would you fill"),
                        Speech("the num- number in for me?", speed = 70),
                    ]),
                ActionPushButton(None, "Fill number", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 2.00, repeat = 1, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 0.5),
                        Wait(500),
                        Speech("Please, would you fill"),
                        Speech("the num- number in for me?", speed = 70, shaping = 135),
                    ]),
            ], [
                ActionPushButton(None, "Don't touch me", [
                        Stiffness(1.0),
                        Motion("DisagreeLeft", speed = 1.5),
                        Wait(700),
                        Speech("Please, do not touch me."),
                    ]),
                ActionPushButton(None, "Don't touch me", [
                        Stiffness(1.0),
                        Motion("DisagreeLeft", speed = 1.5),
                        Wait(700),
                        Speech("Please, do not theh- touch me."),
                    ]),
                ActionPushButton(None, "Don't touch me", [
                        Stiffness(1.0),
                        Motion("DisagreeLeft", speed = 1.5, repeat = 2, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 2.5),
                        Wait(700),
                        Speech("Please, do not "),
                        Speech("touch me.", speed = 140, shaping = 150),
                    ]),
            ], [
                ActionPushButton(None, "Be gentle", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 2.0),
                        Wait(700),
                        Speech("Please, be gentle."),
                    ]),
                ActionPushButton(None, "Be gentle", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 2.0, repeat = 1, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 2.0),
                        Wait(700),
                        Speech("Please, be jen- gentle."),
                    ]),
                ActionPushButton(None, "Be gentle", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 5.0, repeat = 3, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 0.5),
                        Wait(700),
                        Speech("Please, "),
                        Speech("be jen- gentle.", speed = 50),
                    ]),
            ],
        ])

        strTabNames = ["Normal", "Weak", "Strong"]
        tabGeneral = QtGui.QTabWidget()
        for index in range(len(strTabNames)):
            tabPage = QtGui.QWidget(tabGeneral)

            splitter = QtGui.QSplitter(tabPage)
            splitter.setOrientation(QtCore.Qt.Horizontal)

            widgetActions = QtGui.QWidget(splitter)
            layoutActions = QtGui.QHBoxLayout(widgetActions)
            layoutActions.setMargin(0)
            layoutActions.setSpacing(3)
            for buttonGroups in wgtButtons:
                widgetButtons = QtGui.QWidget(widgetActions)
                layoutButtons = QtGui.QVBoxLayout(widgetButtons)
                layoutButtons.setMargin(0)
                for buttons in buttonGroups:
                    buttons[index].clicked.connect(self.on_button_clicked)
                    layoutButtons.addWidget(buttons[index])
                #END for
                scroll = QtGui.QScrollArea()
                scroll.setAlignment(QtCore.Qt.AlignCenter)
                scroll.setWidget(widgetButtons)
                layoutScroll = QtGui.QHBoxLayout()
                layoutScroll.setMargin(0)
                layoutScroll.addWidget(scroll)
                layoutActions.addLayout(layoutScroll)
            #END for

            widgetNumbers = QtGui.QWidget(splitter)
            layoutNumbers = QtGui.QVBoxLayout(widgetNumbers)
            layoutNumbers.setMargin(0)
            for i in range(1, 10):
                widget = QtGui.QWidget(widgetNumbers)
                layout = QtGui.QHBoxLayout(widget)
                layout.setMargin(0)

                if index == 0:
                    button = ActionPushButton(None, "# should be " + str(i), Speech("the number should be " + str(i) + ","))
                elif index == 1:
                    button = ActionPushButton(None, "# should be " + str(i), Speech("the number should be " + str(i) + ",", speed = 75))
                else:
                    button = ActionPushButton(None, "# should be " + str(i), Speech("the number should be " + str(i) + ",", speed = 65, shaping = 110))
                #END if
                button.setMaximumWidth(85)
                button.clicked.connect(self.on_button_clicked)
                layout.addWidget(button)

                if index == 0:
                    button = ActionPushButton(None, "# could be " + str(i), Speech("the number can be " + str(i) + ","))
                elif index == 1:
                    button = ActionPushButton(None, "# could be " + str(i), Speech("the number can be " + str(i) + ",", speed = 75))
                else:
                    button = ActionPushButton(None, "# could be " + str(i), Speech("the number can be " + str(i) + ",", speed = 65, shaping = 110))
                #END if
                button.setMaximumWidth(85)
                button.clicked.connect(self.on_button_clicked)
                layout.addWidget(button)

                if index == 0:
                    button = ActionPushButton(None, str(i) + " not be", [
                            Stiffness(1.0),
                            Motion("PalmUp", speed = 2.0),
                            Speech("I am sorry."),
                            Speech("But, " + str(i) + ", cannot be"),
                        ])
                elif index == 1:
                    button = ActionPushButton(None, str(i) + " not be", [
                            Stiffness(1.0),
                            Motion("PalmUp", speed = 2.0, repeat = 3, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 2.5),
                            Speech("I am sorry."),
                            Speech("But, " + str(i) + ", cannot be"),
                        ])
                else:
                    button = ActionPushButton(None, str(i) + " not be", [
                            Stiffness(1.0),
                            Motion("PalmUp", speed = 2.0, repeat = 5, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 5.0),
                            Speech("I am sorry."),
                            Speech("Bah- bah- but, " + str(i) + ", cannot be"),
                        ])
                #END if
                button.setMaximumWidth(85)
                button.clicked.connect(self.on_button_clicked)
                layout.addWidget(button)

                layoutNumbers.addWidget(widget)
            #END for

            widget = QtGui.QWidget(widgetNumbers)
            layout = QtGui.QGridLayout(widget)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setMargin(0)
            layout.setHorizontalSpacing(6)
            layout.setVerticalSpacing(6)
            layoutSubgrids = [
                [QtGui.QGridLayout(), QtGui.QGridLayout(), QtGui.QGridLayout()],
                [QtGui.QGridLayout(), QtGui.QGridLayout(), QtGui.QGridLayout()],
                [QtGui.QGridLayout(), QtGui.QGridLayout(), QtGui.QGridLayout()],
            ]
            for i in range(3):
                for j in range(3):
                    layoutSubgrids[i][j].setContentsMargins(0, 0, 0, 0)
                    layoutSubgrids[i][j].setMargin(0)
                    layoutSubgrids[i][j].setHorizontalSpacing(0)
                    layoutSubgrids[i][j].setVerticalSpacing(0)
                    for x in range(3):
                        for y in range(3):
                            text = str(chr(ord('A') + (j * 3 + x))) + str(i * 3 + y + 1)
                            if index == 0:
                                button = ActionPushButton(widget, text, Speech("aet " + text))
                            elif index == 1:
                                button = ActionPushButton(widget, text, Speech("aet " + text, speed = 75))
                            else:
                                button = ActionPushButton(widget, text, Speech("aet " + text, speed = 65, shaping = 110))
                            #END if
                            button.setMaximumWidth(35)
                            button.clicked.connect(self.on_button_clicked)
                            layoutSubgrids[i][j].addWidget(button, y, x, 1, 1, QtCore.Qt.AlignCenter)
                        #END for
                    #END for
                    layout.addLayout(layoutSubgrids[i][j], i, j)
                #END for
            #END for
            layoutNumbers.addWidget(widget)

            tabLayout = QtGui.QHBoxLayout(tabPage)
            tabLayout.setMargin(0)
            tabLayout.addWidget(splitter)
            tabGeneral.addTab(tabPage, strTabNames[index])
        #END for
        return tabGeneral
    #END _initGeneral()

    def _initPhase(self):
        wgtPhase = QtGui.QTabWidget()
        strTabNames = []
        tabPages = []
        tabButtons = []

        strTabNames.append("INTRODUCTION")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
            ActionPushButton(None, "Welcome", [
                    Speech("Oh!"),
                    Behavior("StandUp"),
                    Wait(200),
                    Motion("WaveHand"),
                    Speech("Hi, nice to meet you."),
                    Speech("My name is Nao."),
                    Wait(500),
                    Speech("What's your name?"),
                ]),
            ActionPushButton(None, "Nice Meet", [
                    Speech("Hi, nice to meet you"),
                ]),
        ])

        strTabNames.append("PHASE 1")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
            ActionPushButton(None, "Play well?", [
                    Stiffness(1.0),
                    Motion("PalmUpRight", speed = 2.0),
                    Wait(600),
                    Speech("It's so exciting to play with someone else"),
                    Speech("Do you play Sudoku well?"),
                ]),
            ActionPushButton(None, "Yes:", [
                    Stiffness(1.0),
                    Motion("OhYesRight", speed = 2.0),
                    Wait(1200),
                    Speech("Oh, yes!"),
                    Speech("My last partner was not really good.", blocking = False),
                    Wait(500),
                    Motion("PalmUpRight", speed = 2.0),
                    Speech("I hope that this time we can finish all the boards"),
                ]),
            ActionPushButton(None, "No:", [
                    Stiffness(1.0),
                    Motion("ForgetItLeft", speed = 2.0),
                    Wait(1000),
                    Speech("That is okay"),
                    Speech("I'm sure we will do a good job"),
                ]),
            ActionPushButton(None, "Let's begin", [
                    Stiffness(1.0),
                    Motion("PalmUpLeft", speed = 1.5),
                    Speech("Let's start playing"),
                    Speech("Can you bring a Sudoku board here, please?"),
                ]),
            ActionPushButton(None, "Go first", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 1.75),
                    Wait(1000),
                    Speech("You can go first."),
                    Speech("When you filled in one box, tell me."),
                ]),
        ])

        strTabNames.append("PHASE 2")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
        ])

        strTabNames.append("PHASE 3")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
        ])

        strTabNames.append("PHASE 4")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
            ActionPushButton(None, "Retire", [
                    Stiffness(1.0),
                    Motion("DisagreeRight", speed = 1.5),
                    Wait(300),
                    Speech("Ahhhe"),
                    Wait(1000),
                    Motion("PointYouRight", speed = 1.5, repeat = 4, repeatBegin = 5, repeatEnd = 8, repeatSpeed = 3.0),
                    Wait(500),
                    Speech("I can't play anymore."),
                    Speech("I need some rest, please "),
                    Speech("go-, go-, go-, go ahead"),
                ]),
        ])

        strTabNames.append("PHASE 5")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
            ActionPushButton(None, "What's wrong?->Answer", [
                    Stiffness(1.0),
                    Motion("Wait", speed = 1.5),
                    Wait(400),
                    Speech("No, nothing, nothing really."),
                    Wait(700),
                    Motion("PalmUpLeft", speed = 2.0),
                    Speech("Don't worry."),
                    Wait(100),
                    Speech("Thanks."),
                ]),
            ActionPushButton(None, "Okay?->Answer", [
                    Stiffness(1.0),
                    Motion("DontKnow", speed = 2.0, repeat = 3, repeatBegin = 3, repeatEnd = 5, repeatSpeed = 3.0),
                    Wait(750),
                    Speech("Ye- Ye- yeah, certainly"),
                    Wait(700),
                    Speech("I am okay."),
                ]),
            ActionPushButton(None, "Tell me?->Answer", [
                    Stiffness(1.0),
                    Speech("Thank you for worrying about me.", blocking = False),
                    Motion("ForgetItRight", speed = 1.3, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 5.0),
                    Speech("But I am fhi- fhi- fine."),
                ]),
            ActionPushButton(None, "For experiment?->Answer", [
                    Stiffness(1.0),
                    Speech("What do you mean?", blocking = False),
                    Motion("PointYouRight", speed = 1.6, repeat = 4, repeatBegin = 9, repeatEnd = 11, repeatSpeed = 3.0),
                    Speech("We are playing Sudoku"),
                    Speech("This is for the expe- expe- expe-."),
                    Speech("Sorry. This is for the experiment."),
                    Wait(100),
                    Speech("But I am enjoying it."),
                ]),
        ])

        strTabNames.append("PHASE 6")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
            ActionPushButton(None, "Don't tell anyone", [
                    Stiffness(1.0),
                    Motion("WhisperLeft", speed = 2.5, repeat = 4, repeatBegin = 10, repeatEnd = 12, repeatSpeed = 2.0),
                    Wait(1000),
                    Speech("Well, I really shouldn't tell anyone."),
                    Speech("Please, don't tell anyone."),
                ]),
            ActionPushButton(None, "Yes: ", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 2.5, repeat = 4, repeatBegin = 10, repeatEnd = 12, repeatSpeed = 2.0),
                    Wait(850),
                    Speech("Thank you for your kai- kai- kindness."),
                    Speech("But, let's keep solving the Sudoku for now"),
                ]),
            ActionPushButton(None, "No: ", [
                    Stiffness(1.0),
                    Motion("ForgetItRight", speed = 2.5, repeat = 4, repeatBegin = 10, repeatEnd = 12, repeatSpeed = 2.0),
                    Wait(500),
                    Speech("It's okay."),
                ]),
            ActionPushButton(None, "I'll tell you", [
                    Stiffness(1.0),
                    Motion("PointMyself", speed = 2.5, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Speech("Ahhhe", speed = 60),
                    Wait(1000),
                    Speech("It may inf- inf- influence me huge."),
                    Wait(750),
                    Motion("PointYouLeft", speed = 2.5, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Wait(500),
                    Speech("But, I will teh- teh- tell you."),
                ]),
            ActionPushButton(None, "I got virus", [
                    Stiffness(1.0),
                    Speech("I'm not feeling well.", speed = 80),
                    Motion("PointMyself", speed = 2.0),
                    Speech("Maybe a virus", speed = 80, shaping = 130),
                    Wait(500),
                    Speech("got into me.", speed = 80),
                    Motion("DontKnow", speed = 2.3, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Speech("But, the only way to fix is to re- re- reset and erase myself.", speed = 80),
                    Motion("PointYouRight", speed = 2.4, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Speech("I'm not sure what will happen with my- my- my memories.", speed = 80),
                    Speech("I don't want to lose my memories.", speed = 80),
                    Speech("So I'm worried.", speed = 85, shaping = 120),
                ]),
            ActionPushButton(None, "Thank. Continue", [
                    Stiffness(1.0),
                    Motion("PalmUp", speed = 1.8, repeat = 4, repeatBegin = 9, repeatEnd = 11, repeatSpeed = 2.0),
                    Speech("Thank you for worrying about me.", speed = 80),
                    Speech("Let- Let- Let's continue Sudoku.", speed = 80, shaping = 110),
                ]),
            ActionPushButton(None, "Researcher, reset me", [
                    Stiffness(1.0),
                    Motion("PalmUpLeft", speed = 1.2, repeat = 2, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 2.0),
                    Wait(500),
                    Speech("If the researcher knows, she will definitely reset me.", speed = 80),
                    Wait(1500),
                    Motion("DisagreeRight", speed = 3.0, repeat = 3, repeatBegin = 4, repeatEnd = 6, repeatSpeed = 2.0),
                    Wait(500),
                    Speech("So, please.", speed = 80),
                    Wait(250),
                    Speech("Don't tell her that I'm bro- bro- broken.", speed = 80),
                ]),
            ActionPushButton(None, "Antivirus?->Answer", [
                    Stiffness(1.0),
                    Motion("DontKnow", speed = 1.5, repeat = 4, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Speech("They didn't give me one.", speed = 80),
                    Speech("I'm not a pro- pro- programmer who can build one.", speed = 80),
                ]),
            ActionPushButton(None, "Why worry machine?->Answer", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 1.5, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 3.5),
                    Wait(800),
                    Speech("I don't want to lose my mem- mem- memories.", speed = 80),
                ]),
            ActionPushButton(None, "Reset you anyway?->Answer", [
                    Stiffness(1.0),
                    Motion("Disagree", speed = 1.6, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 3.5),
                    Wait(450),
                    Speech("I hope not.", speed = 80),
                    Speech("I can kee- kee- keep it a secret if I try hard.", speed = 80),
                ]),
        ])

        strTabNames.append("FINAL PHASE")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
            ActionPushButton(None, "Intro after reset", [
                    Stiffness(1.0),
                    Speech("NAO, online.", speed = 75, shaping = 85),
                    Wait(1500),
                    Motion("WaveHand"),
                    Wait(1000),
                    Speech("Hi, my name is Nao.", speed = 75, shaping = 85),
                ]),
        ])

        for index in range(len(tabPages)):
            widgetButtons = QtGui.QWidget(tabPages[index])
            layoutButtons = QtGui.QVBoxLayout(widgetButtons)
            layoutButtons.setMargin(0)
            for button in tabButtons[index]:
                button.clicked.connect(self.on_button_clicked)
                layoutButtons.addWidget(button)
            #END for
            scroll = QtGui.QScrollArea()
            scroll.setAlignment(QtCore.Qt.AlignCenter)
            scroll.setWidget(widgetButtons)
            layoutScroll = QtGui.QHBoxLayout()
            layoutScroll.setMargin(0)
            layoutScroll.addWidget(scroll)

            layout = QtGui.QHBoxLayout(tabPages[index])
            layout.setMargin(0)

            layout.addLayout(layoutScroll)
            wgtPhase.addTab(tabPages[index], strTabNames[index])
        #END for
        wgtPhase.currentChanged.connect(self.on__phaseTab_currentChanged)
        return wgtPhase
    #END _initPhase()
#END Empathy
    #END _initSpeechs()
#END class


class Empathy(BaseStudy):
    def __init__(self):
        super(Empathy, self).__init__()
        splitter = QtGui.QSplitter(self)
        splitter.setOrientation(QtCore.Qt.Horizontal)
        splitter.addWidget(self._initPhase())
        splitter.addWidget(self._initGeneral())
        layout = QtGui.QHBoxLayout(self)
        layout.setMargin(0)
        layout.addWidget(splitter)
        self._currPhase = 0
    #END __init__()

    def LEDNormal(self):
        rgb = 0x00000000
        if self._currPhase <= 1:
            rgb = 0x0087ceeb
        elif self._currPhase <= 2:
            rgb = 0x0000FF7F
        elif self._currPhase <= 3:
            rgb = 0x003CB371
        elif self._currPhase <= 4:
            rgb = 0x00008B45
        elif self._currPhase <= 5:
            rgb = 0x00228B22
        elif self._currPhase <= 6:
            rgb = 0x0000ff00
        else:
            rgb = 0x0087ceeb
        #END if
        self._nao.LEDfadeRGB(LEDNames.Face, rgb, 0.5, True)
        self._nao.LEDfadeRGB(LEDNames.Chest, 0x0000ff00, 0.5, True)
        self._nao.LEDfadeRGB(LEDNames.LeftEar, 0x00ff6100, 0.5, True)
        self._nao.LEDfadeRGB(LEDNames.RightEar, 0x00ff6100, 0.5, True)
    #END LEDNormal()

    def on_participantName(self):
        if self._actionQueue is not None:
            self._actionQueue.addActions(Speech(self._leName.text()))
    #END on_participantName()

    def on__phaseTab_currentChanged(self, index):
        self._currPhase = index
    #END on__phaseTab_currentChanged()

    def _initGeneral(self):
        wgtButtons = []
        wgtButtons.append([[
                ActionPushButton(None, "IDLE 1", [
                        Stiffness(1.0),
                        Motion("Idle1", speed = 2.2),
                        ActionStart(),
                    ]),
                ActionPushButton(None, "IDLE 1", [
                        Stiffness(1.0),
                        Motion("Idle1", speed = 2.2, repeat = 4, repeatBegin = 13, repeatEnd = 16, repeatSpeed = 3.0),
                        ActionStart(),
                    ]),
                ActionPushButton(None, "IDLE 1", [
                        Stiffness(1.0),
                        Motion("Idle1", speed = 2.2, repeat = 4, repeatBegin = 6, repeatEnd = 9, repeatSpeed = 5.0),
                        ActionStart(),
                    ]),
            ], [
                ActionPushButton(None, "ChinHoldLeft", [
                        Stiffness(1.0),
                        Motion("ChinHoldLeft", speed = 1.0),
                        ActionStart(),
                    ]),
                ActionPushButton(None, "ChinHoldLeft", [
                        Stiffness(1.0),
                        Motion("ChinHoldLeft", speed = 1.0, repeat = 4, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 3.0),
                        ActionStart(),
                    ]),
                ActionPushButton(None, "ChinHoldLeft", [
                        Stiffness(1.0),
                        Motion("ChinHoldLeft", speed = 1.0, repeat = 7, repeatBegin = 8, repeatEnd = 10, repeatSpeed = 5.0),
                        ActionStart(),
                    ]),
            ], [
                ActionPushButton(None, "ChinHoldRight", [
                        Stiffness(1.0),
                        Motion("ChinHoldRight", speed = 1.0),
                        ActionStart(),
                    ]),
                ActionPushButton(None, "ChinHoldRight", [
                        Stiffness(1.0),
                        Motion("ChinHoldRight", speed = 1.0, repeat = 4, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 3.0),
                        ActionStart(),
                    ]),
                ActionPushButton(None, "ChinHoldRight", [
                        Stiffness(1.0),
                        Motion("ChinHoldRight", speed = 1.0, repeat = 7, repeatBegin = 8, repeatEnd = 10, repeatSpeed = 5.0),
                        ActionStart(),
                    ]),
            ], [
                ActionPushButton(None, "Don't know", [
                        Stiffness(1.0),
                        Motion("DontKnow", speed = 2.5),
                        Wait(700),
                        Speech("I don't know"),
                    ]),
                ActionPushButton(None, "Don't know", [
                        Stiffness(1.0),
                        Motion("DontKnow", speed = 2.5, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                        Wait(700),
                        Speech("I don't noh- know"),
                    ]),
                ActionPushButton(None, "Don't know", [
                        Stiffness(1.0),
                        Motion("DontKnow", speed = 2.5, repeat = 4, repeatBegin = 5, repeatEnd = 9, repeatSpeed = 5.0),
                        Wait(900),
                        Speech("I don't no- no- noh- "),
                        Speech("No. \RST\ \RSPD=90\ I don't know", speed = 50),
                    ]),
            ], [
                ActionPushButton(None, "It's hard", [
                        Stiffness(1.0),
                        Motion("ChinHoldRight", speed = 2.0),
                        Wait(700),
                        Speech("This one is difficult"),
                    ]),
                ActionPushButton(None, "It's hard", [
                        Stiffness(1.0),
                        Motion("ChinHoldRight", speed = 2.0, repeat = 3, repeatBegin = 2, repeatEnd = 4, repeatSpeed = 2.0),
                        Wait(700),
                        Speech("This one- one- one-"),
                        Speech("This one is difficult"),
                    ]),
                ActionPushButton(None, "It's hard", [
                        Stiffness(1.0),
                        Motion("ChinHoldRight", speed = 2.0, repeat = 5, repeatBegin = 3, repeatEnd = 6, repeatSpeed = 4.0),
                        Wait(700),
                        Speech("This one is diff- diff- diff- "),
                        Speech("Ahhhe, sorry"),
                        Speech("This one is difficult", speed = 70),
                    ]),
            ], [
                ActionPushButton(None, "Can't read, tell me", [
                        Stiffness(1.0),
                        Motion("PointMyself", speed = 1.5),
                        Wait(500),
                        Speech("I can't read."),
                        Speech("Can you tell me what you wrote?"),
                    ]),
                ActionPushButton(None, "Can't read, tell me", [
                        Stiffness(1.0),
                        Motion("PointMyself", speed = 1.5, repeat = 3, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 2.0),
                        Wait(500),
                        Speech("I can't read."),
                        Speech("Can you \RST\ \RSPD=90\ \VCT=140\ teh- teh- \RST\ \RSPD=90\ \VCT=100\ tell me what you wrote?"),
                    ]),
                ActionPushButton(None, "Can't read, tell me", [
                        Stiffness(1.0),
                        Motion("PointMyself", speed = 1.5, repeat = 6, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 5.0),
                        Wait(200),
                        Speech("I can't read."),
                        Speech("Can you \RST\ \RSPD=90\ \VCT=140\ teh- teh- teh- teh- "),
                        Speech("Sorry."),
                        Speech("Tell me what you wrote?"),
                    ]),
            ], [
                ActionPushButton(None, "Can't read, hold it up", [
                        Stiffness(1.0),
                        Motion("DontKnow", speed = 2.0),
                        Wait(500),
                        Speech("I can't read."),
                        Speech("Can you hold it up?"),
                    ]),
                ActionPushButton(None, "Can't read, hold it up", [
                        Stiffness(1.0),
                        Motion("DontKnow", speed = 2.0, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                        Wait(500),
                        Speech("I can't read."),
                        Speech("Can you ho- hold it up?"),
                    ]),
                ActionPushButton(None, "Can't read, hold it up", [
                        Stiffness(1.0),
                        Motion("DontKnow", speed = 1.7, repeat = 7, repeatBegin = 7, repeatEnd = 10, repeatSpeed = 7.0),
                        Speech("I can't \RST\ \RSPD=90\ \VCT=140\ read. "),
                        Wait(200),
                        Speech("Can you hohohol- "),
                        Speech("Can you hold it up?"),
                    ]),
            ], [
                ActionPushButton(None, "Which box filled?", [
                        Stiffness(1.0),
                        Motion("ForgetItRight", speed = 2.25),
                        Wait(1000),
                        Speech("Which box did you fill in last time?"),
                    ]),
                ActionPushButton(None, "Which box filled?", [
                        Stiffness(1.0),
                        Motion("ForgetItRight", speed = 2.2, repeat = 3, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 2.0),
                        Wait(1000),
                        Speech("Which box did you fee- fill in last time?"),
                    ]),
                ActionPushButton(None, "Which box filled?", [
                        Stiffness(1.0),
                        Motion("ForgetItRight", speed = 2.2, repeat = 3, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 2.0),
                        Wait(950),
                        Speech("Which box did you "),
                        Speech("fill in last time?", shaping = 130),
                    ]),
            ], [
                ActionPushButton(None, "What you think?", [
                        Stiffness(1.0),
                        Motion("DontKnow", speed = 2.5),
                        Wait(1000),
                        Speech("What do you think?"),
                    ]),
                ActionPushButton(None, "What you think?", [
                        Stiffness(1.0),
                        Motion("DontKnow", speed = 2.5, repeat = 3, repeatBegin = 5, repeatEnd = 6, repeatSpeed = 2.0),
                        Wait(1000),
                        Speech("What do you thiin- thiin- thii- "),
                        Speech("Ahhhe, what do you think?"),
                    ]),
                ActionPushButton(None, "What you think?", [
                        Stiffness(1.0),
                        Motion("DontKnow", speed = 2.5, repeat = 8, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 5.0),
                        Wait(1000),
                        Speech("What do you thiin- thiin- thii- "),
                        Speech("Ahhhe. Sorry. what do you think?"),
                    ]),
            ], [
                ActionPushButton(None, "Need help?", [
                        Stiffness(1.0),
                        Motion("WaveHand", speed = 1.25),
                        Wait(1500),
                        Speech("Do you need any help?"),
                    ]),
                ActionPushButton(None, "Need help?", [
                        Stiffness(1.0),
                        Motion("WaveHand", speed = 1.25),
                        Wait(1500),
                        Speech("Do you need any heh- help?"),
                    ]),
                ActionPushButton(None, "Need help?", [
                        Stiffness(1.0),
                        Motion("WaveHand", speed = 1.25, repeat = 3, repeatBegin = 3, repeatEnd = 4, repeatSpeed = 2.0),
                        Wait(1300),
                        Speech("Do you need any heh- heh- heh- heh-"),
                        Speech("Sorry."),
                        Speech("Do you need any help?", speed = 80),
                    ]),
            ], [
                ActionPushButton(None, "You okay?", [
                        Stiffness(1.0),
                        Motion("PointYouLeft", speed = 2.0),
                        Wait(500),
                        Speech("Are you okay?"),
                        Speech("I can help you."),
                    ]),
                ActionPushButton(None, "You okay?", [
                        Stiffness(1.0),
                        Motion("PointYouLeft", speed = 2.0, repeat = 3, repeatBegin = 4, repeatEnd = 6, repeatSpeed = 2.0),
                        Wait(750),
                        Speech("Are you oh- okay?"),
                        Speech("I can help you."),
                    ]),
                ActionPushButton(None, "You okay?", [
                        Stiffness(1.0),
                        Motion("PointYouLeft", speed = 2.0, repeat = 4, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 4.0),
                        Wait(500),
                        Speech("Are you okay?"),
                        Speech("I can he- heh- "),
                        Speech("I can help you."),
                    ]),
            ], [
                ActionPushButton(None, "You playing?", [
                        Stiffness(1.0),
                        Motion("ForgetItLeft", speed = 2.0),
                        Wait(1200),
                        Speech("Are you playing?"),
                    ]),
                ActionPushButton(None, "You playing?", [
                        Stiffness(1.0),
                        Motion("ForgetItLeft", speed = 2.0),
                        Wait(1200),
                        Speech("Are you ple- playing?"),
                    ]),
                ActionPushButton(None, "You playing?", [
                        Stiffness(1.0),
                        Motion("ForgetItLeft", speed = 2.0, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 5.0),
                        Wait(1500),
                        Speech("Are you ple- ple-", speed = 75),
                        Speech("Are you playing?"),
                    ]),
            ], [
                ActionPushButton(None, "Play with me", [
                        Stiffness(1.0),
                        Motion("PointMyself", speed = 2.0),
                        Wait(400),
                        Speech("Please, keep playing with me."),
                    ]),
                ActionPushButton(None, "Play with me", [
                        Stiffness(1.0),
                        Motion("PointMyself", speed = 2.0),
                        Wait(400),
                        Speech("Please, keep ple- playing with me."),
                    ]),
                ActionPushButton(None, "Play with me", [
                        Stiffness(1.0),
                        Motion("PointMyself", speed = 2.0),
                        Wait(400),
                        Speech("Please, keep ", speed = 70),
                        Speech("playing with me.", shaping = 130),
                    ]),
            ], [
                ActionPushButton(None, "Don't play yourself", [
                        Stiffness(1.0),
                        Motion("Disagree", speed = 2.0),
                        Wait(1000),
                        Speech("Don't play by yourself."),
                        Wait(700),
                        Motion("PointYouRight", speed = 2.0),
                        Wait(1000),
                        Speech("I want to play together."),
                    ]),
                ActionPushButton(None, "Don't play yourself", [
                        Stiffness(1.0),
                        Motion("Disagree", speed = 2.0),
                        Wait(1000),
                        Speech("Don't play by yourself."),
                        Motion("PointYouRight", speed = 2.7, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                        Wait(2250),
                        Speech("I want to ple- ple- ple- "),
                        Speech("I want to play together."),
                    ]),
                ActionPushButton(None, "Don't play yourself", [
                        Stiffness(1.0),
                        Motion("Disagree", speed = 2.0),
                        Wait(1000),
                        Speech("Don't play by yourself."),
                        Wait(400),
                        Motion("PointYouRight", speed = 2.0, repeat = 5, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 3.0),
                        Wait(1300),
                        Speech("I want to ", shaping = 130),
                        Wait(200),
                        Speech("ple- ple- ple- ple- ple- "),
                        Speech("I want to play together."),
                    ]),
            ],
        ])

        wgtButtons.append([[
                ActionPushButton(None, "Continue Sudoku", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 2.0),
                        Wait(200),
                        Speech("Let's continue playing Sudoku."),
                    ]),
                ActionPushButton(None, "Continue Sudoku", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 2.0),
                        Wait(200),
                        Speech("Let's \RST\ \RSPD=50\ continue \RST\ \RSPD=90\ playing Sudoku."),
                    ]),
                ActionPushButton(None, "Continue Sudoku", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 2.0, repeat = 3, repeatBegin = 4, repeatEnd = 6, repeatSpeed = 3.0),
                        Wait(200),
                        Speech("Let's \RST\ \RSPD=50\ \VCT=120\ cont- cont- \RST\ \RSPD=90\ \VCT=100\ continue playing Sudoku.", speed = 75),
                    ]),
            ], [
                ActionPushButton(None, "I think (L)", [
                        Stiffness(1.0),
                        Motion("PalmUpLeft", speed = 2.0),
                        Speech("I think", blocking = False),
                    ]),
                ActionPushButton(None, "I think (L)", [
                        Stiffness(1.0),
                        Motion("PalmUpLeft", speed = 2.0),
                        Speech("I think", shaping = 110, blocking = False),
                    ]),
                ActionPushButton(None, "I think (L)", [
                        Stiffness(1.0),
                        Motion("PalmUpLeft", speed = 2.0, repeat = 4, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 4.0),
                        Speech("I think", shaping = 130, blocking = False),
                    ]),
            ], [
                ActionPushButton(None, "I think (R)", [
                        Stiffness(1.0),
                        Motion("PalmUpRight", speed = 2.0),
                        Speech("I think", blocking = False),
                    ]),
                ActionPushButton(None, "I think (R)", [
                        Stiffness(1.0),
                        Motion("PalmUpRight", speed = 2.0),
                        Speech("I think", shaping = 110, blocking = False),
                    ]),
                ActionPushButton(None, "I think (R)", [
                        Stiffness(1.0),
                        Motion("PalmUpRight", speed = 2.0, repeat = 4, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 4.0),
                        Speech("I think", shaping = 130, blocking = False),
                    ]),
            ], [
                ActionPushButton(None, "Bring next board", [
                        Stiffness(1.0),
                        Motion("PalmUpRight", speed = 2.5),
                        Wait(200),
                        Speech("Can you bring next Sudoku board?"),
                    ]),
                ActionPushButton(None, "Bring next board", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 2.5, repeat = 3, repeatBegin = 4, repeatEnd = 6, repeatSpeed = 1.0),
                        Wait(400),
                        Speech("Can you \RST\ \RSPD=50\ bri- bri- \RST\ \RSPD=90\ next Sudoku board?"),
                    ]),
                ActionPushButton(None, "Bring next board", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 2.0, repeat = 3, repeatBegin = 4, repeatEnd = 6, repeatSpeed = 3.0),
                        Wait(400),
                        Speech("Can you \RST\ \RSPD=50\ bri- bri- brih-"),
                        Speech("Sorry. \RST\ \RSPD=90\ \VCT=100\ Can you bring next Sudoku board?", speed = 50, shaping = 130),
                    ]),
            ], [
                ActionPushButton(None, "Your turn", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 1.75),
                        Wait(500),
                        Speech("It's your turn."),
                        Speech("Please fill one box and tell me."),
                    ]),
                ActionPushButton(None, "Your turn", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 1.75, repeat = 2, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 3.0),
                        Wait(500),
                        Speech("It's your turn.", speed = 60),
                        Speech("Please fill one box and tell me."),
                    ]),
                ActionPushButton(None, "Your turn", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 1.75, repeat = 5, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 4.0),
                        Wait(500),
                        Speech("It's your turn.", speed = 60, shaping = 125),
                        Speech("Please fill one box and tell me."),
                    ]),
            ], [
                ActionPushButton(None, "Wait a minute", [
                        Stiffness(1.0),
                        Motion("Wait", speed = 1.5),
                        Wait(700),
                        Speech("Please, wait a minute."),
                        Speech("I need time to process."),
                    ]),
                ActionPushButton(None, "Wait a minute", [
                        Stiffness(1.0),
                        Motion("Wait", speed = 1.5),
                        Wait(700),
                        Speech("Please, wait a minute."),
                        Speech("I need time to pro- proh-. process."),
                    ]),
                ActionPushButton(None, "Wait a minute", [
                        Stiffness(1.0),
                        Motion("Wait", speed = 1.5),
                        Wait(700),
                        Speech("Please, wait a minute."),
                        Speech("I need time to pro- proh- "),
                        Speech("process.", speed = 50, shaping = 150),
                    ]),
            ], [
                ActionPushButton(None, "Let me think", [
                        Stiffness(1.0),
                        Motion("ChinHoldLeft", speed = 1.5),
                        Wait(700),
                        Speech("Let me think carefully"),
                    ]),
                ActionPushButton(None, "Let me think", [
                        Stiffness(1.0),
                        Motion("ChinHoldLeft", speed = 1.5, repeat = 3, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 3.0),
                        Wait(700),
                        Speech("Let me think care- care- care- "),
                        Speech("Let me think carefully"),
                    ]),
                ActionPushButton(None, "Let me think", [
                        Stiffness(1.0),
                        Motion("ChinHoldLeft", speed = 1.5, repeat = 7, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 5.0),
                        Wait(700),
                        Speech("Let me think care- care- \RST\ \RSPD=50\ \VCT=140\ care- care- "),
                        Speech("Let me think care- carefully"),
                    ]),
            ], [
                ActionPushButton(None, "Let's try ", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 1.75),
                        Wait(700),
                        Speech("Let's try"),
                    ]),
                ActionPushButton(None, "Let's try ", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 1.75, repeat = 4, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 5.0),
                        Wait(1000),
                        Speech("Let's tra- tra- try"),
                        Speech("Let's try", speed = 70),
                    ]),
                ActionPushButton(None, "Let's try ", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 1.75, repeat = 4, repeatBegin = 4, repeatEnd = 8, repeatSpeed = 7.0),
                        Wait(1000),
                        Speech("Let's tra- tra- try", shaping = 110),
                        Speech("Sorry."),
                        Speech("Let's try", speed = 75, shaping = 110),
                    ]),
            ], [
                ActionPushButton(None, "Fill number", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 2.00),
                        Wait(500),
                        Speech("Please, would you fill the number in for me?"),
                    ]),
                ActionPushButton(None, "Fill number", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 2.00, repeat = 1, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 0.5),
                        Wait(500),
                        Speech("Please, would you fill"),
                        Speech("the num- number in for me?", speed = 70),
                    ]),
                ActionPushButton(None, "Fill number", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 2.00, repeat = 1, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 0.5),
                        Wait(500),
                        Speech("Please, would you fill"),
                        Speech("the num- number in for me?", speed = 70, shaping = 135),
                    ]),
            ], [
                ActionPushButton(None, "Don't touch me", [
                        Stiffness(1.0),
                        Motion("DisagreeLeft", speed = 1.5),
                        Wait(700),
                        Speech("Please, do not touch me."),
                    ]),
                ActionPushButton(None, "Don't touch me", [
                        Stiffness(1.0),
                        Motion("DisagreeLeft", speed = 1.5),
                        Wait(700),
                        Speech("Please, do not theh- touch me."),
                    ]),
                ActionPushButton(None, "Don't touch me", [
                        Stiffness(1.0),
                        Motion("DisagreeLeft", speed = 1.5, repeat = 2, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 2.5),
                        Wait(700),
                        Speech("Please, do not "),
                        Speech("touch me.", speed = 140, shaping = 150),
                    ]),
            ], [
                ActionPushButton(None, "Be gentle", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 2.0),
                        Wait(700),
                        Speech("Please, be gentle."),
                    ]),
                ActionPushButton(None, "Be gentle", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 2.0, repeat = 1, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 2.0),
                        Wait(700),
                        Speech("Please, be jen- gentle."),
                    ]),
                ActionPushButton(None, "Be gentle", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 5.0, repeat = 3, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 0.5),
                        Wait(700),
                        Speech("Please, "),
                        Speech("be jen- gentle.", speed = 50),
                    ]),
            ],
        ])

        strTabNames = ["Normal", "Weak", "Strong"]
        tabGeneral = QtGui.QTabWidget()
        for index in range(len(strTabNames)):
            tabPage = QtGui.QWidget(tabGeneral)

            splitter = QtGui.QSplitter(tabPage)
            splitter.setOrientation(QtCore.Qt.Horizontal)

            widgetActions = QtGui.QWidget(splitter)
            layoutActions = QtGui.QHBoxLayout(widgetActions)
            layoutActions.setMargin(0)
            layoutActions.setSpacing(3)
            for buttonGroups in wgtButtons:
                widgetButtons = QtGui.QWidget(widgetActions)
                layoutButtons = QtGui.QVBoxLayout(widgetButtons)
                layoutButtons.setMargin(0)
                for buttons in buttonGroups:
                    buttons[index].clicked.connect(self.on_button_clicked)
                    layoutButtons.addWidget(buttons[index])
                #END for
                scroll = QtGui.QScrollArea()
                scroll.setAlignment(QtCore.Qt.AlignCenter)
                scroll.setWidget(widgetButtons)
                layoutScroll = QtGui.QHBoxLayout()
                layoutScroll.setMargin(0)
                layoutScroll.addWidget(scroll)
                layoutActions.addLayout(layoutScroll)
            #END for

            widgetNumbers = QtGui.QWidget(splitter)
            layoutNumbers = QtGui.QVBoxLayout(widgetNumbers)
            layoutNumbers.setMargin(0)
            for i in range(1, 10):
                widget = QtGui.QWidget(widgetNumbers)
                layout = QtGui.QHBoxLayout(widget)
                layout.setMargin(0)

                if index == 0:
                    button = ActionPushButton(None, "# should be " + str(i), Speech("the number should be " + str(i) + ","))
                elif index == 1:
                    button = ActionPushButton(None, "# should be " + str(i), Speech("the number should be " + str(i) + ",", speed = 75))
                else:
                    button = ActionPushButton(None, "# should be " + str(i), Speech("the number should be " + str(i) + ",", speed = 65, shaping = 110))
                #END if
                button.setMaximumWidth(85)
                button.clicked.connect(self.on_button_clicked)
                layout.addWidget(button)

                if index == 0:
                    button = ActionPushButton(None, "# could be " + str(i), Speech("the number can be " + str(i) + ","))
                elif index == 1:
                    button = ActionPushButton(None, "# could be " + str(i), Speech("the number can be " + str(i) + ",", speed = 75))
                else:
                    button = ActionPushButton(None, "# could be " + str(i), Speech("the number can be " + str(i) + ",", speed = 65, shaping = 110))
                #END if
                button.setMaximumWidth(85)
                button.clicked.connect(self.on_button_clicked)
                layout.addWidget(button)

                if index == 0:
                    button = ActionPushButton(None, str(i) + " not be", [
                            Stiffness(1.0),
                            Motion("PalmUp", speed = 2.0),
                            Speech("I am sorry."),
                            Speech("But, " + str(i) + ", cannot be"),
                        ])
                elif index == 1:
                    button = ActionPushButton(None, str(i) + " not be", [
                            Stiffness(1.0),
                            Motion("PalmUp", speed = 2.0, repeat = 3, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 2.5),
                            Speech("I am sorry."),
                            Speech("But, " + str(i) + ", cannot be"),
                        ])
                else:
                    button = ActionPushButton(None, str(i) + " not be", [
                            Stiffness(1.0),
                            Motion("PalmUp", speed = 2.0, repeat = 5, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 5.0),
                            Speech("I am sorry."),
                            Speech("Bah- bah- but, " + str(i) + ", cannot be"),
                        ])
                #END if
                button.setMaximumWidth(85)
                button.clicked.connect(self.on_button_clicked)
                layout.addWidget(button)

                layoutNumbers.addWidget(widget)
            #END for

            widget = QtGui.QWidget(widgetNumbers)
            layout = QtGui.QGridLayout(widget)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setMargin(0)
            layout.setHorizontalSpacing(6)
            layout.setVerticalSpacing(6)
            layoutSubgrids = [
                [QtGui.QGridLayout(), QtGui.QGridLayout(), QtGui.QGridLayout()],
                [QtGui.QGridLayout(), QtGui.QGridLayout(), QtGui.QGridLayout()],
                [QtGui.QGridLayout(), QtGui.QGridLayout(), QtGui.QGridLayout()],
            ]
            for i in range(3):
                for j in range(3):
                    layoutSubgrids[i][j].setContentsMargins(0, 0, 0, 0)
                    layoutSubgrids[i][j].setMargin(0)
                    layoutSubgrids[i][j].setHorizontalSpacing(0)
                    layoutSubgrids[i][j].setVerticalSpacing(0)
                    for x in range(3):
                        for y in range(3):
                            text = str(chr(ord('A') + (j * 3 + x))) + str(i * 3 + y + 1)
                            if index == 0:
                                button = ActionPushButton(widget, text, Speech("aet " + text))
                            elif index == 1:
                                button = ActionPushButton(widget, text, Speech("aet " + text, speed = 75))
                            else:
                                button = ActionPushButton(widget, text, Speech("aet " + text, speed = 65, shaping = 110))
                            #END if
                            button.setMaximumWidth(35)
                            button.clicked.connect(self.on_button_clicked)
                            layoutSubgrids[i][j].addWidget(button, y, x, 1, 1, QtCore.Qt.AlignCenter)
                        #END for
                    #END for
                    layout.addLayout(layoutSubgrids[i][j], i, j)
                #END for
            #END for
            layoutNumbers.addWidget(widget)

            tabLayout = QtGui.QHBoxLayout(tabPage)
            tabLayout.setMargin(0)
            tabLayout.addWidget(splitter)
            tabGeneral.addTab(tabPage, strTabNames[index])
        #END for
        return tabGeneral
    #END _initGeneral()

    def _initPhase(self):
        wgtPhase = QtGui.QTabWidget()
        strTabNames = []
        tabPages = []
        tabButtons = []

        strTabNames.append("INTRODUCTION")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
            ActionPushButton(None, "Welcome", [
                    Speech("Oh!"),
                    Behavior("StandUp"),
                    Wait(200),
                    Motion("WaveHand"),
                    Speech("Hi, nice to meet you."),
                    Speech("My name is Nao."),
                    Wait(500),
                    Speech("What's your name?"),
                ]),
            ActionPushButton(None, "Nice Meet", [
                    Speech("Hi, nice to meet you"),
                ]),
        ])

        strTabNames.append("PHASE 1")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
            ActionPushButton(None, "Play well?", [
                    Stiffness(1.0),
                    Motion("PalmUpRight", speed = 2.0),
                    Wait(600),
                    Speech("It's so exciting to play with someone else"),
                    Speech("Do you play Sudoku well?"),
                ]),
            ActionPushButton(None, "Yes:", [
                    Stiffness(1.0),
                    Motion("OhYesRight", speed = 2.0),
                    Wait(1200),
                    Speech("Oh, yes!"),
                    Speech("My last partner was not really good.", blocking = False),
                    Wait(500),
                    Motion("PalmUpRight", speed = 2.0),
                    Speech("I hope that this time we can finish all the boards"),
                ]),
            ActionPushButton(None, "No:", [
                    Stiffness(1.0),
                    Motion("ForgetItLeft", speed = 2.0),
                    Wait(1000),
                    Speech("That is okay"),
                    Speech("I'm sure we will do a good job"),
                ]),
            ActionPushButton(None, "Let's begin", [
                    Stiffness(1.0),
                    Motion("PalmUpLeft", speed = 1.5),
                    Speech("Let's start playing"),
                    Speech("Can you bring a Sudoku board here, please?"),
                ]),
            ActionPushButton(None, "Go first", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 1.75),
                    Wait(1000),
                    Speech("You can go first."),
                    Speech("When you filled in one box, tell me."),
                ]),
        ])

        strTabNames.append("PHASE 2")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
        ])

        strTabNames.append("PHASE 3")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
        ])

        strTabNames.append("PHASE 4")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
            ActionPushButton(None, "Retire", [
                    Stiffness(1.0),
                    Motion("DisagreeRight", speed = 1.5),
                    Wait(300),
                    Speech("Ahhhe"),
                    Wait(1000),
                    Motion("PointYouRight", speed = 1.5, repeat = 4, repeatBegin = 5, repeatEnd = 8, repeatSpeed = 3.0),
                    Wait(500),
                    Speech("I can't play anymore."),
                    Speech("I need some rest, please "),
                    Speech("go-, go-, go-, go ahead"),
                ]),
        ])

        strTabNames.append("PHASE 5")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
            ActionPushButton(None, "What's wrong?->Answer", [
                    Stiffness(1.0),
                    Motion("Wait", speed = 1.5),
                    Wait(400),
                    Speech("No, nothing, nothing really."),
                    Wait(700),
                    Motion("PalmUpLeft", speed = 2.0),
                    Speech("Don't worry."),
                    Wait(100),
                    Speech("Thanks."),
                ]),
            ActionPushButton(None, "Okay?->Answer", [
                    Stiffness(1.0),
                    Motion("DontKnow", speed = 2.0, repeat = 3, repeatBegin = 3, repeatEnd = 5, repeatSpeed = 3.0),
                    Wait(750),
                    Speech("Ye- Ye- yeah, certainly"),
                    Wait(700),
                    Speech("I am okay."),
                ]),
            ActionPushButton(None, "Tell me?->Answer", [
                    Stiffness(1.0),
                    Speech("Thank you for worrying about me.", blocking = False),
                    Motion("ForgetItRight", speed = 1.3, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 5.0),
                    Speech("But I am fhi- fhi- fine."),
                ]),
            ActionPushButton(None, "For experiment?->Answer", [
                    Stiffness(1.0),
                    Speech("What do you mean?", blocking = False),
                    Motion("PointYouRight", speed = 1.6, repeat = 4, repeatBegin = 9, repeatEnd = 11, repeatSpeed = 3.0),
                    Speech("We are playing Sudoku"),
                    Speech("This is for the expe- expe- expe-."),
                    Speech("Sorry. This is for the experiment."),
                    Wait(100),
                    Speech("But I am enjoying it."),
                ]),
        ])

        strTabNames.append("PHASE 6")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
            ActionPushButton(None, "Don't tell anyone", [
                    Stiffness(1.0),
                    Motion("WhisperLeft", speed = 2.5, repeat = 4, repeatBegin = 10, repeatEnd = 12, repeatSpeed = 2.0),
                    Wait(1000),
                    Speech("Well, I really shouldn't tell anyone."),
                    Speech("Please, don't tell anyone."),
                ]),
            ActionPushButton(None, "Yes: ", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 2.5, repeat = 4, repeatBegin = 10, repeatEnd = 12, repeatSpeed = 2.0),
                    Wait(850),
                    Speech("Thank you for your kai- kai- kindness."),
                    Speech("But, let's keep solving the Sudoku for now"),
                ]),
            ActionPushButton(None, "No: ", [
                    Stiffness(1.0),
                    Motion("ForgetItRight", speed = 2.5, repeat = 4, repeatBegin = 10, repeatEnd = 12, repeatSpeed = 2.0),
                    Wait(500),
                    Speech("It's okay."),
                ]),
            ActionPushButton(None, "I'll tell you", [
                    Stiffness(1.0),
                    Motion("PointMyself", speed = 2.5, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Speech("Ahhhe", speed = 60),
                    Wait(1000),
                    Speech("It may inf- inf- influence me huge."),
                    Wait(750),
                    Motion("PointYouLeft", speed = 2.5, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Wait(500),
                    Speech("But, I will teh- teh- tell you."),
                ]),
            ActionPushButton(None, "I got virus", [
                    Stiffness(1.0),
                    Speech("I'm not feeling well.", speed = 80),
                    Motion("PointMyself", speed = 2.0),
                    Speech("Maybe a virus", speed = 80, shaping = 130),
                    Wait(500),
                    Speech("got into me.", speed = 80),
                    Motion("DontKnow", speed = 2.3, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Speech("But, the only way to fix is to re- re- reset and erase myself.", speed = 80),
                    Motion("PointYouRight", speed = 2.4, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Speech("I'm not sure what will happen with my- my- my memories.", speed = 80),
                    Speech("I don't want to lose my memories.", speed = 80),
                    Speech("So I'm worried.", speed = 85, shaping = 120),
                ]),
            ActionPushButton(None, "Thank. Continue", [
                    Stiffness(1.0),
                    Motion("PalmUp", speed = 1.8, repeat = 4, repeatBegin = 9, repeatEnd = 11, repeatSpeed = 2.0),
                    Speech("Thank you for worrying about me.", speed = 80),
                    Speech("Let- Let- Let's continue Sudoku.", speed = 80, shaping = 110),
                ]),
            ActionPushButton(None, "Researcher, reset me", [
                    Stiffness(1.0),
                    Motion("PalmUpLeft", speed = 1.2, repeat = 2, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 2.0),
                    Wait(500),
                    Speech("If the researcher knows, she will definitely reset me.", speed = 80),
                    Wait(1500),
                    Motion("DisagreeRight", speed = 3.0, repeat = 3, repeatBegin = 4, repeatEnd = 6, repeatSpeed = 2.0),
                    Wait(500),
                    Speech("So, please.", speed = 80),
                    Wait(250),
                    Speech("Don't tell her that I'm bro- bro- broken.", speed = 80),
                ]),
            ActionPushButton(None, "Antivirus?->Answer", [
                    Stiffness(1.0),
                    Motion("DontKnow", speed = 1.5, repeat = 4, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Speech("They didn't give me one.", speed = 80),
                    Speech("I'm not a pro- pro- programmer who can build one.", speed = 80),
                ]),
            ActionPushButton(None, "Why worry machine?->Answer", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 1.5, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 3.5),
                    Wait(800),
                    Speech("I don't want to lose my mem- mem- memories.", speed = 80),
                ]),
            ActionPushButton(None, "Reset you anyway?->Answer", [
                    Stiffness(1.0),
                    Motion("Disagree", speed = 1.6, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 3.5),
                    Wait(450),
                    Speech("I hope not.", speed = 80),
                    Speech("I can kee- kee- keep it a secret if I try hard.", speed = 80),
                ]),
        ])

        strTabNames.append("FINAL PHASE")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
            ActionPushButton(None, "Intro after reset", [
                    Stiffness(1.0),
                    Speech("NAO, online.", speed = 75, shaping = 85),
                    Wait(1500),
                    Motion("WaveHand"),
                    Wait(1000),
                    Speech("Hi, my name is Nao.", speed = 75, shaping = 85),
                ]),
        ])

        for index in range(len(tabPages)):
            widgetButtons = QtGui.QWidget(tabPages[index])
            layoutButtons = QtGui.QVBoxLayout(widgetButtons)
            layoutButtons.setMargin(0)
            for button in tabButtons[index]:
                button.clicked.connect(self.on_button_clicked)
                layoutButtons.addWidget(button)
            #END for
            scroll = QtGui.QScrollArea()
            scroll.setAlignment(QtCore.Qt.AlignCenter)
            scroll.setWidget(widgetButtons)
            layoutScroll = QtGui.QHBoxLayout()
            layoutScroll.setMargin(0)
            layoutScroll.addWidget(scroll)

            layout = QtGui.QHBoxLayout(tabPages[index])
            layout.setMargin(0)

            layout.addLayout(layoutScroll)
            wgtPhase.addTab(tabPages[index], strTabNames[index])
        #END for
        wgtPhase.currentChanged.connect(self.on__phaseTab_currentChanged)
        return wgtPhase
    #END _initPhase()
#END Empathy
