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
