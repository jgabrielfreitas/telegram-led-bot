from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import RPi.GPIO as GPIO
import RPi.GPIO as GPIO

BOT_TOKEN   = "351567687:AAHgnFGUOG0Cg7sEIEM0PoEbywOLNmzkESg"
updater     = Updater(BOT_TOKEN)
pin_default = 12        
ON  = 1
OFF = 0                  
GPIO.setmode(GPIO.BOARD)

#Define pin 12 as output
GPIO.setup(pin_default, GPIO.OUT)

def start(bot, update):
	ledon()
    

def stop(bot, update):
	ledoff()

def ledon(pin_led = pin_default):
    GPIO.output(pin_led, ON)

def ledoff(pin_led = pin_default):
    GPIO.output(pin_led, OFF)
    
def message(bot, update):
	print(update.message.text)

updater.dispatcher.add_handler(CommandHandler('on', start))
updater.dispatcher.add_handler(CommandHandler('off', stop))
updater.dispatcher.add_handler(MessageHandler(Filters.text, message))

updater.start_polling()
updater.idle()



