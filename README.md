##NAO Robotic Controller
Robotic Controller for use with the NAO Humanoid Systems.

[HCI Lab, University of Manitoba](http://www.hci.cs.umanitoba.ca)

-----------------------
| Table of Contents |
-----------------------
	1. Action
		a. __init__.py
		b. ActionModel.py
		c. ActionQueue.py	
		d. ActionStart.py
		e. ActionStop.py
		f. BaseAction.py
		g. Behavior.py
		h. HeadMotion.py
		i. LED.py
		j. Motion.py
		k. ReplaceableSpeech.py
		l. Speech.py
		m. Stiffness.py
		n. StopMotion.py
		o. StopSpeech.py
		p. ThreadTimer.py
		q. Wait.py
		r. WaitMotion.py
		s. WaitSpeech.py
	
	2. NAO
		a. __init__.py
		b. NAO.py
		c. NAOCamera.py
		d. NAOMotion.py
		e. NAOMotionList.py
	
	3. Study
		a. __init__.py
		b. BaseStudy.py
		c. Empathy.py
		d. EmpathyGUI.py
		e. EmpathyMotionList.py
		f. EmpathyRandomButton.py
		g. EmpathyScenarioButton.py
		h. EmpathySpeech.py
		i. EmpathySudoku.py
		j. General.py
		k. Jitter.py
		l. MentalChallenge.py
		m. Tedium.py


	4. UI
		a. __init__.py
		b. AboutWindow.py
		c. ActionListWidget.py
		d. ActionPushButton.py
		e. CameraWidget.py
		f. ConnectDialog.py
		g. MainWindow.py
		h. MovementWidget.py
		i. SpeechWidget.py
		j. SubmittableLineEdit.py
		k. SubmittableTextEdit.py
		l. SudokuBoard.py
		m. TimerWidget.py
	
	5. build
		a. General Information
	
	6. dist
		a. General Information
	
	7. images
		a. General Information
	
	8. Miscellaneous
		a. Defintions.py
		b. main.py
		c. servertesting.py
		d. setup.py
		e. sudoku.py
		f. SudokuSolver.py

----------
| Action |
----------
	1a. __init__.py
		Marks the directory as a Python package.
		
	1b. ActionModel.py
		Queues up actions (speech or motions) to be run by NAO.

	1c. ActionQueue.py
		Creates a queue for speech/motions to be used.

	1d. ActionStart.py
		Starts the inputted action.

	1e. ActionStop.py
		Stops the current action.

	1f. BaseAction.py
		Executes the current action.		

	1g. Behavior.py
		Calls the behavior.

	1h. HeadMotion.py
		Moves the NAO's head.
	1i. LED.py
		Changes the LED colors.

	1j. Motion.py
		Modifies the motion files stored in the NAO.

	1k. ReplaceableSpeech.py
		Replaces arguments in the speech.

	1l. Speech.py
		Changes the volume, speed and shape of the NAO's voice.

	1m. Stiffness.py
		Sets the stiffness for the NAO's joints.

	1n. StopMotion.py
		Stops the current motion.

	1o. StopSpeech.py
		Stops the current speech.

	1p. ThreadTimer.py
		Creates a thread for the timer.

	1q. Wait.py
		Creates a delay between speech and motions.

	1r. WaitMotion.py
		Wait function for motions.

	1s. WaitSpeech.py
		Wait function for speech.

-------
| NAO |
-------
	2a. __init__.py
		Marks the directory as a Python package.
		
	2b. NAO.py
		Old code used for connecting to the NAO.

	2c. NAOCamera.py
		Creates a thread for the camera.

	2d. NAOMotion.py
		Creates a motion.

	2e. NAOMotionList.py
		List of various motions

---------
| Study |
---------
	3a. __init__.py
		Marks the directory as a Python package.
		
	3b. BaseStudy.py
		General speech and motion features that will be used in all/most studies.

	3c. Empathy.py
		Various functions used in the Empathy study.

	3d. EmpathyGUI.py
		Buttons with various assignments used in the Empathy study.

	3e. EmpathyMotionList.py
		Random motions used throughout the conversation.

	3f. EmpathyRandomButton.py
		Randomly picks a motion from a list.
		
	3g. EmpathyScenarioButton.py
		Randomly picks a motion from the scenario.

	3h. EmpathySpeech.py
		Stores the participants name for future use.

	3i. EmpathySudoku.py
		Stores the various boards used in the Empathy study.

	3j. General.py		
		General buttons for the Empathy study.

	3k. Jitter.py
		Jitters the motions for use in the Empathy study.

	3l. MentalChallenge.py
		Speech used in the mental challenge study.

	3m. Tedium.py
		Speech used in the tedium study.
	
------
| UI |
------
	4a. __init__.py
		Marks the directory as a Python package.
		
	4b. AboutWindow.py
		Popup window with a link to the HCI website.

	4c. ActionListWidget.py
		List of buttons used with the movement GUI.

	4d. ActionPushButton.py
		Creates a button which sets a title for it, and contains a paragraph of 
		text which the NAO will say.

	4e. CameraWidget.py
		GUI Camera Widget that shows a live feed from the NAO, allows for 
		switching between the top and bottom camera.

	4f. ConnectDialog.py
		Popup for the connection window, which allows various connections to 
		the robot, camera, and speech.

	4g. MainWindow.py
		The main window of the software.

	4h. MovementWidget.py
		GUI Queue for storing motions that will be run.

	4i. SpeechWidget.py
		Text to speech widget.

	4j. SubmittableLineEdit.py
		UI specific for editing a single line.

	4k. SubmittableTextEdit.py
		UI specific for editing multiple lines.

	4l. SudokuBoard.py
		Creates a GUI for the Sudoku board.

	4m. TimerWidget.py
		Creates a simple timer.
	

---------
| build |
---------
	5a. General Information
		Auto generated files by Py2Exe.
	
--------
| dist |
--------
	6a. General Information
		Contains the executable version of the software, along with all the
		required files for running.
	
----------
| images |
----------
	7a. General Information
		Images used throughout the code, includes some extras that have been 
		removed from older versions.
	
-----------------
| Miscellaneous |
-----------------
	8a. Defintions.py
		Definitions of various words used throughout the project, such as 
		default IP address, port, etcetera. 
	
	8b. main.py
		The main code for running the software.
	
	8c. servertesting.py
		Old code used for testing the connection to the NAO.
	
	8d. setup.py
		The code required for generating an executable version of the software.
	
	8e. sudoku.py
		Creates a Sudoku board.
	
	8f. SudokuSolver.py
		Allows for solving the next most obvious position, or the entire board.
