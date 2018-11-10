from ImgPC import *
from OCRTTS2 import *
from DetectPaperPi import *
import RPi.GPIO as GPIO
import time
import os
import pygame

pygame.mixer.init()

def main_process(LANG='kor'):
    #the main function that consist of all the functions
    #takes a photo and speaks recognized letters
    pygame.mixer.init()
    src_points, resolution, x = find_paper()
    if x:
        pygame.mixer.music.load('/home/pi/capstonefinal/finded.mp3')
        pygame.mixer.music.play()
        img = capture_paper(src_points, resolution)
        #os.system("xdg-open HRimage.jpg")
        #os.system("xdg-open paper_roi.jpg")
        try:
            print('Image Processing Started.')
            img_final = main_filter(img)
            cv2.imwrite('processed_img.jpg', img_final)
            #os.system("xdg-open processed_img.jpg")
            cv2.destroyAllWindows()
            try:
                ocr_tts('processed_img.jpg')
                pygame.mixer.music.load('/home/pi/capstonefinal/speech.mp3')
                pygame.mixer.music.play()
            except:
                print('Letter Recognizing Failed')
                pygame.mixer.music.load('/home/pi/capstonefinal/failtts.mp3')
                pygame.mixer.music.play()
        except:
            print('Image Processing Failed')
            pygame.mixer.music.load('/home/pi/capstonefinal/failtts.mp3')
            pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('/home/pi/capstonefinal/failpaper.mp3')
        pygame.mixer.music.play()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pygame.mixer.music.load('/home/pi/capstonefinal/ready.mp3') #notice has been prepared
pygame.mixer.music.play()

while True:
    button_input = GPIO.input(40)
    start_time = 0
    if not button_input:
        print('Button Pushed')
        
        pygame.mixer.music.load('/home/pi/capstonefinal/paper.mp3') #notice has been started
        pygame.mixer.music.play()
        
        start_time = time.time()
        lang = 'kor'
        while not button_input:
            if time.time() - start_time > 1: #if the botton is pushed for 1 sec, the selected language will be English
                lang = 'eng'
                break
            button_input = GPIO.input(40)
        print('Selected Language : {}'.format(lang))
        main_process(LANG=lang)
        print('Waiting for Response...')
        
GPIO.cleanup()