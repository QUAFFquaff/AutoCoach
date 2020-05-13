import socket
import board
import busio
import adafruit_tcs34725
import RPi.GPIO as GPIO
import time

# GPIO Setting Up
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)
GPIO.setmode(GPIO.BCM)
red = 18
green = 23
yellow = 24
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


# Define moving functions

def init():

    GPIO.output(red, GPIO.LOW)
    GPIO.output(yellow, GPIO.LOW)
    GPIO.output(green, GPIO.LOW)
def flash(num, col):
    print("blink ", col)
    GPIO.output(num, GPIO.LOW)
    time.sleep(1)
    GPIO.output(num, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(num, GPIO.LOW)
    time.sleep(1)
    GPIO.output(num, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(num, GPIO.LOW)
    time.sleep(1)

def quick_flash(num, col):
    print("quick flash ", col)
    GPIO.output(num, GPIO.LOW)
    time.sleep(0.25)
    GPIO.output(num, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(num, GPIO.LOW)
    time.sleep(0.25)
    GPIO.output(num, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(num, GPIO.LOW)
    time.sleep(0.25)
def RED():
    flash(red, 'red')
    print ("Forward")


def GREEN():
    flash(green, 'green')
    print ("Stop")


def YELLOW():
    flash(yellow, 'yellow')
    print ("Stop")


options = {"0": RED,
           "1": YELLOW,
           "2": GREEN,
           }
def collect_data():
    print('collect data')
    r, g, b, lux = 0, 0, 0, 0
    for i in range(8):
        temp = sensor.color_temperature
        lux += sensor.lux
        r += sensor.color_rgb_bytes[0]
        g += sensor.color_rgb_bytes[1]
        b += sensor.color_rgb_bytes[2]

        # print("Temperature: {0}K Lux: {1}".format(temp, lux))
        # Delay for a second and repeat.
        time.sleep(0.25)
    lux = lux/8
    print('Average Color: ({0}, {1}, {2})'.format(r/8,g/8,b/8))
    print(lux)
    return lux
def light_two():
    GPIO.output(yellow, GPIO.HIGH)
    GPIO.output(green, GPIO.HIGH)
    GPIO.output(red, GPIO.LOW)
def light_one():
    GPIO.output(yellow, GPIO.HIGH)
    GPIO.output(green, GPIO.LOW)
    GPIO.output(red, GPIO.LOW)

if __name__ == "__main__":

    # Create a Server Socket and wait for a client to connect
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', 6666))
    print ("UDPServer Waiting for client on port 6666")

    # Recive data from client and decide which function to call
    while True:
        try:
            flash(red,'red')
            dataFromClient, address = server_socket.recvfrom(256)
            print('get data from client: ',dataFromClient)
            print('get data from client ord: ',ord(dataFromClient))
            quick_flash(red,"red")
            lux = collect_data()
            data = int(ord(dataFromClient))
            print("lux:",lux)
            if lux >data:
                light_two()
            else:
                light_one()
            IPADRESS = "192.168.0.53"
            server_socket.sendto(0, (IPADRESS,6666))
        except Exception as ex:
            print(ex)