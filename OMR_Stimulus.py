#import libraries needed from PsychoPy
from psychopy import visual, core, event, sys 
#create a window
mywin = visual.Window([800,600], monitor="testMonitor", units="deg", fullscr = True)
#To run the stimulus, "save" + "run"
#Create OMR Stimuli
TIME = 10 #this is seconds of stimulus display and should be changed based on experimental needs (See Table 2) 
SPEED = 1.033 #1.033 is adult optimal, 1.04 is larvae optimal. See table for additional speeds. 
grating = visual.RadialStim(win=mywin, mask='circle', tex='saw',size=20, rgb=[1,1,1],pos=[0,0],angularCycles = 4, angularRes = 3600, contrast = -1.0) #angularCycles are the number of black/white bars presented by the stimulus. Adult optimal is 12 angular cycles, larvae optimal is 16 angular cycles (See Table 1).  
fixation = visual.GratingStim(win=mywin, size=999, pos=[0,0], sf=0, rgb=[0.5,0.5,0.5])
timer = core.CountdownTimer(TIME)
#draw the stimuli and update the window. The phase is always advanced by 0.05 of a cycle. 
while True: #this creates a never-ending loop
    while timer.getTime()>0:
        grating.setAngularPhase(SPEED, '-')
        grating.draw()
        mywin.flip()
        if len(event.getKeys())>0: sys.exit(0)
        event.clearEvents()
    timer.reset(TIME)
    while timer.getTime()>0:
        fixation.draw()
        mywin.flip()
        if len(event.getKeys())>0: sys.exit(0)
        event.clearEvents()
    timer.reset(TIME)
    while timer.getTime()>0:
        grating.setAngularPhase(SPEED, '+')
        grating.draw()
        mywin.flip()
        if len(event.getKeys())>0: sys.exit(0)
        event.clearEvents()
    timer.reset(TIME)
    while timer.getTime()>0:
        fixation.draw()
        mywin.flip()
        if len(event.getKeys())>0: sys.exit(0)
        event.clearEvents()
    timer.reset(TIME)
    if len(event.getKeys())>0: break
    event.clearEvents()
#cleanup. To exit, press any key. 
mywin.close()
core.quit()