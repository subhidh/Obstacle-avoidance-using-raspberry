
import RPi.GPIO as GPIO
import time


# Define GPIO For Driver motors
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)


# Define GPIO for ultrasonic central
GPIO_TRIGGER_CENTRAL = 16
GPIO_ECHO_CENTRAL = 18
GPIO.setup(GPIO_TRIGGER_CENTRAL, GPIO.OUT)  # Trigger > Out
GPIO.setup(GPIO_ECHO_CENTRAL, GPIO.IN)      # Echo < In


# Define GPIO for ultrasonic Right
GPIO_TRIGGER_RIGHT = 33
GPIO_ECHO_RIGHT = 35
GPIO.setup(GPIO_TRIGGER_RIGHT, GPIO.OUT)  # Trigger > Out
GPIO.setup(GPIO_ECHO_RIGHT, GPIO.IN)      # Echo < In


# Define GPIO for ultrasonic Left
GPIO_TRIGGER_LEFT = 38
GPIO_ECHO_LEFT = 40
GPIO.setup(GPIO_TRIGGER_LEFT, GPIO.OUT)  # Trigger > Out
GPIO.setup(GPIO_ECHO_LEFT, GPIO.IN)      # Echo < In




# Functions for driving
def goforward():
    GPIO.output(11, True)
    GPIO.output(37, False)
    GPIO.output(15, True)
    GPIO.output(13, False)


def turnleft():
    GPIO.output(11, True)
    GPIO.output(37, False)
    GPIO.output(13, True)
    GPIO.output(15, False)
    time.sleep(0.8)
    goforward()

def turnright():
    GPIO.output(15, True)
    GPIO.output(13, False)
    
    GPIO.output(37, True)
    GPIO.output(11, False)
    time.sleep(0.8)
    goforward()


def gobackward():
    GPIO.output(11, False)
    GPIO.output(37, True)
    GPIO.output(15, False)
    GPIO.output(13, True)


def stopmotors():
    GPIO.output(15, False)
    GPIO.output(11, False)
    GPIO.output(37, False)
    GPIO.output(13, False)


# Detect front obstacle
def frontobstacle():


    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER_CENTRAL, False)
    # Allow module to settle
    time.sleep(0.2)
    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER_CENTRAL, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_CENTRAL, False)
    start = time.time()
    while GPIO.input(GPIO_ECHO_CENTRAL) == 0:
        start = time.time()
    while GPIO.input(GPIO_ECHO_CENTRAL) == 1:
        stop = time.time()
    # Calculate pulse length
    elapsed = stop - start
    # Distance pulse travelled in that time is time
    # Multiplied by the speed of sound (cm/s)
     distance = pulse_duration * 17150
     distance = round(distance+1.15, 2) # distance of both directions so divide by 2
    print "Front Distance : %.1f" % distance
    return distance


def rightobstacle():
    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER_RIGHT, False)
    # Allow module to settle
    time.sleep(0.2)
    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER_RIGHT, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_RIGHT, False)
    start = time.time()
    while GPIO.input(GPIO_ECHO_RIGHT) == 0:
        start = time.time()
    while GPIO.input(GPIO_ECHO_RIGHT) == 1:
        stop = time.time()
    # Calculate pulse length
    elapsed = stop - start
    # Distance pulse travelled in that time is time
    # Multiplied by the speed of sound (cm/s)
     distance = pulse_duration * 17150
     distance = round(distance+1.15, 2)# Distance of both directions so divide by 2
    print "Right Distance : %.1f" % distance
    return distance

def leftobstacle():
    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER_LEFT, False)
    # Allow module to settle
    time.sleep(0.2)
    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER_LEFT, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_LEFT, False)
    start = time.time()
    while GPIO.input(GPIO_ECHO_LEFT) == 0:
        start = time.time()
    while GPIO.input(GPIO_ECHO_LEFT) == 1:
        stop = time.time()
    # Calculate pulse length
    elapsed = stop - start
    # Distance pulse travelled in that time is time
    # Multiplied by the speed of sound (cm/s)
    distance = pulse_duration * 17150

    distance = round(distance+1.15, 2)  # Distance of both directions so divide by 2
    print "Left Distance : %.1f" % distance
    return distance

# Check front obstacle and turn right if there is an obstacle

# Check left obstacle and turn right if there is an obstacle

# Avoid obstacles and drive forward
def obstacleavoiddrive():
    
    while True:
        frontobstacle()
        rightobstacle()
        leftobstacle()
        if (frontobstacle()>15):
            goforward()
        elif(frontobstacle()<15)
            stopmotors()
            gobackward()
            time.sleep(0.4)
            stopmotors()
            rightobstacle()
            leftobstacle()
        elif (rightobstacle()>leftobstacle()):
            turnright()
        else:
            turnleft()
            
                   
    cleargpios()


def cleargpios():
    print "clearing GPIO"
    GPIO.output(37, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    GPIO.output(16, False)
    GPIO.output(33, False)
    GPIO.output(38, False)    
    print "All GPIOs CLEARED"


def main():
    # First clear GPIOs
    cleargpios()
    print "start driving: "
    # Start obstacle avoid driving
    obstacleavoiddrive()

if __name__ == "__main__":
    main()    
    cleargpios()
