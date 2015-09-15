import os, sys, pipes
import atexit
import time




def exit_fn():
	proc.terminate()
	pipein.close()
def read():
	nums = self.pipein.read(24)
	x1,y1,z1,x2,y2,z2 = struct.unpack('ffffff',nums)
	print "x1: {}, y1: {}, z1:{}\n x2:{},y2:{},z2:{}".format(x1,y1,z1,x2,y2,z2)
	return x1,y1,z1,x2,y2,z2


cmd = "./../build/getcoords"
proc = subprocess.Popen(cmd, shell=True,preexec_fn=os.setsid)

time.sleep(3)
pipein = open("/tmp/autoarm",'r')
while(1):
	read();