#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was originally created using PsychoPy3 Experiment Builder (v2020.2.10).

 The following study should be referred to access the original study.
    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

For current study, the original code has been adapted with relevant changes made to make it suitable for the study. 
"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'IAT-1.4'  # from the Builder filename that created this script
expInfo = {'participant': '', 'order': ['random', 1, 2], 'session': '001', 'gender': ['male', 'female', 'other']}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\beenish\\Desktop\\IITGN\\Brain_Imaging\\Assignment 3\\openiat-master\\openIAT_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
  
  # create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
if expInfo['order']=='random':
    expInfo['order'] = randint(1,2)
    
blocks_file = "blocks_order"+str(expInfo['order'])+".xlsx"
instructs_text = visual.TextStim(win=win, name='instructs_text',
    text='default text',
    font='Arial',
    units='height', pos=[0, 0], height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instruct_done = keyboard.Keyboard()
instr_done_button = visual.Rect(
    win=win, name='instr_done_button',units='height', 
    width=(0.4, 0.1)[0], height=(0.4, 0.1)[1],
    ori=0, pos=(0, -0.4),
    lineWidth=1, lineColor='darkgreen', lineColorSpace='rgb',
    fillColor='lightgreen', fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
instr_done_label = visual.TextStim(win=win, name='instr_done_label',
    text='Next...',
    font='Arial',
    units='height', pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='darkgreen', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
instr_done_touch = event.Mouse(win=win)
x, y = [None, None]
instr_done_touch.mouseClock = core.Clock()

# Initialize components for Routine "ready"
readyClock = core.Clock()
main_ready_msg = visual.TextStim(win=win, name='main_ready_msg',
    text='Take note of the categories below\n \nPosition your index fingers \n \nPress the space bar (or one of the green buttons) to begin',
    font='Arial',
    units='height', pos=[0, 0], height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
button_L = visual.Rect(
    win=win, name='button_L',units='height', 
    width=(0.4, 0.2)[0], height=(0.4, 0.2)[1],
    ori=0, pos=(-0.4, -0.3),
    lineWidth=1, lineColor='darkgreen', lineColorSpace='rgb',
    fillColor='lightgreen', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
ready_label_L = visual.TextStim(win=win, name='ready_label_L',
    text='default text',
    font='Arial',
    units='height', pos=[-0.4, -0.3], height=0.05, wrapWidth=None, ori=0, 
    color='darkgreen', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
button_R = visual.Rect(
    win=win, name='button_R',units='height', 
    width=(0.4, 0.2)[0], height=(0.4, 0.2)[1],
    ori=0, pos=(0.4, -0.3),
    lineWidth=1, lineColor='darkgreen', lineColorSpace='rgb',
    fillColor='lightgreen', fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
ready_label_R = visual.TextStim(win=win, name='ready_label_R',
    text='default text',
    font='Arial',
    units='height', pos=[0.4, -0.3], height=0.05, wrapWidth=None, ori=0, 
    color='darkgreen', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ready_done_mouse = event.Mouse(win=win)
x, y = [None, None]
ready_done_mouse.mouseClock = core.Clock()
ready_done = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    units='height', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_stim = visual.ImageStim(
    win=win,
    name='image_stim', units='height', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_stim = visual.TextStim(win=win, name='text_stim',
    text='default text',
    font='Arial',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp = keyboard.Keyboard()
touch_resp = event.Mouse(win=win)
x, y = [None, None]
touch_resp.mouseClock = core.Clock()
button_left = visual.Rect(
    win=win, name='button_left',units='height', 
    width=(0.4, 0.2)[0], height=(0.4, 0.2)[1],
    ori=0, pos=(-0.4, -0.3),
    lineWidth=1, lineColor='darkgreen', lineColorSpace='rgb',
    fillColor='lightgreen', fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
trial_label_left = visual.TextStim(win=win, name='trial_label_left',
    text='default text',
    font='Arial',
    units='height', pos=[-0.4, -0.3], height=0.05, wrapWidth=None, ori=0, 
    color='darkgreen', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
button_right = visual.Rect(
    win=win, name='button_right',units='height', 
    width=(0.4, 0.2)[0], height=(0.4, 0.2)[1],
    ori=0, pos=(0.4, -0.3),
    lineWidth=1, lineColor='darkgreen', lineColorSpace='rgb',
    fillColor='lightgreen', fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
trial_label_right = visual.TextStim(win=win, name='trial_label_right',
    text='default text',
    font='Arial',
    units='height', pos=[0.4, -0.3], height=0.05, wrapWidth=None, ori=0, 
    color='darkgreen', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback_msg = visual.TextStim(win=win, name='feedback_msg',
    text='default text',
    font='Arial',
    units='height', pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "end_thanks"
end_thanksClock = core.Clock()
thanks_text = visual.TextStim(win=win, name='thanks_text',
    text='The End. \n \nThank you for your participation.',
    font='Arial',
    units='height', pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
instruct_pages = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('instructs.xlsx'),
    seed=None, name='instruct_pages')
thisExp.addLoop(instruct_pages)  # add the loop to the experiment
thisInstruct_page = instruct_pages.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstruct_page.rgb)
if thisInstruct_page != None:
    for paramName in thisInstruct_page:
        exec('{} = thisInstruct_page[paramName]'.format(paramName))

for thisInstruct_page in instruct_pages:
    currentLoop = instruct_pages
    # abbreviate parameter names if possible (e.g. rgb = thisInstruct_page.rgb)
    if thisInstruct_page != None:
        for paramName in thisInstruct_page:
            exec('{} = thisInstruct_page[paramName]'.format(paramName))
    
 # Prepare to start Routine "instructions"
    continueRoutine = True
    # update component parameters for each repeat
    instructs_text.setText(instruct_text)
    instruct_done.keys = []
    instruct_done.rt = []
    _instruct_done_allKeys = []
    # setup some python lists for storing info about the instr_done_touch
    instr_done_touch.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    instructionsComponents = [instructs_text, instruct_done, instr_done_button, instr_done_label, instr_done_touch]
    for thisComponent in instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

     # -------Run Routine "instructions"-------
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructs_text* updates
        if instructs_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructs_text.frameNStart = frameN  # exact frame index
            instructs_text.tStart = t  # local t and not account for scr refresh
            instructs_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructs_text, 'tStartRefresh')  # time at next scr refresh
            instructs_text.setAutoDraw(True)
        
        # *instruct_done* updates
        waitOnFlip = False
        if instruct_done.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruct_done.frameNStart = frameN  # exact frame index
            instruct_done.tStart = t  # local t and not account for scr refresh
            instruct_done.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct_done, 'tStartRefresh')  # time at next scr refresh
            instruct_done.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instruct_done.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instruct_done.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instruct_done.status == STARTED and not waitOnFlip:
            theseKeys = instruct_done.getKeys(keyList=['space'], waitRelease=False)
            _instruct_done_allKeys.extend(theseKeys)
            if len(_instruct_done_allKeys):
                instruct_done.keys = _instruct_done_allKeys[-1].name  # just the last key pressed
                instruct_done.rt = _instruct_done_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *instr_done_button* updates
        if instr_done_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_done_button.frameNStart = frameN  # exact frame index
            instr_done_button.tStart = t  # local t and not account for scr refresh
            instr_done_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_done_button, 'tStartRefresh')  # time at next scr refresh
            instr_done_button.setAutoDraw(True)
        
        # *instr_done_label* updates
        if instr_done_label.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_done_label.frameNStart = frameN  # exact frame index
            instr_done_label.tStart = t  # local t and not account for scr refresh
            instr_done_label.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_done_label, 'tStartRefresh')  # time at next scr refresh
            instr_done_label.setAutoDraw(True)
        # *instr_done_touch* updates
        if instr_done_touch.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_done_touch.frameNStart = frameN  # exact frame index
            instr_done_touch.tStart = t  # local t and not account for scr refresh
            instr_done_touch.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_done_touch, 'tStartRefresh')  # time at next scr refresh
            instr_done_touch.status = STARTED
            instr_done_touch.mouseClock.reset()
            prevButtonState = instr_done_touch.getPressed()  # if button is down already this ISN'T a new click
        if instr_done_touch.status == STARTED:  # only update if started and not finished!
            buttons = instr_done_touch.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [instr_done_button]:
                        if obj.contains(instr_done_touch):
                            gotValidClick = True
                            instr_done_touch.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
 # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instruct_pages.addData('instr_done_button.started', instr_done_button.tStartRefresh)
    instruct_pages.addData('instr_done_button.stopped', instr_done_button.tStopRefresh)
    instruct_pages.addData('instr_done_label.started', instr_done_label.tStartRefresh)
    instruct_pages.addData('instr_done_label.stopped', instr_done_label.tStopRefresh)
    # store data for instruct_pages (TrialHandler)
    x, y = instr_done_touch.getPos()
    buttons = instr_done_touch.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [instr_done_button]:
            if obj.contains(instr_done_touch):
                gotValidClick = True
                instr_done_touch.clicked_name.append(obj.name)
    instruct_pages.addData('instr_done_touch.x', x)
    instruct_pages.addData('instr_done_touch.y', y)
    instruct_pages.addData('instr_done_touch.leftButton', buttons[0])
    instruct_pages.addData('instr_done_touch.midButton', buttons[1])
    instruct_pages.addData('instr_done_touch.rightButton', buttons[2])
    if len(instr_done_touch.clicked_name):
        instruct_pages.addData('instr_done_touch.clicked_name', instr_done_touch.clicked_name[0])
    instruct_pages.addData('instr_done_touch.started', instr_done_touch.tStart)
    instruct_pages.addData('instr_done_touch.stopped', instr_done_touch.tStop)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'instruct_pages'


# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(blocks_file),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
      
 # ------Prepare to start Routine "ready"-------
    continueRoutine = True
    # update component parameters for each repeat
    ready_label_L.setText(label_left)
    ready_label_R.setText(label_right)
    # setup some python lists for storing info about the ready_done_mouse
    ready_done_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    ready_done.keys = []
    ready_done.rt = []
    _ready_done_allKeys = []
    # keep track of which components have finished
    readyComponents = [main_ready_msg, button_L, ready_label_L, button_R, ready_label_R, ready_done_mouse, ready_done]
    for thisComponent in readyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    readyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ready"-------
    while continueRoutine:
        # get current time
        t = readyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=readyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *main_ready_msg* updates
        if main_ready_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            main_ready_msg.frameNStart = frameN  # exact frame index
            main_ready_msg.tStart = t  # local t and not account for scr refresh
            main_ready_msg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_ready_msg, 'tStartRefresh')  # time at next scr refresh
            main_ready_msg.setAutoDraw(True)
        
        # *button_L* updates
        if button_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_L.frameNStart = frameN  # exact frame index
            button_L.tStart = t  # local t and not account for scr refresh
            button_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_L, 'tStartRefresh')  # time at next scr refresh
            button_L.setAutoDraw(True)
        
        # *ready_label_L* updates
        if ready_label_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ready_label_L.frameNStart = frameN  # exact frame index
            ready_label_L.tStart = t  # local t and not account for scr refresh
            ready_label_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ready_label_L, 'tStartRefresh')  # time at next scr refresh
            ready_label_L.setAutoDraw(True)
        
        # *button_R* updates
        if button_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_R.frameNStart = frameN  # exact frame index
            button_R.tStart = t  # local t and not account for scr refresh
            button_R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_R, 'tStartRefresh')  # time at next scr refresh
            button_R.setAutoDraw(True)
        
        # *ready_label_R* updates
        if ready_label_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ready_label_R.frameNStart = frameN  # exact frame index
            ready_label_R.tStart = t  # local t and not account for scr refresh
            ready_label_R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ready_label_R, 'tStartRefresh')  # time at next scr refresh
            ready_label_R.setAutoDraw(True)
        # *ready_done_mouse* updates
        if ready_done_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ready_done_mouse.frameNStart = frameN  # exact frame index
            ready_done_mouse.tStart = t  # local t and not account for scr refresh
            ready_done_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ready_done_mouse, 'tStartRefresh')  # time at next scr refresh
            ready_done_mouse.status = STARTED
            ready_done_mouse.mouseClock.reset()
            prevButtonState = ready_done_mouse.getPressed()  # if button is down already this ISN'T a new click
        if ready_done_mouse.status == STARTED:  # only update if started and not finished!
            buttons = ready_done_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [button_L, button_R]:
                        if obj.contains(ready_done_mouse):
                            gotValidClick = True
                            ready_done_mouse.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *ready_done* updates
        waitOnFlip = False
        if ready_done.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ready_done.frameNStart = frameN  # exact frame index
            ready_done.tStart = t  # local t and not account for scr refresh
            ready_done.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ready_done, 'tStartRefresh')  # time at next scr refresh
            ready_done.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ready_done.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ready_done.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ready_done.status == STARTED and not waitOnFlip:
            theseKeys = ready_done.getKeys(keyList=['space'], waitRelease=False)
            _ready_done_allKeys.extend(theseKeys)
            if len(_ready_done_allKeys):
                ready_done.keys = _ready_done_allKeys[-1].name  # just the last key pressed
                ready_done.rt = _ready_done_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in readyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
