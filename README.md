# Selenium-Termux
How To Install And Use Selenium On Termux

# How To Install
- Install Termux Version 0.118 Or Higher
- Open Termux & Setup
- Type ```termux-setup-storage && apt update && apt upgrade && pkg install python && pip install --upgrade pip && pip install pyvirtualdisplay && pip install selenium```.

#### Requirement Library
```
pkg install x11-repo -y
pkg install tur-repo -y
pkg install xorg-server-xvfb -y
```

#### Install FireFox or Chromium
- Chromium
```
pkg install chromium -y
```
- FireFox
```
pkg install firefox -y
pkg install geckodriver -y
```
# Last Step
- Done, You Can Use Selenium On Termux Now
- You Can See Example File To Know How To Use

