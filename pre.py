from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime

def main():
    root = Tk()
    app = Window1(root)

class Window1:

    presivote = 0
    officervote = 0
    facultyvote = 0
    
    
    
    def __init__(self, master):
        self.master =master
        self.master.title("GSU Login System")
        # self.master.geometry('1350x750+0+0')
        # self.master.config(bg ='powder blue')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text = 'GSU Login System', font=('Silkscreen',25,'bold'))
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=40)
        #====================================================================================================
        self.LoginFrame1 = LabelFrame(self.frame, width=1350, height=600,font=('Silkscreen',20,'bold'),relief='ridge')
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2 = LabelFrame(self.frame, width=1000, height=600,font=('Silkscreen',20,'bold'),relief='ridge')
        self.LoginFrame2.grid(row=2, column=0)
        #==============================Label And Entry=======================================================
        self.lblUsername=Label(self.LoginFrame1, text = 'Username',font=('Silkscreen',20,'bold'),bd=22)
        self.lblUsername.grid(row=0,column=0)
        self.txtUsername=Entry(self.LoginFrame1,font=('Silkscreen',20,'bold'))
        self.txtUsername.grid(row=0,column=1)

        self.lblPassword=Label(self.LoginFrame1, text = 'Password',font=('Silkscreen',20,'bold'),bd=22)
        self.lblPassword.grid(row=1,column=0)
        self.txtPassword=Entry(self.LoginFrame1,font=('Silkscreen',20,'bold'),show="*")
        self.txtPassword.grid(row=1,column=1)

        #==============================Buttons===============================================================

        self.btnLogin = Button(self.LoginFrame2, text = 'Login', width = 17,font=('Silkscreen',20,'bold'),command =self._login_btn_clicked)
        self.btnLogin.grid(row=3,column=0, pady=20, padx=8)

        self.btnExit = Button(self.LoginFrame2, text = 'Exit', width = 17,font=('Silkscreen',20,'bold'),command =self.iExit)
        self.btnExit.grid(row=3,column=2, pady=20, padx=8)
        #==============================Buttons===========================================================

    def verifycred(self,username,password):
        usercred = {}
        validusername = []
        with open("Voting System\StudentVoters.txt") as i:    
            for line in i:
                line = line.rstrip("\n")
                (key, val) = line.split(',')
                usercred[str(key)] = val
        
        for key in usercred.keys():
            validusername.append(key)

        if username in validusername and password == usercred[username]:
            return 1
        else:
            return 0

    def _login_btn_clicked(self):
        username = self.txtUsername.get()
        password = self.txtPassword.get()
        print('username is %s' %username)
        verify_out = self.verifycred(username,password)
        if verify_out == 1:
            self.newWindow = Toplevel(self.master)
            self.app = Window2(self.newWindow)
            self.master.destroy()
            
        else:
            tkinter.messagebox.showerror("Login error", "Incorrect Credentials")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Login Systems", "Confirm you want to exit")
        if self.iExit > 0:
            self.master.destroy()
        else:
            command = self.new_window
            return
 
    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

class Window2(Window1):
    def __init__(self, master):
        self.master =master
        self.master.title("GSU Login System")
        self.frame = Frame(self.master)
        self.frame.pack()
        root = Tk()
        root.title("GSU Voting Options")
        Tops = Frame(root,bd=20,pady=5)
        Tops.pack(side=TOP)

        self.frame = Frame(self.master)
        self.frame.pack()
        lblTitle = Label(Tops,font=('Silkscreen',30,'bold'),text='Welcome To GSU Voting System')
        lblTitle.grid(row=0,column=0)

        buttonPresident = Button(Tops,text='President Voting Ballot', width = 20,font=('Silkscreen',20,'bold'),command=self.testing)
        buttonPresident.grid(row=1,column=0, pady=20, padx=8)
        
        buttonOfficer = Button(Tops,text='Officer Voting Ballot', width = 20,font=('Silkscreen',20,'bold'))
        buttonOfficer.grid(row=2,column=0, pady=20, padx=8)
        
        buttonFaculty = Button(Tops,text='Faculty Voting Ballot', width = 20,font=('Silkscreen',20,'bold'))
        buttonFaculty.grid(row=3,column=0, pady=20, padx=8)
        
        buttonResults = Button(Tops,text='View Results', width = 20,font=('Silkscreen',20,'bold'))
        buttonResults.grid(row=3,column=0, pady=20, padx=8)
        
    def testing(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)

class Window3:
    def __init__(self, master):
        self.master =master
        self.master.title("GSU Login System")
        self.frame = Frame(self.master)
        self.frame.pack()
        root = Tk()
        root.title("GSU Voting Options")
        Tops = Frame(root,bd=20,pady=5)
        Tops.pack(side=TOP)

        self.frame = Frame(self.master)
        self.frame.pack()
        lblTitle = Label(Tops,font=('Silkscreen',30,'bold'),text='Welcome To GSU Voting System')
        lblTitle.grid(row=0,column=0)






    # def resultwindow(self):
    #     self.newWindow = Toplevel(self.master)
    #     self.app = Result(self.newWindow)

    # def presiwindow(self):
    #     if Window1.presivote == 0:
    #         self.newWindow = Toplevel(self.master)
    #         self.app = PresidentVote(self.newWindow)
    #     else:
    #         tkinter.messagebox.showerror("Error", "You Have already voted for GSU President")

    # def gsuofficerwindow(self):
    #     if Window1.officervote == 0:
    #         self.newWindow = Toplevel(self.master)
    #         self.app = GSU_officer_vote(self.newWindow)
    #     else:
    #         tkinter.messagebox.showerror("Error", "You Have already voted for GSU Offcier")           

    # def facultyofficerwindow(self):
    #     if Window1.facultyvote == 0:
    #         self.newWindow = Toplevel(self.master)
    #         self.app = Faculty_officer_vote(self.newWindow)
    #     else:
    #         tkinter.messagebox.showerror("Error", "You Have already voted for GSU Faculty Offcier")   




if __name__== '__main__':
    root = Tk()
    application = Window1(root)
    root.mainloop()
