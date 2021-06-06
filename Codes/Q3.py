#19BDS0042 SAMARTH GUPTA

from random import randint
class sel_repeat_ARQ(object):
    def __init__(self,n,frame_send_instance=None,li=None,transmit=None,rcvd=None,rcvd_ack=None,
rc=None,sw=None):
        self.n=n
        self.frame_send_instance=frame_send_instance
        self.li=li
        self.rc=rc
        self.transmit=transmit
        self.sw=sw
        self.rcvd=rcvd
        self.rcvd_ack=rcvd_ack        
    def receiver(self,msg):
        for i in range(0,self.frame_send_instance):
            if (self.rcvd_ack[i] == 'n'):
                f = randint(0,32767) % 10
                if (f != 5):
                    for j in range(0,self.frame_send_instance):
                        if (self.rcvd[j] == self.transmit[i]):
                            print("receiver:Frame "+str(self.rcvd[j])+" received correctly\n")
                            self.rcvd[j] = self.li[self.rc]
                            self.rc = (self.rc + 1) % msg
                            break
                        if (j == self.frame_send_instance):
                            print("receiver:Duplicate frame"+str(self.transmit[i])+"discarded\n")
                        a1 = randint(0,32767) % 5
                        if (a1 == 3):
                            print("(acknowledgement "+str(self.transmit[i])+" lost)\n")
                            print("(sender timeouts-->Resend the frame)\n")
                            self.rcvd_ack[i] = ' n '
                        else:
                            print("(acknowledgement "+str(self.transmit[i])+" received)\n")
                            self.rcvd_ack[i] = ' p '
            else:
                ld = randint(0,32767) % 2
                if (ld == 0):
                    print("RECEIVER : Frame "+str(self.transmit[i])+" is damaged\n")
                    print("RECEIVER : Negative Acknowledgement "+str(self.transmit[i])+" sent\n")
                else:
                    print(" RECIEVER : Frame" + str(self.transmit[i])+"is lost \n")
                    print("(SENDER TIMEOUTS-->RESEND THE FRAME)\n")
                self.rcvd_ack[i] = ' n '
        for j in range(0,self.frame_send_instance):
            if (self.rcvd_ack[j] == ' n '):
                break
        i = 0
        for k in range(j,self.frame_send_instance):
            self.transmit[i] = self.transmit[k]
            if (self.rcvd_ack[k] == ' n '):
                self.rcvd_ack[i] = ' n '
            else:
                self.rcvd_ack[i] = ' p '
            i=i+1
        if (i != self.frame_send_instance):
            for k in range(i,self.frame_send_instance):
                self.transmit[k] = self.li[self.sw]
                sw = (self.sw + 1) % msg
                self.rcvd_ack[k] = ' n '
        ch=input("Want to continue:- ")
        if (ch == 'y'):
            self.sender(msg)
        else:
            exit(0)
    def sender(self,msg):
        for i in range(0,self.frame_send_instance):
            if self.rcvd_ack[i] == 'n':
                print("SENDER : Frame "+str(self.transmit[i])+" is sent\n")
        self.receiver(msg)
    def para(self,n):
        self.li=[None]*TOT_FRAMES
        self.transmit=[None]*FRAMES_SEND
        self.rcvd=[None]*FRAMES_SEND
        self.rcvd_ack=[None]*FRAMES_SEND
        #print(FRAMES_SEND)
        msg = pow(2, n)
        t = 0
        self.frame_send_instance = int((msg / 2))
        #print(self.frame_send_instance)
        for i in range(0,TOT_FRAMES-1):
            self.li[i] = t
            t = (t + 1) % msg
        #print(self.li)
        for i in range(0,self.frame_send_instance):
            #print(self.frame_send_instance)
            self.transmit[i] = self.li[i]
            self.rcvd[i] = self.li[i]
            self.rcvd_ack[i] = 'n'
        self.rc = self.sw = self.frame_send_instance
        self.sender(n)
    
TOT_FRAMES=500
FRAMES_SEND=10
n=int(input("Enter the size of the Window : "))
obj=sel_repeat_ARQ(n)
obj.para(n)