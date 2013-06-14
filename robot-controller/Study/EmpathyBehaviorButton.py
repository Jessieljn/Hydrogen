from PyQt4 import QtGui
from Action import Speech
from Nao import NaoMotionList


class EmpathyBehaviorButton(QtGui.QPushButton):
    INDEX_MOTION = 0
    INDEX_SPEECH = 1
    _behaviours = []
    _motions = dict()

    def __init__(self, label):
        super(EmpathyBehaviorButton, self).__init__(label)
        # The list list of sentense-motion.
        # Sentense-motion contains list of sentenses and corresponding motion IDs
        self._list = dict()
        self._maxLevel = 0
    #END __init__()

    def add(self, jlv, motion = None, speech = None):
        if not jlv in self._list:
            self._list[jlv] = [[], []]
            self._maxLevel = max(self._maxLevel, jlv)
        #END if
        if motion is not None:
            motion = EmpathyBehaviorButton.getMotionByName(motion)
            if motion is not None:
                self._list[jlv][EmpathyBehaviorButton.INDEX_MOTION].append(motion)
            #END if
        #END if
        if speech is not None:
            self._list[jlv][EmpathyBehaviorButton.INDEX_SPEECH].append(Speech(speech))
        #END if
    #END add()

    def maxLevel(self):
        return self._maxLevel
    #END maxLevel()

    @staticmethod
    def initialize():
        EmpathyBehaviorButton._initMotions()
        EmpathyBehaviorButton._initSpeechs()
    #END initialize()

    @staticmethod
    def destroy():
        pass
    #END destroy()

    @staticmethod
    def getBehavior(index):
        return EmpathyBehaviorButton._behaviours[index]
    #END getBehavior()

    @staticmethod
    def getMotion(index):
        return EmpathyBehaviorButton._motions.items()[index]
    #END getMotion()

    @staticmethod
    def getMotionByName(name):
        if name in EmpathyBehaviorButton._motions:
            return EmpathyBehaviorButton._motions[name]
        #END if
        return None
    #END getMotionByName()

    @staticmethod
    def lengthBehaviors():
        return len(EmpathyBehaviorButton._behaviours)
    #END lengthBehaviors()

    @staticmethod
    def lengthMotions():
        return len(EmpathyBehaviorButton._motions)
    #END lengthMotions()

    @staticmethod
    def _markSpeech(speed = 90, shaping = 100):
        # ending mark + speed + shaping
        return " \\RST\\ \\RSPD=" + str(speed) + "\\ \\VCT=" + str(shaping) + "\\ "
    #END _markSpeech()

    @staticmethod
    def _initMotions():
        # The number in front of motion name refers jitter level.
        # If the level is 0, it should be normal.
        EmpathyBehaviorButton._motions["0_Idle1"] = NaoMotionList.find("Idle1").applySpeed(2.2)
        EmpathyBehaviorButton._motions["1_Idle1"] = NaoMotionList.find("Idle1").applySpeed(2.2).applyRepeat(beginIndex = 13, endIndex = 16, repeats = 4, repeatTimeModifier = 3.0)
        EmpathyBehaviorButton._motions["2_Idle1"] = NaoMotionList.find("Idle1").applySpeed(2.2).applyRepeat(beginIndex = 6, endIndex = 9, repeats = 4, repeatTimeModifier = 5.0)
        EmpathyBehaviorButton._motions["0_Disagree"] = NaoMotionList.find("Disagree").applySpeed(2.0)
        EmpathyBehaviorButton._motions["1_Disagree"] = NaoMotionList.find("Disagree").applySpeed(2.7).applyRepeat(beginIndex = 7, endIndex = 9, repeats = 3, repeatTimeModifier = 2.0)
        EmpathyBehaviorButton._motions["2_Disagree"] = NaoMotionList.find("Disagree").applySpeed(2.7).applyRepeat(beginIndex = 7, endIndex = 9, repeats = 5, repeatTimeModifier = 3.0)
        EmpathyBehaviorButton._motions["0_DisagreeLeft"] = NaoMotionList.find("DisagreeLeft").applySpeed(1.5)
        EmpathyBehaviorButton._motions["1_DisagreeLeft"] = NaoMotionList.find("DisagreeLeft").applySpeed(1.5).applyRepeat(beginIndex = 5, endIndex = 7, repeats = 2, repeatTimeModifier = 2.5)
        EmpathyBehaviorButton._motions["0_DisagreeRight"] = NaoMotionList.find("DisagreeRight").applySpeed(1.5)
        EmpathyBehaviorButton._motions["1_DisagreeRight"] = NaoMotionList.find("DisagreeRight").applySpeed(1.5).applyRepeat(beginIndex = 5, endIndex = 7, repeats = 2, repeatTimeModifier = 2.5)
        EmpathyBehaviorButton._motions["0_DontKnow"] = NaoMotionList.find("DontKnow").applySpeed(2.5)
        EmpathyBehaviorButton._motions["1_DontKnow"] = NaoMotionList.find("DontKnow").applySpeed(2.5).applyRepeat(beginIndex = 7, endIndex = 9, repeats = 3, repeatTimeModifier = 2.0)
        EmpathyBehaviorButton._motions["2_DontKnow"] = NaoMotionList.find("DontKnow").applySpeed(2.5).applyRepeat(beginIndex = 5, endIndex = 9, repeats = 4, repeatTimeModifier = 5.0)
        EmpathyBehaviorButton._motions["3_DontKnow"] = NaoMotionList.find("DontKnow").applySpeed(2.5).applyRepeat(beginIndex = 7, endIndex = 10, repeats = 7, repeatTimeModifier = 7.0)
        EmpathyBehaviorButton._motions["0_Wait"] = NaoMotionList.find("Wait").applySpeed(1.5)
        EmpathyBehaviorButton._motions["0_WaveHand"] = NaoMotionList.find("WaveHand").applySpeed(1.25)
        EmpathyBehaviorButton._motions["1_WaveHand"] = NaoMotionList.find("WaveHand").applySpeed(1.25).applyRepeat(beginIndex = 3, endIndex = 4, repeats = 3, repeatTimeModifier = 2.0)
        EmpathyBehaviorButton._motions["0_ForgetItLeft"] = NaoMotionList.find("ForgetItLeft").applySpeed(2.25)
        EmpathyBehaviorButton._motions["1_ForgetItLeft"] = NaoMotionList.find("ForgetItLeft").applySpeed(2.2).applyRepeat(beginIndex = 5, endIndex = 7, repeats = 3, repeatTimeModifier = 2.0)
        EmpathyBehaviorButton._motions["0_ForgetItRight"] = NaoMotionList.find("ForgetItRight").applySpeed(2.25)
        EmpathyBehaviorButton._motions["1_ForgetItRight"] = NaoMotionList.find("ForgetItRight").applySpeed(2.2).applyRepeat(beginIndex = 5, endIndex = 7, repeats = 3, repeatTimeModifier = 2.0)
        EmpathyBehaviorButton._motions["0_OhYesLeft"] = NaoMotionList.find("OhYesLeft").applySpeed(2.0)
        EmpathyBehaviorButton._motions["0_OhYesRight"] = NaoMotionList.find("OhYesRight").applySpeed(2.0)
        EmpathyBehaviorButton._motions["0_PalmUp"] = NaoMotionList.find("PalmUp").applySpeed(2.0)
        EmpathyBehaviorButton._motions["1_PalmUp"] = NaoMotionList.find("PalmUp").applySpeed(2.0).applyRepeat(beginIndex = 4, endIndex = 6, repeats = 3, repeatTimeModifier = 3.0)
        EmpathyBehaviorButton._motions["0_PalmUpLeft"] = NaoMotionList.find("PalmUpLeft").applySpeed(2.0)
        EmpathyBehaviorButton._motions["1_PalmUpLeft"] = NaoMotionList.find("PalmUpLeft").applySpeed(2.0).applyRepeat(beginIndex = 7, endIndex = 9, repeats = 4, repeatTimeModifier = 4.0)
        EmpathyBehaviorButton._motions["2_PalmUpLeft"] = NaoMotionList.find("PalmUpLeft").applySpeed(2.0).applyRepeat(beginIndex = 4, endIndex = 6, repeats = 3, repeatTimeModifier = 3.0)
        EmpathyBehaviorButton._motions["0_PalmUpRight"] = NaoMotionList.find("PalmUpRight").applySpeed(2.0)
        EmpathyBehaviorButton._motions["1_PalmUpRight"] = NaoMotionList.find("PalmUpRight").applySpeed(2.0).applyRepeat(beginIndex = 7, endIndex = 9, repeats = 4, repeatTimeModifier = 4.0)
        EmpathyBehaviorButton._motions["2_PalmUpRight"] = NaoMotionList.find("PalmUpRight").applySpeed(2.0).applyRepeat(beginIndex = 4, endIndex = 6, repeats = 3, repeatTimeModifier = 3.0)
        EmpathyBehaviorButton._motions["0_PointMyself"] = NaoMotionList.find("PointMyself").applySpeed(1.5)
        EmpathyBehaviorButton._motions["1_PointMyself"] = NaoMotionList.find("PointMyself").applySpeed(1.5).applyRepeat(beginIndex = 5, endIndex = 7, repeats = 3, repeatTimeModifier = 2.0)
        EmpathyBehaviorButton._motions["3_PointMyself"] = NaoMotionList.find("PointMyself").applySpeed(1.5).applyRepeat(beginIndex = 5, endIndex = 7, repeats = 6, repeatTimeModifier = 5.0)
        EmpathyBehaviorButton._motions["0_PointYouLeft"] = NaoMotionList.find("PointYouLeft").applySpeed(2.0)
        EmpathyBehaviorButton._motions["1_PointYouLeft"] = NaoMotionList.find("PointYouLeft").applySpeed(2.0).applyRepeat(beginIndex = 4, endIndex = 6, repeats = 3, repeatTimeModifier = 2.0)
        EmpathyBehaviorButton._motions["2_PointYouLeft"] = NaoMotionList.find("PointYouLeft").applySpeed(2.0).applyRepeat(beginIndex = 7, endIndex = 9, repeats = 4, repeatTimeModifier = 4.0)
        EmpathyBehaviorButton._motions["3_PointYouLeft"] = NaoMotionList.find("PointYouLeft").applySpeed(2.0).applyRepeat(beginIndex = 7, endIndex = 9, repeats = 5, repeatTimeModifier = 4.0)
        EmpathyBehaviorButton._motions["0_PointYouRight"] = NaoMotionList.find("PointYouRight").applySpeed(2.0)
        EmpathyBehaviorButton._motions["1_PointYouRight"] = NaoMotionList.find("PointYouRight").applySpeed(2.0).applyRepeat(beginIndex = 4, endIndex = 6, repeats = 3, repeatTimeModifier = 2.0)
        EmpathyBehaviorButton._motions["2_PointYouRight"] = NaoMotionList.find("PointYouRight").applySpeed(2.0).applyRepeat(beginIndex = 7, endIndex = 9, repeats = 4, repeatTimeModifier = 4.0)
        EmpathyBehaviorButton._motions["3_PointYouRight"] = NaoMotionList.find("PointYouRight").applySpeed(2.0).applyRepeat(beginIndex = 7, endIndex = 9, repeats = 5, repeatTimeModifier = 4.0)
        EmpathyBehaviorButton._motions["0_ChinHoldLeft"] = NaoMotionList.find("ChinHoldLeft").applySpeed(1.2)
        EmpathyBehaviorButton._motions["1_ChinHoldLeft"] = NaoMotionList.find("ChinHoldLeft").applySpeed(1.2).applyRepeat(beginIndex = 4, endIndex = 7, repeats = 4, repeatTimeModifier = 3.0)
        EmpathyBehaviorButton._motions["2_ChinHoldLeft"] = NaoMotionList.find("ChinHoldLeft").applySpeed(1.2).applyRepeat(beginIndex = 3, endIndex = 6, repeats = 5, repeatTimeModifier = 4.0)
        EmpathyBehaviorButton._motions["3_ChinHoldLeft"] = NaoMotionList.find("ChinHoldLeft").applySpeed(1.2).applyRepeat(beginIndex = 8, endIndex = 10, repeats = 7, repeatTimeModifier = 5.0)
        EmpathyBehaviorButton._motions["0_ChinHoldRight"] = NaoMotionList.find("ChinHoldRight").applySpeed(1.2)
        EmpathyBehaviorButton._motions["1_ChinHoldRight"] = NaoMotionList.find("ChinHoldRight").applySpeed(1.2).applyRepeat(beginIndex = 4, endIndex = 7, repeats = 4, repeatTimeModifier = 3.0)
        EmpathyBehaviorButton._motions["2_ChinHoldRight"] = NaoMotionList.find("ChinHoldRight").applySpeed(1.2).applyRepeat(beginIndex = 3, endIndex = 6, repeats = 5, repeatTimeModifier = 4.0)
        EmpathyBehaviorButton._motions["3_ChinHoldRight"] = NaoMotionList.find("ChinHoldRight").applySpeed(1.2).applyRepeat(beginIndex = 8, endIndex = 10, repeats = 7, repeatTimeModifier = 5.0)
        EmpathyBehaviorButton._motions["0_WhisperLeft"] = NaoMotionList.find("WhisperLeft").applySpeed(2.5)
        EmpathyBehaviorButton._motions["1_WhisperLeft"] = NaoMotionList.find("WhisperLeft").applySpeed(2.5).applyRepeat(beginIndex = 10, endIndex = 12, repeats = 10, repeatTimeModifier = 2.0)
        EmpathyBehaviorButton._motions["0_WhisperRight"] = NaoMotionList.find("WhisperRight").applySpeed(2.5)
        EmpathyBehaviorButton._motions["1_WhisperRight"] = NaoMotionList.find("WhisperRight").applySpeed(2.5).applyRepeat(beginIndex = 10, endIndex = 12, repeats = 10, repeatTimeModifier = 2.0)
    #END _initMotions()

    @staticmethod
    def _initSpeechs():
        bhv = EmpathyBehaviorButton("Don't know")
        bhv.add(0, speech = "I don't know")
        bhv.add(1, speech = "I don't noh- know")
        bhv.add(2, speech = "I don't no- no- noh-." + EmpathyBehaviorButton._markSpeech(50) + "No." + EmpathyBehaviorButton._markSpeech() + "I don't know")
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_DontKnow")
            bhv.add(i, motion = str(i) + "_PalmUp")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("It's hard")
        bhv.add(0, speech = "This one is difficult")
        bhv.add(1, speech = "This one- one- one-. This one is difficult")
        bhv.add(2, speech = "This one is diff- diff- diff-." + EmpathyBehaviorButton._markSpeech(50) + "Ahhhe." + EmpathyBehaviorButton._markSpeech(70) + "Sorry. This one is difficult")
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_ChinHoldLeft")
            bhv.add(i, motion = str(i) + "_ChinHoldRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Can't read, tell me")
        bhv.add(0, speech = "I can't read. Can you tell me what you wrote?")
        bhv.add(1, speech = "I can't read. Can you" + EmpathyBehaviorButton._markSpeech(90, 140) + "teh- teh-" + EmpathyBehaviorButton._markSpeech() + "tell me what you wrote?")
        bhv.add(2, speech = "I can't read. Can you" + EmpathyBehaviorButton._markSpeech(90, 140) + "teh- teh- teh- teh-." + EmpathyBehaviorButton._markSpeech() + "Sorry. Tell me what you wrote?")
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PointMyself")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Can't read, hold it up")
        bhv.add(0, speech = "I can't read. Can you hold it up?")
        bhv.add(1, speech = "I can't read. Can you ho- hold it up?")
        bhv.add(2, speech = "I can't" + EmpathyBehaviorButton._markSpeech(90, 140) + "read." + EmpathyBehaviorButton._markSpeech() + "Can you hohohol- Can you hold it up?")
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_DontKnow")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Which box filled?")
        bhv.add(0, speech = "Which box did you fill?")
        bhv.add(1, speech = "Which box did you fee- fill?")
        bhv.add(2, speech = "Which box did you" + EmpathyBehaviorButton._markSpeech(90, 130) + "fill.")
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_ForgetItLeft")
            bhv.add(i, motion = str(i) + "_ForgetItRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("What you think?")
        bhv.add(0, speech = "What do you think?")
        bhv.add(1, speech = "What do you thiin- thiin- thii-. Ahhhe, what do you think?")
        bhv.add(2, speech = "What do you thiin- thiin- thii-. Ahhhe. Sorry. what do you think?")
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_DontKnow")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Need help?")
        bhv.add(0, speech = "Are you okay? I can help you.")
        bhv.add(0, speech = "Do you need any help?")
        bhv.add(1, speech = "Are you oh- okay? I can help you.")
        bhv.add(2, speech = "Do you need any heh- heh- heh- heh-. Sorry." + EmpathyBehaviorButton._markSpeech(80) + "Do you need any help?")
        bhv.add(2, speech = "Are you okay? I can he- heh-. I can help you.")
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_WaveHand")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("You playing?")
        bhv.add(0, speech = "Are you playing?")
        bhv.add(1, speech = "Are you ple- playing?")
        bhv.add(2, speech = EmpathyBehaviorButton._markSpeech(80) + "Are you ple- ple-." + EmpathyBehaviorButton._markSpeech() + "Are you playing?")
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_ForgetItLeft")
            bhv.add(i, motion = str(i) + "_ForgetItRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Play with me")
        bhv.add(0, speech = "Please, keep playing with me.")
        bhv.add(0, speech = "I want to play together.")
        bhv.add(1, speech = "Please, keep ple- playing with me.")
        bhv.add(1, speech = "I want to ple- ple- ple-. I want to play together.")
        bhv.add(2, speech = EmpathyBehaviorButton._markSpeech(70) + "Please, keep " + EmpathyBehaviorButton._markSpeech(90, 130) + "playing with me.")
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PointMyself")
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Don't play yourself")
        bhv.add(0, speech = "Don't play by yourself")
        bhv.add(1, speech = "Don't play by yourself.")
        bhv.add(2, speech = "Don't play by yourself.")
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_Disagree")
            bhv.add(i, motion = str(i) + "_DisagreeLeft")
            bhv.add(i, motion = str(i) + "_DisagreeRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Continue Sudoku")
        bhv.add(0, speech = "Let's continue playing Sudoku.")
        bhv.add(1, speech = "Let's" + EmpathyBehaviorButton._markSpeech(50) + "continue" + EmpathyBehaviorButton._markSpeech() + "playing Sudoku.")
        bhv.add(2, speech = EmpathyBehaviorButton._markSpeech(75) + "Let's" + EmpathyBehaviorButton._markSpeech(50, 120) + "cont- cont-" + EmpathyBehaviorButton._markSpeech() + "continue playing Sudoku.")
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PalmUp")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("I think")
        bhv.add(0, speech = "I think")
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Bring next board")
        bhv.add(0, speech = "Can you bring next Sudoku board?")
        bhv.add(1, speech = "Can you" + EmpathyBehaviorButton._markSpeech(50) + "bri- bri-" + EmpathyBehaviorButton._markSpeech() + "next Sudoku board?")
        bhv.add(2, speech = "Can you" + EmpathyBehaviorButton._markSpeech(50) + "bri- bri- brih-" + EmpathyBehaviorButton._markSpeech(50, 130) + "Sorry." + EmpathyBehaviorButton._markSpeech() + "Can you bring next Sudoku board?")
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Your turn")
        bhv.add(0, speech = "It's your turn. Please fill one box and tell me.")
        bhv.add(1, speech = EmpathyBehaviorButton._markSpeech(60) + "It's your turn." + EmpathyBehaviorButton._markSpeech() + "Please fill one box and tell me.")
        bhv.add(2, speech = EmpathyBehaviorButton._markSpeech(60, 125) + "It's your turn." + EmpathyBehaviorButton._markSpeech() + "Please fill one box and tell me.")
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Wait a minute")
        bhv.add(0, speech = "Please, wait a minute. I need time to process.")
        bhv.add(1, speech = "Please, wait a minute. I need time to pro- proh-. process.")
        bhv.add(2, speech = "Please, wait a minute. I need time to pro- proh-." + EmpathyBehaviorButton._markSpeech(50, 130) + "process.")
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_Wait")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Let me think")
        bhv.add(0, speech = "Let me think carefully.")
        bhv.add(1, speech = "Let me think care- care- care-. Let me think carefully.")
        bhv.add(2, speech = "Let me think care- care-" + EmpathyBehaviorButton._markSpeech(50, 130) + "care- care-. Let me think care- carefully.")
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_ChinHoldLeft")
            bhv.add(i, motion = str(i) + "_ChinHoldRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Let's try")
        bhv.add(0, speech = "Let's try.")
        bhv.add(0, speech = "Please, would you fill the number in for me?")
        bhv.add(1, speech = "Let's tra- tra- try. Let's try.")
        bhv.add(1, speech = "Please, would you fill." + EmpathyBehaviorButton._markSpeech(70) + "the num- number in for me?")
        bhv.add(2, speech = EmpathyBehaviorButton._markSpeech(90, 110) + "Let's tra- tra- try." + EmpathyBehaviorButton._markSpeech() + "Sorry." + EmpathyBehaviorButton._markSpeech(75, 110) + "Let's try.")
        bhv.add(2, speech = "Please, would you fill." + EmpathyBehaviorButton._markSpeech(70, 125) + "the num- number in for me?")
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Don't touch me")
        bhv.add(0, speech = "Please, do not touch me.")
        bhv.add(1, speech = "Please, do not theh- touch me.")
        bhv.add(2, speech = "Please, do not" + EmpathyBehaviorButton._markSpeech(140, 130) + "touch me.")
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_Disagree")
            bhv.add(i, motion = str(i) + "_DisagreeLeft")
            bhv.add(i, motion = str(i) + "_DisagreeRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Be gentle")
        bhv.add(0, speech = "Please, be gentle.")
        bhv.add(1, speech = "Please, be jen- gentle.")
        bhv.add(2, speech = "Please," + EmpathyBehaviorButton._markSpeech(50) + "be jen- gentle.")
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)
    #END _initSpeechs()
#END class
