import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
	os.system("python SendWheel.py " + 'a' )
	time.sleep(1)
	os.system("python SendWheel.py " + 's' )
	time.sleep(3)
	
	if(GPIO.input(12)==1):
		print 'Motion Detected'
		os.system("python SendWheel.py" + 'x')
		time.sleep(2)
	