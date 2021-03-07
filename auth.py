from support import *
import chat


def main():
    #Creating Login Page
    global val, w, root,top,username,name
    root = tk.Tk()
    username = tk.StringVar()
    name = tk.StringVar()

    #root.attributes('-fullscreen',True)
    top = Toplevel1 (root)
    init(root, top)
    root.mainloop()




def authentication():
    #Logining and receiving token
    global username_info,name_info,token,username,name
    username_info=username.get()
    name_info=name.get()
    print("Username:",username_info)
    print("Name:",name_info)
    try:
        response = requests.post(
        'http://127.0.0.1:5000/send',
        json={'name': name_info, 'username': username_info, 'text': '', 'status': 'login'}
        )
    except:
        messagebox.showinfo("Error!","No connection with server!")
        return


    data = response.json()
    if data['status'] == 'Ok':
        chat.main(name_info,username_info)
    else:
        messagebox.showinfo("Error!","That username was used! Input your username again!")
        return







        #messagebox.showinfo("Wrong", "You entered wrong credentials!")
    #print(r1.text)


class Toplevel1:
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
        top.title("Login")
        #Background image
        self.img = tk.PhotoImage(file="images/bg.png")
        self.my_canvas = tk.Canvas(top)
        self.my_canvas.place(relx=0.0, rely=0.0,height=size_y,width=size_x)
        self.my_canvas.create_image(0,0,image=self.img,anchor="nw")
        #Entries
        self.my_canvas.create_text(255,130,text="Username",font="-family {DejaVu Sans} -size 20")
        self.Entry1 = tk.Entry(top,textvariable=username)
        self.Entry1.place(relx=0.300, rely=0.420, height=23, relwidth=0.40)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="FixedFont")
        self.my_canvas.create_text(255,220,text="Full name",font="-family {DejaVu Sans} -size 20")
        self.Entry2 = tk.Entry(top,textvariable=name)
        self.Entry2.place(relx=0.300, rely=0.650, height=23, relwidth=0.40)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="FixedFont")
        #Login Button
        self.butn1 = tk.Button(text='Login',command=authentication)
        self.butn1.place(relx=0.440, rely=0.800,height=30,width=70)