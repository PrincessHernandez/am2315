import time
from tentacle_pi.AM2315 import AM2315
am = AM2315(0x5c,"/dev/ic2-1")

for x in range(0,10):
	temperature, humidity, crc_check = am.sense()
	print "temperature: %s" % temperature
	print "humidity: %s" % humidity
	print "crc: %s" % crc_check
	time.sleep(2)

