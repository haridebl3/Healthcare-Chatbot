import time
import tkinter
from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
c1 = '#263238'
c2 = '#faa21f'
c3 = '#1e282d'
c6 = '#577e75'

c4 = '#faa21f'
c5 = '#577e75'

c7 = '#1e282d'
c8 = '#faa21f'
answer=''
def chat1(s='quit'):
    chatbot = ChatBot('Debl')
    trainer = ListTrainer(chatbot)
    dic={
        
        "heart attack":[
            "Dr.Sathyamurthy I","Cardiologist","Apollo Hospitals"," 21, Greams Lane Off Greams Road", "Chennai 600 006", "Ph:044-28290200/3333"
            ],

        "cancer":[
            "Dr.Bellarmine Vincent Lawrence","Oncologist","Fortis Malar Hospital" ,"52,First Main road Adyar","Chennai 600 020"
        ],

        "thyroid":[
             "Dr.Ramkumar Ramadas","Endocrinologist","Thyroid centre","Palace Villa Apartments", "No: 34/8, G-A  Ground Floor, R-Block, 4th Main Road, Anna Nagar", "Chennai, Tamil Nadu 600040"
             "Phone: 091501 16829"
        ],

        "diabetes":[
            "Dr Shanmugasundar","Endocrinologist","Dr Shanmugasundar's Clinic","Chennai","Phone:93801 99199"
        ],

        "appendicitis":[
            "Dr.G Gopalaswamy","Surgical Gastroenterologist","Prashanth super speciality Hospital","Velachery","Chennai"
        ]


    }
    f=open('c:\\users\\hari debl\\desktop\\hacko\\conversation.json','r')
    data=json.load(f)
    for i in data['conversations']:
            trainer.train(i)


    print("Enter quit to Exit")
    try:
        

        if s=='quit':
            print("Bye,Take care")
            

        out=str(chatbot.get_response(s))
        print(out)

        tokens=out.split(" ")
        for i in tokens:
            det=''
            print(i)
            if i in dic:
                print(dic[i])
                for k in dic[i]:
                    det+=k
                    det+=" "
    except:
        pass
    return out+'\n'+det
def topic_1():
    global no_topic
    no_topic = 1
    
    global top
    top = 'conversation.json'

    global a
    a = open( top , 'r')

    global doc
    doc = a.readlines()

    frame_topic.pack_forget ()
    frame_chat.pack()    

    topic = 'Healthcare'
    label_topic.config(text = topic)

    
    
def write_ans () :

    
    window.destroy()





def info () :

    global myname
    myname = entry_user.get('1.0' , 'end-1c')
                                                                        
    global chatbot                           
    chatbot = entry_chat.get('1.0' , 'end-1c')
    
    if myname == "" or chatbot == "":
        Label(frame_info , text = "Fill both fields to proceed." , bg = "red" , fg = "white" , font = 'Verdana 11 bold').place( x = 182 , y = 96)
        return 

    entry_user.delete('1.0' , END)
    entry_chat.delete('1.0' , END)

    frame_info.pack_forget ()
    frame_topic.pack ()
    
#------------------------------------------------------------------------------------------


def submit() :

    

    
    

    global chat_raw
    chat_raw = entry.get('1.0' , 'end-1c')

                        
    entry.delete('1.0' , END)
    
    chat = chat_raw.lower()
    chat = chat.replace(' ','')
    global label_request
    label_request = Label(frame_chats ,text=chat_raw , bg = c4 , fg= c7  , justify = LEFT , wraplength = 300, font = 'Verdana 10 bold')
    
    label_request.pack(anchor = 'w')  

     

    

    global label_response
 
    var=chat1(str(chat_raw))
    label_response = Label(frame_chats ,text=var ,bg= c5 , fg = c8 , justify = LEFT , wraplength = 300, font = 'Verdana 10 bold')

    label_response.pack(anchor = 'e')

    if answer ==  'Bye':
        root.destroy()




def welcome_to_info ():
    frame_welcome.pack_forget ()
    frame_info.pack ()
    
def info_to_topic ():
    frame_info.pack_forget ()
    frame_topic.pack ()

def topic_to_chat ():
    frame_topic.pack_forget ()
    frame_chat.pack()

def chat_to_topic ():
    frame_chat.pack_forget ()
    frame_topic.pack ()

def topic_to_info ():
    frame_topic.pack_forget ()
    frame_info.pack ()

def info_to_welcome ():
    frame_info.pack_forget ()
    frame_welcome.pack ()



root = Tk ()  



back = PhotoImage(file = 'arrow_behind.png')

front = PhotoImage(file = 'arrow_ahead.png')

exitt = PhotoImage(file = 'exit.png')

screen_1 = PhotoImage(file = 'image_5.png')

submit_img = PhotoImage(file = 'image_8.png')



frame_welcome = Frame (root , bg = c1 , height = '670' , width = '550')
frame_welcome.pack_propagate(0)
frame_welcome.pack()                 

  
welcome = Label (frame_welcome , text = 'Welcome' , font = "Vardana 40 bold" , bg = c1 , fg = "white")
welcome.place(x = 160 , y = 200)

welcome_chatbot = Label (frame_welcome , text = 'I am Chatbot ! ' , font = "Helvetica 15 bold italic" , bg = c1 , fg = c6)
welcome_chatbot.place(x = 200 , y = 270)

pic_1 = Label (frame_welcome , image = screen_1)
pic_1.place(x = -2 , y = 357 )

