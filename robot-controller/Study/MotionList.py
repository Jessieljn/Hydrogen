from PyQt4 import QtGui
from Nao import NaoMotionList


class MotionList(QtGui.QPushButton):
    _motions = dict()

    @staticmethod
    def initialize():
        # The number in front of motion name refers jitter level.
        # If the level is 0, it should be normal.
        MotionList._motions["0_Idle0"] = NaoMotionList.find("Idle0").applySpeed(3.5)
        MotionList._motions["1_Idle0"] = NaoMotionList.find("Idle0").applySpeed(5.0)
        MotionList._motions["2_Idle0"] = NaoMotionList.find("Idle0").applySpeed(5.0).applyRepeat(1, 2, repeats = 2, repeatSpeed = 5.0)
        MotionList._motions["3_Idle0"] = NaoMotionList.find("Idle0").applySpeed(5.0).applyRepeat(1, 2, repeats = 2, repeatSpeed = 10.0)
        MotionList._motions["0_Idle1"] = NaoMotionList.find("Idle1").applySpeed(3.5)
        MotionList._motions["1_Idle1"] = NaoMotionList.find("Idle1").applySpeed(5.0)
        MotionList._motions["2_Idle1"] = NaoMotionList.find("Idle1").applySpeed(5.0).applyRepeat(1, 2, repeats = 2, repeatSpeed = 5.0)
        MotionList._motions["3_Idle1"] = NaoMotionList.find("Idle1").applySpeed(5.0).applyRepeat(1, 2, repeats = 2, repeatSpeed = 10.0)
        MotionList._motions["0_Idle2"] = NaoMotionList.find("Idle2").applySpeed(3.5)
        MotionList._motions["1_Idle2"] = NaoMotionList.find("Idle2").applySpeed(5.0)
        MotionList._motions["2_Idle2"] = NaoMotionList.find("Idle2").applySpeed(5.0).applyRepeat(1, 2, repeats = 2, repeatSpeed = 5.0)
        MotionList._motions["3_Idle2"] = NaoMotionList.find("Idle2").applySpeed(5.0).applyRepeat(1, 2, repeats = 2, repeatSpeed = 10.0)
        MotionList._motions["0_Idle3"] = NaoMotionList.find("Idle3").applySpeed(1.0)
        #MotionList._motions["1_Idle3"] = NaoMotionList.find("Idle3").applySpeed(1.0).applyRepeat(2, 3, repeats = 3, repeatSpeed = 2.0)
        #MotionList._motions["2_Idle3"] = NaoMotionList.find("Idle3").applySpeed(1.0).applyRepeat(3, 4, repeats = 4, repeatSpeed = 4.2)
        MotionList._motions["1_Idle3"] = NaoMotionList.find("Idle3").applySpeed(1.0).applyRepeat(3, 6, repeats = 4, repeatSpeed = 4.2)
        MotionList._motions["2_Idle3"] = NaoMotionList.find("Idle3").applySpeed(1.3).applyRepeat(3, 6, repeats = 6, repeatSpeed = 5.0)
        MotionList._motions["3_Idle3"] = NaoMotionList.find("Idle3").applySpeed(1.6).applyRepeat(1, 5, repeats = 4, repeatSpeed = 4.0)
        MotionList._motions["0_Idle5"] = NaoMotionList.find("Idle5").applySpeed(1.0)
        #MotionList._motions["1_Idle5"] = NaoMotionList.find("Idle5").applySpeed(1.0).applyRepeat(2, 3, repeats = 3, repeatSpeed = 2.0)
        #MotionList._motions["2_Idle5"] = NaoMotionList.find("Idle5").applySpeed(1.0).applyRepeat(3, 4, repeats = 4, repeatSpeed = 4.2)
        MotionList._motions["1_Idle5"] = NaoMotionList.find("Idle5").applySpeed(1.0).applyRepeat(3, 6, repeats = 4, repeatSpeed = 4.2)
        MotionList._motions["2_Idle5"] = NaoMotionList.find("Idle5").applySpeed(1.3).applyRepeat(3, 6, repeats = 6, repeatSpeed = 5.0)
        MotionList._motions["3_Idle5"] = NaoMotionList.find("Idle5").applySpeed(1.6).applyRepeat(1, 5, repeats = 4, repeatSpeed = 4.0)
        MotionList._motions["0_Idle6"] = NaoMotionList.find("Idle6").applySpeed(1.0)
        #MotionList._motions["1_Idle6"] = NaoMotionList.find("Idle6").applySpeed(1.0).applyRepeat(2, 3, repeats = 3, repeatSpeed = 2.0)
        #MotionList._motions["2_Idle6"] = NaoMotionList.find("Idle6").applySpeed(1.0).applyRepeat(3, 4, repeats = 4, repeatSpeed = 4.2)
        MotionList._motions["1_Idle6"] = NaoMotionList.find("Idle6").applySpeed(1.0).applyRepeat(3, 6, repeats = 4, repeatSpeed = 4.2)
        MotionList._motions["2_Idle6"] = NaoMotionList.find("Idle6").applySpeed(1.3).applyRepeat(3, 6, repeats = 6, repeatSpeed = 5.0)
        MotionList._motions["3_Idle6"] = NaoMotionList.find("Idle6").applySpeed(1.6).applyRepeat(1, 5, repeats = 4, repeatSpeed = 4.0)
        MotionList._motions["0_Disagree"] = NaoMotionList.find("Disagree").applySpeed(1.3)
        #MotionList._motions["1_Disagree"] = NaoMotionList.find("Disagree").applySpeed(1.4).applyRepeat(1, 3, repeats = 3, repeatSpeed = 1.7)
        MotionList._motions["1_Disagree"] = NaoMotionList.find("Disagree").applySpeed(1.4).applyRepeat(1, 3, repeats = 3, repeatSpeed = 2.4)
        #MotionList._motions["3_Disagree"] = NaoMotionList.find("Disagree").applySpeed(1.4).applyRepeat(0, 3, repeats = 4, repeatSpeed = 3.2)
        MotionList._motions["2_Disagree"] = NaoMotionList.find("Disagree").applySpeed(1.5).applyRepeat(0, 3, repeats = 4, repeatSpeed = 4.0)
        MotionList._motions["3_Disagree"] = NaoMotionList.find("Disagree").applySpeed(1.7).applyRepeat(0, 3, repeats = 5, repeatSpeed = 4.5)
        MotionList._motions["0_DisagreeLeft"] = NaoMotionList.find("DisagreeLeft").applySpeed(1.3)
        #MotionList._motions["1_DisagreeLeft"] = NaoMotionList.find("DisagreeLeft").applySpeed(1.4).applyRepeat(1, 3, repeats = 3, repeatSpeed = 1.7)
        MotionList._motions["1_DisagreeLeft"] = NaoMotionList.find("DisagreeLeft").applySpeed(1.4).applyRepeat(1, 3, repeats = 3, repeatSpeed = 2.4)
        #MotionList._motions["3_DisagreeLeft"] = NaoMotionList.find("DisagreeLeft").applySpeed(1.4).applyRepeat(0, 3, repeats = 4, repeatSpeed = 3.2)
        MotionList._motions["2_DisagreeLeft"] = NaoMotionList.find("DisagreeLeft").applySpeed(1.5).applyRepeat(0, 3, repeats = 4, repeatSpeed = 4.0)
        MotionList._motions["3_DisagreeLeft"] = NaoMotionList.find("DisagreeLeft").applySpeed(1.7).applyRepeat(0, 3, repeats = 5, repeatSpeed = 4.5)
        MotionList._motions["0_DisagreeRight"] = NaoMotionList.find("DisagreeRight").applySpeed(1.3)
        #MotionList._motions["1_DisagreeRight"] = NaoMotionList.find("DisagreeRight").applySpeed(1.4).applyRepeat(1, 3, repeats = 3, repeatSpeed = 1.7)
        MotionList._motions["1_DisagreeRight"] = NaoMotionList.find("DisagreeRight").applySpeed(1.4).applyRepeat(1, 3, repeats = 3, repeatSpeed = 2.4)
        #MotionList._motions["3_DisagreeRight"] = NaoMotionList.find("DisagreeRight").applySpeed(1.4).applyRepeat(0, 3, repeats = 4, repeatSpeed = 3.2)
        MotionList._motions["2_DisagreeRight"] = NaoMotionList.find("DisagreeRight").applySpeed(1.5).applyRepeat(0, 3, repeats = 4, repeatSpeed = 4.0)
        MotionList._motions["3_DisagreeRight"] = NaoMotionList.find("DisagreeRight").applySpeed(1.7).applyRepeat(0, 3, repeats = 5, repeatSpeed = 4.5)
        MotionList._motions["0_DontKnow"] = NaoMotionList.find("DontKnow").applySpeed(2.0)
        #MotionList._motions["1_DontKnow"] = NaoMotionList.find("DontKnow").applySpeed(2.0).applyRepeat(5, 6, repeats = 3, repeatSpeed = 1.5)
        MotionList._motions["1_DontKnow"] = NaoMotionList.find("DontKnow").applySpeed(2.1).applyRepeat(5, 6, repeats = 4, repeatSpeed = 3.0)
        #MotionList._motions["3_DontKnow"] = NaoMotionList.find("DontKnow").applySpeed(2.1).applyRepeat(4, 6, repeats = 4, repeatSpeed = 3.0)
        MotionList._motions["2_DontKnow"] = NaoMotionList.find("DontKnow").applySpeed(2.1).applyRepeat(3, 5, repeats = 5, repeatSpeed = 4.0)
        MotionList._motions["3_DontKnow"] = NaoMotionList.find("DontKnow").applySpeed(2.2).applyRepeat(3, 6, repeats = 5, repeatSpeed = 5.0)
        MotionList._motions["0_DontKnowLeft"] = NaoMotionList.find("DontKnowLeft").applySpeed(1.5)
        #MotionList._motions["1_DontKnowLeft"] = NaoMotionList.find("DontKnowLeft").applySpeed(1.5).applyRepeat(5, 6, repeats = 3, repeatSpeed = 1.5)
        MotionList._motions["1_DontKnowLeft"] = NaoMotionList.find("DontKnowLeft").applySpeed(1.6).applyRepeat(5, 6, repeats = 4, repeatSpeed = 3.0)
        #MotionList._motions["3_DontKnowLeft"] = NaoMotionList.find("DontKnowLeft").applySpeed(1.6).applyRepeat(4, 6, repeats = 4, repeatSpeed = 3.0)
        MotionList._motions["2_DontKnowLeft"] = NaoMotionList.find("DontKnowLeft").applySpeed(1.6).applyRepeat(3, 5, repeats = 5, repeatSpeed = 4.0)
        MotionList._motions["3_DontKnowLeft"] = NaoMotionList.find("DontKnowLeft").applySpeed(1.7).applyRepeat(3, 6, repeats = 5, repeatSpeed = 5.0)
        MotionList._motions["0_DontKnowRight"] = NaoMotionList.find("DontKnowRight").applySpeed(1.5)
        #MotionList._motions["1_DontKnowRight"] = NaoMotionList.find("DontKnowRight").applySpeed(1.5).applyRepeat(5, 6, repeats = 3, repeatSpeed = 1.5)
        MotionList._motions["1_DontKnowRight"] = NaoMotionList.find("DontKnowRight").applySpeed(1.6).applyRepeat(5, 6, repeats = 4, repeatSpeed = 3.0)
        #MotionList._motions["3_DontKnowRight"] = NaoMotionList.find("DontKnowRight").applySpeed(1.6).applyRepeat(4, 6, repeats = 4, repeatSpeed = 3.0)
        MotionList._motions["2_DontKnowRight"] = NaoMotionList.find("DontKnowRight").applySpeed(1.6).applyRepeat(3, 5, repeats = 5, repeatSpeed = 4.0)
        MotionList._motions["3_DontKnowRight"] = NaoMotionList.find("DontKnowRight").applySpeed(1.7).applyRepeat(3, 6, repeats = 5, repeatSpeed = 5.0)
        MotionList._motions["0_Wait"] = NaoMotionList.find("Wait").applySpeed(1.5)
        MotionList._motions["0_WaveHandLeft"] = NaoMotionList.find("WaveHandLeft").applySpeed(1.25)
        MotionList._motions["0_WaveHandRight"] = NaoMotionList.find("WaveHandRight").applySpeed(1.25)
        MotionList._motions["0_ForgetItLeft"] = NaoMotionList.find("ForgetItLeft").applySpeed(1.9)
        #MotionList._motions["1_ForgetItLeft"] = NaoMotionList.find("ForgetItLeft").applySpeed(2.0).applyRepeat(6, 7, repeats = 3, repeatSpeed = 2.0)
        MotionList._motions["1_ForgetItLeft"] = NaoMotionList.find("ForgetItLeft").applySpeed(2.0).applyRepeat(6, 7, repeats = 3, repeatSpeed = 3.0)
        #MotionList._motions["3_ForgetItLeft"] = NaoMotionList.find("ForgetItLeft").applySpeed(2.0).applyRepeat(6, 8, repeats = 3, repeatSpeed = 2.6)
        MotionList._motions["2_ForgetItLeft"] = NaoMotionList.find("ForgetItLeft").applySpeed(2.0).applyRepeat(6, 8, repeats = 3, repeatSpeed = 3.5)
        MotionList._motions["3_ForgetItLeft"] = NaoMotionList.find("ForgetItLeft").applySpeed(2.2).applyRepeat(5, 8, repeats = 3, repeatSpeed = 5.0)
        MotionList._motions["0_ForgetItRight"] = NaoMotionList.find("ForgetItRight").applySpeed(1.9)
        #MotionList._motions["1_ForgetItRight"] = NaoMotionList.find("ForgetItRight").applySpeed(2.0).applyRepeat(6, 7, repeats = 3, repeatSpeed = 2.0)
        MotionList._motions["1_ForgetItRight"] = NaoMotionList.find("ForgetItRight").applySpeed(2.0).applyRepeat(6, 7, repeats = 3, repeatSpeed = 3.0)
        #MotionList._motions["3_ForgetItRight"] = NaoMotionList.find("ForgetItRight").applySpeed(2.0).applyRepeat(6, 8, repeats = 3, repeatSpeed = 2.6)
        MotionList._motions["2_ForgetItRight"] = NaoMotionList.find("ForgetItRight").applySpeed(2.0).applyRepeat(6, 8, repeats = 3, repeatSpeed = 3.5)
        MotionList._motions["3_ForgetItRight"] = NaoMotionList.find("ForgetItRight").applySpeed(2.2).applyRepeat(5, 8, repeats = 3, repeatSpeed = 5.0)
        MotionList._motions["0_OhYesLeft"] = NaoMotionList.find("OhYesLeft").applySpeed(1.8)
        MotionList._motions["0_OhYesRight"] = NaoMotionList.find("OhYesRight").applySpeed(1.8)
        MotionList._motions["0_PalmUp"] = NaoMotionList.find("PalmUp").applySpeed(1.7)
        #MotionList._motions["1_PalmUp"] = NaoMotionList.find("PalmUp").applySpeed(1.7).applyRepeat(2, 3, repeats = 3, repeatSpeed = 2.4)
        MotionList._motions["1_PalmUp"] = NaoMotionList.find("PalmUp").applySpeed(1.7).applyRepeat(2, 3, repeats = 3, repeatSpeed = 3.6)
        #MotionList._motions["3_PalmUp"] = NaoMotionList.find("PalmUp").applySpeed(1.8).applyRepeat(3, 4, repeats = 4, repeatSpeed = 4.0)
        MotionList._motions["2_PalmUp"] = NaoMotionList.find("PalmUp").applySpeed(1.8).applyRepeat(2, 4, repeats = 3, repeatSpeed = 4.0)
        MotionList._motions["3_PalmUp"] = NaoMotionList.find("PalmUp").applySpeed(1.8).applyRepeat(2, 4, repeats = 5, repeatSpeed = 5.0)
        MotionList._motions["0_PalmUpLeft"] = NaoMotionList.find("PalmUpLeft").applySpeed(1.7)
        #MotionList._motions["1_PalmUpLeft"] = NaoMotionList.find("PalmUpLeft").applySpeed(1.7).applyRepeat(2, 3, repeats = 3, repeatSpeed = 2.4)
        MotionList._motions["1_PalmUpLeft"] = NaoMotionList.find("PalmUpLeft").applySpeed(1.7).applyRepeat(2, 3, repeats = 3, repeatSpeed = 3.6)
        #MotionList._motions["3_PalmUpLeft"] = NaoMotionList.find("PalmUpLeft").applySpeed(1.8).applyRepeat(3, 4, repeats = 4, repeatSpeed = 4.0)
        MotionList._motions["2_PalmUpLeft"] = NaoMotionList.find("PalmUpLeft").applySpeed(1.8).applyRepeat(2, 4, repeats = 3, repeatSpeed = 4.0)
        MotionList._motions["3_PalmUpLeft"] = NaoMotionList.find("PalmUpLeft").applySpeed(1.8).applyRepeat(2, 4, repeats = 5, repeatSpeed = 5.0)
        MotionList._motions["0_PalmUpRight"] = NaoMotionList.find("PalmUpRight").applySpeed(1.7)
        #MotionList._motions["1_PalmUpRight"] = NaoMotionList.find("PalmUpRight").applySpeed(1.7).applyRepeat(2, 3, repeats = 3, repeatSpeed = 2.4)
        MotionList._motions["1_PalmUpRight"] = NaoMotionList.find("PalmUpRight").applySpeed(1.7).applyRepeat(2, 3, repeats = 3, repeatSpeed = 3.6)
        #MotionList._motions["3_PalmUpRight"] = NaoMotionList.find("PalmUpRight").applySpeed(1.8).applyRepeat(3, 4, repeats = 4, repeatSpeed = 4.0)
        MotionList._motions["2_PalmUpRight"] = NaoMotionList.find("PalmUpRight").applySpeed(1.8).applyRepeat(2, 4, repeats = 3, repeatSpeed = 4.0)
        MotionList._motions["3_PalmUpRight"] = NaoMotionList.find("PalmUpRight").applySpeed(1.8).applyRepeat(2, 4, repeats = 5, repeatSpeed = 5.0)
        MotionList._motions["0_PointMyself"] = NaoMotionList.find("PointMyself").applySpeed(2.0)
        #MotionList._motions["1_PointMyself"] = NaoMotionList.find("PointMyself").applySpeed(2.0).applyRepeat(1, 3, repeats = 3, repeatSpeed = 1.7)
        MotionList._motions["1_PointMyself"] = NaoMotionList.find("PointMyself").applySpeed(2.0).applyRepeat(1, 3, repeats = 3, repeatSpeed = 2.4)
        #MotionList._motions["3_PointMyself"] = NaoMotionList.find("PointMyself").applySpeed(2.0).applyRepeat(0, 3, repeats = 3, repeatSpeed = 2.9)
        MotionList._motions["2_PointMyself"] = NaoMotionList.find("PointMyself").applySpeed(2.0).applyRepeat(0, 3, repeats = 3, repeatSpeed = 4.0)
        MotionList._motions["3_PointMyself"] = NaoMotionList.find("PointMyself").applySpeed(2.1).applyRepeat(0, 4, repeats = 4, repeatSpeed = 5.0)
        MotionList._motions["0_PointMyselfLeft"] = NaoMotionList.find("PointMyselfLeft").applySpeed(2.0)
        #MotionList._motions["1_PointMyselfLeft"] = NaoMotionList.find("PointMyselfLeft").applySpeed(2.0).applyRepeat(1, 3, repeats = 3, repeatSpeed = 1.7)
        MotionList._motions["1_PointMyselfLeft"] = NaoMotionList.find("PointMyselfLeft").applySpeed(2.0).applyRepeat(1, 3, repeats = 3, repeatSpeed = 2.4)
        #MotionList._motions["3_PointMyselfLeft"] = NaoMotionList.find("PointMyselfLeft").applySpeed(2.0).applyRepeat(0, 3, repeats = 3, repeatSpeed = 2.9)
        MotionList._motions["2_PointMyselfLeft"] = NaoMotionList.find("PointMyselfLeft").applySpeed(2.0).applyRepeat(0, 3, repeats = 3, repeatSpeed = 4.0)
        MotionList._motions["3_PointMyselfLeft"] = NaoMotionList.find("PointMyselfLeft").applySpeed(2.1).applyRepeat(0, 4, repeats = 4, repeatSpeed = 5.0)
        MotionList._motions["0_PointMyselfRight"] = NaoMotionList.find("PointMyselfRight").applySpeed(2.0)
        #MotionList._motions["1_PointMyselfRight"] = NaoMotionList.find("PointMyselfRight").applySpeed(2.0).applyRepeat(1, 3, repeats = 3, repeatSpeed = 1.7)
        MotionList._motions["1_PointMyselfRight"] = NaoMotionList.find("PointMyselfRight").applySpeed(2.0).applyRepeat(1, 3, repeats = 3, repeatSpeed = 2.4)
        #MotionList._motions["3_PointMyselfRight"] = NaoMotionList.find("PointMyselfRight").applySpeed(2.0).applyRepeat(0, 3, repeats = 3, repeatSpeed = 2.9)
        MotionList._motions["2_PointMyselfRight"] = NaoMotionList.find("PointMyselfRight").applySpeed(2.0).applyRepeat(0, 3, repeats = 3, repeatSpeed = 4.0)
        MotionList._motions["3_PointMyselfRight"] = NaoMotionList.find("PointMyselfRight").applySpeed(2.1).applyRepeat(0, 4, repeats = 4, repeatSpeed = 5.0)
        MotionList._motions["0_PointYou"] = NaoMotionList.find("PointYou").applySpeed(1.8)
        #MotionList._motions["1_PointYou"] = NaoMotionList.find("PointYou").applySpeed(1.8).applyRepeat(4, 7, repeats = 3, repeatSpeed = 2.2)
        MotionList._motions["1_PointYou"] = NaoMotionList.find("PointYou").applySpeed(2.0).applyRepeat(4, 7, repeats = 4, repeatSpeed = 2.7)
        #MotionList._motions["3_PointYou"] = NaoMotionList.find("PointYou").applySpeed(2.0).applyRepeat(3, 6, repeats = 4, repeatSpeed = 3.4)
        MotionList._motions["2_PointYou"] = NaoMotionList.find("PointYou").applySpeed(2.1).applyRepeat(3, 7, repeats = 4, repeatSpeed = 4.2)
        MotionList._motions["3_PointYou"] = NaoMotionList.find("PointYou").applySpeed(2.3).applyRepeat(3, 7, repeats = 4, repeatSpeed = 5.0)
        MotionList._motions["0_PointYouLeft"] = NaoMotionList.find("PointYouLeft").applySpeed(1.8)
        #MotionList._motions["1_PointYouLeft"] = NaoMotionList.find("PointYouLeft").applySpeed(1.8).applyRepeat(4, 7, repeats = 3, repeatSpeed = 2.2)
        MotionList._motions["1_PointYouLeft"] = NaoMotionList.find("PointYouLeft").applySpeed(2.0).applyRepeat(4, 7, repeats = 4, repeatSpeed = 2.7)
        #MotionList._motions["3_PointYouLeft"] = NaoMotionList.find("PointYouLeft").applySpeed(2.0).applyRepeat(3, 6, repeats = 4, repeatSpeed = 3.4)
        MotionList._motions["2_PointYouLeft"] = NaoMotionList.find("PointYouLeft").applySpeed(2.1).applyRepeat(3, 7, repeats = 4, repeatSpeed = 4.2)
        MotionList._motions["3_PointYouLeft"] = NaoMotionList.find("PointYouLeft").applySpeed(2.3).applyRepeat(3, 7, repeats = 4, repeatSpeed = 5.0)
        MotionList._motions["0_PointYouRight"] = NaoMotionList.find("PointYouRight").applySpeed(1.8)
        #MotionList._motions["1_PointYouRight"] = NaoMotionList.find("PointYouRight").applySpeed(1.8).applyRepeat(4, 7, repeats = 3, repeatSpeed = 2.2)
        MotionList._motions["1_PointYouRight"] = NaoMotionList.find("PointYouRight").applySpeed(2.0).applyRepeat(4, 7, repeats = 4, repeatSpeed = 2.7)
        #MotionList._motions["3_PointYouRight"] = NaoMotionList.find("PointYouRight").applySpeed(2.0).applyRepeat(3, 6, repeats = 4, repeatSpeed = 3.4)
        MotionList._motions["2_PointYouRight"] = NaoMotionList.find("PointYouRight").applySpeed(2.1).applyRepeat(3, 7, repeats = 4, repeatSpeed = 4.2)
        MotionList._motions["3_PointYouRight"] = NaoMotionList.find("PointYouRight").applySpeed(2.3).applyRepeat(3, 7, repeats = 4, repeatSpeed = 5.0)
        MotionList._motions["0_ChinHoldLeft"] = NaoMotionList.find("ChinHoldLeft").applySpeed(1.5)
        #MotionList._motions["1_ChinHoldLeft"] = NaoMotionList.find("ChinHoldLeft").applySpeed(1.5).applyRepeat(3, 5, repeats = 3, repeatSpeed = 1.9)
        MotionList._motions["1_ChinHoldLeft"] = NaoMotionList.find("ChinHoldLeft").applySpeed(1.5).applyRepeat(2, 5, repeats = 3, repeatSpeed = 2.5)
        #MotionList._motions["3_ChinHoldLeft"] = NaoMotionList.find("ChinHoldLeft").applySpeed(1.6).applyRepeat(2, 5, repeats = 3, repeatSpeed = 3.2)
        MotionList._motions["2_ChinHoldLeft"] = NaoMotionList.find("ChinHoldLeft").applySpeed(1.7).applyRepeat(2, 5, repeats = 4, repeatSpeed = 4.0)
        MotionList._motions["3_ChinHoldLeft"] = NaoMotionList.find("ChinHoldLeft").applySpeed(1.8).applyRepeat(1, 5, repeats = 3, repeatSpeed = 5.0)
        MotionList._motions["0_ChinHoldRight"] = NaoMotionList.find("ChinHoldRight").applySpeed(1.5)
        #MotionList._motions["1_ChinHoldRight"] = NaoMotionList.find("ChinHoldRight").applySpeed(1.5).applyRepeat(3, 5, repeats = 3, repeatSpeed = 1.9)
        MotionList._motions["1_ChinHoldRight"] = NaoMotionList.find("ChinHoldRight").applySpeed(1.5).applyRepeat(2, 5, repeats = 3, repeatSpeed = 2.5)
        #MotionList._motions["3_ChinHoldRight"] = NaoMotionList.find("ChinHoldRight").applySpeed(1.6).applyRepeat(2, 5, repeats = 3, repeatSpeed = 3.2)
        MotionList._motions["2_ChinHoldRight"] = NaoMotionList.find("ChinHoldRight").applySpeed(1.7).applyRepeat(2, 5, repeats = 4, repeatSpeed = 4.0)
        MotionList._motions["3_ChinHoldRight"] = NaoMotionList.find("ChinHoldRight").applySpeed(1.8).applyRepeat(1, 5, repeats = 3, repeatSpeed = 5.0)
        MotionList._motions["0_WhisperLeft"] = NaoMotionList.find("WhisperLeft").applySpeed(2.5)
        MotionList._motions["3_WhisperLeft"] = NaoMotionList.find("WhisperLeft").applySpeed(2.5).applyRepeat(10, 12, repeats = 10, repeatSpeed = 2.0)
        MotionList._motions["0_WhisperRight"] = NaoMotionList.find("WhisperRight").applySpeed(2.5)
        MotionList._motions["3_WhisperRight"] = NaoMotionList.find("WhisperRight").applySpeed(2.5).applyRepeat(10, 12, repeats = 10, repeatSpeed = 2.0)
    #END initialize()

    @staticmethod
    def destroy():
        pass
    #END destroy()

    @staticmethod
    def getByName(name):
        if name in MotionList._motions:
            return MotionList._motions[name]
        #END if
        return None
    #END getByName()

    @staticmethod
    def getMotions():
        return MotionList._motions.keys()
    #END getMotions()

    @staticmethod
    def length():
        return len(MotionList._motions)
    #END length()
#END class
