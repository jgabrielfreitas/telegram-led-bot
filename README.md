# Telegram Led Bot
bot to turn on and off a raspberry led via Telegram (just a playground to learn how to work with both technologies)

First of all, build a simple [blink](http://www.thirdeyevis.com/pi-page-2.php) project

<img src="http://johnny-five.io/img/breadboard/led-13-raspberry-pi.png" width="220"> 

**IMPORTANT -** You need generate your own bot token with [BotFather](https://telegram.me/BotFather) and edit the `ledbot.py` file

### Installation

``` terminal
# install python telegram bot library
$ pip install python-telegram-bot

# clone repo
$ git clone git@github.com:jgabrielfreitas/telegram-led-bot.git
$ cd telegram-led-bot/
$ python ledbot.py
```

#### LINCENSE
```
MIT License

Copyright (c) 2017 João Freitas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
