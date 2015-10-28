from time import sleep
from UUGear import *
from time import gmtime, strftime

UUGearDevice.setShowLogs(1)

device = UUGearDevice('UUGear-Arduino-####-####')

if device.isValid():
	for i in range(200):
		temperature = device.readDS18b20(4) 
		print strftime("Time: %H:%M:%S", gmtime())
		print 'T:', temperature, 'F'
		sleep(1)
	device.detach()
	device.stopDaemon()
else:
	print 'UUGear device is not correctly initialized.'