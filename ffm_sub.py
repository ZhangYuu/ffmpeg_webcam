import subprocess
import multiprocessing
import time
def ffmpeg1():
	pipline = 'ffmpeg -re -f v4l2 -i /dev/video0 -vcodec h264 -preset:v ultrafast -tune:v zerolatency -f tee -map 0:v "[f=h264]udp://192.168.1.209:6970?pkt_size=1000|[f=h264]udp://192.168.1.99:6970?pkt_size=1000"'
	p = subprocess.Popen(pipline,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out = p.communicate()[0]

def ffmpeg2():
        pipline = 'ffmpeg -re -f v4l2 -i /dev/video0 -vcodec h264 -preset:v ultrafast -tune:v zerolatency -f tee -map 0:v "[f=h264]udp://192.168.1.209:6970?pkt_size=1000|[f=h264]udp://192.168.1.241:6970?pkt_size=1000"'
        p = subprocess.Popen(pipline,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out = p.communicate()[0]


proc = multiprocessing.Process(target=ffmpeg1)
prob = multiprocessing.Process(target=ffmpeg2)

proc.start()
#prob.start()
time.sleep(10)
proc.terminate()

time.sleep(0.3)

prob.start()
time.sleep(20)
#prob.terminate()

#proc.kill()
'''
proc = subprocess.Popen(['ffmpeg -re -f v4l2 -i /dev/video0 -vcodec h264 -preset:v ultrafast -tune:v zerolatency -f tee -map 0:v "[f=h264]udp://192.168.1.209:6970?pkt_size=1000|[f=h264]udp://192.168.1.241:6970?pkt_size=1000"'],shell=True)

time.sleep(12)
proc.kill()
'''
