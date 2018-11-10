# hefby(HElper For Blind eYes)

INTRODUCTION
---------------------------------

hefby is a system that helps the visually impaired. It recognizes letters on paper then speaks recognized letters.

Before you run this system, you need to complete tasks below.

--------------------------------

Required Libraries
--------

OpenCV, numpy, pygame, paramiko, 

--------------------------------

Required Hardwares
------

Raspberry Pi

3.5mm 4pole earphone with a botton

4pole(female) - 3pole(male) : mic jack of 2 3pole jack must be divided in order to connect to GPIO

330ohm, 1.1kohm resistor

                    please see circuit.png to understand how to connect

Raspberry Pi camera module

---------------------------------

Required Process
-----------

                    sudo git clone https://github.com/dys0763/hefby.git

                    sudo git clone https://github.com/jbardin/scp.py.git

                    sudo find /home/pi/scp.py/ -exec sudo cp -r {} /home/pi/hefby/ \;
                    
Open "OCRTTS2.py" and edit config (ip, username, password)
                  
                  
Required Process(PC)
-------------

Install OpenSSH Server 

                      https://www.youtube.com/watch?v=0G1Qh-_jBTQ
                      
Download "gTTS.py" to C:\users\"username"Download gTTS.py in C:\users\"username"

Intall tesseract-OCR
