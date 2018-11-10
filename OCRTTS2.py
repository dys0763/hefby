import paramiko
from paramiko import AutoAddPolicy
from paramiko import SSHClient
from scp import SCPClient


def ocr_tts(img_path):
    #initial settings
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(hostname='',username='',password='')
    #hostname : IP of your PC , username : username of your PC, password : paasword of your PC
    scp = SCPClient(client.get_transport())

    client.exec_command('del RC.txt && del check.txt && speech.mp3') #initialize files

    scp.put(img_path, img_path)
    client.exec_command('tesseract {} RC -l kor55+kor100'.format(img_path)) #run OCR
    print('Recognizing Letters...')

    stdin, stdout, stderr = client.exec_command('type RC.txt')
    while stdout.readlines() == []:
        stdin, stdout, stderr = client.exec_command('type RC.txt') #check if OCR is completed
    print('Letters has been recognized')
    
    client.exec_command('python gTTSpc.py')

    print('Producing a voice file...')
    stdin, stdout, stderr = client.exec_command('if exist check.txt echo DONE!')
    while stdout.readlines() == []:
        stdin, stdout, stderr = client.exec_command('if exist check.txt echo DONE!') #check if gTTS is completed
    print('The file has been produced')

    scp.get('speech.mp3')

    scp.close()
