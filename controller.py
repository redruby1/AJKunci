import bluetooth
import mysql.connector
import RPi.GPIO as GPIO
from gpiozero import Servo
from time import sleep

servo = 11

GPIO.setmode(GPIO.BOARD)

GPIO.setup(servo, GPIO.OUT)

p = GPIO.PWM(servo, 50)  # 50hz frequency
p.start(2.5)  # starting duty cycle ( it set the servo to 2.5 degree )


def check_panto(flag):  # function project

    target_address = []  # make list of mac address

    db = mysql.connector.connect(  # connect to database for get the mac address
        host="localhost",  # host, you can use your IP or "localhost" if the database is on your comp
        user="user",  # user for you login database
        passwd="password",
        database="Mac"  # name of your database
    )

    cursor = db.cursor()

    sql = "SELECT mac_addr FROM mac"  # sintax to get table mac from Mac database
    cursor.execute(sql)

    hasil = cursor.fetchall()  # send all data you get to "hasil"
    for data, in hasil:
        target_address.append(data)  # send your data from hasil to list targer_adrres

    list = [str(i) for i in target_address]  # delete variabel "u" from the targer_adrress and copied to "list"
    ##    print list

    ##    if db.is_connected():
    ##        print("tetet")
    ##
    ##    else:
    ##        print("nope")

    ##    input_addr = input("Enter address to add new device : ")
    ##    print(input_addr)

    length = len(list)  # send length of list to variabel length

    ##    target_address.append(input_addr)

    print("Search Device...")
    nearby_devices = bluetooth.discover_devices()  # search nearby device bluetooth
    ##    print "bum"

    for bdaddr in nearby_devices:  # matching the device mac address with your list mac address from database
        for i in range(length):
            if (list[i]) == bdaddr:
                print(list[i])
                flag = 0  # if match the flag value will be 0
                break

    ##    servo = Servo(servo)
    print("Rassberry Working..");
    if flag < 1:  # make servo cycle to open
        sleep(0.5)
        p.ChangeDutyCycle(7.5)
        print("Opened")
        sleep(0.5)
    else:
        sleep(1)  # make servo comeback to fist posisition if flag >=1
        p.ChangeDutyCycle(2.5)
        print("no device... Locked")


if __name__ == '__main__':  # this make the program looping
    while (True):
        check_panto(1)
