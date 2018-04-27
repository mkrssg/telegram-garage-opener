import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO
import time
from picamera import PiCamera
import os


GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

GPIO.output(2, GPIO.HIGH)
GPIO.output(3, GPIO.HIGH)
    
camera = PiCamera()

def handle(msg):
    #chat_id = msg['chat']['id']
    content_type, chat_type, chat_id = telepot.glance(msg)
    print (content_type)
    
    GPIO.output(2, GPIO.HIGH)
    GPIO.output(3, GPIO.HIGH)

    #print 'Got command: %s' % command
    if content_type == 'text':
        command = msg['text']
        if command == 'Roll':
            bot.sendMessage(chat_id, random.randint(1,6))
        elif command == 'What's the time?':
            bot.sendMessage(chat_id, str(datetime.datetime.now()))
        elif command == 'What up?':
            bot.sendMessage(chat_id, 'not much...')
        elif command == 'Hi':
            bot.sendMessage(chat_id, 'Yo what up?')
        
        elif (command == 'Right door') or (command == 'right door'):
            bot.sendMessage(chat_id, 'Right door')
            GPIO.output(2, GPIO.LOW)
            time.sleep(1)
            GPIO.output(2, GPIO.HIGH)
        
        elif (command == 'stop') or (command == 'Stop'):
            bot.sendMessage(chat_id, 'stop')
            GPIO.output(2, GPIO.HIGH)
            GPIO.output(3, GPIO.HIGH)
        
        
        elif (command == 'Left door') or (command == 'left door'):
            bot.sendMessage(chat_id, 'Garage left')
            GPIO.output(3, GPIO.LOW)
            time.sleep(1)
            GPIO.output(3, GPIO.HIGH)

        
        
        #photo
        elif command == 'Pic':
            bot.sendMessage(chat_id, 'Picture coming..')
            camera.capture('/home/pi/projects/tg-bot/foto.jpg')
            bot.sendPhoto(chat_id, open('/home/pi/projects/tg-bot/foto.jpg', 'rb'))
            
               
    elif content_type == 'photo':
        bot.sendMessage(chat_id, 'nice pic')
        bot.download_file(msg['photo'][-1]['file_id'], '/home/pi/projects/tg-bot/pic.jpg')


bot = telepot.Bot('')

MessageLoop(bot, handle).run_as_thread()
print ('I am listening ...')

while 1:
    time.sleep(10)