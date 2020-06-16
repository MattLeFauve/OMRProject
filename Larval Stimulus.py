from psychopy import visual, core, event, sys #import some libraries from PsychoPy
      
#create a window
mywin = visual.Window([800,600],monitor="testMonitor", units="deg", fullscr = True)

#create some stimuli
TIME = 60
SPEED = 1.04
grating = visual.RadialStim(win=mywin, mask='circle', tex= 'saw',size=20, rgb=[1,1,1],pos=[0,0],angularCycles = 16, angularRes = 3600, contrast = .90 )
fixation = visual.GratingStim(win=mywin, size=999, pos=[0,0], sf=0, rgb=[.5,.5,.5])
timer = core.CountdownTimer(TIME)
#draw the stimuli and update the window
while True: #this creates a never-ending loop
    while timer.getTime()>0:
        grating.setAngularPhase(SPEED, '-')#advance phase by 0.05 of a cycle  This constant cycle/sec
        #grating.ori = g rating.ori-  .4   #This is rotations per sec`
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

