from psychopy import visual, core, event, sys #import some libraries from PsychoPy

#create a window
mywin = visual.Window([800,600],monitor="testMonitor", units="deg", fullscr = True)

#create some stimuli
TIME = 30
SPEED = 1.033
grating = visual.RadialStim(win=mywin, mask='circle', tex= 'saw',size=20, rgb=[1,1,1],pos=[0,0],angularCycles = 12, angularRes = 3600, contrast = -1.0)
fixation = visual.GratingStim(win=mywin, size=999, pos=[0,0], sf=0, rgb=[1,1,0])
timer = core.CountdownTimer(TIME)
#draw the stimuli and update the window
while True: #this creates a never-ending loop
    while timer.getTime()>0:
        grating.setAngularPhase(SPEED, '-')#advance phase by 0.05 of a cycle
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
        grating.setAngularPhase(SPEED, '+')#advance phase by 0.05 of a cycle
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

#cleanup
mywin.close()
core.quit()