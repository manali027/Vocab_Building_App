from plyer import notification
import datetime
import time
counter=1
def getNewWord(counter):
    with open("data.txt",mode='r') as file:
             current_line=1
             for line in file:
                 if current_line==counter:
                     #print(line)
                     word=line.split(':')[0]
                     meaning=line.split(':')[1]
                     return word, meaning
                     break

                 current_line+=1

             time.sleep(60)

def notify_new_words():



     while(True):
         global counter
         new_word, meaning= getNewWord(counter)
         notification.notify(
             title="Learn this Word" ,
             message=f"Your word is {new_word}  and its meaning is {meaning}" ,
             app_icon="C:\\Users\\lenovo\\Downloads\\picture.ico",
             timeout=40)
         counter+=1
         time.sleep(60)

notify_new_words()