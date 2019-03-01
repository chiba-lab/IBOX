import time,random, sys
import InstrumentControl

def timeCheck(goalTime):
	global startTime
	endTime = time.time()
	if(endTime - startTime > goalTime):
		endTime = startTime
		return True
	return False

def randomMotor(moveControl):
	global StepperControl
	global goalTime
	StepperControl.SetPosition(1,1.8, moveControl)
 
	timeControl = timeCheck(goalTime)
	while (not (timeControl)):
		timeControl = timeCheck(goalTime)

	StepperControl.setPosition(1, 1.8, 0)

	timeControl = timeCheck(goalTime)
	while (not (timeControl)):
		timeControl = timeCheck(goalTime)

if __name__ == "__main__":
	import time, random, InstrumentControl, sys
	
	arr = [-725, 725]
	COMId = 6
        StepperControl =InstrumentControl.StepperMotor('COM%d' %COMId)
	startTime = time.time()
	systemStartTime = time.time()

	defaultTime = 900
	if(len(sys.argv) > 1):
		defaultTime = int(sys.argv[1]) * 60

	while (time.time() - systemStartTime < defaultTime):
		goalTime = random.randint(5,90)
		randomMotor(arr[random.randint(0,1)])

	sys.exit(0)

