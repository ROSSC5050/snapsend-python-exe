from tkinter import *
import socket
from tkinter import filedialog
import os

root=Tk()
root.title("SnapSend")
root.geometry("1000x560+280+200")
root.configure(bg="#f0f0f0")
root.resizable(False,False)

def Send():
    window=Toplevel(root)
    window.title("Send")
    window.geometry("1000x560+280+200")
    window.configure(bg="#f0f0f0")
    window.resizable(False,False)

    def selfl():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='SELECT FILE',filetypes=(('file_type','*.txt'),('all files','*.*')))
    def sender():
        s= socket.socket()
        host=socket.gethostname()
        port=8888
        s.bind((host,port))
        s.listen(1)
        print(host)
        print("waiting for any connection...")
        conn,addr=s.accept()
        file=open(filename,'rb')
        file_data=file.read(1024)
        conn.send(file_data)
        print("file transferred!!")
    image_icon1=PhotoImage(file="C:/snapsend/img/send.png")
    window.iconphoto(False,image_icon1)
    sback=PhotoImage(file="C:/snapsend/img/Transfer files-cuate.png")
    Label(window,image=sback).place(x=500 ,y=150)
    host=socket.gethostname()
    Label(window,text=f'ID: {host}',font="sans-serif 30 bold",bg='#f0f0f0',fg="black").place(x=200,y=300)



    Button(window,text="SELECT FILE",width=20,height=1,font="sans-serif 30 bold", bg="#000",fg="deep pink" ,command=selfl).place(x=90,y=100)
    Button(window,text="SEND",width=20,height=1,font="sans-serif 30 bold", bg="deep pink",fg="#000",command=sender).place(x=90,y=200)
    window.mainloop()
def Rec():
    main=Toplevel(root)
    main.title("Recieve")
    main.geometry("1000x560+280+200")
    main.configure(bg="#f0f0f0")
    main.resizable(False,False)


    def recd():
        ID=SenderID.get()
        filename1=newname.get()

        s=socket.socket()
        port=8888
        s.connect((ID,port))
        file=open(filename1,'wb')
        file_data=s.recv(1024)
        file.write(file_data)
        file.close()
        print("FIle Transfered!!")

    image_icon1=PhotoImage(file="C:/snapsend/img/direct-download.png")
    main.iconphoto(False,image_icon1)
    hback=PhotoImage(file="C:/snapsend/img/Transfer files-pana.png")
    Label(main,image=hback).place(x=500 ,y=150)
    logo=PhotoImage(file="C:/snapsend/img/logo-raia-drogasil-icon-1024.png")
    Label(main,image=logo).place(x=10 ,y=0)
    #Label(main,text="Receive",font=('sans serif',20,'bold'),bg="#f0f0f0").place(x=100,y=0)
    Label(main,text="Sender ID :",font=('sans serif',20,'bold'),bg="#f0f0f0").place(x=100,y=200)
    SenderID =Entry(main,width=25,fg="black",border=2,bg="white",font=('sans serif',20,'bold'))
    SenderID.place(x=100,y=250)
    SenderID.focus()

    Label(main,text="Name for the receiving file :",font=('sans serif',20,'bold'),bg="#f0f0f0").place(x=100,y=300)
    newname =Entry(main,width=25,fg="black",border=2,bg="white",font=('sans serif',20,'bold'))
    newname.place(x=100,y=350)

    imageicon=PhotoImage(file="C:/snapsend/img/direct-download.png")
    rr=Button(main,text="Receive",compound=LEFT,image=imageicon,width=200,bg="black",font="sans-serif 20 bold",fg="white",command=recd)
    rr.place(x=100,y=400)



    main.mainloop()

image_icon=PhotoImage(file='C:/snapsend/img/share.png')
root.iconphoto(False,image_icon)
Label(root,text="FILE TRANSFER",font=('sans serif',30,'bold'),bg="#f0f0f0").place(x=20,y=50)
Frame(root,width=400,height=2,bg="#f0f0f0").place(x=25,y=180)

send_image=PhotoImage(file="C:/snapsend/img/send.png")
send=Button(root,image=send_image,bg="#f0f0f0",bd=0,command=Send)
send.place(x=100,y=200)

rec_image=PhotoImage(file="C:/snapsend/img/direct-download.png")
rec=Button(root,image=rec_image,bg="#f0f0f0",bd=0,command=Rec)
rec.place(x=100,y=300)

Label(root,text="SEND",font=('sans serif',30,'bold'),bg="#f0f0f0",fg="green").place(x=200,y=210)
Label(root,text="RECEIVE",font=('sans serif',30,'bold'),bg="#f0f0f0",fg="deep pink").place(x=200,y=310)

background=PhotoImage(file="C:/snapsend/img/Transfer files-amico.png")
Label(root,image=background).place(x=500,y=0)

root.mainloop()