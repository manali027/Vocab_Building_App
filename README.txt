------------------------------Vocab Building App(automation script)---------------------------------------------------

A)Purpose of this app:
-I am avid learner of memorizing new words and using them in my day to day life.
-But due to everyday wok,it becomes difficult to specifically read something everyday and learn new words from them.
-That's when the idea hit me,to have something  handy while using laptop .
-So ,I thought of developing an automation script for myself where I could get new words and meanings while working,
or watching movies.
-By just looking at the words and their meanings,it sometimes gets memorized.


B)Python Module used in this:

-I have used 'plyer' and basic 'datetime','time'  module for this automation.It doesnot comes built-in.we can need to download it.
-The main class used from plyer module is 'notification' class.
-Plyer module is a python library for accessing features of your hardware and platform.
-Different other classes of plyer module includes - accelerometer,audio,brightness,call,camera,notification.
-Various methods of these classes can be used using this module.



C)Working/internal implementation of this application:
-The 'plyer' module is first installed in the project using Settings/Interpreter/pip option or
 pip install plyer

-After installing the module,we need to import 'notification' class which is used for sending the notification.

-Then we need a file here
  1)data.txt -which is an config file containing the list of words with their meanings separated by a ':' .

-This app works by reading each new line which is a set of word-meaning from the data.txt and notifies in the screen

-time.sleep(60) method is used to put it sleep and then display the next line (i.e next set of word-meanning) in the screen.



C)notification() method:

-notification() method has few parameters:
 notify(title='', message='', app_name='', app_icon='', timeout=10, ticker='', toast=False)

toast (bool) – simple Android message instead of full notification

D)Issue faced while developing this mini project:

-Issue 1
  Firstly I thought of diplaying the whole file each time.But then,I had difficulty in reading all words at a time
  Then I thought of reading the line one at a time and memorizing the words in that way.



E)Exception where it would fail:

-Where the word and mean is not separetd by a ':' .

Note-For more details:
    https://plyer.readthedocs.io/en/latest/#:~:text=Plyer%20is%20a%20Python%20library,features%20of%20your%20hardware%20%2F%20platforms.

