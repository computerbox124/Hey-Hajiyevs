from support import *

def clear_entry(event, entry):
    entry.delete(0, tk.END)




def main(name,username):
    destroy_window()
    #Creating Login Page
    global val, w, root,top,name_info,username_info,text
    username_info=username
    name_info=name
    root = tk.Tk()
    text = tk.StringVar()
    #root.attributes('-fullscreen',True)
    top = Toplevel1 (root)
    init(root, top)
    root.mainloop()

def logout():
    destroy_window()



def send_message(text_s,name, username,entry):
    if text_s == '/logout':
        pass
    else:
        text_s = text.get()
    print(text_s)
    entry.delete(0, tk.END)
    entry.insert(0, "Enter your text")
    if text_s == "/logout":
        response = requests.post(
            'http://127.0.0.1:5000/send',
            json={'name': name, 'username': username, 'text': text_s, 'status': 'logout'}
        )
        logout()

    response = requests.post(
        'http://127.0.0.1:5000/send',
        json={'name': name, 'username': username, 'text': text_s, 'status': 'chat'}
    )

def format(message):
    dt = datetime.fromtimestamp(message['time'])
    dt_str = dt.strftime('%d %b %H:%M:%S')
    one = dt_str + ' ' + message['name'] + '@' + message['username']
    return one


def conv_text(message):
    return message['text']

def receiver(after,entry):
    while True:

        messages = []
        try:
            response = requests.get(
            'http://127.0.0.1:5000/messages',
            params={'after': after}
            )
            messages = response.json()['messages']
        except:
            messagebox.showinfo("Error!")


        for message in messages:

            #print_message(message)
            entry.insert(tk.END,format(message))
            entry.insert(tk.END, '\n')
            entry.insert(tk.END,conv_text(message))
            entry.insert(tk.END,'\n')
            entry.insert(tk.END, '\n')
            after = message['time']
        time.sleep(1)

class Toplevel1:


        # make the callback only work once
    def __init__(self, top=None):
         #This class contains information about our Window
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        top.geometry("{}x{}".format(size_x, size_y))
        top.minsize(1, 1)
        top.maxsize(size_x,size_y)
        top.resizable(1,  1)
        top.title("Hey Hajiyevs!")
        self.sec = 0.0
        #Background image
        self.img = tk.PhotoImage(file="images/bg.png")
        self.my_canvas = tk.Canvas(top)
        self.my_canvas.place(relx=0.0, rely=0.0,height=size_y,width=size_x)
        self.my_canvas.create_image(0,0,image=self.img,anchor="nw")
        #Entries
        self.chat = tk.Text(top)
        self.chat.configure(background="white")
        self.chat.place(relx=0.050, rely=0.220, height=200, relwidth=0.9)
        self.t1 = threading.Thread(target=receiver, args=(self.sec,self.chat))
        self.t1.start()
        #self.chat.after(1000, receiver(self.sec,self.chat))
        self.message = tk.Entry(top, textvariable=text)
        self.message.place(relx=0.020, rely=0.860, height=23, relwidth=0.78)
        self.message.configure(background="white")
        self.message.configure(font="FixedFont")
        self.message.insert(0, "Enter your text")
        self.message.bind("<Button-1>", lambda event: clear_entry(event, self.message))
        #Login Button
        self.butn1 = tk.Button(text='Send',command=partial(send_message,'',name_info,username_info,self.message))
        self.butn1.place(relx=0.820, rely=0.850,height=30,width=70)
        self.butn2 = tk.Button(text='Logout', command=partial(send_message,'/logout',name_info,username_info,self.message))
        self.butn2.place(relx=0.820, rely=0.100, height=30, width=70)