from PyQt4 import QtGui
from Action import BaseAction
from Action import Motion
from Action import Speech
from Action import Stiffness
from Action import Wait
from Nao import NaoMotionList
import random


class EmpathyBehaviorButton(QtGui.QPushButton):
    INDEX_ACTIONS = 0
    INDEX_MOTION = 1

    INDEX_BIG_IDLE = 0
    INDEX_SMALL_IDLE = 1
    INDEX_SUDOKU_ANSWER = 2

    _behaviours = []
    _motions = dict()

    def __init__(self, label, motion_blocks = False):
        super(EmpathyBehaviorButton, self).__init__(label)
        # The list list of action-motion.
        # action-motion contains list of actions and corresponding motion IDs
        self._list = dict()
        self._maxLevel = 0
        self._motion_blocks = motion_blocks
    #END __init__()

    def add(self, jlv, actions = None, motion = None):
        if not jlv in self._list:
            self._list[jlv] = [[], []]
            self._maxLevel = max(self._maxLevel, jlv)
        #END if
        if actions is not None:
            if isinstance(actions, BaseAction):
                actions = [actions]
            #END if
            self._list[jlv][EmpathyBehaviorButton.INDEX_ACTIONS].append(actions)
        #END if
        if motion is not None:
            motion = EmpathyBehaviorButton.getMotionByName(motion)
            if motion is not None:
                self._list[jlv][EmpathyBehaviorButton.INDEX_MOTION].append(motion)
            #END if
        #END if
    #END add()

    def getRobotActions(self, jlv):
        while not jlv in self._list:
            jlv = jlv - 1 # try to use less jittery version if we don't have corresponding version of actions
        #END while
        if jlv < 0:
            return [] # if there is no version of actions, return empty list
        #END if

        actions = []
        if len(self._list[jlv][EmpathyBehaviorButton.INDEX_MOTION]) > 0:
            val = random.randint(0, len(self._list[jlv][EmpathyBehaviorButton.INDEX_MOTION]) - 1)
            actions.append(Stiffness(1.0))
            actions.append(Motion(motion = self._list[jlv][EmpathyBehaviorButton.INDEX_MOTION][val], blocking = self._motion_blocks))
        #END if
        if len(self._list[jlv][EmpathyBehaviorButton.INDEX_ACTIONS]) > 0:
            val = random.randint(0, len(self._list[jlv][EmpathyBehaviorButton.INDEX_ACTIONS]) - 1)
            actions = actions + self._list[jlv][EmpathyBehaviorButton.INDEX_ACTIONS][val]
        #END if
        return actions
    #END getRobotActions()

    def maxLevel(self):
        return self._maxLevel
    #END maxLevel()

    @staticmethod
    def initialize():
        random.seed()
        EmpathyBehaviorButton._initMotions()
        EmpathyBehaviorButton._initBehaviors()
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
    def getMotions():
        return EmpathyBehaviorButton._motions.keys()
    #END getMotions()

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
        EmpathyBehaviorButton._motions["0_Idle1"] = NaoMotionList.find("Idle1").applySpeed(1.0)
        EmpathyBehaviorButton._motions["1_Idle1"] = NaoMotionList.find("Idle1").applySpeed(1.0).applyRepeat(2, 3, repeats = 3, repeatSpeed = 2.0)
        EmpathyBehaviorButton._motions["2_Idle1"] = NaoMotionList.find("Idle1").applySpeed(1.0).applyRepeat(3, 4, repeats = 4, repeatSpeed = 4.2)
        EmpathyBehaviorButton._motions["3_Idle1"] = NaoMotionList.find("Idle1").applySpeed(1.0).applyRepeat(3, 6, repeats = 4, repeatSpeed = 4.2)
        EmpathyBehaviorButton._motions["4_Idle1"] = NaoMotionList.find("Idle1").applySpeed(1.3).applyRepeat(3, 6, repeats = 6, repeatSpeed = 5.0)
        EmpathyBehaviorButton._motions["5_Idle1"] = NaoMotionList.find("Idle1").applySpeed(1.6).applyRepeat(1, 5, repeats = 4, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["0_Idle2"] = NaoMotionList.find("Idle2").applySpeed(1.0)
        EmpathyBehaviorButton._motions["1_Idle2"] = NaoMotionList.find("Idle2").applySpeed(1.0).applyRepeat(2, 3, repeats = 3, repeatSpeed = 2.0)
        EmpathyBehaviorButton._motions["2_Idle2"] = NaoMotionList.find("Idle2").applySpeed(1.0).applyRepeat(3, 4, repeats = 4, repeatSpeed = 4.2)
        EmpathyBehaviorButton._motions["3_Idle2"] = NaoMotionList.find("Idle2").applySpeed(1.0).applyRepeat(3, 6, repeats = 4, repeatSpeed = 4.2)
        EmpathyBehaviorButton._motions["4_Idle2"] = NaoMotionList.find("Idle2").applySpeed(1.3).applyRepeat(3, 6, repeats = 6, repeatSpeed = 5.0)
        EmpathyBehaviorButton._motions["5_Idle2"] = NaoMotionList.find("Idle2").applySpeed(1.6).applyRepeat(1, 5, repeats = 4, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["0_Idle3"] = NaoMotionList.find("Idle3").applySpeed(1.0)
        EmpathyBehaviorButton._motions["1_Idle3"] = NaoMotionList.find("Idle3").applySpeed(1.0).applyRepeat(2, 3, repeats = 3, repeatSpeed = 2.0)
        EmpathyBehaviorButton._motions["2_Idle3"] = NaoMotionList.find("Idle3").applySpeed(1.0).applyRepeat(3, 4, repeats = 4, repeatSpeed = 4.2)
        EmpathyBehaviorButton._motions["3_Idle3"] = NaoMotionList.find("Idle3").applySpeed(1.0).applyRepeat(3, 6, repeats = 4, repeatSpeed = 4.2)
        EmpathyBehaviorButton._motions["4_Idle3"] = NaoMotionList.find("Idle3").applySpeed(1.3).applyRepeat(3, 6, repeats = 6, repeatSpeed = 5.0)
        EmpathyBehaviorButton._motions["5_Idle3"] = NaoMotionList.find("Idle3").applySpeed(1.6).applyRepeat(1, 5, repeats = 4, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["0_Idle4"] = NaoMotionList.find("Idle4").applySpeed(1.0)
        EmpathyBehaviorButton._motions["1_Idle4"] = NaoMotionList.find("Idle4").applySpeed(1.0).applyRepeat(2, 3, repeats = 3, repeatSpeed = 2.0)
        EmpathyBehaviorButton._motions["2_Idle4"] = NaoMotionList.find("Idle4").applySpeed(1.0).applyRepeat(3, 4, repeats = 4, repeatSpeed = 4.2)
        EmpathyBehaviorButton._motions["3_Idle4"] = NaoMotionList.find("Idle4").applySpeed(1.0).applyRepeat(3, 6, repeats = 4, repeatSpeed = 4.2)
        EmpathyBehaviorButton._motions["4_Idle4"] = NaoMotionList.find("Idle4").applySpeed(1.3).applyRepeat(3, 6, repeats = 6, repeatSpeed = 5.0)
        EmpathyBehaviorButton._motions["5_Idle4"] = NaoMotionList.find("Idle4").applySpeed(1.6).applyRepeat(1, 5, repeats = 4, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["0_Disagree"] = NaoMotionList.find("Disagree").applySpeed(1.3)
        EmpathyBehaviorButton._motions["1_Disagree"] = NaoMotionList.find("Disagree").applySpeed(1.4).applyRepeat(1, 3, repeats = 3, repeatSpeed = 1.7)
        EmpathyBehaviorButton._motions["2_Disagree"] = NaoMotionList.find("Disagree").applySpeed(1.4).applyRepeat(1, 3, repeats = 3, repeatSpeed = 2.4)
        EmpathyBehaviorButton._motions["3_Disagree"] = NaoMotionList.find("Disagree").applySpeed(1.4).applyRepeat(0, 3, repeats = 4, repeatSpeed = 3.2)
        EmpathyBehaviorButton._motions["4_Disagree"] = NaoMotionList.find("Disagree").applySpeed(1.5).applyRepeat(0, 3, repeats = 4, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["5_Disagree"] = NaoMotionList.find("Disagree").applySpeed(1.7).applyRepeat(0, 3, repeats = 5, repeatSpeed = 4.5)
        EmpathyBehaviorButton._motions["0_DisagreeLeft"] = NaoMotionList.find("DisagreeLeft").applySpeed(1.3)
        EmpathyBehaviorButton._motions["1_DisagreeLeft"] = NaoMotionList.find("DisagreeLeft").applySpeed(1.4).applyRepeat(1, 3, repeats = 3, repeatSpeed = 1.7)
        EmpathyBehaviorButton._motions["2_DisagreeLeft"] = NaoMotionList.find("DisagreeLeft").applySpeed(1.4).applyRepeat(1, 3, repeats = 3, repeatSpeed = 2.4)
        EmpathyBehaviorButton._motions["3_DisagreeLeft"] = NaoMotionList.find("DisagreeLeft").applySpeed(1.4).applyRepeat(0, 3, repeats = 4, repeatSpeed = 3.2)
        EmpathyBehaviorButton._motions["4_DisagreeLeft"] = NaoMotionList.find("DisagreeLeft").applySpeed(1.5).applyRepeat(0, 3, repeats = 4, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["5_DisagreeLeft"] = NaoMotionList.find("DisagreeLeft").applySpeed(1.7).applyRepeat(0, 3, repeats = 5, repeatSpeed = 4.5)
        EmpathyBehaviorButton._motions["0_DisagreeRight"] = NaoMotionList.find("DisagreeRight").applySpeed(1.3)
        EmpathyBehaviorButton._motions["1_DisagreeRight"] = NaoMotionList.find("DisagreeRight").applySpeed(1.4).applyRepeat(1, 3, repeats = 3, repeatSpeed = 1.7)
        EmpathyBehaviorButton._motions["2_DisagreeRight"] = NaoMotionList.find("DisagreeRight").applySpeed(1.4).applyRepeat(1, 3, repeats = 3, repeatSpeed = 2.4)
        EmpathyBehaviorButton._motions["3_DisagreeRight"] = NaoMotionList.find("DisagreeRight").applySpeed(1.4).applyRepeat(0, 3, repeats = 4, repeatSpeed = 3.2)
        EmpathyBehaviorButton._motions["4_DisagreeRight"] = NaoMotionList.find("DisagreeRight").applySpeed(1.5).applyRepeat(0, 3, repeats = 4, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["5_DisagreeRight"] = NaoMotionList.find("DisagreeRight").applySpeed(1.7).applyRepeat(0, 3, repeats = 5, repeatSpeed = 4.5)
        EmpathyBehaviorButton._motions["0_DontKnow"] = NaoMotionList.find("DontKnow").applySpeed(2.0)
        EmpathyBehaviorButton._motions["1_DontKnow"] = NaoMotionList.find("DontKnow").applySpeed(2.0).applyRepeat(5, 6, repeats = 3, repeatSpeed = 1.5)
        EmpathyBehaviorButton._motions["2_DontKnow"] = NaoMotionList.find("DontKnow").applySpeed(2.1).applyRepeat(5, 6, repeats = 4, repeatSpeed = 3.0)
        EmpathyBehaviorButton._motions["3_DontKnow"] = NaoMotionList.find("DontKnow").applySpeed(2.1).applyRepeat(4, 6, repeats = 4, repeatSpeed = 3.0)
        EmpathyBehaviorButton._motions["4_DontKnow"] = NaoMotionList.find("DontKnow").applySpeed(2.1).applyRepeat(3, 5, repeats = 5, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["5_DontKnow"] = NaoMotionList.find("DontKnow").applySpeed(2.2).applyRepeat(3, 6, repeats = 5, repeatSpeed = 5.0)
        EmpathyBehaviorButton._motions["0_DontKnowLeft"] = NaoMotionList.find("DontKnowLeft").applySpeed(1.5)
        EmpathyBehaviorButton._motions["1_DontKnowLeft"] = NaoMotionList.find("DontKnowLeft").applySpeed(1.5).applyRepeat(5, 6, repeats = 3, repeatSpeed = 1.5)
        EmpathyBehaviorButton._motions["2_DontKnowLeft"] = NaoMotionList.find("DontKnowLeft").applySpeed(1.6).applyRepeat(5, 6, repeats = 4, repeatSpeed = 3.0)
        EmpathyBehaviorButton._motions["3_DontKnowLeft"] = NaoMotionList.find("DontKnowLeft").applySpeed(1.6).applyRepeat(4, 6, repeats = 4, repeatSpeed = 3.0)
        EmpathyBehaviorButton._motions["4_DontKnowLeft"] = NaoMotionList.find("DontKnowLeft").applySpeed(1.6).applyRepeat(3, 5, repeats = 5, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["5_DontKnowLeft"] = NaoMotionList.find("DontKnowLeft").applySpeed(1.7).applyRepeat(3, 6, repeats = 5, repeatSpeed = 5.0)
        EmpathyBehaviorButton._motions["0_DontKnowRight"] = NaoMotionList.find("DontKnowRight").applySpeed(1.5)
        EmpathyBehaviorButton._motions["1_DontKnowRight"] = NaoMotionList.find("DontKnowRight").applySpeed(1.5).applyRepeat(5, 6, repeats = 3, repeatSpeed = 1.5)
        EmpathyBehaviorButton._motions["2_DontKnowRight"] = NaoMotionList.find("DontKnowRight").applySpeed(1.6).applyRepeat(5, 6, repeats = 4, repeatSpeed = 3.0)
        EmpathyBehaviorButton._motions["3_DontKnowRight"] = NaoMotionList.find("DontKnowRight").applySpeed(1.6).applyRepeat(4, 6, repeats = 4, repeatSpeed = 3.0)
        EmpathyBehaviorButton._motions["4_DontKnowRight"] = NaoMotionList.find("DontKnowRight").applySpeed(1.6).applyRepeat(3, 5, repeats = 5, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["5_DontKnowRight"] = NaoMotionList.find("DontKnowRight").applySpeed(1.7).applyRepeat(3, 6, repeats = 5, repeatSpeed = 5.0)
        EmpathyBehaviorButton._motions["0_Wait"] = NaoMotionList.find("Wait").applySpeed(1.5)
        EmpathyBehaviorButton._motions["0_WaveHandLeft"] = NaoMotionList.find("WaveHandLeft").applySpeed(1.25)
        EmpathyBehaviorButton._motions["0_WaveHandRight"] = NaoMotionList.find("WaveHandRight").applySpeed(1.25)
        EmpathyBehaviorButton._motions["0_ForgetItLeft"] = NaoMotionList.find("ForgetItLeft").applySpeed(1.9)
        EmpathyBehaviorButton._motions["1_ForgetItLeft"] = NaoMotionList.find("ForgetItLeft").applySpeed(2.0).applyRepeat(6, 7, repeats = 3, repeatSpeed = 2.0)
        EmpathyBehaviorButton._motions["2_ForgetItLeft"] = NaoMotionList.find("ForgetItLeft").applySpeed(2.0).applyRepeat(6, 7, repeats = 3, repeatSpeed = 3.0)
        EmpathyBehaviorButton._motions["3_ForgetItLeft"] = NaoMotionList.find("ForgetItLeft").applySpeed(2.0).applyRepeat(6, 8, repeats = 3, repeatSpeed = 2.6)
        EmpathyBehaviorButton._motions["4_ForgetItLeft"] = NaoMotionList.find("ForgetItLeft").applySpeed(2.0).applyRepeat(6, 8, repeats = 3, repeatSpeed = 3.5)
        EmpathyBehaviorButton._motions["5_ForgetItLeft"] = NaoMotionList.find("ForgetItLeft").applySpeed(2.2).applyRepeat(5, 8, repeats = 3, repeatSpeed = 5.0)
        EmpathyBehaviorButton._motions["0_ForgetItRight"] = NaoMotionList.find("ForgetItRight").applySpeed(1.9)
        EmpathyBehaviorButton._motions["1_ForgetItRight"] = NaoMotionList.find("ForgetItRight").applySpeed(2.0).applyRepeat(6, 7, repeats = 3, repeatSpeed = 2.0)
        EmpathyBehaviorButton._motions["2_ForgetItRight"] = NaoMotionList.find("ForgetItRight").applySpeed(2.0).applyRepeat(6, 7, repeats = 3, repeatSpeed = 3.0)
        EmpathyBehaviorButton._motions["3_ForgetItRight"] = NaoMotionList.find("ForgetItRight").applySpeed(2.0).applyRepeat(6, 8, repeats = 3, repeatSpeed = 2.6)
        EmpathyBehaviorButton._motions["4_ForgetItRight"] = NaoMotionList.find("ForgetItRight").applySpeed(2.0).applyRepeat(6, 8, repeats = 3, repeatSpeed = 3.5)
        EmpathyBehaviorButton._motions["5_ForgetItRight"] = NaoMotionList.find("ForgetItRight").applySpeed(2.2).applyRepeat(5, 8, repeats = 3, repeatSpeed = 5.0)
        EmpathyBehaviorButton._motions["0_OhYesLeft"] = NaoMotionList.find("OhYesLeft").applySpeed(1.8)
        EmpathyBehaviorButton._motions["0_OhYesRight"] = NaoMotionList.find("OhYesRight").applySpeed(1.8)
        EmpathyBehaviorButton._motions["0_PalmUp"] = NaoMotionList.find("PalmUp").applySpeed(1.7)
        EmpathyBehaviorButton._motions["1_PalmUp"] = NaoMotionList.find("PalmUp").applySpeed(1.7).applyRepeat(2, 3, repeats = 3, repeatSpeed = 2.4)
        EmpathyBehaviorButton._motions["2_PalmUp"] = NaoMotionList.find("PalmUp").applySpeed(1.7).applyRepeat(2, 3, repeats = 3, repeatSpeed = 3.6)
        EmpathyBehaviorButton._motions["3_PalmUp"] = NaoMotionList.find("PalmUp").applySpeed(1.8).applyRepeat(3, 4, repeats = 4, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["4_PalmUp"] = NaoMotionList.find("PalmUp").applySpeed(1.8).applyRepeat(2, 4, repeats = 3, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["5_PalmUp"] = NaoMotionList.find("PalmUp").applySpeed(1.8).applyRepeat(2, 4, repeats = 5, repeatSpeed = 5.0)
        EmpathyBehaviorButton._motions["0_PalmUpLeft"] = NaoMotionList.find("PalmUpLeft").applySpeed(1.7)
        EmpathyBehaviorButton._motions["1_PalmUpLeft"] = NaoMotionList.find("PalmUpLeft").applySpeed(1.7).applyRepeat(2, 3, repeats = 3, repeatSpeed = 2.4)
        EmpathyBehaviorButton._motions["2_PalmUpLeft"] = NaoMotionList.find("PalmUpLeft").applySpeed(1.7).applyRepeat(2, 3, repeats = 3, repeatSpeed = 3.6)
        EmpathyBehaviorButton._motions["3_PalmUpLeft"] = NaoMotionList.find("PalmUpLeft").applySpeed(1.8).applyRepeat(3, 4, repeats = 4, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["4_PalmUpLeft"] = NaoMotionList.find("PalmUpLeft").applySpeed(1.8).applyRepeat(2, 4, repeats = 3, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["5_PalmUpLeft"] = NaoMotionList.find("PalmUpLeft").applySpeed(1.8).applyRepeat(2, 4, repeats = 5, repeatSpeed = 5.0)
        EmpathyBehaviorButton._motions["0_PalmUpRight"] = NaoMotionList.find("PalmUpRight").applySpeed(1.7)
        EmpathyBehaviorButton._motions["1_PalmUpRight"] = NaoMotionList.find("PalmUpRight").applySpeed(1.7).applyRepeat(2, 3, repeats = 3, repeatSpeed = 2.4)
        EmpathyBehaviorButton._motions["2_PalmUpRight"] = NaoMotionList.find("PalmUpRight").applySpeed(1.7).applyRepeat(2, 3, repeats = 3, repeatSpeed = 3.6)
        EmpathyBehaviorButton._motions["3_PalmUpRight"] = NaoMotionList.find("PalmUpRight").applySpeed(1.8).applyRepeat(3, 4, repeats = 4, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["4_PalmUpRight"] = NaoMotionList.find("PalmUpRight").applySpeed(1.8).applyRepeat(2, 4, repeats = 3, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["5_PalmUpRight"] = NaoMotionList.find("PalmUpRight").applySpeed(1.8).applyRepeat(2, 4, repeats = 5, repeatSpeed = 5.0)
        EmpathyBehaviorButton._motions["0_PointMyself"] = NaoMotionList.find("PointMyself").applySpeed(2.0)
        EmpathyBehaviorButton._motions["1_PointMyself"] = NaoMotionList.find("PointMyself").applySpeed(2.0).applyRepeat(1, 3, repeats = 3, repeatSpeed = 1.7)
        EmpathyBehaviorButton._motions["2_PointMyself"] = NaoMotionList.find("PointMyself").applySpeed(2.0).applyRepeat(1, 3, repeats = 3, repeatSpeed = 2.4)
        EmpathyBehaviorButton._motions["3_PointMyself"] = NaoMotionList.find("PointMyself").applySpeed(2.0).applyRepeat(0, 3, repeats = 3, repeatSpeed = 2.9)
        EmpathyBehaviorButton._motions["4_PointMyself"] = NaoMotionList.find("PointMyself").applySpeed(2.0).applyRepeat(0, 3, repeats = 3, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["5_PointMyself"] = NaoMotionList.find("PointMyself").applySpeed(2.1).applyRepeat(0, 4, repeats = 4, repeatSpeed = 5.0)
        EmpathyBehaviorButton._motions["0_PointMyselfLeft"] = NaoMotionList.find("PointMyselfLeft").applySpeed(2.0)
        EmpathyBehaviorButton._motions["1_PointMyselfLeft"] = NaoMotionList.find("PointMyselfLeft").applySpeed(2.0).applyRepeat(1, 3, repeats = 3, repeatSpeed = 1.7)
        EmpathyBehaviorButton._motions["2_PointMyselfLeft"] = NaoMotionList.find("PointMyselfLeft").applySpeed(2.0).applyRepeat(1, 3, repeats = 3, repeatSpeed = 2.4)
        EmpathyBehaviorButton._motions["3_PointMyselfLeft"] = NaoMotionList.find("PointMyselfLeft").applySpeed(2.0).applyRepeat(0, 3, repeats = 3, repeatSpeed = 2.9)
        EmpathyBehaviorButton._motions["4_PointMyselfLeft"] = NaoMotionList.find("PointMyselfLeft").applySpeed(2.0).applyRepeat(0, 3, repeats = 3, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["5_PointMyselfLeft"] = NaoMotionList.find("PointMyselfLeft").applySpeed(2.1).applyRepeat(0, 4, repeats = 4, repeatSpeed = 5.0)
        EmpathyBehaviorButton._motions["0_PointMyselfRight"] = NaoMotionList.find("PointMyselfRight").applySpeed(2.0)
        EmpathyBehaviorButton._motions["1_PointMyselfRight"] = NaoMotionList.find("PointMyselfRight").applySpeed(2.0).applyRepeat(1, 3, repeats = 3, repeatSpeed = 1.7)
        EmpathyBehaviorButton._motions["2_PointMyselfRight"] = NaoMotionList.find("PointMyselfRight").applySpeed(2.0).applyRepeat(1, 3, repeats = 3, repeatSpeed = 2.4)
        EmpathyBehaviorButton._motions["3_PointMyselfRight"] = NaoMotionList.find("PointMyselfRight").applySpeed(2.0).applyRepeat(0, 3, repeats = 3, repeatSpeed = 2.9)
        EmpathyBehaviorButton._motions["4_PointMyselfRight"] = NaoMotionList.find("PointMyselfRight").applySpeed(2.0).applyRepeat(0, 3, repeats = 3, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["5_PointMyselfRight"] = NaoMotionList.find("PointMyselfRight").applySpeed(2.1).applyRepeat(0, 4, repeats = 4, repeatSpeed = 5.0)
        EmpathyBehaviorButton._motions["0_PointYou"] = NaoMotionList.find("PointYou").applySpeed(1.8)
        EmpathyBehaviorButton._motions["1_PointYou"] = NaoMotionList.find("PointYou").applySpeed(1.8).applyRepeat(4, 7, repeats = 3, repeatSpeed = 2.2)
        EmpathyBehaviorButton._motions["2_PointYou"] = NaoMotionList.find("PointYou").applySpeed(2.0).applyRepeat(4, 7, repeats = 4, repeatSpeed = 2.7)
        EmpathyBehaviorButton._motions["3_PointYou"] = NaoMotionList.find("PointYou").applySpeed(2.0).applyRepeat(3, 6, repeats = 4, repeatSpeed = 3.4)
        EmpathyBehaviorButton._motions["4_PointYou"] = NaoMotionList.find("PointYou").applySpeed(2.1).applyRepeat(3, 7, repeats = 4, repeatSpeed = 4.2)
        EmpathyBehaviorButton._motions["5_PointYou"] = NaoMotionList.find("PointYou").applySpeed(2.3).applyRepeat(3, 7, repeats = 4, repeatSpeed = 5.0)
        EmpathyBehaviorButton._motions["0_PointYouLeft"] = NaoMotionList.find("PointYouLeft").applySpeed(1.8)
        EmpathyBehaviorButton._motions["1_PointYouLeft"] = NaoMotionList.find("PointYouLeft").applySpeed(1.8).applyRepeat(4, 7, repeats = 3, repeatSpeed = 2.2)
        EmpathyBehaviorButton._motions["2_PointYouLeft"] = NaoMotionList.find("PointYouLeft").applySpeed(2.0).applyRepeat(4, 7, repeats = 4, repeatSpeed = 2.7)
        EmpathyBehaviorButton._motions["3_PointYouLeft"] = NaoMotionList.find("PointYouLeft").applySpeed(2.0).applyRepeat(3, 6, repeats = 4, repeatSpeed = 3.4)
        EmpathyBehaviorButton._motions["4_PointYouLeft"] = NaoMotionList.find("PointYouLeft").applySpeed(2.1).applyRepeat(3, 7, repeats = 4, repeatSpeed = 4.2)
        EmpathyBehaviorButton._motions["5_PointYouLeft"] = NaoMotionList.find("PointYouLeft").applySpeed(2.3).applyRepeat(3, 7, repeats = 4, repeatSpeed = 5.0)
        EmpathyBehaviorButton._motions["0_PointYouRight"] = NaoMotionList.find("PointYouRight").applySpeed(1.8)
        EmpathyBehaviorButton._motions["1_PointYouRight"] = NaoMotionList.find("PointYouRight").applySpeed(1.8).applyRepeat(4, 7, repeats = 3, repeatSpeed = 2.2)
        EmpathyBehaviorButton._motions["2_PointYouRight"] = NaoMotionList.find("PointYouRight").applySpeed(2.0).applyRepeat(4, 7, repeats = 4, repeatSpeed = 2.7)
        EmpathyBehaviorButton._motions["3_PointYouRight"] = NaoMotionList.find("PointYouRight").applySpeed(2.0).applyRepeat(3, 6, repeats = 4, repeatSpeed = 3.4)
        EmpathyBehaviorButton._motions["4_PointYouRight"] = NaoMotionList.find("PointYouRight").applySpeed(2.1).applyRepeat(3, 7, repeats = 4, repeatSpeed = 4.2)
        EmpathyBehaviorButton._motions["5_PointYouRight"] = NaoMotionList.find("PointYouRight").applySpeed(2.3).applyRepeat(3, 7, repeats = 4, repeatSpeed = 5.0)
        EmpathyBehaviorButton._motions["0_ChinHoldLeft"] = NaoMotionList.find("ChinHoldLeft").applySpeed(1.5)
        EmpathyBehaviorButton._motions["1_ChinHoldLeft"] = NaoMotionList.find("ChinHoldLeft").applySpeed(1.5).applyRepeat(3, 5, repeats = 3, repeatSpeed = 1.9)
        EmpathyBehaviorButton._motions["2_ChinHoldLeft"] = NaoMotionList.find("ChinHoldLeft").applySpeed(1.5).applyRepeat(2, 5, repeats = 3, repeatSpeed = 2.5)
        EmpathyBehaviorButton._motions["3_ChinHoldLeft"] = NaoMotionList.find("ChinHoldLeft").applySpeed(1.6).applyRepeat(2, 5, repeats = 3, repeatSpeed = 3.2)
        EmpathyBehaviorButton._motions["4_ChinHoldLeft"] = NaoMotionList.find("ChinHoldLeft").applySpeed(1.7).applyRepeat(2, 5, repeats = 4, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["5_ChinHoldLeft"] = NaoMotionList.find("ChinHoldLeft").applySpeed(1.8).applyRepeat(1, 5, repeats = 3, repeatSpeed = 5.0)
        EmpathyBehaviorButton._motions["0_ChinHoldRight"] = NaoMotionList.find("ChinHoldRight").applySpeed(1.5)
        EmpathyBehaviorButton._motions["1_ChinHoldRight"] = NaoMotionList.find("ChinHoldRight").applySpeed(1.5).applyRepeat(3, 5, repeats = 3, repeatSpeed = 1.9)
        EmpathyBehaviorButton._motions["2_ChinHoldRight"] = NaoMotionList.find("ChinHoldRight").applySpeed(1.5).applyRepeat(2, 5, repeats = 3, repeatSpeed = 2.5)
        EmpathyBehaviorButton._motions["3_ChinHoldRight"] = NaoMotionList.find("ChinHoldRight").applySpeed(1.6).applyRepeat(2, 5, repeats = 3, repeatSpeed = 3.2)
        EmpathyBehaviorButton._motions["4_ChinHoldRight"] = NaoMotionList.find("ChinHoldRight").applySpeed(1.7).applyRepeat(2, 5, repeats = 4, repeatSpeed = 4.0)
        EmpathyBehaviorButton._motions["5_ChinHoldRight"] = NaoMotionList.find("ChinHoldRight").applySpeed(1.8).applyRepeat(1, 5, repeats = 3, repeatSpeed = 5.0)
        EmpathyBehaviorButton._motions["0_WhisperLeft"] = NaoMotionList.find("WhisperLeft").applySpeed(2.5)
        EmpathyBehaviorButton._motions["4_WhisperLeft"] = NaoMotionList.find("WhisperLeft").applySpeed(2.5).applyRepeat(10, 12, repeats = 10, repeatSpeed = 2.0)
        EmpathyBehaviorButton._motions["0_WhisperRight"] = NaoMotionList.find("WhisperRight").applySpeed(2.5)
        EmpathyBehaviorButton._motions["4_WhisperRight"] = NaoMotionList.find("WhisperRight").applySpeed(2.5).applyRepeat(10, 12, repeats = 10, repeatSpeed = 2.0)
    #END _initMotions()

    @staticmethod
    def _initBehaviors():
        bhv = EmpathyBehaviorButton("Idle (Big)", True)
        for i in range(10):
            bhv.add(i, motion = str(i) + "_ChinHoldLeft")
            bhv.add(i, motion = str(i) + "_ChinHoldRight")
            bhv.add(i, motion = str(i) + "_Idle1")
            bhv.add(i, motion = str(i) + "_Idle2")
            bhv.add(i, motion = str(i) + "_Idle3")
            bhv.add(i, motion = str(i) + "_Idle4")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Idle (Small)", True)
        for i in range(10):
            bhv.add(i, motion = str(i) + "_Idle1")
            bhv.add(i, motion = str(i) + "_Idle2")
            bhv.add(i, motion = str(i) + "_Idle3")
            bhv.add(i, motion = str(i) + "_Idle4")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("#")
        bhv.add(0, [Speech("I believe the answer is,")])
        bhv.add(0, [Speech("I believe the number is,")])
        bhv.add(0, [Speech("I believe the value is,")])
        bhv.add(0, [Speech("I guess the answer is,")])
        bhv.add(0, [Speech("I guess the number is,")])
        bhv.add(0, [Speech("I guess the value is,")])
        bhv.add(0, [Speech("I think the answer is,")])
        bhv.add(0, [Speech("I think the number is,")])
        bhv.add(0, [Speech("I think the value is,")])
        bhv.add(0, [Speech("The answer is,")])
        bhv.add(0, [Speech("The number is,")])
        bhv.add(0, [Speech("The value is,")])
        bhv.add(1, [Speech("I believe" + EmpathyBehaviorButton._markSpeech(110) + "the answer is,", speed = 50)])
        bhv.add(1, [Speech("I believe" + EmpathyBehaviorButton._markSpeech(110) + "the number is,", speed = 50)])
        bhv.add(1, [Speech("I believe" + EmpathyBehaviorButton._markSpeech(110) + "the value is,", speed = 50)])
        bhv.add(1, [Speech("I guess" + EmpathyBehaviorButton._markSpeech(110) + "the answer is,", speed = 50)])
        bhv.add(1, [Speech("I guess" + EmpathyBehaviorButton._markSpeech(110) + "the number is,", speed = 50)])
        bhv.add(1, [Speech("I guess" + EmpathyBehaviorButton._markSpeech(110) + "the value is,", speed = 50)])
        bhv.add(1, [Speech("I think" + EmpathyBehaviorButton._markSpeech(110) + "the answer is,", speed = 50)])
        bhv.add(1, [Speech("I think" + EmpathyBehaviorButton._markSpeech(110) + "the number is,", speed = 50)])
        bhv.add(1, [Speech("I think" + EmpathyBehaviorButton._markSpeech(110) + "the value is,", speed = 50)])
        bhv.add(1, [Speech("The answer" + EmpathyBehaviorButton._markSpeech(110) + "is,", speed = 50)])
        bhv.add(1, [Speech("The number" + EmpathyBehaviorButton._markSpeech(110) + "is,", speed = 50)])
        bhv.add(1, [Speech("The value" + EmpathyBehaviorButton._markSpeech(110) + "is,", speed = 50)])
        bhv.add(2, [Speech("I believe" + EmpathyBehaviorButton._markSpeech(110) + "the answer is,", speed = 50, shaping = 110)])
        bhv.add(2, [Speech("I believe" + EmpathyBehaviorButton._markSpeech(110) + "the number is,", speed = 50, shaping = 110)])
        bhv.add(2, [Speech("I believe" + EmpathyBehaviorButton._markSpeech(110) + "the value is,", speed = 50, shaping = 110)])
        bhv.add(2, [Speech("I guess" + EmpathyBehaviorButton._markSpeech(110) + "the answer is,", speed = 50, shaping = 110)])
        bhv.add(2, [Speech("I guess" + EmpathyBehaviorButton._markSpeech(110) + "the number is,", speed = 50, shaping = 110)])
        bhv.add(2, [Speech("I guess" + EmpathyBehaviorButton._markSpeech(110) + "the value is,", speed = 50, shaping = 110)])
        bhv.add(2, [Speech("I think" + EmpathyBehaviorButton._markSpeech(110) + "the answer is,", speed = 50, shaping = 110)])
        bhv.add(2, [Speech("I think" + EmpathyBehaviorButton._markSpeech(110) + "the number is,", speed = 50, shaping = 110)])
        bhv.add(2, [Speech("I think" + EmpathyBehaviorButton._markSpeech(110) + "the value is,", speed = 50, shaping = 110)])
        bhv.add(2, [Speech("The answer" + EmpathyBehaviorButton._markSpeech(110) + "is,", speed = 50, shaping = 110)])
        bhv.add(2, [Speech("The number" + EmpathyBehaviorButton._markSpeech(110) + "is,", speed = 50, shaping = 110)])
        bhv.add(2, [Speech("The value" + EmpathyBehaviorButton._markSpeech(110) + "is,", speed = 50, shaping = 110)])
        bhv.add(3, [Speech("I believe" + EmpathyBehaviorButton._markSpeech(115) + "the answer is,", speed = 50, shaping = 110)])
        bhv.add(3, [Speech("I believe" + EmpathyBehaviorButton._markSpeech(115) + "the number is,", speed = 50, shaping = 110)])
        bhv.add(3, [Speech("I believe" + EmpathyBehaviorButton._markSpeech(115) + "the value is,", speed = 50, shaping = 110)])
        bhv.add(3, [Speech("I guess" + EmpathyBehaviorButton._markSpeech(115) + "the answer is,", speed = 50, shaping = 110)])
        bhv.add(3, [Speech("I guess" + EmpathyBehaviorButton._markSpeech(115) + "the number is,", speed = 50, shaping = 110)])
        bhv.add(3, [Speech("I guess" + EmpathyBehaviorButton._markSpeech(115) + "the value is,", speed = 50, shaping = 110)])
        bhv.add(3, [Speech("I think" + EmpathyBehaviorButton._markSpeech(115) + "the answer is,", speed = 50, shaping = 110)])
        bhv.add(3, [Speech("I think" + EmpathyBehaviorButton._markSpeech(115) + "the number is,", speed = 50, shaping = 110)])
        bhv.add(3, [Speech("I think" + EmpathyBehaviorButton._markSpeech(115) + "the value is,", speed = 50, shaping = 110)])
        bhv.add(3, [Speech("The answer" + EmpathyBehaviorButton._markSpeech(115) + "is,", speed = 50, shaping = 110)])
        bhv.add(3, [Speech("The number" + EmpathyBehaviorButton._markSpeech(115) + "is,", speed = 50, shaping = 110)])
        bhv.add(3, [Speech("The value" + EmpathyBehaviorButton._markSpeech(115) + "is,", speed = 50, shaping = 110)])
        bhv.add(4, [Speech("I believe" + EmpathyBehaviorButton._markSpeech(120) + "the answer is,", speed = 50, shaping = 115)])
        bhv.add(4, [Speech("I believe" + EmpathyBehaviorButton._markSpeech(120) + "the number is,", speed = 50, shaping = 115)])
        bhv.add(4, [Speech("I believe" + EmpathyBehaviorButton._markSpeech(120) + "the value is,", speed = 50, shaping = 115)])
        bhv.add(4, [Speech("I guess" + EmpathyBehaviorButton._markSpeech(120) + "the answer is,", speed = 50, shaping = 115)])
        bhv.add(4, [Speech("I guess" + EmpathyBehaviorButton._markSpeech(120) + "the number is,", speed = 50, shaping = 115)])
        bhv.add(4, [Speech("I guess" + EmpathyBehaviorButton._markSpeech(120) + "the value is,", speed = 50, shaping = 115)])
        bhv.add(4, [Speech("I think" + EmpathyBehaviorButton._markSpeech(120) + "the answer is,", speed = 50, shaping = 115)])
        bhv.add(4, [Speech("I think" + EmpathyBehaviorButton._markSpeech(120) + "the number is,", speed = 50, shaping = 115)])
        bhv.add(4, [Speech("I think" + EmpathyBehaviorButton._markSpeech(120) + "the value is,", speed = 50, shaping = 115)])
        bhv.add(4, [Speech("The answer" + EmpathyBehaviorButton._markSpeech(120) + "is,", speed = 50, shaping = 115)])
        bhv.add(4, [Speech("The number" + EmpathyBehaviorButton._markSpeech(120) + "is,", speed = 50, shaping = 115)])
        bhv.add(4, [Speech("The value" + EmpathyBehaviorButton._markSpeech(120) + "is,", speed = 50, shaping = 115)])
        bhv.add(5, [Speech("I believe" + EmpathyBehaviorButton._markSpeech(125) + "the answer is,", speed = 70, shaping = 120)])
        bhv.add(5, [Speech("I believe" + EmpathyBehaviorButton._markSpeech(125) + "the number is,", speed = 70, shaping = 120)])
        bhv.add(5, [Speech("I believe" + EmpathyBehaviorButton._markSpeech(125) + "the value is,", speed = 70, shaping = 120)])
        bhv.add(5, [Speech("I guess" + EmpathyBehaviorButton._markSpeech(125) + "the answer is,", speed = 70, shaping = 120)])
        bhv.add(5, [Speech("I guess" + EmpathyBehaviorButton._markSpeech(125) + "the number is,", speed = 70, shaping = 120)])
        bhv.add(5, [Speech("I guess" + EmpathyBehaviorButton._markSpeech(125) + "the value is,", speed = 70, shaping = 120)])
        bhv.add(5, [Speech("I think" + EmpathyBehaviorButton._markSpeech(125) + "the answer is,", speed = 70, shaping = 120)])
        bhv.add(5, [Speech("I think" + EmpathyBehaviorButton._markSpeech(125) + "the number is,", speed = 70, shaping = 120)])
        bhv.add(5, [Speech("I think" + EmpathyBehaviorButton._markSpeech(125) + "the value is,", speed = 70, shaping = 120)])
        bhv.add(5, [Speech("The answer" + EmpathyBehaviorButton._markSpeech(125) + "is,", speed = 70, shaping = 120)])
        bhv.add(5, [Speech("The number" + EmpathyBehaviorButton._markSpeech(125) + "is,", speed = 70, shaping = 120)])
        bhv.add(5, [Speech("The value" + EmpathyBehaviorButton._markSpeech(125) + "is,", speed = 70, shaping = 120)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PointMyself")
            bhv.add(i, motion = str(i) + "_PointMyselfLeft")
            bhv.add(i, motion = str(i) + "_PointMyselfRight")
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Good")
        bhv.add(0, [Speech("Good.")])
        bhv.add(0, [Speech("Cool.")])
        bhv.add(0, [Speech("Exactly.")])
        bhv.add(0, [Speech("Nice.")])
        bhv.add(0, [Speech("Perfect.")])
        bhv.add(0, [Speech("Yes.")])
        bhv.add(0, [Speech("Right.")])
        bhv.add(0, [Speech("I agree.")])
        bhv.add(0, [Speech("You are right.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PointMyselfLeft")
            bhv.add(i, motion = str(i) + "_PointMyselfRight")
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("How are you?")
        bhv.add(0, [Speech("How are you today?")])
        bhv.add(0, [Speech("How is it going?")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_DontKnowLeft")
            bhv.add(i, motion = str(i) + "_DontKnowRight")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Weather?")
        bhv.add(0, [Speech("How's the weather today?")])
        bhv.add(0, [Speech("Is the weather good today?")])
        bhv.add(0, [Speech("Is it sunny day?")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_DontKnow")
            bhv.add(i, motion = str(i) + "_DontKnowLeft")
            bhv.add(i, motion = str(i) + "_DontKnowRight")
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        #TODO more general items

        EmpathyBehaviorButton._behaviours.append(EmpathyBehaviorButton("\\CUT\\"))

        bhv = EmpathyBehaviorButton("Can't read")
        bhv.add(0, [Speech("I barely can read."), Speech("Tell me what you wrote.")])
        bhv.add(0, [Speech("I barely can read."), Speech("Can you hold it up?")])
        bhv.add(0, [Speech("I can't read."), Speech("Can you tell me what you wrote?")])
        bhv.add(0, [Speech("I can't read."), Speech("Can you hold it up?")])
        bhv.add(1, [Speech("I barely can read."), Speech("Teh- teh-" + EmpathyBehaviorButton._markSpeech() + "tell me what you wrote.", speed = 90, shaping = 130)])
        bhv.add(1, [Speech("I barely can read."), Speech("Can you ho- hold it up?")])
        bhv.add(1, [Speech("I can't read."), Speech("Can you" + EmpathyBehaviorButton._markSpeech(90, 130) + "teh- teh-" + EmpathyBehaviorButton._markSpeech() + "tell me what you wrote?")])
        bhv.add(1, [Speech("I can't read."), Speech("Can you ho- hold it up?")])
        bhv.add(2, [Speech("I barely can read."), Speech("Teh- teh- teh- teh-.", speed = 90, shaping = 130), Speech("Sorry. Tell me what you wrote.")])
        bhv.add(2, [Speech("I barely can" + EmpathyBehaviorButton._markSpeech(90, 140) + "read."), Speech("Can you hohohol- Can you hold it up?")])
        bhv.add(2, [Speech("I can't read."), Speech("Can you" + EmpathyBehaviorButton._markSpeech(90, 130) + "teh- teh- teh- teh-."), Speech("Sorry. Tell me what you wrote?")])
        bhv.add(2, [Speech("I can't" + EmpathyBehaviorButton._markSpeech(90, 140) + "read."), Speech("Can you hohohol- Can you hold it up?")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_Disagree")
            bhv.add(i, motion = str(i) + "_DisagreeLeft")
            bhv.add(i, motion = str(i) + "_DisagreeRight")
            bhv.add(i, motion = str(i) + "_DontKnow")
            bhv.add(i, motion = str(i) + "_DontKnowLeft")
            bhv.add(i, motion = str(i) + "_DontKnowRight")
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
            bhv.add(i, motion = str(i) + "_PointMyself")
            bhv.add(i, motion = str(i) + "_PointMyselfLeft")
            bhv.add(i, motion = str(i) + "_PointMyselfRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Which box filled?")
        bhv.add(0, [Speech("Which box did you fill?")])
        bhv.add(1, [Speech("Which box did you fee- fill?")])
        bhv.add(2, [Speech("Which box did you" + EmpathyBehaviorButton._markSpeech(90, 130) + "fill.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_DontKnow")
            bhv.add(i, motion = str(i) + "_DontKnowLeft")
            bhv.add(i, motion = str(i) + "_DontKnowRight")
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
            bhv.add(i, motion = str(i) + "_ForgetItLeft")
            bhv.add(i, motion = str(i) + "_ForgetItRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("What you think?")
        bhv.add(0, [Speech("What do you think?")])
        bhv.add(0, [Speech("Let's try.")])
        bhv.add(1, [Speech("What do you thiin- thiin- thii-. Ahhhe, what do you think?")])
        bhv.add(1, [Speech("Let's tra- tra- try. Let's try.")])
        bhv.add(2, [Speech("What do you thiin- thiin- thii-. Ahhhe. Sorry. what do you think?")])
        bhv.add(2, [Speech(EmpathyBehaviorButton._markSpeech(90, 110) + "Let's tra- tra- try." + EmpathyBehaviorButton._markSpeech() + "Sorry." + EmpathyBehaviorButton._markSpeech(75, 110) + "Let's try.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
            bhv.add(i, motion = str(i) + "_PointYou")
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Fill number for me")
        bhv.add(0, [Speech("Would you fill the number in for me?")])
        bhv.add(1, [Speech("Would you fill." + EmpathyBehaviorButton._markSpeech(70) + "the num- number in for me?")])
        bhv.add(2, [Speech("Would you fill." + EmpathyBehaviorButton._markSpeech(70, 125) + "the num- number in for me?")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
            bhv.add(i, motion = str(i) + "_PointYou")
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Need help?")
        bhv.add(0, [Speech("Are you okay?"), Speech("I can help you.")])
        bhv.add(0, [Speech("I can help you out.")])
        bhv.add(0, [Speech("Do you need any help?")])
        bhv.add(1, [Speech("Are you oh- okay?"), Speech("I can help you.")])
        bhv.add(1, [Speech("I can" + EmpathyBehaviorButton._markSpeech(80, 120) + "help you out.")])
        bhv.add(1, [Speech("Do you need any heh- heh-." + EmpathyBehaviorButton._markSpeech(80) + "Do you need any help?")])
        bhv.add(2, [Speech("Are you okay?"), Speech("I can he- heh-."), Speech("I can help you.")])
        bhv.add(2, [Speech("I can" + EmpathyBehaviorButton._markSpeech(80, 120) + "help you out.")])
        bhv.add(2, [Speech("Do you need any heh- heh- heh- heh-."), Speech("Sorry." + EmpathyBehaviorButton._markSpeech(80) + "Do you need any help?")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PointMyself")
            bhv.add(i, motion = str(i) + "_PointMyselfLeft")
            bhv.add(i, motion = str(i) + "_PointMyselfRight")
            bhv.add(i, motion = str(i) + "_PointYou")
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
            bhv.add(i, motion = str(i) + "_ForgetItLeft")
            bhv.add(i, motion = str(i) + "_ForgetItRight")
            bhv.add(i, motion = str(i) + "_WaveHandLeft")
            bhv.add(i, motion = str(i) + "_WaveHandRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Difficult!")
        bhv.add(0, [Wait(300), Speech("I don't know")])
        bhv.add(0, [Wait(300), Speech("This one is difficult")])
        bhv.add(1, [Wait(300), Speech("I don't noh- know")])
        bhv.add(1, [Wait(300), Speech("This one- one- one-."), Speech("This one is difficult")])
        bhv.add(2, [Wait(300), Speech("I don't no- no- noh-."), Speech("No.", speed = 50), Speech("I don't know")])
        bhv.add(2, [Wait(300), Speech("This one is diff- diff- diff-."), Speech("Ahhhe.", speed = 50), Speech("Sorry. This one is difficult", speed = 70)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_DontKnow")
            bhv.add(i, motion = str(i) + "_DontKnowLeft")
            bhv.add(i, motion = str(i) + "_DontKnowRight")
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
            bhv.add(i, motion = str(i) + "_ChinHoldLeft")
            bhv.add(i, motion = str(i) + "_ChinHoldRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Let me think")
        bhv.add(0, [Speech("Please, wait a minute. I need time to process.")])
        bhv.add(0, [Speech("Let me think carefully.")])
        bhv.add(1, [Speech("Please, wait a minute. I need time to pro- proh-. process.")])
        bhv.add(1, [Speech("Let me think care- care- care-. Let me think carefully.")])
        bhv.add(2, [Speech("Please, wait a minute. I need time to pro- proh-." + EmpathyBehaviorButton._markSpeech(50, 130) + "process.")])
        bhv.add(2, [Speech("Let me think care- care-" + EmpathyBehaviorButton._markSpeech(50, 130) + "care- care-. Let me think care- carefully.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_Wait")
            bhv.add(i, motion = str(i) + "_ChinHoldLeft")
            bhv.add(i, motion = str(i) + "_ChinHoldRight")
            bhv.add(i, motion = str(i) + "_PointMyself")
            bhv.add(i, motion = str(i) + "_PointMyselfLeft")
            bhv.add(i, motion = str(i) + "_PointMyselfRight")
            bhv.add(i, motion = str(i) + "_ParmUp")
            bhv.add(i, motion = str(i) + "_ParmUpLeft")
            bhv.add(i, motion = str(i) + "_ParmUpRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Play together")
        bhv.add(0, [Speech("Let's play together")])
        bhv.add(0, [Speech("Don't play by yourself")])
        bhv.add(0, [Speech("I want to play together.")])
        bhv.add(1, [Speech(EmpathyBehaviorButton._markSpeech(70) + "Let's play" + EmpathyBehaviorButton._markSpeech(90, 130) + "together")])
        bhv.add(1, [Speech(EmpathyBehaviorButton._markSpeech(70) + "Don't play" + EmpathyBehaviorButton._markSpeech(90, 130) + "by yourself.")])
        bhv.add(1, [Speech("I want to ple- ple- ple-."), Speech("I want to play together.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_DisagreeLeft")
            bhv.add(i, motion = str(i) + "_DisagreeRight")
            bhv.add(i, motion = str(i) + "_PointYou")
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Continue Sudoku")
        bhv.add(0, [Speech("Let's continue playing Sudoku.")])
        bhv.add(1, [Speech("Let's" + EmpathyBehaviorButton._markSpeech(50) + "continue" + EmpathyBehaviorButton._markSpeech() + "playing Sudoku.")])
        bhv.add(2, [Speech(EmpathyBehaviorButton._markSpeech(75) + "Let's" + EmpathyBehaviorButton._markSpeech(50, 120) + "cont- cont-" + EmpathyBehaviorButton._markSpeech() + "continue playing Sudoku.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Bring next board")
        bhv.add(0, [Speech("Can you bring next Sudoku board?")])
        bhv.add(1, [Speech("Can you" + EmpathyBehaviorButton._markSpeech(50) + "bri- bri-" + EmpathyBehaviorButton._markSpeech() + "next Sudoku board?")])
        bhv.add(2, [Speech("Can you" + EmpathyBehaviorButton._markSpeech(50) + "bri- bri- brih-" + EmpathyBehaviorButton._markSpeech(50, 130) + "Sorry." + EmpathyBehaviorButton._markSpeech() + "Can you bring next Sudoku board?")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PointMyself")
            bhv.add(i, motion = str(i) + "_PointMyselfLeft")
            bhv.add(i, motion = str(i) + "_PointMyselfRight")
            bhv.add(i, motion = str(i) + "_PointYou")
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Your turn")
        bhv.add(0, [Speech("It's your turn. Please fill one box and tell me.")])
        bhv.add(1, [Speech(EmpathyBehaviorButton._markSpeech(60) + "It's your turn." + EmpathyBehaviorButton._markSpeech() + "Please fill one box and tell me.")])
        bhv.add(2, [Speech(EmpathyBehaviorButton._markSpeech(60, 125) + "It's your turn." + EmpathyBehaviorButton._markSpeech() + "Please fill one box and tell me.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PointYou")
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)

        bhv = EmpathyBehaviorButton("Don't touch me")
        bhv.add(0, [Speech("Please, do not touch me.")])
        bhv.add(1, [Speech("Please, do not theh- touch me.")])
        bhv.add(2, [Speech("Please, do not" + EmpathyBehaviorButton._markSpeech(140, 130) + "touch me.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_Disagree")
            bhv.add(i, motion = str(i) + "_DisagreeLeft")
            bhv.add(i, motion = str(i) + "_DisagreeRight")
        #END for
        EmpathyBehaviorButton._behaviours.append(bhv)
    #END _initBehaviors()
#END class
