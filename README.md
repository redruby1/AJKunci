# AJKunci
AJKunci merupakan miniatur dari sebuah pintu yang menerapkan IoT (Internet of Things). Miniatur ini memanfaatkan bluetooth pada raspberry pi untuk mendeteksi device, dan SQL database untuk menyimpan trusted device yang bisa membuka kunci pintu

## Requirements
1. Raspberry pi
2. Servo
3. Bluetooth
4. Monitor
5. Miniatur pintu

## Configuration
1. Install Raspbian pada sd card untuk Raspberry pi
2. Install mySQL untuk database
3. Konfigurasi awal raspberry pi
    ```
    import bluetooth
    import mysql.connector
    import RPi.GPIO as GPIO
    from gpiozero import Servo
    from time import sleep

    servo = 11

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(servo,GPIO.OUT)

    p=GPIO.PWM(servo,50)# 50hz frequency
    p.start(2.5)# starting duty cycle ( it set the servo to 2.5 degree )
    ```
    Apabila fungsi import belum berfungsi, bisa menginstall packagenya terlebih dahulu
3. Buat script menggunakan python untuk mengkoneksikan raspberry pi dan database
   ```
   db = mysql.connector.connect( #connect to database for get the mac address
   host = "localhost", #host, you can use your IP or "localhost" if the database is on your comp
   user = "user", #user for you login database
   passwd = "password", 
   database = "Mac" #name of your database) 
   ```
4. Buat script menggunakan python untuk mengambil data dari database
   ```
   cursor = db.cursor()

   sql = "SELECT mac_addr FROM mac" #sintax to get table mac from Mac database
   cursor.execute(sql)

   hasil = cursor.fetchall() #send all data you get to "hasil"
   for data, in hasil:
        target_address.append(data) # send your data from hasil to list targer_adrres

   list = [str(i) for i in target_address] #delete variabel "u" from the targer_adrress and copied to "list"   
   ```
5. Buat script untuk mendeteksi device dan mencocokkan dengan data di database
   ```
   nearby_devices = bluetooth.discover_devices() # search nearby device bluetooth
    
    for bdaddr in nearby_devices: # matching the device mac address with your list mac address from database
        for i in range(length):
            if (list [i])== bdaddr:
                print(list[i])
                flag=0 #if match the flag value will be 0
                break
   ```
6. Jika device terdapat di database maka kunci akan membuka dan menutup kembali saat tidak ada device terdeteksi
   ```
   if flag < 1: # make servo cycle to open
        sleep(0.5)
        p.ChangeDutyCycle(7.5)
        print("Opened")
        sleep(0.5)
    else:
        sleep(1) # make servo comeback to fist posisition if flag >=1
        p.ChangeDutyCycle(2.5)
        print("no device... Locked")
        
   if __name__ == '__main__': # this make the program looping
    while(True):
        check_panto(1)
   ```
   
## Test the project
1. Sambungkan monitor, raspberry pi, dan miniatur pintu
2. Pasang pin raspberry pi sesuai kebutuhan
3. Pastikan raspberry pi tersambung ke internet
4. Jalankan controller.py di terminal
5. AJKunci sudah dapat mendeteksi device di sekitarnya melalui bluetooth
