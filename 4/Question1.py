import random
import time
DELAY_TIMER = 1 #Timeout value in seconds
MAX_RETRIES = 5 #Retry limit
ack = 0

#------------- Receiver -------------
def receiver(position, bit, down=False):
	if(down==True): #If server is down then the receiver can't send acknowledgement
		return 0
	global ack
	probability = random.randint(3, 9) #Randomly selects if the receiver will send a proper acknowledgement or not. This is done to simulate loss of acknowledgement due to noisy channel
	if probability%3==0:
		ack=ack^1
	if ack==position:
		return 1
	else:
		return 0
#-------------------------------------


#------------- Sender -------------
def sender(frame):
	down_status = random.randint(1, 10) #Randomly selects if the receiver is down or not (For testing)
	if(down_status%7==0):
		down=True
	else:
		down=False
	i=0
	retry=0
	retry_flag=True
	position=0
	while (i!=len(frame)):
		bit=frame[i] #Selects a bit from the frame
		print("Sent: P={i}, b={bit}".format(i=i, bit=bit))
		count_timer=0
		flag=False
		while(count_timer<=DELAY_TIMER):
			value=receiver(position, bit, down) #The selected bit is sent to the reciever
			if(value==1): #Acknowledgement received by the receiver is checked
				flag=True
				position=position^1
				break
			else:
				count_timer+=1
			time.sleep(1)
		if flag==True:
			if(i!=len(frame)-1):
				print("Acknowledgement received. Sending next bit...\n")
			i+=1
		elif flag==False:
			if(retry==MAX_RETRIES): #Checks if retries have exceeded the MAX_RETRIES
				retry_flag=False
				break
			retry+=1
			print("Didn't receive an acknowledgement. Resending...\n")
	if(retry_flag==False):
		return 0
	else:
		return 1
#-------------------------------------

if __name__ == '__main__':
	frame = input("Enter the frame: ")
	value=sender(frame)
	if(value==1):
		print("All data have been transmitted successfully!")
	else:
		print("Server is down. Please try again after sometime")

