#mycopi_GPIO.py
import RPi.GPIO as GPIO
import smbus
import time
import math
import mycopi_convert

led1Pin = 11 #GPIO17
led2Pin = 12 #GPIO18
led3Pin = 16 #GPIO23
led4Pin = 13 #GPIO27
ledPWMPin = 18 #GPIO24

S1Pin = 21 #GPIO9
S2Pin = 22 #GPIO25
D0Pin = 29 #GPIO5
D1Pin = 31 #GPIO6
D2Pin = 33 #GPIO13
D3Pin = 35 #GPIO19

RSPin = 40 #GPIO21

address = 0x48
bus=smbus.SMBus(1)
time.sleep(1)
cmd=0x40

def setup():
	global p
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(led1Pin, GPIO.OUT)
	GPIO.setup(led2Pin, GPIO.OUT)
	GPIO.setup(led3Pin, GPIO.OUT)
	GPIO.setup(led4Pin, GPIO.OUT)
	GPIO.setup(ledPWMPin, GPIO.OUT)
	
	GPIO.setup(S1Pin, GPIO.IN,pull_up_down=GPIO.PUD_UP)
	GPIO.setup(S2Pin, GPIO.IN,pull_up_down=GPIO.PUD_UP)	
	GPIO.setup(D0Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(D1Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(D2Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(D3Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	GPIO.setup(RSPin, GPIO.IN,pull_up_down=GPIO.PUD_UP)
	
	GPIO.output(led1Pin, GPIO.LOW)
	GPIO.output(led2Pin, GPIO.LOW)
	GPIO.output(led3Pin, GPIO.LOW)
	GPIO.output(led4Pin, GPIO.LOW)
	GPIO.setup(ledPWMPin, GPIO.LOW)
	
	p = GPIO.PWM(ledPWMPin, 1000)
	p.start(0)


def out(data):
	if data==('0'):
		GPIO.output(led1Pin, GPIO.LOW)
		GPIO.output(led2Pin, GPIO.LOW)
		GPIO.output(led3Pin, GPIO.LOW)
		GPIO.output(led4Pin, GPIO.LOW)
	if data==('1'):
		GPIO.output(led1Pin, GPIO.HIGH)
		GPIO.output(led2Pin, GPIO.LOW)
		GPIO.output(led3Pin, GPIO.LOW)
		GPIO.output(led4Pin, GPIO.LOW)
	if data==('2'):
		GPIO.output(led1Pin, GPIO.LOW)
		GPIO.output(led2Pin, GPIO.HIGH)
		GPIO.output(led3Pin, GPIO.LOW)
		GPIO.output(led4Pin, GPIO.LOW)
	if data==('3'):
		GPIO.output(led1Pin, GPIO.HIGH)
		GPIO.output(led2Pin, GPIO.HIGH)
		GPIO.output(led3Pin, GPIO.LOW)
		GPIO.output(led4Pin, GPIO.LOW)
	if data==('4'):
		GPIO.output(led1Pin, GPIO.LOW)
		GPIO.output(led2Pin, GPIO.LOW)
		GPIO.output(led3Pin, GPIO.HIGH)
		GPIO.output(led4Pin, GPIO.LOW)
	if data==('5'):
		GPIO.output(led1Pin, GPIO.HIGH)
		GPIO.output(led2Pin, GPIO.LOW)
		GPIO.output(led3Pin, GPIO.HIGH)
		GPIO.output(led4Pin, GPIO.LOW)
	if data==('6'):
		GPIO.output(led1Pin, GPIO.LOW)
		GPIO.output(led2Pin, GPIO.HIGH)
		GPIO.output(led3Pin, GPIO.HIGH)
		GPIO.output(led4Pin, GPIO.LOW)
	if data==('7'):
		GPIO.output(led1Pin, GPIO.HIGH)
		GPIO.output(led2Pin, GPIO.HIGH)
		GPIO.output(led3Pin, GPIO.HIGH)
		GPIO.output(led4Pin, GPIO.LOW)
	if data==('8'):
		GPIO.output(led1Pin, GPIO.LOW)
		GPIO.output(led2Pin, GPIO.LOW)
		GPIO.output(led3Pin, GPIO.LOW)
		GPIO.output(led4Pin, GPIO.HIGH)
	if data==('9'):
		GPIO.output(led1Pin, GPIO.HIGH)
		GPIO.output(led2Pin, GPIO.LOW)
		GPIO.output(led3Pin, GPIO.LOW)
		GPIO.output(led4Pin, GPIO.HIGH)
	if data==('A'):
		GPIO.output(led1Pin, GPIO.LOW)
		GPIO.output(led2Pin, GPIO.HIGH)
		GPIO.output(led3Pin, GPIO.LOW)
		GPIO.output(led4Pin, GPIO.HIGH)
	if data==('B'):
		GPIO.output(led1Pin, GPIO.HIGH)
		GPIO.output(led2Pin, GPIO.HIGH)
		GPIO.output(led3Pin, GPIO.LOW)
		GPIO.output(led4Pin, GPIO.HIGH)
	if data==('C'):
		GPIO.output(led1Pin, GPIO.LOW)
		GPIO.output(led2Pin, GPIO.LOW)
		GPIO.output(led3Pin, GPIO.HIGH)
		GPIO.output(led4Pin, GPIO.HIGH)
	if data==('D'):
		GPIO.output(led1Pin, GPIO.HIGH)
		GPIO.output(led2Pin, GPIO.LOW)
		GPIO.output(led3Pin, GPIO.HIGH)
		GPIO.output(led4Pin, GPIO.HIGH)
	if data==('E'):
		GPIO.output(led1Pin, GPIO.LOW)
		GPIO.output(led2Pin, GPIO.HIGH)
		GPIO.output(led3Pin, GPIO.HIGH)
		GPIO.output(led4Pin, GPIO.HIGH)
	if data==('F'):
		GPIO.output(led1Pin, GPIO.HIGH)
		GPIO.output(led2Pin, GPIO.HIGH)
		GPIO.output(led3Pin, GPIO.HIGH)
		GPIO.output(led4Pin, GPIO.HIGH)
	if data==('i1'):
		GPIO.output(led1Pin, GPIO.HIGH)
	if data==('i0'):
			GPIO.output(led1Pin, GPIO.LOW)
	if data==('ii1'):
		GPIO.output(led2Pin, GPIO.HIGH)
	if data==('ii0'):
		GPIO.output(led2Pin, GPIO.LOW)
	if data==('iii1'):
		GPIO.output(led3Pin, GPIO.HIGH)
	if data==('iii0'):
		GPIO.output(led3Pin, GPIO.LOW)
	if data==('iv1'):
		GPIO.output(led4Pin, GPIO.HIGH)
	if data==('iv0'):
		GPIO.output(led4Pin, GPIO.LOW)

def AD1():
	reading = bus.read_byte_data(address,cmd+0)#chn=0
	voltage = reading / 255.0 * 3.3
	print ('ADC Value : %d, Voltage : %.2f'%(reading,voltage))
	reading=255-reading#PCF8591 reads voltage across LDR; Juergen requires voltage across other resistor
	value=math.floor(reading/16)
	value=mycopi_convert.hex_from_decimal(value)
	return value
	
def AD2():
	reading = bus.read_byte_data(address,cmd+1)#chn=1: external input
	voltage = reading / 255.0 * 3.3
	print ('ADC Value : %d, Voltage : %.2f'%(reading,voltage))
#	reading=255-reading#PCF8591 reads voltage across LDR; Juergen requires voltage across other resistor
	value=math.floor(reading/16)
	value=mycopi_convert.hex_from_decimal(value)
	return value
	
def D0():#input switch 0
	if GPIO.input(D0Pin)==GPIO.LOW:
		value='0'
	else:
		value='1'
	return value

def D1():#input switch 1
	if GPIO.input(D1Pin)==GPIO.LOW:
		value='0'
	else:
		value='1'
	return value

def D2():#input switch 2
	if GPIO.input(D2Pin)==GPIO.LOW:
		value='0'
	else:
		value='1'
	return value

def D3():#input switch 3
	if GPIO.input(D3Pin)==GPIO.LOW:
		value='0'
	else:
		value='1'
	return value

def DI():#input switches 0-3
	value=mycopi_convert.bin_to_hex(D3()+D2()+D1()+D0())
	
	return value

def S1():#button 1
	if GPIO.input(S1Pin)==GPIO.LOW:
		value='0'
	else:
		value='1'
	return value

def S2():#button 2
	if GPIO.input(S2Pin)==GPIO.LOW:
		value='0'
	else:
		value='1'
	return value

def RS():#reset
	if GPIO.input(RSPin)==GPIO.LOW:
		value='0'
	else:
		value='1'
	return value

def pwm(data):
	data=mycopi_convert.hex_to_decimal(data)
	dc=data
	dc=int(dc)*6
	p.ChangeDutyCycle(dc)
	
def destroy():
	GPIO.output(led1Pin, GPIO.LOW)
	GPIO.output(led2Pin, GPIO.LOW)
	GPIO.output(led3Pin, GPIO.LOW)
	GPIO.output(led4Pin, GPIO.LOW)
	
	p.stop
	GPIO.output(ledPWMPin, GPIO.LOW)
	
	bus.close()
	
	GPIO.cleanup()
