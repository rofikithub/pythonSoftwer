import tkinter as tk
import webbrowser


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")

        self.root.sms = tk.StringVar()
        self.root.sms.set('Your mobile or password is incorrect !')
        self.root.title('System login')
        self.root.protocol('WM_DELETE_WINDOW', self.root.quit)
        self.root.configure(bg="#87A922")
        # sw = self.winfo_screenwidth()
        # sh = self.winfo_screenheight()-70
        # self.geometry(f'{sw}x{sh}+{-10}+{0}')
        self.root.geometry(f'400x360+500+100')
        self.root.resizable(False, False)
        self.root.iconbitmap(r'win.ico')

        def goLink(event):
                webbrowser.open_new('https://rofikit.com/')
        
        self.canvas = tk.Frame(self.root, bg='#87A922')
        self.canvas.pack(fill='both', anchor='center', padx=20, pady=30)
        
        frame = tk.Frame(self.canvas, bg='#87A922')
        frame.pack(side='top')
        
        title_frame = tk.Frame(frame, bg='#87A922')
        title_frame.pack(side='top')
        title_label = tk.Label(title_frame, text="System Login", bg='#87A922', fg='white', font=('Stencil', 18))
        title_label.pack(fill='both', pady=20)
        
        mobile_frame = tk.Frame(frame, bg='#87A922')
        mobile_frame.pack(side='top', pady=10)
        mobile_label = tk.Label(mobile_frame, text='Mobile No', bg='#87A922', fg='white', width=12, font=('Bahnschrift SemiBold Condensed',13))
        mobile_label.pack(side='left', anchor='w')
        mobile_entry = tk.Entry(mobile_frame, textvariable=None, width=25)
        mobile_entry.pack(side='left',ipady=2)
        
        password_frame = tk.Frame(frame, bg='#87A922')
        password_frame.pack(side='top', pady=10)
        password_label = tk.Label(password_frame, text='Password', bg='#87A922', fg='white', width=12, font=('Bahnschrift SemiBold Condensed',13))
        password_label.pack(side='left', anchor='w')
        password_entry = tk.Entry(password_frame, textvariable=None, show="*", width=25)
        password_entry.pack(side='left',ipady=2)
        
        button_frame = tk.Frame(frame, bg='#87A922')
        button_frame.pack(side='top', fill='both', anchor='center', pady=40)
        login_button = tk.Button(button_frame, text='Login', command=lambda:self.loginAction(), bg='green', fg='white', width=10, cursor="hand2", font=('Stencil', 10)) # type: ignore
        login_button.pack(anchor='center')
        
        link_frame = tk.Frame(frame, bg='#87A922')
        link_frame.pack(side='top', fill='both', anchor='s')
        link_label = tk.Label(link_frame, text='Create a new system account', bg='#87A922', fg='white', cursor="hand2")
        link_label.pack(side='bottom',anchor='s')
        link_label.bind("<Button-1>", goLink)


    def loginAction(self):
        self.root.destroy()
        new_root = tk.Tk()
        Main(new_root)


class Main:
    def __init__(self, root):
        self.root = root
        self.root.title('Main window')
        self.root.protocol('WM_DELETE_WINDOW', root.quit)
        self.root.configure(bg="#87A922")
        # sw = self.root.winfo_screenwidth()
        # sh = self.root.winfo_screenheight()-70
        # self.root.geometry(f'{sw}x{sh}+{-10}+{0}')
        self.root.geometry(f'400x350+500+100')

        fram = tk.Frame(self.root, bg="#87A922")
        fram.pack(fill=tk.BOTH,side=tk.TOP)

        button = tk.Button(fram, text="Send mail", bg="#ddd", fg="black", font=("Arial", 9))
        button.pack(side=tk.TOP,padx=30, pady=30, anchor='center')


if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
