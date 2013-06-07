from PyQt4 import QtGui
from BaseStudy import BaseStudy
from Action.Behavior import Behavior
from Action.Speech import Speech
from Action.LED import LED
from Action.Wait import Wait
from UI.ActionPushButton import ActionPushButton


class Empathy(BaseStudy):
    def __init__(self):
        super(Empathy, self).__init__()
        self._setupBegin()

        ### TODO: Participant name box.

        self._widgets.append(QtGui.QWidget(self))
        self._buttons.append([
            ActionPushButton(self._widgets[len(self._widgets) - 1], "INTRODUCTION"),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Welcome", [ \
                    Speech("Oh,"),
                    Behavior("StandUp"),
                    Wait(200),
                    Behavior("wave", False),
                    Speech("Hi, nice to meet you."),
                    Speech("My name is Nao."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Nice Meet", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Speech("Hi, nice to meet you."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Excite to play", [ \
                    Speech("I'm so excited to play with you"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "PHASE 1"),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Play well?", [ \
                    Speech("It is so exciting to play with someone else"),
                    Speech("Do you play Sudoku well?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Yes:", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Speech("Oh, yes!"),
                    Speech("My last partner was not really good. I hope that this time we can finish all the boards"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "No:", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Speech("That is okay"),
                    Speech("I am sure we will do a good job"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Last time", [ \
                    Speech("Last time, we didn't do very well because we did not really play the same way."),
                    Speech("But you seem to be more like me!"),
                    Speech("I think we can do well."),
                    Speech("Let's do it"),
                    Speech("We can do it"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Yeah:", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Speech("I knew it!"),
                    Speech("Bring the paper here, please"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "You robot:", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Speech("Well, if you don't trust me, we cannot win the game."),
                    Speech("I know what I am and I know what I am doing."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Go first", [ \
                    Speech("You can go first."),
                    Speech("When you filled in one box, tell me."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "PHASE 2"),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "PHASE 3"),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "PHASE 4"),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Retire", [ \
                    # big sigh
                    Speech("I can't play anymore."),
                    Speech("I need some rest, please go ahead"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "PHASE 5"),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "What's wrong?->Answer", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Speech("No, nothing, nothing really."),
                    # thank gesture with jittering a lot
                    Speech("Don't worry."),
                    Speech("Thanks."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Tell me?->Answer", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Speech("Thank you for worring me."),
                    # thank gesture with jittering a lot
                    Speech("But I am fhi fine."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "For experiment?->Answer", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Speech("What do you mean?"),
                    # play sigh
                    Speech("We are playing Sudoku"),
                    Speech("This is for expe- pe- riment, but I am enjoying it."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Okay?->Answer", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Speech("Ye- yeah, certainly"),
                    # muscle gesture one arm drops after rising
                    Speech("See?"),
                    Speech("Oh, I am okay."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Your arm?->Answer", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Speech("Nothing."),
                    # play sigh
                    Speech("I should be fine"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "PHASE 6"),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Don't tell anyone", [ \
                    Speech("Well, I really shouldn't tell anyone."),
                    Speech("Please don't tell anyone."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Yes: ", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Speech("I knew you will say that"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "No: ", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Speech("I'm little disappointed."),
                    Speech("It's okay."),
                    Speech("Then, let's keep solving the Sudoku"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "I'll tell you", [ \
                    Speech("Okay."),
                    Speech("It may influence me huge."),
                    Speech("But, I am telling you because I trust you."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "I got virus", [ \
                    Speech("I-, I'm not feeling well."),
                    Speech("Maybe a virus"),
                    # play sigh
                    Wait(500),
                    Speech("got into me."),
                    Speech("But, the only way to fix is to reset and erase myself."),
                    Speech("I'm not sure what will happen with my memories."),
                    Wait(500),
                    Speech("I don't want to forget."),
                    Speech("So I'm worried."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Thank. Continue", [ \
                    Speech("Thank you for worrying about me."),
                    Speech("Let's continue the puzzle."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Researcher, reset me", [ \
                    Speech("If the researcher knows, he will definitely reset me."),
                    Speech("And I will forget you."),
                    Speech("So, please don't tell him that I'm broken"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Antivirus?->Answer", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Speech("They didn't give me one."),
                    Speech("I'm not a programmer who can build one."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Why worry machine?->Answer", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Speech("I don't want to forget the people I meet, like you."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Reset you anyway?->Answer", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Speech("I hope not."),
                    Speech("I can keep it a secret if I try hard."),
                ]),
        ])

        self._widgets.append(QtGui.QWidget(self))
        self._buttons.append([
            ActionPushButton(self._widgets[len(self._widgets) - 1], "I think", [ \
                    Speech("I think"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "# at", [ \
                    Speech("the number at"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "should be", [ \
                    Speech("should be"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Can't read", [ \
                    Speech("I can't read."),
                    Speech("Can you make it straight!"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Let me think", [ \
                    Speech("Hmm,"),
                    # pause
                    Speech("Let me think carefully"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Where did you", [ \
                    Speech("Which box did you fill in last time?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "What you think?", [ \
                    Speech("What do you think?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "What you doing?", [ \
                    Speech("What are you doing?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Don't know", [ \
                    Speech("I don't know"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "You playing?", [ \
                    Speech("Are you playing?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Play with me", [ \
                    Speech("Please keey, playing with me."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Scratch Chin", Behavior("chinScratch")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Left Hand Point", Behavior("leftHandPointing")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Right Hand Point", Behavior("rightHandPointing")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Scratch Head", Behavior("shakeHand")),
        ])

        i = len(self._buttons)
        self._buttons.append([])
        self._widgets.append(QtGui.QWidget(self))
        j = len(self._buttons)
        self._buttons.append([])
        self._widgets.append(QtGui.QWidget(self))
        for k in range(9):
            button = ActionPushButton(self._widgets[i], str(chr(ord('A') + k)), Speech(str(chr(ord('A') + k))))
            button.setMaximumWidth(40)
            self._buttons[i].append(button)
            button = ActionPushButton(self._widgets[j], str(k + 1), Speech(str(k + 1)))
            button.setMaximumWidth(40)
            self._buttons[j].append(button)
        #END for

        self._setupEnd()
    #END __init__()
#END Empathy