button_front = Button (frame_welcome , image = front , relief = "flat" , bg = c1 , bd = "3px solid black" , command = welcome_to_info ).place(x=470 , y=10)



def clock () :
    current = time.strftime("%H:%M:%S")
    label_time = Label (frame_welcome , bd = 5 ,  text = current , height = 1 , width = 8 , font = 'Ariel 11 bold' ,  fg = "white" , relief = 'groove' , bg = c3)
    label_time.place(x= 120 , y = 63)

    label_time.after( 1000 , clock )
   
button_time = Button (frame_welcome , text = 'Time' , height = 1 , font = 'Vardana 10 bold' ,  width = 8 , bg = c2 , fg = c1 ,  command = clock)
button_time.place(x=30 , y = 63)



def date () :
    
    try:
        date = time.strftime("%d %B , 20%y")
        label_date = Label (frame_welcome , bd = 5 , relief = 'groove' ,  text = date , bg = c3 , fg = "white"  , height = 1 , font = 'Ariel 11 bold')
        label_date.place(x= 400 , y = 63)

        label_date.after(86400000 , date)
        
    except AttributeError:
        print('')        
        
        
button_date = Button (frame_welcome , text = 'Date' ,height = 1 , font = 'Vardana 10 bold' ,  width = 8 , bg = c2 , fg= c1 , command = date)
button_date.place(x = 310 , y = 63)
  

frame_info = Frame (root , bg = c1 , height = '670' , width = '550')
frame_info.pack_propagate(0)

spacer1 = Label(frame_info , bg = c1)
spacer1.pack()

spacer2 = Label(frame_info , bg = c1)
spacer2.pack()


label_sub = Label (frame_info ,text = "Enter Information" , bg = c1 , fg = "white" , font = 'Verdana 30 italic')
label_sub.pack()
                            
user_name = Label (frame_info , text = 'Enter your name : ' , bg = c1 , fg = c2 , font = 'Ariel 15')
user_name.place(x = 80,y=130)

entry_user = Text (frame_info , bg = c6, fg = "white" , height ='1'  , width ='40' , font = 'Ariel 15')
entry_user.focus()
entry_user.place(x = 80 , y = 170)

chatbot_name = Label (frame_info , text = 'Give Chatbot a Name : ' , bg = c1 , fg = c2 , font = 'Ariel 15')
chatbot_name.place(x = 80 , y = 220)

entry_chat = Text (frame_info , bg = c6, fg = "white" , height ='1'  , width ='40' , font = 'Ariel 15')
entry_chat.place(x = 80 , y = 260)

button_1 = Button (frame_info , text ='submit' , font = 'Vardana 10 bold' , bg = c2 , fg = c1 , command = info )
button_1.place(x = 470 , y = 330)



button_back = Button (frame_info , image =  back , relief = "flat" , bg = c1 , command = info_to_welcome).place(x=10 , y = 10)

frame_topic = Frame (root , bg = c1 , height = '670' , width = '550')
frame_topic.pack_propagate(0)
                            
spacer3 = Label(frame_topic , bg = c1)
spacer3.pack()

spacer4 = Label(frame_topic , bg = c1)
spacer4.pack()

select_label = Label (frame_topic , text = "Select Topic" , bg = c1 , fg = "white" , font = 'Ariel 30 italic')
select_label.pack()

spacer5 = Label(frame_topic , bg = c1)
spacer5.pack()

option_1 = Label (frame_topic , text = ' Healthcare' , font = 'Verdana 15 italic' , bg = c1 , fg= c2)
option_1.place(x = 30 , y = 120)

button_opt_1 = Button (frame_topic , text = 'Proceed' , image = front , relief = "flat" , bg = c1 ,command = topic_1)
button_opt_1.place(x = 350 , y = 120)

button_back = Button (frame_topic , image = back , relief = "flat", bg = c1 , command = topic_to_info).place(x=10 , y = 10)


frame_chat = Frame (root , bg = c1 , height = '670' , width = '550')
frame_chat.pack_propagate(0)

frame_top = Frame( frame_chat , bg = c3 , height = '100' , width = '550')
frame_top.pack()

label_topic = Label ( frame_top , bg = c3 , fg = 'white' , font = 'Verdana 20 bold ')
label_topic.pack(pady = '30')

frame_spacer = Frame( frame_top , bg = c2 , height = "10" , width = "550" )
frame_spacer.pack()

bottom_frame = Frame (frame_chat , bg = c2 , height = '100' , width = '650')
bottom_frame.pack_propagate(0)
bottom_frame.pack(side = BOTTOM)

button = Button (bottom_frame , image = submit_img , relief = "flat", font = 'Vardana 10 bold' , bg = c3 , command = submit )
button.place(x = 280 , y = 27)


                                   
entry = Text (bottom_frame , bg = c3 , fg = c6 , height = '5'  , width ='30' , font  ='Verdana 10')
entry.bind ('<Return>' , submit)
entry.place(x = 20, y = 10)


frame_chats = Frame (frame_chat , bg = c1 , height = '450' , width = '550' )
frame_chats.pack_propagate (0)
frame_chats.pack()

label_space = Label(frame_chats , bg = c1).pack()

button_back = Button (frame_chat , image = back , relief = "flat" , bg = c3 , command = chat_to_topic).place(x=10 , y = 10)
button_front = Button (frame_chat , image = exitt , relief = "flat" , bg = c3 , command = root.destroy ).place(x=440 , y = 10)


root.mainloop ()
