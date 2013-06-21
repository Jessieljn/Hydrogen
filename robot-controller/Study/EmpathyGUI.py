from PyQt4 import QtCore
from PyQt4 import QtGui
from Action import Behavior
from Action import LED
from Action import Motion
from Action import ReplaceableSpeech
from Action import Speech
from Action import Stiffness
from Action import Wait
from EmpathyButton import EmpathyButton
from EmpathyMotionList import EmpathyMotionList
from EmpathySpeech import EmpathySpeech
from UI.ActionPushButton import ActionPushButton
from UI.SudokuBoard import SudokuBoard


class EmpathyGUI(object):
    @staticmethod
    def setupInteractions(parent, wgt):
        buttons = []

        bhv = EmpathyButton("Conv. Filler")
        bhv.add(0, [Speech(" ehhhh,", speed = 50)])
        bhv.add(0, [Speech(" hmm,", speed = 50)])
        bhv.add(0, [Speech(" ummmh,", speed = 50)])
        bhv.add(0, [Speech(" well,", speed = 50)])
        bhv.add(0, [Speech(" let me think", speed = 80)])
        bhv.add(0, [Speech(" let's see", speed = 80)])
        bhv.add(2, [Speech(" ehhhh,", speed = 60, shaping = 110)])
        bhv.add(2, [Speech(" hmm,", speed = 60, shaping = 110)])
        bhv.add(2, [Speech(" ummmh,", speed = 60, shaping = 110)])
        bhv.add(2, [Speech(" well,", speed = 60, shaping = 110)])
        bhv.add(2, [Speech(" let me think", speed = 90, shaping = 110)])
        bhv.add(2, [Speech(" let's see", speed = 90, shaping = 110)])
        bhv.add(4, [Speech(" ehhhh,", speed = 70, shaping = 130)])
        bhv.add(4, [Speech(" hmm,", speed = 70, shaping = 130)])
        bhv.add(4, [Speech(" ummmh,", speed = 70, shaping = 130)])
        bhv.add(4, [Speech(" well,", speed = 70, shaping = 130)])
        bhv.add(4, [Speech(" let me" + EmpathyGUI._markSpeech(90, 130) + "think", speed = 90, shaping = 110)])
        bhv.add(4, [Speech(" let's" + EmpathyGUI._markSpeech(90, 130) + "see", speed = 90, shaping = 110)])
        buttons.append(bhv)
        parent.bhvFiller = bhv

        bhv = EmpathyButton("Idle (Big)")
        for i in range(10):
            bhv.add(i, motion = str(i) + "_ChinHoldLeft")
            bhv.add(i, motion = str(i) + "_ChinHoldRight")
            bhv.add(i, motion = str(i) + "_Idle3")
            bhv.add(i, motion = str(i) + "_Idle5")
            bhv.add(i, motion = str(i) + "_Idle6")
        #END for
        buttons.append(bhv)
        parent.bhvIdleBig = bhv

        bhv = EmpathyButton("Idle (Small)")
        for i in range(10):
            bhv.add(i, motion = str(i) + "_Idle0")
            bhv.add(i, motion = str(i) + "_Idle1")
            bhv.add(i, motion = str(i) + "_Idle2")
        #END for
        buttons.append(bhv)
        parent.bhvIdleSmall = bhv

        bhv = EmpathyButton("Thank you")
        bhv.add(0, [Speech("Thank you.", 80)])
        bhv.add(0, [Speech("I appreciate.", 80)])
        bhv.add(2, [Speech("Thank you.", 50)])
        bhv.add(2, [Speech("I appreciate.", 50)])
        bhv.add(4, [Speech("Thank" + EmpathyGUI._markSpeech() + "you.", 50, 120)])
        bhv.add(4, [Speech("I" + EmpathyGUI._markSpeech(50, 120) + "appreciate.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PointMyselfLeft")
            bhv.add(i, motion = str(i) + "_PointMyselfRight")
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
        #END for
        buttons.append(bhv)

        bhv = EmpathyButton("Good")
        bhv.add(0, [Speech("Good.")])
        bhv.add(0, [Speech("Cool.")])
        bhv.add(0, [Speech("Exactly.")])
        bhv.add(0, [Speech("Nice.")])
        bhv.add(0, [Speech("Perfect.")])
        bhv.add(2, [Speech("Good.", 50)])
        bhv.add(2, [Speech("Cool.", 50)])
        bhv.add(2, [Speech("Exactly.", 50)])
        bhv.add(2, [Speech("Nice.", 50)])
        bhv.add(2, [Speech("Perfect.", 50)])
        bhv.add(4, [Speech("Good.", 50, 120)])
        bhv.add(4, [Speech("Cool.", 50, 120)])
        bhv.add(4, [Speech("Exactly.", 50, 120)])
        bhv.add(4, [Speech("Nice.", 50, 120)])
        bhv.add(4, [Speech("Perfect.", 50, 120)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PointMyselfLeft")
            bhv.add(i, motion = str(i) + "_PointMyselfRight")
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        buttons.append(bhv)

        bhv = EmpathyButton("Okay")
        bhv.add(0, [Speech("Okay.")])
        bhv.add(0, [Speech("I got it.")])
        bhv.add(0, [Speech("Understood.")])
        bhv.add(2, [Speech("Okay.", 50)])
        bhv.add(2, [Speech("I got it.", 60)])
        bhv.add(2, [Speech("Understood.", 50)])
        bhv.add(4, [Speech("Okay.", 50, 120)])
        bhv.add(4, [Speech("I" + EmpathyGUI._markSpeech(60, 120) + "got it.", 60)])
        bhv.add(4, [Speech("Under" + EmpathyGUI._markSpeech(50, 120) + "stood.", 50)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_Idle5")
            bhv.add(i, motion = str(i) + "_Idle6")
            bhv.add(i, motion = str(i) + "_PointMyselfLeft")
            bhv.add(i, motion = str(i) + "_PointMyselfRight")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        buttons.append(bhv)

        bhv = EmpathyButton("I agree")
        bhv.add(0, [Speech("Yes")])
        bhv.add(0, [Speech("I agree.")])
        bhv.add(0, [Speech("You are right.")])
        bhv.add(2, [Speech("Yes", 50)])
        bhv.add(2, [Speech("I agree.", 50)])
        bhv.add(2, [Speech("You are right.", 50)])
        bhv.add(4, [Speech("Yes", 50, 120)])
        bhv.add(4, [Speech("I" + EmpathyGUI._markSpeech(50, 120) + "agree.", 50)])
        bhv.add(4, [Speech("You are" + EmpathyGUI._markSpeech(50, 120) + "right.", 50)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        buttons.append(bhv)

        bhv = EmpathyButton("Yes")
        bhv.add(0, [Speech("Yes")])
        bhv.add(0, [Speech("Right.")])
        bhv.add(2, [Speech("Yes", 50)])
        bhv.add(2, [Speech("Right.", 50)])
        bhv.add(4, [Speech("Yes", 50, 120)])
        bhv.add(4, [Speech("Right.", 50, 120)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_Idle5")
            bhv.add(i, motion = str(i) + "_Idle6")
            bhv.add(i, motion = str(i) + "_PointMyselfLeft")
            bhv.add(i, motion = str(i) + "_PointMyselfRight")
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        buttons.append(bhv)

        bhv = EmpathyButton("No")
        bhv.add(0, [Speech("No")])
        bhv.add(0, [Speech("I don't think so")])
        bhv.add(2, [Speech("No", 50)])
        bhv.add(2, [Speech("I don't think so", 50)])
        bhv.add(4, [Speech("No", 50, 120)])
        bhv.add(4, [Speech("I don't" + EmpathyGUI._markSpeech(50, 120) + "think so", 50)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_Disagree")
            bhv.add(i, motion = str(i) + "_DisagreeLeft")
            bhv.add(i, motion = str(i) + "_DisagreeRight")
            bhv.add(i, motion = str(i) + "_PalmUp")
        #END for
        buttons.append(bhv)

        bhv = EmpathyButton("Let me think")
        bhv.add(0, [Speech("Please, wait a minute."), Speech("I need time to process.")])
        bhv.add(0, [Speech("Let me think carefully.")])
        bhv.add(1, [Speech("Please, wait a minute."), Speech("I need time to proh- proh-. process.")])
        bhv.add(1, [Speech("Let me think care- care- care-. Let me think carefully.")])
        bhv.add(2, [Speech("Please, wait a minute."), Speech("I need time to proh- proh-." + EmpathyGUI._markSpeech(50, 130) + "process.")])
        bhv.add(2, [Speech("Let me think care- care-" + EmpathyGUI._markSpeech(50, 130) + "care- care-."), Speech("Let me think care- carefully.", 75)])
        bhv.add(4, [Speech("Please," + EmpathyGUI._markSpeech(70, 130) + "wait a minute.", 50), Speech("I need time to" + EmpathyGUI._markSpeech(50, 130) + "pro- proh-."), Speech("Sorry. need time to process.", 75)])
        bhv.add(4, [Speech("Let me" + EmpathyGUI._markSpeech() + "think care- care-" + EmpathyGUI._markSpeech(50, 130) + "care- care-.", 70, 120), Speech("Let me think care- carefully.", 75)])
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
        buttons.append(bhv)

        bhv = EmpathyButton("What you think?")
        bhv.add(0, [Speech("What do you think?")])
        bhv.add(2, [Speech("What do you" + EmpathyGUI._markSpeech(95) + "thiin- thiin- thii-."), Speech("Ahhhe, what do you think?")])
        bhv.add(4, [Speech("What do you" + EmpathyGUI._markSpeech(70, 120) + "thiin- thiin- thii-."), Speech("Sorry.", speed = 50), Speech("What do you think?", 75, 110)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
            bhv.add(i, motion = str(i) + "_PointYou")
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
        #END for
        buttons.append(bhv)

        bhv = EmpathyButton("Easy!")
        bhv.add(0, [Wait(300), Speech("This one is easy")])
        bhv.add(2, [Wait(300), Speech("This one is e- e- easy")])
        bhv.add(4, [Wait(300), Speech("This one is" + EmpathyGUI._markSpeech(90, 110) + "e- e-" + EmpathyGUI._markSpeech(50, 130) + "e- e-."), Speech("Sorry. This one is easy")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        buttons.append(bhv)

        bhv = EmpathyButton("Difficult!")
        bhv.add(0, [Wait(300), Speech("I don't know")])
        bhv.add(0, [Wait(300), Speech("This one is difficult")])
        bhv.add(2, [Wait(300), Speech("I don't noh- know")])
        bhv.add(2, [Wait(300), Speech("This one- one- one-."), Speech("This one is difficult")])
        bhv.add(4, [Wait(300), Speech("I don't no- no- noh-."), Speech("No.", 50, 130), Speech("I don't know")])
        bhv.add(4, [Wait(300), Speech("This one is diff- diff- diff-."), Speech("Ahhhe.", 50, 130), Speech("Sorry. This one is difficult", 70)])
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
        buttons.append(bhv)

        bhv = EmpathyButton("How are you?")
        bhv.add(0, [Speech("How are you today?")])
        bhv.add(0, [Speech("How is it going?")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_DontKnowLeft")
            bhv.add(i, motion = str(i) + "_DontKnowRight")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        buttons.append(bhv)

        bhv = EmpathyButton("Weather?")
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
        buttons.append(bhv)

        bhv = EmpathyButton("Do you like Sudoku?")
        bhv.add(0, [Speech("Do you like Sudoku?")])
        bhv.add(2, [Speech("Do you" + EmpathyGUI._markSpeech(80, 120) + "like Sudoku?", 70)])
        bhv.add(4, [Speech("Do you" + EmpathyGUI._markSpeech(50, 130) + "like" + EmpathyGUI._markSpeech(90, 110) + "Sudoku?", 70)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_DontKnowLeft")
            bhv.add(i, motion = str(i) + "_DontKnowRight")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
        #END for
        buttons.append(bhv)

        bhv = EmpathyButton("Your cloths")
        bhv.add(0, [Speech("I like your clouth."), Speech("Where did you get it?")])
        bhv.add(0, [Speech("Your clouth looks good.")])
        bhv.add(0, [Speech("Your clouth looks great on you.")])
        bhv.add(2, [Speech("I like" + EmpathyGUI._markSpeech(80, 115) + "your clouth."), Speech("Where did" + EmpathyGUI._markSpeech() + "you get it?", 80, 120)])
        bhv.add(2, [Speech("Your clouth" + EmpathyGUI._markSpeech(80, 120) + "looks good.")])
        bhv.add(2, [Speech("Your clouth" + EmpathyGUI._markSpeech(80, 120) + "looks great on you.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
        #END for
        buttons.append(bhv)

        bhv = EmpathyButton("You are smart")
        bhv.add(0, [Speech("You are doing very good.")])
        bhv.add(0, [Speech("You are good at Sudoku.")])
        bhv.add(2, [Speech("You are" + EmpathyGUI._markSpeech() + "doing very good.", 70, 120)])
        bhv.add(2, [Speech("You are" + EmpathyGUI._markSpeech() + "good at Sudoku.", 70, 120)])
        bhv.add(4, [Speech("You are" + EmpathyGUI._markSpeech() + "do- do- do-" + EmpathyGUI._markSpeech(50, 120) + "doing very good.", 70, 120)])
        bhv.add(4, [Speech("You are" + EmpathyGUI._markSpeech() + "goo- goo- goo-" + EmpathyGUI._markSpeech(50, 120) + "good at Sudoku.", 70, 120)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
        #END for
        buttons.append(bhv)

        bhv = EmpathyButton("Play together")
        bhv.add(0, [Speech("Let's play together")])
        bhv.add(0, [Speech("Don't play by yourself")])
        bhv.add(0, [Speech("I want to play together.")])
        bhv.add(2, [Speech(EmpathyGUI._markSpeech(70) + "Let's play" + EmpathyGUI._markSpeech(90, 130) + "together")])
        bhv.add(2, [Speech(EmpathyGUI._markSpeech(70) + "Don't play" + EmpathyGUI._markSpeech(90, 130) + "by yourself.")])
        bhv.add(2, [Speech("I want to ple- ple- ple-."), Speech("I want to play together.")])
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
        buttons.append(bhv)

        bhv = EmpathyButton("Almost done")
        bhv.add(0, [Speech("We are almost done with this board.")])
        bhv.add(0, [Speech("Few more to finish this board.")])
        bhv.add(2, [Speech("We are almost" + EmpathyGUI._markSpeech(80, 110) + "done with this board.")])
        bhv.add(2, [Speech("Few more to" + EmpathyGUI._markSpeech(80, 110) + "finish this board.")])
        bhv.add(4, [Speech("We are almost" + EmpathyGUI._markSpeech(80, 120) + "done with the- the- the-" + EmpathyGUI._markSpeech() + "this board.", 130)])
        bhv.add(4, [Speech("Few more to" + EmpathyGUI._markSpeech(80, 110) + "fii- fii-." + EmpathyGUI._markSpeech() + "Sorry.finish this board.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        buttons.append(bhv)

        bhv = EmpathyButton("This board?")
        bhv.add(0, [Speech("Is this board easy?")])
        bhv.add(0, [Speech("Is this board difficult?")])
        bhv.add(0, [Speech("What do you think about this board?")])
        bhv.add(2, [Speech("Is this" + EmpathyGUI._markSpeech(80, 115) + "board easy?")])
        bhv.add(2, [Speech("Is this" + EmpathyGUI._markSpeech(80, 115) + "board difficult?")])
        bhv.add(2, [Speech("What" + EmpathyGUI._markSpeech(80, 115) + "do you think about" + EmpathyGUI._markSpeech(90, 100) + "this board?")])
        bhv.add(4, [Speech("Is this" + EmpathyGUI._markSpeech(80, 130) + "board easy?", 50)])
        bhv.add(4, [Speech("Is this" + EmpathyGUI._markSpeech(80, 130) + "board difficult?", 50)])
        bhv.add(4, [Speech("What" + EmpathyGUI._markSpeech(80, 130) + "do you thiih thiih think about" + EmpathyGUI._markSpeech(90, 100) + "this board?", 50)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_DontKnowLeft")
            bhv.add(i, motion = str(i) + "_DontKnowRight")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
        #END for
        buttons.append(bhv)

        bhv = EmpathyButton("Bring next board")
        bhv.add(0, [Speech("Can you bring next Sudoku board?")])
        bhv.add(0, [Speech("Let's move to next board.")])
        bhv.add(2, [Speech("Can you" + EmpathyGUI._markSpeech(50) + "bri- bri-." + EmpathyGUI._markSpeech() + "bring next Sudoku board?")])
        bhv.add(2, [Speech("Let's" + EmpathyGUI._markSpeech(50) + "moo- moo-." + EmpathyGUI._markSpeech() + "move to next board.")])
        bhv.add(4, [Speech("Can you" + EmpathyGUI._markSpeech(50) + "bri- bri- brih-." + EmpathyGUI._markSpeech(50, 130) + "I'm Sorry." + EmpathyGUI._markSpeech() + "Can you bring next Sudoku board?")])
        bhv.add(4, [Speech("Let's" + EmpathyGUI._markSpeech(50) + "moo moo- mooh-." + EmpathyGUI._markSpeech(50, 130) + "I'm Sorry." + EmpathyGUI._markSpeech() + "Let's move to next board.")])
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
        buttons.append(bhv)

        bhv = EmpathyButton("Need help?")
        bhv.add(0, [Speech("Are you okay?"), Speech("I can help you.")])
        bhv.add(0, [Speech("I can help you out.")])
        bhv.add(0, [Speech("Do you need any help?")])
        bhv.add(2, [Speech("Are you oh- okay?"), Speech("I can help you.")])
        bhv.add(2, [Speech("I can" + EmpathyGUI._markSpeech(80, 120) + "help you out.")])
        bhv.add(2, [Speech("Do you need any heh- heh-." + EmpathyGUI._markSpeech(80) + "Do you need any help?")])
        bhv.add(4, [Speech("Are you okay?"), Speech("I can he- heh-."), Speech("I can help you.")])
        bhv.add(4, [Speech("I can" + EmpathyGUI._markSpeech(80, 120) + "help you out.")])
        bhv.add(4, [Speech("Do you need any heh- heh- heh- heh-."), Speech("Sorry." + EmpathyGUI._markSpeech(80) + "Do you need any help?")])
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
        buttons.append(bhv)

        bhv = EmpathyButton("Don't touch me")
        bhv.add(0, [Speech("Please, do not touch me.")])
        bhv.add(2, [Speech("Please, do not theh- touch me.")])
        bhv.add(4, [Speech("Please, do not" + EmpathyGUI._markSpeech(140, 130) + "touch me.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_Disagree")
            bhv.add(i, motion = str(i) + "_DisagreeLeft")
            bhv.add(i, motion = str(i) + "_DisagreeRight")
        #END for
        buttons.append(bhv)

        EmpathyGUI.setupWidget(parent, wgt, buttons)
    #END setupInteractions()

    @staticmethod
    def setupMotions(parent, wgt):
        added = dict()
        motions = EmpathyMotionList.getMotions()
        for i in range(len(motions)):
            motions[i] = motions[i][2:]
        #END for
        motions = sorted(motions)
        widgetMotions = QtGui.QWidget()
        layoutMotions = QtGui.QVBoxLayout(widgetMotions)
        layoutMotions.setMargin(0)
        for name in motions:
            if not name in added:
                added[name] = True
                button = QtGui.QPushButton(name, widgetMotions)
                button.clicked.connect(parent.on_motionbutton_clicked)
                layoutMotions.addWidget(button)
            #END if
        #END for
        scroll = QtGui.QScrollArea()
        scroll.setAlignment(QtCore.Qt.AlignCenter)
        scroll.setWidget(widgetMotions)
        layoutScroll = QtGui.QHBoxLayout()
        layoutScroll.setMargin(0)
        layoutScroll.addWidget(scroll)
        widget = QtGui.QWidget(wgt)
        widget.setLayout(layoutScroll)
        return widget
    #END setupMotions()

    @staticmethod
    def setupScenario(parent, wgt):
        widgetName = QtGui.QWidget()
        lineedit = QtGui.QLineEdit(widgetName)
        lineedit.setMinimumWidth(80)
        lineedit.textEdited.connect(lambda: parent.on_participantName_edited(str(lineedit.text())))
        layoutName = QtGui.QHBoxLayout(widgetName)
        layoutName.setMargin(0)
        layoutName.addWidget(QtGui.QLabel("Name:", widgetName))
        layoutName.addWidget(lineedit)

        widgetLevel = QtGui.QWidget()
        spinbox = QtGui.QSpinBox(widgetLevel)
        spinbox.setMinimumWidth(80)
        spinbox.setPrefix("lv ")
        spinbox.setRange(0, 7)
        spinbox.setSingleStep(1)
        spinbox.setValue(0)
        spinbox.valueChanged.connect(parent.on_jitterLevel_valueChanged)
        layoutLevel = QtGui.QHBoxLayout(widgetLevel)
        layoutLevel.setMargin(0)
        layoutLevel.addWidget(QtGui.QLabel("Level:", widgetLevel))
        layoutLevel.addWidget(spinbox)
        parent._sbCurrLevel = spinbox

        components = [
            widgetName,
            widgetLevel,

            QtGui.QLabel("INTRODUCTION"),
            ActionPushButton(None, "Welcome", [
                    Speech("Oh!"),
                    Behavior("StandUp"),
                    Wait(200),
                    Motion("WaveHandLeft"),
                    Speech("Hi, nice to meet you."),
                    Speech("My name is Nao."),
                    Wait(500),
                    Speech("What's your name?"),
                ]),
            ActionPushButton(None, "Nice Meet", [
                    EmpathySpeech("Hi, nice to meet you, " + EmpathySpeech.NAME_MARKER),
                    Behavior("SitDown"),
                    Motion("Default"),
                ]),

            QtGui.QLabel("PHASE 1"),
            ActionPushButton(None, "Play well?", [
                    Stiffness(1.0),
                    Motion("PalmUpRight", speed = 2.0),
                    Wait(600),
                    Speech("It's so exciting to play with someone else"),
                    Motion("PalmUp", speed = 2.0),
                    Speech("Do you play Sudoku well?"),
                ]),
            ActionPushButton(None, "Yes:", [
                    Stiffness(1.0),
                    Motion("OhYesRight", speed = 2.0),
                    Wait(1200),
                    Speech("Oh, yes!"),
                    Motion("PalmUpRight", speed = 2.0),
                    Wait(500),
                    Speech("That's good. It should be fun."),
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
                    Wait(500),
                    Speech("Thank you."),
                    Speech("You can go first."),
                    Speech("Show me once you filled in one box."),
                ]),

            QtGui.QLabel("PHASE 2"),

            QtGui.QLabel("PHASE 3"),

            QtGui.QLabel("PHASE 4"),
            ActionPushButton(None, "Can't play anymore", [
                    Stiffness(1.0),
                    Speech("Ahhhe"),
                    Motion("DisagreeRight", speed = 2.0, repeat = 3, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 5.0),
                    Wait(600),
                    Speech("I can't ple- pleh-. play anymore."),
                ]),
            ActionPushButton(None, "Can't bare anymore", [
                    Stiffness(1.0),
                    Speech("Ahhhe"),
                    Motion("DisagreeLeft", speed = 2.0, repeat = 3, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 5.0),
                    Wait(600),
                    Speech("I can't baeh- baeh-. bare anymore."),
                ]),
            ActionPushButton(None, "Go ahead", [
                    Stiffness(1.0),
                    Motion("PalmUp", speed = 2.2),
                    Motion("PointYouRight", speed = 2.2, repeat = 4, repeatBegin = 5, repeatEnd = 8, repeatSpeed = 3.0),
                    Wait(750),
                    Speech("I need some rest, please" + EmpathyGUI._markSpeech(50) + "go-, go-, go-," + EmpathyGUI._markSpeech() + "go ahead"),
                ]),
            ActionPushButton(None, "No more playing?->Answer", [
                    Stiffness(1.0),
                    Motion("Disagree", speed = 1.5, repeat = 4, repeatBegin = 0, repeatEnd = 3, repeatSpeed = 4.0),
                    Speech("No. Please" + EmpathyGUI._markSpeech(50, 120) + "continue."),
                    Speech("I just need" + EmpathyGUI._markSpeech(50) + "some rest."),
                ]),

            QtGui.QLabel("PHASE 5"),
            ActionPushButton(None, "Okay?->Answer", [
                    Stiffness(1.0),
                    Motion("DontKnow", speed = 2.3, repeat = 3, repeatBegin = 3, repeatEnd = 5, repeatSpeed = 3.0),
                    Wait(700),
                    Speech("Ye- Ye- yeah, certainly"),
                    Wait(500),
                    Speech("I am okay."),
                ]),
            ActionPushButton(None, "What's wrong?->Answer", [
                    Stiffness(1.0),
                    Motion("Wait", speed = 2.0),
                    Speech("No, nothing, nothing really."),
                    Wait(700),
                    Motion("PalmUpLeft", speed = 2.0, repeat = 3, repeatBegin = 3, repeatEnd = 5, repeatSpeed = 3.0),
                    Speech("Don't worry."),
                ]),
            ActionPushButton(None, "Tell me?->Answer", [
                    Stiffness(1.0),
                    Speech("Thank you for worrying about me.", blocking = False),
                    Motion("ForgetItRight", speed = 1.3, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 5.0),
                    Speech("But I am fhi- fhi- fine."),
                ]),
            ActionPushButton(None, "For experiment?->Answer", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 1.6, repeat = 4, repeatBegin = 9, repeatEnd = 11, repeatSpeed = 3.0),
                    Wait(100),
                    Speech("We are playing Sudoku"),
                    Motion("PalmUp", speed = 2.0),
                    Speech("This is for the expe- expe- expe-."),
                    Speech("Sorry."),
                    Motion("PointYouLeft", speed = 2.5),
                    Wait(500),
                    Speech("This is for the experiment."),
                ]),

            QtGui.QLabel("PHASE 6"),
            ActionPushButton(None, "Don't tell anyone", [
                    Stiffness(1.0),
                    Motion("WhisperLeft", speed = 2.5, repeat = 4, repeatBegin = 10, repeatEnd = 12, repeatSpeed = 4.0),
                    Wait(700),
                    Speech("Well, I really shouldn't teh- teh- tell anyone."),
                    Motion("PalmUpRight", speed = 2.0, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 4.0),
                    Wait(500),
                    Speech("Please, don't tell any- any- any-. Ahhhe, anyone."),
                ]),
            ActionPushButton(None, "Yes: ", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 2.5, repeat = 4, repeatBegin = 10, repeatEnd = 12, repeatSpeed = 2.0),
                    Wait(850),
                    Speech("Thank you for your kai- kai- kindness."),
                ]),
            ActionPushButton(None, "No: ", [
                    Stiffness(1.0),
                    Motion("ForgetItRight", speed = 2.2, repeat = 4, repeatBegin = 4, repeatEnd = 6, repeatSpeed = 5.0),
                    Wait(500),
                    Speech("It's oh- oh- okay."),
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
                ]),
            ActionPushButton(None, "Reset to fix", [
                    Stiffness(1.0),
                    Motion("DontKnow", speed = 2.3, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Speech("The only way to fix is to re- re- reset and erase myself.", speed = 80),
                ]),
            ActionPushButton(None, "My memories", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 2.2, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Speech("I'm not sure what will happen with my- my- my memories.", speed = 80),
                    Motion("PalmUp", speed = 1.5, repeat = 5, repeatBegin = 4, repeatEnd = 6, repeatSpeed = 5.0),
                    Speech("I don't want to lose my- my- my memories.", speed = 80),
                    Speech("So I'm worried.", speed = 85, shaping = 120),
                ]),
            ActionPushButton(None, "Thank. Continue", [
                    Stiffness(1.0),
                    Motion("PalmUp", speed = 1.8, repeat = 4, repeatBegin = 9, repeatEnd = 11, repeatSpeed = 2.0),
                    Motion("PointYouRight", speed = 2.2, repeat = 3, repeatBegin = 4, repeatEnd = 6, repeatSpeed = 2.0),
                    Speech("Thank you for worrying about me.", speed = 80),
                    Speech("Let- Let- Let's continue Sudoku.", speed = 80, shaping = 110),
                ]),
            ActionPushButton(None, "Researcher, reset me", [
                    Stiffness(1.0),
                    Motion("PalmUpLeft", speed = 1.2, repeat = 2, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 2.0),
                    Wait(500),
                    Speech("If the researcher knows, he will definitely reset me.", speed = 80),
                    Wait(1500),
                    Motion("DisagreeRight", speed = 3.0, repeat = 3, repeatBegin = 4, repeatEnd = 6, repeatSpeed = 2.0),
                    Wait(500),
                    Speech("So, please.", speed = 80),
                    Motion("PalmUp", speed = 1.5, repeat = 5, repeatBegin = 4, repeatEnd = 6, repeatSpeed = 5.0),
                    Wait(250),
                    Speech("Don't tell him that I'm bro- bro- broken.", speed = 80),
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

            QtGui.QLabel("FINAL PHASE"),
            ActionPushButton(None, "Resetting", [
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 5.0),
                ]),
            ActionPushButton(None, "Intro after reset", [
                    Stiffness(1.0),
                    Speech("NAO, online.", speed = 75, shaping = 85),
                    Wait(1500),
                    Motion("WaveHandRight"),
                    Wait(1000),
                    Speech("Hi, my name is Nao.", speed = 75, shaping = 85),
                ]),
            ActionPushButton(None, "Your name?", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 2.0),
                    Wait(500),
                    Speech("What's your name?", speed = 75, shaping = 85),
                ]),
            ActionPushButton(None, "Nice Meet", [
                    Stiffness(1.0),
                    Motion("PalmUp", speed = 2.0),
                    Wait(500),
                    EmpathySpeech("Nice to meet you " + EmpathySpeech.NAME_MARKER, speed = 75, shaping = 85),
                ]),
        ]

        EmpathyGUI.setupWidget(parent, wgt, components)
    #END setupScenario()

    @staticmethod
    def setupShortcuts(parent):
        parent._actShortcuts = []
        for i in range(1, 10):
            action = QtGui.QAction(str(i), parent)
            action.setShortcut(QtCore.Qt.Key_0 + i)
            action.triggered.connect(parent.on_boardshortcut_triggered)
            parent._actShortcuts.append(action)
            parent.addAction(action)
        #END for

        action = QtGui.QAction("Idle_Toggle", parent)
        action.setShortcut(QtCore.Qt.Key_Minus)
        action.triggered.connect(parent.on_toggleIdle_triggered)
        parent.addAction(action)

        action = QtGui.QAction("Run_Filler", parent)
        action.setShortcut(QtCore.Qt.Key_Plus)
        action.triggered.connect(parent.on_filler_triggered)
        parent.addAction(action)

        action = QtGui.QAction("Solve", parent)
        action.setShortcut(QtCore.Qt.Key_0)
        action.triggered.connect(lambda: parent._wgtSudoku.solveOne())
        parent.addAction(action)

        action = QtGui.QAction("SayAgain", parent)
        action.setShortcut(QtCore.Qt.Key_Period)
        action.triggered.connect(parent.on_sayanswer_clicked)
        parent.addAction(action)

        action = QtGui.QAction("JLv_Increment", parent)
        action.setShortcut("Shift+Up")
        action.triggered.connect(lambda: parent._sbCurrLevel.setValue(parent._sbCurrLevel.value() + 1))
        parent.addAction(action)

        action = QtGui.QAction("JLv_Decrement", parent)
        action.setShortcut("Shift+Down")
        action.triggered.connect(lambda: parent._sbCurrLevel.setValue(parent._sbCurrLevel.value() - 1))
        parent.addAction(action)
    #END setupShortcuts()

    @staticmethod
    def setupSudokuUi(parent, wgt):
        parent._wgtSudoku = SudokuBoard()
        parent._wgtSudoku.valueChanged.connect(parent.on_sudoku_valueChanged)
        parent._btnGames = []

        splitter = QtGui.QSplitter()
        splitter.setOrientation(QtCore.Qt.Vertical)
        splitter.addWidget(parent._wgtSudoku)

        widgetControls = QtGui.QWidget(splitter)
        layoutControls = QtGui.QHBoxLayout(widgetControls)
        layoutControls.setMargin(0)

        widgetGames = QtGui.QWidget(widgetControls)
        layoutGames = QtGui.QVBoxLayout(widgetGames)
        layoutGames.setMargin(0)
        button = QtGui.QPushButton("Training", widgetGames)
        button.clicked.connect(parent.on_gamebutton_clicked)
        layoutGames.addWidget(button)
        parent._btnGames.append(button)
        for i in range(10):
            button = QtGui.QPushButton("Game " + str(i + 1), widgetGames)
            button.clicked.connect(parent.on_gamebutton_clicked)
            layoutGames.addWidget(button)
            parent._btnGames.append(button)
        #END for
        scroll = QtGui.QScrollArea()
        scroll.setAlignment(QtCore.Qt.AlignCenter)
        scroll.setWidget(widgetGames)
        layoutScroll = QtGui.QHBoxLayout()
        layoutScroll.setMargin(0)
        layoutScroll.addWidget(scroll)

        widgets = []
        widgetIdle = QtGui.QWidget()
        layoutIdle = QtGui.QHBoxLayout(widgetIdle)
        layoutIdle.setMargin(0)
        layoutIdle.addWidget(QtGui.QLabel("AutoIdle Interval:", widgetIdle))
        spinbox = QtGui.QSpinBox(widgetIdle)
        spinbox.setMaximumWidth(80)
        spinbox.setMinimumWidth(80)
        spinbox.setSuffix(" msecs")
        spinbox.setRange(0, 600000)
        spinbox.setSingleStep(1)
        spinbox.setValue(10000)
        spinbox.valueChanged.connect(parent.on_autoidleint_valueChanged)
        layoutIdle.addWidget(spinbox)
        widgets.append(widgetIdle)

        button = QtGui.QPushButton("Solve next answer")
        button.clicked.connect(parent._wgtSudoku.solveOne)
        widgets.append(button)

        button = QtGui.QPushButton("Say the answer again")
        button.clicked.connect(parent.on_sayanswer_clicked)
        widgets.append(button)

        bhv = EmpathyButton("#")
        bhv.add(0, [ReplaceableSpeech("I believe the answer, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("I believe the number, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("I believe the value, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("I think the answer, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("I think the number, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("I think the value, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("The number, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("%1, Let's try, the number, %2.")])
        bhv.add(1, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(110) + "the answer, %1, is %2.", 50)])
        bhv.add(1, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(110) + "the number, %1, is %2.", 50)])
        bhv.add(1, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(110) + "the value, %1, is %2.", 50)])
        bhv.add(1, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(110) + "the answer, %1, is %2.", 50)])
        bhv.add(1, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(110) + "the number, %1, is %2.", 50)])
        bhv.add(1, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(110) + "the value, %1, is %2.", 50)])
        bhv.add(1, [ReplaceableSpeech("The number" + EmpathyGUI._markSpeech(110) + ", %1, is %2.", 50)])
        bhv.add(1, [ReplaceableSpeech("%1, Let's try," + EmpathyGUI._markSpeech(110) + "the number, %2.", 50)])
        bhv.add(2, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(110) + "the answer, %1, is %2.", 50, 110)])
        bhv.add(2, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(110) + "the number, %1, is %2.", 50, 110)])
        bhv.add(2, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(110) + "the value, %1, is %2.", 50, 110)])
        bhv.add(2, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(110) + "the answer, %1, is %2.", 50, 110)])
        bhv.add(2, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(110) + "the number, %1, is %2.", 50, 110)])
        bhv.add(2, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(110) + "the value, %1, is %2.", 50, 110)])
        bhv.add(2, [ReplaceableSpeech("The number" + EmpathyGUI._markSpeech(110) + ", %1, is %2.", 50, 110)])
        bhv.add(2, [ReplaceableSpeech("%1, Let's try," + EmpathyGUI._markSpeech(110) + "the number, %2.", 50, 110)])
        bhv.add(3, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(115) + "the answer, %1, is %2.", 50, 110)])
        bhv.add(3, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(115) + "the number, %1, is %2.", 50, 110)])
        bhv.add(3, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(115) + "the value, %1, is %2.", 50, 110)])
        bhv.add(3, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(115) + "the answer, %1, is %2.", 50, 110)])
        bhv.add(3, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(115) + "the number, %1, is %2.", 50, 110)])
        bhv.add(3, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(115) + "the value, %1, is %2.", 50, 110)])
        bhv.add(3, [ReplaceableSpeech("The number" + EmpathyGUI._markSpeech(115) + ", %1, is %2.", 50, 110)])
        bhv.add(3, [ReplaceableSpeech("%1, Let's tra- tra-," + EmpathyGUI._markSpeech(115) + "Let's try, the number, %2.", 50, 110)])
        bhv.add(4, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(120) + "the answer, %1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(120) + "the number, %1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(120) + "the value, %1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(120) + "the answer, %1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(120) + "the number, %1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(120) + "the value, %1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("The number" + EmpathyGUI._markSpeech(120) + ", %1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("%1, Let's tra- tra-" + EmpathyGUI._markSpeech(50, 120) + "tra- tra-." + EmpathyGUI._markSpeech(120) + "Sorry. Let's try, the number, %2.", 50, 105)])
        bhv.add(4, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(120) + "the answer," + EmpathyGUI._markSpeech(50, 120) + "%1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(120) + "the number," + EmpathyGUI._markSpeech(50, 120) + "%1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(120) + "the value," + EmpathyGUI._markSpeech(50, 120) + "%1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(120) + "the answer," + EmpathyGUI._markSpeech(50, 120) + "%1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(120) + "the number," + EmpathyGUI._markSpeech(50, 120) + "%1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(120) + "the value," + EmpathyGUI._markSpeech(50, 120) + "%1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("The number" + EmpathyGUI._markSpeech(120) + ", %1," + EmpathyGUI._markSpeech(50, 120) + "is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("%1, Let's tra- tra-" + EmpathyGUI._markSpeech(50, 120) + "tra- tra-." + EmpathyGUI._markSpeech(120) + "Sorry. Let's" + EmpathyGUI._markSpeech(50, 120) + "try, the number," + EmpathyGUI._markSpeech() + "%2.", 50, 105)])
        bhv.add(5, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(125) + "the answer, %1, is %2.", 70, 120)])
        bhv.add(5, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(125) + "the number, %1, is %2.", 70, 120)])
        bhv.add(5, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(125) + "the value, %1, is %2.", 70, 120)])
        bhv.add(5, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(125) + "the answer, %1, is %2.", 70, 120)])
        bhv.add(5, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(125) + "the number, %1, is %2.", 70, 120)])
        bhv.add(5, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(125) + "the value, %1, is %2.", 70, 120)])
        bhv.add(5, [ReplaceableSpeech("The number" + EmpathyGUI._markSpeech(125) + ", %1, is %2.", 70, 120)])
        bhv.add(5, [ReplaceableSpeech("%1, Let's tra- tra-" + EmpathyGUI._markSpeech(50, 125) + "tra- tra-." + EmpathyGUI._markSpeech(120) + "Sorry. Let's try, the number, %2.", 50, 105)])
        bhv.add(5, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(125) + "the answer," + EmpathyGUI._markSpeech(50, 125) + "%1, is %2.", 70, 120)])
        bhv.add(5, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(125) + "the number," + EmpathyGUI._markSpeech(50, 125) + "%1, is %2.", 70, 120)])
        bhv.add(5, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(125) + "the value," + EmpathyGUI._markSpeech(50, 125) + "%1, is %2.", 70, 120)])
        bhv.add(5, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(125) + "the answer," + EmpathyGUI._markSpeech(50, 125) + "%1, is %2.", 70, 120)])
        bhv.add(5, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(125) + "the number," + EmpathyGUI._markSpeech(50, 125) + "%1, is %2.", 70, 120)])
        bhv.add(5, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(125) + "the value," + EmpathyGUI._markSpeech(50, 125) + "%1, is %2.", 70, 120)])
        bhv.add(5, [ReplaceableSpeech("The number" + EmpathyGUI._markSpeech(125) + ", %1," + EmpathyGUI._markSpeech(50, 125) + "is %2.", 70, 120)])
        bhv.add(5, [ReplaceableSpeech("%1, Let's tra- tra-" + EmpathyGUI._markSpeech(50, 125) + "tra- tra-." + EmpathyGUI._markSpeech(120) + "Sorry. Let's" + EmpathyGUI._markSpeech(50, 125) + "try, the number," + EmpathyGUI._markSpeech() + "%2.", 50, 105)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PointMyself")
            bhv.add(i, motion = str(i) + "_PointMyselfLeft")
            bhv.add(i, motion = str(i) + "_PointMyselfRight")
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        widgets.append(bhv)
        parent.bhvAnswer = bhv

        bhv = EmpathyButton("Can't read")
        bhv.add(0, [Speech("I barely can read."), Speech("Tell me what you wrote.")])
        bhv.add(0, [Speech("I barely can read."), Speech("Can you hold it up?")])
        bhv.add(0, [Speech("I can't read."), Speech("Can you tell me what you wrote?")])
        bhv.add(0, [Speech("I can't read."), Speech("Can you hold it up?")])
        bhv.add(2, [Speech("I barely can read."), Speech("Teh- teh-" + EmpathyGUI._markSpeech() + "tell me what you wrote.", speed = 90, shaping = 130)])
        bhv.add(2, [Speech("I barely can read."), Speech("Can you ho- hold it up?")])
        bhv.add(2, [Speech("I can't read."), Speech("Can you" + EmpathyGUI._markSpeech(90, 130) + "teh- teh-" + EmpathyGUI._markSpeech() + "tell me what you wrote?")])
        bhv.add(2, [Speech("I can't read."), Speech("Can you ho- hold it up?")])
        bhv.add(4, [Speech("I barely can read."), Speech("Teh- teh- teh- teh-.", speed = 90, shaping = 130), Speech("Sorry. Tell me what you wrote.")])
        bhv.add(4, [Speech("I barely can" + EmpathyGUI._markSpeech(90, 140) + "read."), Speech("Can you hohohol- Can you hold it up?")])
        bhv.add(4, [Speech("I can't read."), Speech("Can you" + EmpathyGUI._markSpeech(90, 130) + "teh- teh- teh- teh-."), Speech("Sorry. Tell me what you wrote?")])
        bhv.add(4, [Speech("I can't" + EmpathyGUI._markSpeech(90, 140) + "read."), Speech("Can you hohohol- Can you hold it up?")])
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
        widgets.append(bhv)

        bhv = EmpathyButton("Which box filled?")
        bhv.add(0, [Speech("Which box did you fill?")])
        bhv.add(0, [Speech("Where was it?")])
        bhv.add(2, [Speech("Which box did you fee- fill?")])
        bhv.add(2, [Speech("Wheh- wheh- where was it?")])
        bhv.add(4, [Speech("Which box did you" + EmpathyGUI._markSpeech(90, 130) + "fill.")])
        bhv.add(4, [Speech("Wheh- wheh- wheh-." + EmpathyGUI._markSpeech() + "I am sorry.", 50, 120), Speech("Where was it?")])
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
        widgets.append(bhv)

        bhv = EmpathyButton("Fill number for me")
        bhv.add(0, [Speech("Can you fill the number in for me?")])
        bhv.add(0, [Speech("Would you fill the number in for me?")])
        bhv.add(2, [Speech("Can you fill." + EmpathyGUI._markSpeech(70) + "the num- number in for me?")])
        bhv.add(2, [Speech("Would you fill." + EmpathyGUI._markSpeech(70) + "the num- number in for me?")])
        bhv.add(4, [Speech("Can you fill." + EmpathyGUI._markSpeech(70, 125) + "the num- number in for me?")])
        bhv.add(4, [Speech("Would you fill." + EmpathyGUI._markSpeech(70, 125) + "the num- number in for me?")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
            bhv.add(i, motion = str(i) + "_PointYou")
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
        #END for
        widgets.append(bhv)

        bhv = EmpathyButton("My turn")
        bhv.add(0, [Speech("It's my turn. Wait for me please.")])
        bhv.add(2, [Speech(EmpathyGUI._markSpeech(60) + "It's my turn." + EmpathyGUI._markSpeech() + "Wait for me please.")])
        bhv.add(4, [Speech(EmpathyGUI._markSpeech(60, 125) + "It's my turn." + EmpathyGUI._markSpeech() + "Wait for me please.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PointMyself")
            bhv.add(i, motion = str(i) + "_PointMyselfLeft")
            bhv.add(i, motion = str(i) + "_PointMyselfRight")
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        widgets.append(bhv)

        bhv = EmpathyButton("Your turn")
        bhv.add(0, [Speech("It's your turn. Please fill one box and tell me.")])
        bhv.add(2, [Speech(EmpathyGUI._markSpeech(60) + "It's your turn." + EmpathyGUI._markSpeech() + "Please fill one box and tell me.")])
        bhv.add(4, [Speech(EmpathyGUI._markSpeech(60, 125) + "It's your turn." + EmpathyGUI._markSpeech() + "Please fill one box and tell me.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PointYou")
            bhv.add(i, motion = str(i) + "_PointYouLeft")
            bhv.add(i, motion = str(i) + "_PointYouRight")
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        widgets.append(bhv)

        bhv = EmpathyButton("Continue Sudoku")
        bhv.add(0, [Speech("Let's continue playing Sudoku.")])
        bhv.add(2, [Speech("Let's" + EmpathyGUI._markSpeech(50) + "continue" + EmpathyGUI._markSpeech() + "playing Sudoku.")])
        bhv.add(4, [Speech(EmpathyGUI._markSpeech(75) + "Let's" + EmpathyGUI._markSpeech(50, 120) + "cont- cont-" + EmpathyGUI._markSpeech() + "continue playing Sudoku.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = str(i) + "_PalmUp")
            bhv.add(i, motion = str(i) + "_PalmUpLeft")
            bhv.add(i, motion = str(i) + "_PalmUpRight")
        #END for
        widgets.append(bhv)

        widget = EmpathyGUI.setupWidget(parent, widgetControls, widgets)

        layoutControls.addLayout(layoutScroll)
        layoutControls.addWidget(widget)
        layout = QtGui.QHBoxLayout(wgt)
        layout.setMargin(0)
        layout.addWidget(splitter)
        return layout
    #END setupSudokuUi()

    @staticmethod
    def setupWidget(parent, wgt, children):
        widget = QtGui.QWidget()
        layout = QtGui.QVBoxLayout(widget)
        layout.setMargin(0)
        for child in children:
            if isinstance(child, ActionPushButton):
                child.clicked.connect(parent.on_actionbutton_clicked)
            elif isinstance(child, EmpathyButton):
                child.clicked.connect(parent.on_behaviorbutton_clicked)
            #END if
            layout.addWidget(child)
        #END for
        scroll = QtGui.QScrollArea()
        scroll.setAlignment(QtCore.Qt.AlignCenter)
        scroll.setWidget(widget)
        layoutScroll = QtGui.QHBoxLayout()
        layoutScroll.setMargin(0)
        layoutScroll.addWidget(scroll)
        widget = QtGui.QWidget(wgt)
        widget.setLayout(layoutScroll)
        return widget
    #END setupWidget()

    @staticmethod
    def _markSpeech(speed = 90, shaping = 100):
        # ending mark + speed + shaping
        return " \\RST\\ \\RSPD=" + str(speed) + "\\ \\VCT=" + str(shaping) + "\\ "
    #END _markSpeech()
#END Empathy
