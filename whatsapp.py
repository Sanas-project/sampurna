import pyautogui as pg
import time 

# Giving Delay to run Program 
print("program will run after 5 seconds")
time.sleep(5)
print("running")

# Note : After running the program immediately open whatsapp web then open the persons chat you want to send messages

# For loop 
for i in range(150):
    #writing the messeges
    pg.write("I Love You")
    time.sleep(0.5)
    #sending the messages by pressing enter
    pg.press("Enter")