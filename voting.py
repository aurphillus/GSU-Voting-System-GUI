from tkinter import *
import tkinter.messagebox as tm
import datetime
import csv
import sys
from tempfile import NamedTemporaryFile
import shutil




class LoginFrame(Frame):
    
    
    president = {'candidate1':{'preference1':0,'preference2':0,'preference3':0,'preference4':0},
                'candidate2':{'preference1':0,'preference2':0,'preference3':0,'preference4':0},
                'candidate3':{'preference1':0,'preference2':0,'preference3':0,'preference4':0},
                'candidate4':{'preference1':0,'preference2':0,'preference3':0,'preference4':0}}


    gsuofficerdict = {'candidate1':{'preference1':0,'preference2':0,'preference3':0,'preference4':0},
                'candidate2':{'preference1':0,'preference2':0,'preference3':0,'preference4':0},
                'candidate3':{'preference1':0,'preference2':0,'preference3':0,'preference4':0},
                'candidate4':{'preference1':0,'preference2':0,'preference3':0,'preference4':0}}
    
    facultyofficerdict = {'candidate1':{'preference1':0,'preference2':0,'preference3':0,'preference4':0},
                'candidate2':{'preference1':0,'preference2':0,'preference3':0,'preference4':0},
                'candidate3':{'preference1':0,'preference2':0,'preference3':0,'preference4':0},
                'candidate4':{'preference1':0,'preference2':0,'preference3':0,'preference4':0}}
    
    #Mention date in the format of year, month and date
    
    date_test = datetime.date(2019,12,30)
    date_set = 'Voting Date on ' + date_test.strftime('%m/%d/%Y')
    store_username = ''
    p_maxvotes=0
    p_totalvotes=0
    o_maxvotes=0
    o_totalvotes=0
    f_maxvotes=0
    f_totalvotes=0
    t_president = []
    t_gsuofficers = []
    t_facultyofficers = []
    presikey=[]
    offcierkry=[]
    faciltykey=[]
    gsupresident = []
    gsuofficers = []
    facultyofficers = []
    presivote = 0
    officervote = 0
    facultyvote = 0
    t_admin = []
    
    
    presidentholding =['cand1_president1','cand2_president1','cand3_president','cand4_president']
    cand1_president=[]
    cand2_president=[]
    cand3_president=[]
    cand4_president=[]

    def candidateload(self):
        with open("GSUCandidates.txt") as i:    
            for line in i:
                line = line.rstrip("\n")
                (key, val) = line.split(',')
                if key.lower() == 'president':
                    self.t_president.append(val)
                elif key.lower() == 'gsu officers' or key.lower() == 'gsuofficers':
                    self.t_gsuofficers.append(val)
                elif key.lower() == 'faculty officers' or key.lower() =='facultyofficers':
                    self.t_facultyofficers.append(val)
                else:
                    print('%s is an invalid position' %key)
        
        temp_uniqpresi= set(self.t_president) - set(self.t_gsuofficers) - set(self.t_facultyofficers)
        temp_uniqgsuofficers= set(self.t_gsuofficers) - set(self.t_president) - set(self.t_facultyofficers)
        temp_uniqfacultyofficers= set(self.t_facultyofficers) - set(self.t_president) - set(self.t_gsuofficers)
        count = 0
        for t in temp_uniqpresi:
            if count < 4:
                self.gsupresident.append(t)
                count+=1
        count = 0
        for t in temp_uniqgsuofficers:
            if count < 4:
                self.gsuofficers.append(t)
                count+=1
        count=0
        for t in temp_uniqfacultyofficers:
            if count<4:
                self.facultyofficers.append(t)
                count +=1
        
        for key in self.president.keys():
            self.presikey.append(key)
            
        for key in self.gsuofficerdict.keys():
            self.offcierkry.append(key)
            
        for key in self.facultyofficerdict.keys():
            self.faciltykey.append(key)
                
        # print(self.presikey)
        # print(self.gsupresident)
        
        for i , v in zip(self.gsupresident, self.presikey):
            self.president[i] = self.president.pop(v)
            
        for i , v in zip(self.gsuofficers, self.offcierkry):
            self.gsuofficerdict[i] = self.gsuofficerdict.pop(v)
            
        for i , v in zip(self.facultyofficers, self.presikey):
            self.facultyofficerdict[i] = self.facultyofficerdict.pop(v)
        
    
    def csv_loading_president(self,name,out):
        test=[]
        f = open('votestore.csv')
        csv_f = csv.reader(f)

        for row in csv_f:
            # print(row)
            # print(row[0])
            if row[0] == name:
                # print('same')
                test = row
                self.president[name]['preference1']=int(row[1])
                self.president[name]['preference2']=int(row[2])
                self.president[name]['preference3']=int(row[3])
                self.president[name]['preference4']=int(row[4])
    
        if (len(test)==0):
            with open('votestore.csv', 'a') as outcsv:
                writer = csv.writer(outcsv)
                test=[name,0,0,0,0]
                out = test
                writer.writerow(out)
                self.president[name]['preference1']=int(0)
                self.president[name]['preference2']=int(0)
                self.president[name]['preference3']=int(0)
                self.president[name]['preference4']=int(0)
            
        with open('votestore.csv') as infile, open('output.csv', 'w') as outfile:
        
            for line in infile:
            
                if not line.strip(): continue  # skip the empty line
                outfile.write(line) 
      
        shutil.move('output.csv', 'votestore.csv') 
        
        
    def csv_loading_officer(self,name,out):
        test=[]
        f = open('votestore.csv')
        csv_f = csv.reader(f)
        
        for row in csv_f:
            # print(row)
            # print(row[0])
            if row[0] == name:
                print('same')
                test = row
                self.gsuofficerdict[name]['preference1']=int(row[1])
                self.gsuofficerdict[name]['preference2']=int(row[2])
                self.gsuofficerdict[name]['preference3']=int(row[3])
                self.gsuofficerdict[name]['preference4']=int(row[4])
    
        if (len(test)==0):
            print('Entering')
            with open('votestore.csv', 'a') as outcsv:
                writer = csv.writer(outcsv)
                test=[name,0,0,0,0]
                out = test
                writer.writerow(out)
                self.gsuofficerdict[name]['preference1']=int(0)
                self.gsuofficerdict[name]['preference2']=int(0)
                self.gsuofficerdict[name]['preference3']=int(0)
                self.gsuofficerdict[name]['preference4']=int(0)
            
        with open('votestore.csv') as infile, open('output.csv', 'w') as outfile:
                    
            for line in infile:
            
                if not line.strip(): continue  # skip the empty line
                outfile.write(line) 
      
        shutil.move('output.csv', 'votestore.csv') 

            
            
            
    def csv_loading_faculty(self,name,out):
        test=[]
        f = open('votestore.csv')
        csv_f = csv.reader(f)
        
        for row in csv_f:
            # print(row)
            # print(row[0])
            if row[0] == name:
                # print('same')
                test = row
                self.facultyofficerdict[name]['preference1']=int(row[1])
                self.facultyofficerdict[name]['preference2']=int(row[2])
                self.facultyofficerdict[name]['preference3']=int(row[3])
                self.facultyofficerdict[name]['preference4']=int(row[4])
    
        if (len(test)==0):
            with open('votestore.csv', 'a') as outcsv:
                writer = csv.writer(outcsv)
                test=[name,0,0,0,0]
                out = test
                writer.writerow(out)
                self.facultyofficerdict[name]['preference1']=int(0)
                self.facultyofficerdict[name]['preference2']=int(0)
                self.facultyofficerdict[name]['preference3']=int(0)
                self.facultyofficerdict[name]['preference4']=int(0)
            
        with open('votestore.csv') as infile, open('output.csv', 'w') as outfile:
                    
            for line in infile:
            
                if not line.strip(): continue  # skip the empty line
                outfile.write(line) 
      
        shutil.move('output.csv', 'votestore.csv') 


    def formatting(self,name,pref1,pref2,pref3,pref4):
        filename = 'votestore.csv'
        tempfile = NamedTemporaryFile(mode='w', delete=False)


        fields = ['candidate', 'preference1', 'preference2', 'preference3','preference4']

        cand1 = [pref1,pref2,pref3,pref4]

        with open(filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader:
                if row['candidate'] == name:
                    row['candidate'], row['preference1'], row['preference2'], row['preference3'], row['preference4'] = name,cand1[0],cand1[1],cand1[2],cand1[3]
                writer.writerow(row)

        shutil.move(tempfile.name, filename)

        with open('votestore.csv') as infile, open('output.csv', 'w') as outfile:
            for line in infile:
                if not line.strip(): continue  # skip the empty line
                outfile.write(line) 
      
        shutil.move('output.csv', 'votestore.csv')  
        

    def __init__(self, master):
        super().__init__(master)
        
        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked,width=10)
        self.logbtn.grid(row=2,column=0)
        self.exitbtn = Button(self, text="Exit",width=10,command=self.iexit)
        self.exitbtn.grid(row=2,column=1)

        self.pack()

    def iexit(self):
        root.destroy()
    
    def verifycred(self,username,password):
        usercred = {}
        validusername = []
        with open("files\StudentVoters.txt") as i:    
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
        self.store_username = self.entry_username.get()
        password = self.entry_password.get()

        verify_out = self.verifycred(self.store_username,password)
        self.candidateload()
        
        
        for i,v in zip(self.gsupresident,self.presidentholding):
            self.csv_loading_president(i,v)
            
        for i,v in zip(self.gsuofficers,self.presidentholding):
            self.csv_loading_officer(i,v)
            
        for i,v in zip(self.facultyofficers,self.presidentholding):
            self.csv_loading_faculty(i,v)
        # verify_out = 1
        print(self.store_username)
        
        print(self.t_admin)
        
        if self.store_username == 'admin':
            self.t_admin.append(1)
            
        print(self.t_admin)
        
        if verify_out == 1:
            
            self.newWindow = Toplevel(self.master)
            self.app = VoteOptions(self.newWindow)
            self.master.close()
        else:
            tm.showerror("Login error", "Incorrect Credentials")


class VoteOptions(LoginFrame):
    
    def __init__(self,master):
        self.master = master
        self.master.title("GSU Voting System")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg ='#7640BD')
        self.frame = Frame(self.master, bg = '#7640BD')
        self.frame.pack()
        self.spacing = Label(self.frame,text='',font=('Silkscreen',17,'bold'),width = 25,padx=30,pady=20,bg='#7640BD')
        self.spacing.grid(row=0,column=0)
        
        self.time = Label(self.frame,text=LoginFrame.date_set,font=('Silkscreen',17,'bold'),bg='#7640BD')
        self.time.grid(row=0,column=1)
       
        
        self.PresidentVote = Button(self.frame,text='President Voting Ballot',font=('Silkscreen',17,'bold'),width = 25, command = self.presiwindow,padx=30,pady=20)
        self.PresidentVote.grid(row=4,column=0)
        self.ResultPresidentVote = Button(self.frame,text='Result of GSU President',font=('Silkscreen',17,'bold'),width = 25,command=self.Presiresultwindow,padx=30,pady=20)
        self.ResultPresidentVote.grid(row=5,column=0)

        self.GSUOfficerVote = Button(self.frame,text='Officer Voting Ballot',font=('Silkscreen',17,'bold'),width = 25, command = self.gsuofficerwindow,padx=30,pady=20)
        self.GSUOfficerVote.grid(row=4,column=1)

        self.ResultGSUOfficerVote = Button(self.frame,text='Result of GSU Officers',font=('Silkscreen',17,'bold'),width = 25,command=self.Officerresultwindow,padx=30,pady=20)
        self.ResultGSUOfficerVote.grid(row=5,column=1)
        
        
        self.FacultyOfficerVote = Button(self.frame,text='Faculty Officer Voting Ballot',font=('Silkscreen',17,'bold'),width = 25, command = self.facultyofficerwindow,padx=30,pady=20)
        self.FacultyOfficerVote.grid(row=4,column=2)
        
        self.ResultFacultyOfficerVote = Button(self.frame,text='Result of Faculty Officer',font=('Silkscreen',17,'bold'),width = 25, command = self.Facultyresultwindow,padx=30,pady=20)
        self.ResultFacultyOfficerVote.grid(row=5,column=2)

        # self.results = Button(self.frame,text='Results',width = 25, command = self.resultwindow)
        # self.results.grid(row=4,column=3)
        print(LoginFrame.t_admin)
        self.spacing1 = Label(self.frame,text='                             ',font=('Silkscreen',17,'bold'),width = 25,padx=30,pady=20,bg='#7640BD')
        self.spacing1.grid(row=6,column=0)
        
        self.adminbtn = Button(self.frame, text="Admin",width=10,command=self.admin)
        self.adminbtn.grid(row=7,column=1)
        
        self.exitbtn = Button(self.frame, text="Exit",width=10,command=self.iexit)
        self.exitbtn.grid(row=8,column=1)
        



 
    def admin(self):
        print(LoginFrame.t_admin)
        if len(LoginFrame.t_admin) > 0:
            self.newWindow = Toplevel(self.master)
            self.app = AdminWindow(self.newWindow)
        # else:
            # self.adminbtn.config(state='disabled')
        
    
    
    def iexit(self):
        root.destroy()

    def Presiresultwindow(self):
        self.newWindow = Toplevel(self.master)
        self.app = PresiResult(self.newWindow)
        
    def Officerresultwindow(self):
        self.newWindow = Toplevel(self.master)
        self.app = OfficerResult(self.newWindow)
        
    def Facultyresultwindow(self):
        self.newWindow = Toplevel(self.master)
        self.app = FacultyResult(self.newWindow)

    def presiwindow(self):
        if LoginFrame.date_test == datetime.date.today():
            if LoginFrame.presivote == 0:
                self.newWindow = Toplevel(self.master)
                self.app = PresidentVote(self.newWindow)
            else:
                self.PresidentVote.config(state='disabled')
        # else:
        #     self.PresidentVote.config(state='disabled')

    def gsuofficerwindow(self):
        if LoginFrame.date_test == datetime.date.today():    
            if LoginFrame.officervote == 0:
                self.newWindow = Toplevel(self.master)
                self.app = GSU_officer_vote(self.newWindow)
            else:
                self.GSUOfficerVote.config(state='disabled')    
        # else:
        #     self.GSUOfficerVote.config(state='disabled')      

    def facultyofficerwindow(self):
        if LoginFrame.date_test == datetime.date.today():
            if LoginFrame.facultyvote == 0:
                self.newWindow = Toplevel(self.master)
                self.app = Faculty_officer_vote(self.newWindow)
            else:
                # tm.showerror("Error", "You Have already voted for GSU Faculty Offcier")
                self.FacultyOfficerVote.config(state='disabled')
        # else:
        #     self.FacultyOfficerVote.config(state='disabled')



class AdminWindow(LoginFrame):
    def __init__(self,master):
        self.master = master
        self.master.title("Admin Panel")
        self.master.geometry("780x600+250+150")
        self.master.config(bg ='#7640BD')
        self.frame = Frame(self.master,bg='#7640BD')
        self.frame.pack()
        
        self.spacing1 = Label(self.frame,text='',font=('Silkscreen',17,'bold'),width = 25,padx=30,pady=20,bg='#7640BD')
        self.spacing1.grid(row=0,column=0,columnspan=3)
        
        lblTitle = Label(self.frame,font=('Silkscreen',30,'bold'),text='Admin Panel',bg="#7640BD", fg="white")
        lblTitle.grid(row=1,column=2)
        
        self.spacing1 = Label(self.frame,text='',font=('Silkscreen',17,'bold'),width = 25,padx=30,pady=20,bg='#7640BD')
        self.spacing1.grid(row=2,column=2,columnspan=3)
        
        
        self.btnClearVotes = Button(self.frame,text='Clear Votes',font=('Silkscreen',13,'bold'),width = 25, command = self.clear,padx=30,pady=20)
        self.btnClearVotes.grid(row=3,column=2)
        
        self.btnCleartxt = Button(self.frame,text='Clear Votes.txt File',font=('Silkscreen',13,'bold'),width = 25, command = self.cleartxt,padx=30,pady=20)
        self.btnCleartxt.grid(row=4,column=2)
        
        self.spacing2 = Label(self.frame,text='',font=('Silkscreen',17,'bold'),width = 25,padx=30,pady=20,bg='#7640BD')
        self.spacing2.grid(row=5,column=2,columnspan=3)
        
        self.exitbtn = Button(self.frame, text="Exit",width=10,command=self.iexit)
        self.exitbtn.grid(row=6,column=2)


    def iexit(self):
        self.master.destroy()
        
    def cleartxt(self):
        f = open("votes.txt","w")
        f.write('')
        f.close()
        self.btnCleartxt.config(state='disabled')
            
        
    def clear(self):
        f = open("votestore.csv","w")
        f.write('candidate,preference1,preference2,preference3,preference4')
        f.close()
        f = open("votestore.csv","a")
        f.write('\n')
        f.close()      
        for i,v in zip(LoginFrame.gsupresident,LoginFrame.presidentholding):
            self.csv_loading_president(i,v)
            
        for i,v in zip(LoginFrame.gsuofficers,LoginFrame.presidentholding):
            self.csv_loading_officer(i,v)
            
        for i,v in zip(LoginFrame.facultyofficers,LoginFrame.presidentholding):
            self.csv_loading_faculty(i,v)
        
        self.btnClearVotes.config(state='disabled')

            
    




    
class PresidentVote(LoginFrame):
    
    def __init__(self,master):
        self.master = master
        self.master.title("President Voting Ballot")
        self.master.geometry("780x600+250+150")
        self.master.config(bg ='#7640BD')
        self.frame = Frame(self.master,bg='#7640BD')
        self.frame.pack()
        
        self.spacing1 = Label(self.frame,text='',font=('Silkscreen',17,'bold'),width = 25,padx=30,pady=20,bg='#7640BD')
        self.spacing1.grid(row=0,column=0,columnspan=3)
        
        lblTitle = Label(self.frame,font=('Silkscreen',30,'bold'),text='President Voting Ballot',bg="#7640BD", fg="white")
        lblTitle.grid(row=1,column=2)
        
        lblTitle = Label(self.frame,font=('Silkscreen',20,'bold'),text='Candidate Name: ',bg="#7640BD", fg="white")
        lblTitle.grid(row=2,column=2)

        lblLbl0 = Label(self.frame,bg='#7640BD',text="",font=('Silkscreen',15,'bold'))
        lblLbl0.grid(row=5,column=2)

        lblmembers = Label(self.frame,bg="#7640BD", fg="white",font=('Silkscreen',15,'italic'),text=("\n".join(LoginFrame.gsupresident)))
        lblmembers.grid(row=3,column=2)
        
        
        lblpref1 = Label(self.frame,font=('Silkscreen',15,'bold'),text='Preference 1: ',bg="#7640BD", fg="white")
        lblpref2 =  Label(self.frame,font=('Silkscreen',15,'bold'),text='Preference 2: ',bg="#7640BD", fg="white")
        lblpref3 =  Label(self.frame,font=('Silkscreen',15,'bold'),text='Preference 3: ',bg="#7640BD", fg="white")
        lblpref4 =  Label(self.frame,font=('Silkscreen',15,'bold'),text='Preference 4: ',bg="#7640BD", fg="white")
        
        self.entpref1 =  Entry(self.frame,width=80)
        self.entpref2 =  Entry(self.frame,width=80)
        self.entpref3 =  Entry(self.frame,width=80)
        self.entpref4 =  Entry(self.frame,width=80)
        
        lblpref1.grid(row=6,column=1,sticky=E)
        lblpref2.grid(row=7,column=1)
        lblpref3.grid(row=8,column=1)
        lblpref4.grid(row=9,column=1)
        self.entpref1.grid(row=6,column=2)
        self.entpref2.grid(row=7,column=2)
        self.entpref3.grid(row=8,column=2)
        self.entpref4.grid(row=9,column=2)
        
        self.spacing1 = Label(self.frame,text='',font=('Silkscreen',17,'bold'),width = 25,padx=30,pady=20,bg='#7640BD')
        self.spacing1.grid(row=10,column=0,columnspan=3)
        
        btnSubmit = Button(self.frame,text="Submit",command=self.submit)
        btnSubmit.grid(row=11,column=1,columnspan=4)
        
        self.exitbtn = Button(self.frame, text="Exit",width=10,command=self.iexit)
        self.exitbtn.grid(row=0,column=3)


    def iexit(self):
        self.master.destroy()

        
        
        
    def submit(self):
        pref1 = self.entpref1.get()
        pref2 = self.entpref2.get()
        pref3 = self.entpref3.get()
        pref4 = self.entpref4.get()
        
        LoginFrame.president[pref1]['preference1']+=1
        LoginFrame.president[pref2]['preference2']+=1
        LoginFrame.president[pref3]['preference3']+=1
        LoginFrame.president[pref4]['preference4']+=1
        LoginFrame.presivote=1

        self.formatting(LoginFrame.gsupresident[0],LoginFrame.president[self.gsupresident[0]]['preference1'],LoginFrame.president[self.gsupresident[0]]['preference2'],LoginFrame.president[self.gsupresident[0]]['preference3'],LoginFrame.president[self.gsupresident[0]]['preference4'])
        self.formatting(LoginFrame.gsupresident[1],LoginFrame.president[self.gsupresident[1]]['preference1'],LoginFrame.president[self.gsupresident[1]]['preference2'],LoginFrame.president[self.gsupresident[1]]['preference3'],LoginFrame.president[self.gsupresident[1]]['preference4'])
        self.formatting(LoginFrame.gsupresident[2],LoginFrame.president[self.gsupresident[2]]['preference1'],LoginFrame.president[self.gsupresident[2]]['preference2'],LoginFrame.president[self.gsupresident[2]]['preference3'],LoginFrame.president[self.gsupresident[2]]['preference4'])      
        self.formatting(LoginFrame.gsupresident[3],LoginFrame.president[self.gsupresident[3]]['preference1'],LoginFrame.president[self.gsupresident[3]]['preference2'],LoginFrame.president[self.gsupresident[3]]['preference3'],LoginFrame.president[self.gsupresident[3]]['preference4'])            
        f = open("votes.txt","a")
        f.write( str(LoginFrame.president))
        f.close()
        print(LoginFrame.president)
        self.master.destroy()




class GSU_officer_vote(LoginFrame):
    
    def __init__(self,master):
        self.master = master
        self.master.title("GSU Officer Voting Ballot")
        self.master.geometry("780x600+250+150")
        self.master.config(bg ='#7640BD')
        self.frame = Frame(self.master,bg='#7640BD')
        self.frame.pack()
        
        self.spacing1 = Label(self.frame,text='',font=('Silkscreen',17,'bold'),width = 25,padx=30,pady=20,bg='#7640BD')
        self.spacing1.grid(row=0,column=0,columnspan=3)
        
        lblTitle = Label(self.frame,font=('Silkscreen',30,'bold'),text='GSU Officer Voting Ballot',bg="#7640BD", fg="white")
        lblTitle.grid(row=1,column=2)
        
        lblTitle = Label(self.frame,font=('Silkscreen',20,'bold'),text='Candidate Name: ',bg="#7640BD", fg="white")
        lblTitle.grid(row=2,column=2)

        lblLbl0 = Label(self.frame,text="",font=('Silkscreen',15,'italic'),bg="#7640BD", fg="white")
        lblLbl0.grid(row=5,column=2)
       
        lblmembers = Label(self.frame,font=('Silkscreen',15,'italic'),text=("\n".join(LoginFrame.gsuofficers)),bg="#7640BD", fg="white")
        lblmembers.grid(row=3,column=2)
        
        
        lblpref1 = Label(self.frame,font=('Silkscreen',15,'bold'),text='Preference 1: ',bg="#7640BD", fg="white")
        lblpref2 =  Label(self.frame,font=('Silkscreen',15,'bold'),text='Preference 2: ',bg="#7640BD", fg="white")
        lblpref3 =  Label(self.frame,font=('Silkscreen',15,'bold'),text='Preference 3: ',bg="#7640BD", fg="white")
        lblpref4 =  Label(self.frame,font=('Silkscreen',15,'bold'),text='Preference 4: ',bg="#7640BD", fg="white")
        
        self.entpref1 =  Entry(self.frame,width=80)
        self.entpref2 =  Entry(self.frame,width=80)
        self.entpref3 =  Entry(self.frame,width=80)
        self.entpref4 =  Entry(self.frame,width=80)
        
        lblpref1.grid(row=6,column=1,sticky=E)
        lblpref2.grid(row=7,column=1)
        lblpref3.grid(row=8,column=1)
        lblpref4.grid(row=9,column=1)
        self.entpref1.grid(row=6,column=2)
        self.entpref2.grid(row=7,column=2)
        self.entpref3.grid(row=8,column=2)
        self.entpref4.grid(row=9,column=2)

        self.spacing1 = Label(self.frame,text='',font=('Silkscreen',17,'bold'),width = 25,padx=30,pady=20,bg='#7640BD')
        self.spacing1.grid(row=10,column=0,columnspan=3)
        
        btnSubmit = Button(self.frame,text="Submit",command=self.submit)
        btnSubmit.grid(row=11,column=1,columnspan=4)
        
        self.exitbtn = Button(self.frame, text="Exit",width=10,command=self.iexit)
        self.exitbtn.grid(row=0,column=3)


    def iexit(self):
        self.master.destroy()
        
        
        
    def submit(self):
        pref1 = self.entpref1.get()
        pref2 = self.entpref2.get()
        pref3 = self.entpref3.get()
        pref4 = self.entpref4.get()
        
        LoginFrame.gsuofficerdict[pref1]['preference1']+=1
        LoginFrame.gsuofficerdict[pref2]['preference2']+=1
        LoginFrame.gsuofficerdict[pref3]['preference3']+=1
        LoginFrame.gsuofficerdict[pref4]['preference4']+=1
        LoginFrame.officervote=1
        
        self.formatting(LoginFrame.gsuofficers[0],LoginFrame.gsuofficerdict[self.gsuofficers[0]]['preference1'],LoginFrame.gsuofficerdict[self.gsuofficers[0]]['preference2'],LoginFrame.gsuofficerdict[self.gsuofficers[0]]['preference3'],LoginFrame.gsuofficerdict[self.gsuofficers[0]]['preference4'])
        self.formatting(LoginFrame.gsuofficers[1],LoginFrame.gsuofficerdict[self.gsuofficers[1]]['preference1'],LoginFrame.gsuofficerdict[self.gsuofficers[1]]['preference2'],LoginFrame.gsuofficerdict[self.gsuofficers[1]]['preference3'],LoginFrame.gsuofficerdict[self.gsuofficers[1]]['preference4'])
        self.formatting(LoginFrame.gsuofficers[2],LoginFrame.gsuofficerdict[self.gsuofficers[2]]['preference1'],LoginFrame.gsuofficerdict[self.gsuofficers[2]]['preference2'],LoginFrame.gsuofficerdict[self.gsuofficers[2]]['preference3'],LoginFrame.gsuofficerdict[self.gsuofficers[2]]['preference4'])      
        self.formatting(LoginFrame.gsuofficers[3],LoginFrame.gsuofficerdict[self.gsuofficers[3]]['preference1'],LoginFrame.gsuofficerdict[self.gsuofficers[3]]['preference2'],LoginFrame.gsuofficerdict[self.gsuofficers[3]]['preference3'],LoginFrame.gsuofficerdict[self.gsuofficers[3]]['preference4'])            
        
        
        f = open("votes.txt","a")
        f.write( str(LoginFrame.gsuofficerdict))
        f.close()
        print(LoginFrame.gsuofficerdict)
        self.master.destroy()

class Faculty_officer_vote(LoginFrame):
    
    def __init__(self,master):
        self.master = master
        self.master.title("Faculty Officer Voting Ballot")
        self.master.geometry("780x600+250+150")
        self.master.config(bg ='#7640BD')
        self.frame = Frame(self.master,bg='#7640BD')
        self.frame.pack()
        
        self.spacing1 = Label(self.frame,text='',font=('Silkscreen',17,'bold'),width = 25,padx=30,pady=20,bg='#7640BD')
        self.spacing1.grid(row=0,column=0,columnspan=3)
        
        lblTitle = Label(self.frame,font=('Silkscreen',30,'bold'),text='Faculty Officer Voting Ballot',bg="#7640BD", fg="white")
        lblTitle.grid(row=1,column=2)
        
        lblTitle = Label(self.frame,font=('Silkscreen',20,'bold'),text='Candidate Name: ',bg="#7640BD", fg="white")
        lblTitle.grid(row=2,column=2)
        
        lblmembers = Label(self.frame,font=('Silkscreen',15,'italic'),text=("\n".join(LoginFrame.facultyofficers)),bg="#7640BD", fg="white")
        lblmembers.grid(row=3,column=2)
        
        
        lblpref1 = Label(self.frame,font=('Silkscreen',15,'bold'),text='Preference 1: ',bg="#7640BD", fg="white")
        lblpref2 =  Label(self.frame,font=('Silkscreen',15,'bold'),text='Preference 2: ',bg="#7640BD", fg="white")
        lblpref3 =  Label(self.frame,font=('Silkscreen',15,'bold'),text='Preference 3: ',bg="#7640BD", fg="white")
        lblpref4 =  Label(self.frame,font=('Silkscreen',15,'bold'),text='Preference 4: ',bg="#7640BD", fg="white")
        
        self.entpref1 =  Entry(self.frame,width=80)
        self.entpref2 =  Entry(self.frame,width=80)
        self.entpref3 =  Entry(self.frame,width=80)
        self.entpref4 =  Entry(self.frame,width=80)
        
        lblpref1.grid(row=6,column=1,sticky=E)
        lblpref2.grid(row=7,column=1)
        lblpref3.grid(row=8,column=1)
        lblpref4.grid(row=9,column=1)
        self.entpref1.grid(row=6,column=2)
        self.entpref2.grid(row=7,column=2)
        self.entpref3.grid(row=8,column=2)
        self.entpref4.grid(row=9,column=2)
        
        self.spacing1 = Label(self.frame,text='',font=('Silkscreen',17,'bold'),width = 25,padx=30,pady=20,bg='#7640BD')
        self.spacing1.grid(row=10,column=0,columnspan=3)
        
        btnSubmit = Button(self.frame,text="Submit",command=self.submit)
        btnSubmit.grid(row=11,column=1,columnspan=4)
        
        self.exitbtn = Button(self.frame, text="Exit",width=10,command=self.iexit)
        self.exitbtn.grid(row=0,column=3)


    def iexit(self):
        self.master.destroy()

        
        
    def submit(self):
        pref1 = self.entpref1.get()
        pref2 = self.entpref2.get()
        pref3 = self.entpref3.get()
        pref4 = self.entpref4.get()
        
        LoginFrame.facultyofficerdict[pref1]['preference1']+=1
        LoginFrame.facultyofficerdict[pref2]['preference2']+=1
        LoginFrame.facultyofficerdict[pref3]['preference3']+=1
        LoginFrame.facultyofficerdict[pref4]['preference4']+=1
        LoginFrame.facultyvote=1
        print(LoginFrame.facultyofficerdict)
        
        self.formatting(LoginFrame.facultyofficers[0],LoginFrame.facultyofficerdict[self.facultyofficers[0]]['preference1'],LoginFrame.facultyofficerdict[self.facultyofficers[0]]['preference2'],LoginFrame.facultyofficerdict[self.facultyofficers[0]]['preference3'],LoginFrame.facultyofficerdict[self.facultyofficers[0]]['preference4'])
        self.formatting(LoginFrame.facultyofficers[1],LoginFrame.facultyofficerdict[self.facultyofficers[1]]['preference1'],LoginFrame.facultyofficerdict[self.facultyofficers[1]]['preference2'],LoginFrame.facultyofficerdict[self.facultyofficers[1]]['preference3'],LoginFrame.facultyofficerdict[self.facultyofficers[1]]['preference4'])
        self.formatting(LoginFrame.facultyofficers[2],LoginFrame.facultyofficerdict[self.facultyofficers[2]]['preference1'],LoginFrame.facultyofficerdict[self.facultyofficers[2]]['preference2'],LoginFrame.facultyofficerdict[self.facultyofficers[2]]['preference3'],LoginFrame.facultyofficerdict[self.facultyofficers[2]]['preference4'])      
        self.formatting(LoginFrame.facultyofficers[3],LoginFrame.facultyofficerdict[self.facultyofficers[3]]['preference1'],LoginFrame.facultyofficerdict[self.facultyofficers[3]]['preference2'],LoginFrame.facultyofficerdict[self.facultyofficers[3]]['preference3'],LoginFrame.facultyofficerdict[self.facultyofficers[3]]['preference4'])            


        f = open("votes.txt","a")
        f.write( str(LoginFrame.facultyofficerdict))
        f.close()
        self.master.destroy()

class PresiResult(LoginFrame):
    
    def __init__(self,master):
        self.master = master
        self.master.title("Results")
        # self.master.geometry("1750x750+250+150")
        self.master.config(bg ='black')
        self.frame = Frame(self.master,bg='black')
        # self.frame.pack()
        
        # lblTitle = Label(self.master,font=('Silkscreen',20,'bold'),text='Results')
        # lblTitle.grid(row=0,column=2,columnspan=4)
        
        lblTitle = Label(self.master,font=('Silkscreen',20,'bold'),text='GSU President Results',bg='black',fg='white')
        lblTitle.grid(row=1,column=2,columnspan=4)
        
        lbllabel0 = Label(self.master,font=('Silkscreen',15,'bold'),text='Candidate',padx=50,pady=30,bg='black',fg='red')
        lbllabel1 = Label(self.master,font=('Silkscreen',15,'bold'),text='1st Preference',padx=50,pady=30,bg='black',fg='red')
        lbllabel2 = Label(self.master,font=('Silkscreen',15,'bold'),text='2nd Preference',padx=50,pady=30,bg='black',fg='red')
        lbllabel3 = Label(self.master,font=('Silkscreen',15,'bold'),text='3rd Preference',padx=50,pady=30,bg='black',fg='red')
        lbllabel4 = Label(self.master,font=('Silkscreen',15,'bold'),text='4th Preference',padx=50,pady=30,bg='black',fg='red')
        
        lbllabel5 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsupresident[0],padx=50,pady=30,bg='black',fg='red')
        lbllabel6 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsupresident[1],padx=50,pady=30,bg='black',fg='red')
        lbllabel7 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsupresident[2],padx=50,pady=30,bg='black',fg='red')
        lbllabel8 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsupresident[3],padx=50,pady=30,bg='black',fg='red')
        
        lbllabel9 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.president[self.gsupresident[0]]['preference1'],padx=50,pady=30,bg='black',fg='white')
        lbllabel10 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.president[self.gsupresident[0]]['preference2'],padx=50,pady=30,bg='black',fg='white')
        lbllabel11 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.president[self.gsupresident[0]]['preference3'],padx=50,pady=30,bg='black',fg='white')
        lbllabel12 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.president[self.gsupresident[0]]['preference4'],padx=50,pady=30,bg='black',fg='white')

        lbllabel13 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.president[self.gsupresident[1]]['preference1'],padx=50,pady=30,bg='black',fg='white')
        lbllabel14 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.president[self.gsupresident[1]]['preference2'],padx=50,pady=30,bg='black',fg='white')
        lbllabel15 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.president[self.gsupresident[1]]['preference3'],padx=50,pady=30,bg='black',fg='white')
        lbllabel16 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.president[self.gsupresident[1]]['preference4'],padx=50,pady=30,bg='black',fg='white')

        lbllabel17 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.president[self.gsupresident[2]]['preference1'],padx=50,pady=30,bg='black',fg='white')
        lbllabel18 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.president[self.gsupresident[2]]['preference2'],padx=50,pady=30,bg='black',fg='white')
        lbllabel19 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.president[self.gsupresident[2]]['preference3'],padx=50,pady=30,bg='black',fg='white')
        lbllabel20 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.president[self.gsupresident[2]]['preference4'],padx=50,pady=30,bg='black',fg='white')
        
        lbllabel21 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.president[self.gsupresident[3]]['preference1'],padx=50,pady=30,bg='black',fg='white')
        lbllabel22 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.president[self.gsupresident[3]]['preference2'],padx=50,pady=30,bg='black',fg='white')
        lbllabel23 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.president[self.gsupresident[3]]['preference3'],padx=50,pady=30,bg='black',fg='white')
        lbllabel24 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.president[self.gsupresident[3]]['preference4'],padx=50,pady=30,bg='black',fg='white')

        
        lbllabel0.grid(row=2,column=1)
        lbllabel1.grid(row=2,column=2)
        lbllabel2.grid(row=2,column=3)
        lbllabel3.grid(row=2,column=4)
        lbllabel4.grid(row=2,column=5)
        lbllabel5.grid(row=3,column=1)
        lbllabel6.grid(row=4,column=1)
        lbllabel7.grid(row=5,column=1)
        lbllabel8.grid(row=6,column=1)
        
        lbllabel9.grid(row=3,column=2)
        lbllabel10.grid(row=3,column=3)
        lbllabel11.grid(row=3,column=4)
        lbllabel12.grid(row=3,column=5)
        
        lbllabel13.grid(row=4,column=2)
        lbllabel14.grid(row=4,column=3)
        lbllabel15.grid(row=4,column=4)
        lbllabel16.grid(row=4,column=5)
        
        lbllabel17.grid(row=5,column=2)
        lbllabel18.grid(row=5,column=3)
        lbllabel19.grid(row=5,column=4)
        lbllabel20.grid(row=5,column=5)
        
        lbllabel21.grid(row=6,column=2)
        lbllabel22.grid(row=6,column=3)
        lbllabel23.grid(row=6,column=4)
        lbllabel24.grid(row=6,column=5)
        
        test = self.winner()
        print(LoginFrame.gsupresident[test])
        
        
        lblres1 = Label(self.master,font=('Silkscreen',15,'bold'),text='Winner:',bg='black',fg='white')
        lblres1.grid(row=7,column=1,sticky=E)
        
        lblres2 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsupresident[test],bg='black',fg='white')
        lblres2.grid(row=7,column=2,columnspan=3)
        
        lblres3 = Label(self.master,font=('Silkscreen',15,'bold'),text='Votes Recieved:',bg='black',fg='white')
        lblres3.grid(row=8,column=1)
        
        lblres4 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.p_maxvotes,bg='black',fg='white')
        lblres4.grid(row=8,column=2,columnspan=3)
        
        lblres5 = Label(self.master,font=('Silkscreen',15,'bold'),text='Total Votes:',bg='black',fg='white')
        lblres5.grid(row=9,column=1)
        
        lblres6 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.p_totalvotes,bg='black',fg='white')
        lblres6.grid(row=9,column=2,columnspan=3)
        # lbllabel24 = Label(self.master,font=('Silkscreen',10,'bold'),text=LoginFrame.president[self.gsupresident[3]]['preference4'],padx=50,pady=30)
        
        lbltp = Label(self.master,text="",padx=50,bg='black',fg='white')
        lbltp.grid(row=10,column=1)
        
        btnback = Button(self.master,text='Back',padx=10,pady=10,command=self.back)
        btnback.grid(row=11,column=3,columnspan=2)
        
    def back(self):
        self.master.destroy()
        
        
        
        # lbllabel0.pack()
        # lbllabel1.pack()
        # lbllabel2.pack()
        # lbllabel3.pack()
        # lbllabel4.pack()

    def duplicates(self,lst, item):
        return [i for i, x in enumerate(lst) if x == item]
    
    def winner(self):
        self.pref1=[]
        self.pref2=[]
        self.pref3=[]
        self.pref4=[]
        
                
        for i in LoginFrame.gsupresident:
            self.pref1.append(LoginFrame.president[i]['preference1'])
    
        for i in LoginFrame.gsupresident:
            self.pref2.append(LoginFrame.president[i]['preference2'])

        for i in LoginFrame.gsupresident:
            self.pref3.append(LoginFrame.president[i]['preference3'])

        for i in LoginFrame.gsupresident:
            self.pref4.append(LoginFrame.president[i]['preference4'])
        
        for ele in range(0, len(self.pref1)): 
            LoginFrame.p_totalvotes+=self.pref1[ele]

        self.p1 = max(self.pref1)
        self.d1 = self.duplicates(self.pref1,self.p1)
        if len(self.d1) > 1:
            self.p2 = max(self.pref2)
            self.d2 = self.duplicates(self.pref2,self.p2)
            if len(self.d2) > 1:
                self.p3 = max(self.pref3)
                self.d3 = self.duplicates(self.pref3,self.p3)
                if len(self.d3) > 1:
                    self.p4 = max(self.pref4)
                    LoginFrame.maxvotes = self.p4
                    return self.pref4.index(self.p4)
                else:
                    LoginFrame.p_maxvotes = self.p3
                    return self.pref3.index(self.p3)
            else:
                LoginFrame.p_maxvotes = self.p2
                return self.pref2.index(self.p2)
        else:
            LoginFrame.p_maxvotes = self.p1
            return self.pref1.index(self.p1)
        

class OfficerResult(LoginFrame):
    
    def __init__(self,master):
        self.master = master
        self.master.title("Results")
        # self.master.geometry("1750x750+250+150")
        self.master.config(bg ='black')
        self.frame = Frame(self.master,bg='black')
        # self.frame.pack()
        
        # lblTitle = Label(self.master,font=('Silkscreen',20,'bold'),text='Results')
        # lblTitle.grid(row=0,column=2,columnspan=4)
        
        lblTitle = Label(self.master,font=('Silkscreen',20,'bold'),text='GSU Officer Voting Results',bg='black',fg='white')
        lblTitle.grid(row=1,column=2,columnspan=4)
        print(LoginFrame.gsuofficers)
        
        lbllabel0 = Label(self.master,font=('Silkscreen',15,'bold'),text='Candidate',padx=50,pady=30,bg='black',fg='red')
        lbllabel1 = Label(self.master,font=('Silkscreen',15,'bold'),text='1st Preference',padx=50,pady=30,bg='black',fg='red')
        lbllabel2 = Label(self.master,font=('Silkscreen',15,'bold'),text='2nd Preference',padx=50,pady=30,bg='black',fg='red')
        lbllabel3 = Label(self.master,font=('Silkscreen',15,'bold'),text='3rd Preference',padx=50,pady=30,bg='black',fg='red')
        lbllabel4 = Label(self.master,font=('Silkscreen',15,'bold'),text='4th Preference',padx=50,pady=30,bg='black',fg='red')
        
        lbllabel5 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficers[0],padx=50,pady=30,bg='black',fg='red')
        lbllabel6 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficers[1],padx=50,pady=30,bg='black',fg='red')
        lbllabel7 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficers[2],padx=50,pady=30,bg='black',fg='red')
        lbllabel8 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficers[3],padx=50,pady=30,bg='black',fg='red')
        
        lbllabel9 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficerdict[self.gsuofficers[0]]['preference1'],padx=50,pady=30,bg='black',fg='white')
        lbllabel10 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficerdict[self.gsuofficers[0]]['preference2'],padx=50,pady=30,bg='black',fg='white')
        lbllabel11 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficerdict[self.gsuofficers[0]]['preference3'],padx=50,pady=30,bg='black',fg='white')
        lbllabel12 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficerdict[self.gsuofficers[0]]['preference4'],padx=50,pady=30,bg='black',fg='white')

        lbllabel13 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficerdict[self.gsuofficers[1]]['preference1'],padx=50,pady=30,bg='black',fg='white')
        lbllabel14 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficerdict[self.gsuofficers[1]]['preference2'],padx=50,pady=30,bg='black',fg='white')
        lbllabel15 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficerdict[self.gsuofficers[1]]['preference3'],padx=50,pady=30,bg='black',fg='white')
        lbllabel16 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficerdict[self.gsuofficers[1]]['preference4'],padx=50,pady=30,bg='black',fg='white')

        lbllabel17 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficerdict[self.gsuofficers[2]]['preference1'],padx=50,pady=30,bg='black',fg='white')
        lbllabel18 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficerdict[self.gsuofficers[2]]['preference2'],padx=50,pady=30,bg='black',fg='white')
        lbllabel19 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficerdict[self.gsuofficers[2]]['preference3'],padx=50,pady=30,bg='black',fg='white')
        lbllabel20 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficerdict[self.gsuofficers[2]]['preference4'],padx=50,pady=30,bg='black',fg='white')
        
        lbllabel21 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficerdict[self.gsuofficers[3]]['preference1'],padx=50,pady=30,bg='black',fg='white')
        lbllabel22 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficerdict[self.gsuofficers[3]]['preference2'],padx=50,pady=30,bg='black',fg='white')
        lbllabel23 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficerdict[self.gsuofficers[3]]['preference3'],padx=50,pady=30,bg='black',fg='white')
        lbllabel24 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficerdict[self.gsuofficers[3]]['preference4'],padx=50,pady=30,bg='black',fg='white')

        
        lbllabel0.grid(row=2,column=1)
        lbllabel1.grid(row=2,column=2)
        lbllabel2.grid(row=2,column=3)
        lbllabel3.grid(row=2,column=4)
        lbllabel4.grid(row=2,column=5)
        lbllabel5.grid(row=3,column=1)
        lbllabel6.grid(row=4,column=1)
        lbllabel7.grid(row=5,column=1)
        lbllabel8.grid(row=6,column=1)
        
        lbllabel9.grid(row=3,column=2)
        lbllabel10.grid(row=3,column=3)
        lbllabel11.grid(row=3,column=4)
        lbllabel12.grid(row=3,column=5)
        
        lbllabel13.grid(row=4,column=2)
        lbllabel14.grid(row=4,column=3)
        lbllabel15.grid(row=4,column=4)
        lbllabel16.grid(row=4,column=5)
        
        lbllabel17.grid(row=5,column=2)
        lbllabel18.grid(row=5,column=3)
        lbllabel19.grid(row=5,column=4)
        lbllabel20.grid(row=5,column=5)
        
        lbllabel21.grid(row=6,column=2)
        lbllabel22.grid(row=6,column=3)
        lbllabel23.grid(row=6,column=4)
        lbllabel24.grid(row=6,column=5)
        
        test = self.winner()
        print(LoginFrame.gsuofficers[test])
        
        
        lblres1 = Label(self.master,font=('Silkscreen',15,'bold'),text='Winner:',bg='black',fg='white')
        lblres1.grid(row=7,column=1)
        
        lblres2 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.gsuofficers[test],bg='black',fg='white')
        lblres2.grid(row=7,column=2,columnspan=3)
        
        lblres3 = Label(self.master,font=('Silkscreen',15,'bold'),text='Votes Recieved:',bg='black',fg='white')
        lblres3.grid(row=8,column=1)
        
        lblres4 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.o_maxvotes,bg='black',fg='white')
        lblres4.grid(row=8,column=2,columnspan=3)
        
        lblres5 = Label(self.master,font=('Silkscreen',15,'bold'),text='Total Votes:',bg='black',fg='white')
        lblres5.grid(row=9,column=1)
        
        lblres6 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.o_totalvotes,bg='black',fg='white')
        lblres6.grid(row=9,column=2,columnspan=3)
        # lbllabel24 = Label(self.master,font=('Silkscreen',10,'bold'),text=LoginFrame.president[self.gsupresident[3]]['preference4'],padx=50,pady=30)
        lbltp = Label(self.master,text="",padx=50,bg='black',fg='white')
        lbltp.grid(row=10,column=1)
        
        btnback = Button(self.master,text='Back',padx=10,pady=10,command=self.back)
        btnback.grid(row=11,column=3,columnspan=2)
        
    def back(self):
        self.master.destroy()
        
        
        
        # lbllabel0.pack()
        # lbllabel1.pack()
        # lbllabel2.pack()
        # lbllabel3.pack()
        # lbllabel4.pack()

    def duplicates(self,lst, item):
        return [i for i, x in enumerate(lst) if x == item]
    
    def winner(self):
        self.pref1=[]
        self.pref2=[]
        self.pref3=[]
        self.pref4=[]
        
                
        for i in LoginFrame.gsuofficers:
            self.pref1.append(LoginFrame.gsuofficerdict[i]['preference1'])
    
        for i in LoginFrame.gsuofficers:
            self.pref2.append(LoginFrame.gsuofficerdict[i]['preference2'])

        for i in LoginFrame.gsuofficers:
            self.pref3.append(LoginFrame.gsuofficerdict[i]['preference3'])

        for i in LoginFrame.gsuofficers:
            self.pref4.append(LoginFrame.gsuofficerdict[i]['preference4'])
        
        for ele in range(0, len(self.pref1)): 
            LoginFrame.o_totalvotes+=self.pref1[ele]

        self.p1 = max(self.pref1)
        self.d1 = self.duplicates(self.pref1,self.p1)
        if len(self.d1) > 1:
            self.p2 = max(self.pref2)
            self.d2 = self.duplicates(self.pref2,self.p2)
            if len(self.d2) > 1:
                self.p3 = max(self.pref3)
                self.d3 = self.duplicates(self.pref3,self.p3)
                if len(self.d3) > 1:
                    self.p4 = max(self.pref4)
                    LoginFrame.o_maxvotes = self.p4
                    return self.pref4.index(self.p4)
                else:
                    LoginFrame.o_maxvotes = self.p3
                    return self.pref3.index(self.p3)
            else:
                LoginFrame.o_maxvotes = self.p2
                return self.pref2.index(self.p2)
        else:
            LoginFrame.o_maxvotes = self.p1
            return self.pref1.index(self.p1)


class FacultyResult(LoginFrame):
    
    def __init__(self,master):
        self.master = master
        self.master.title("Results")
        # self.master.geometry("1750x750+250+150")
        self.master.config(bg ='black')
        self.frame = Frame(self.master,bg='black')
        # self.frame.pack()
        
        # lblTitle = Label(self.master,font=('Silkscreen',20,'bold'),text='Results')
        # lblTitle.grid(row=0,column=2,columnspan=4)
        
        lblTitle = Label(self.master,font=('Silkscreen',20,'bold'),text='GSU Faculty Officer Results',bg='black',fg='white')
        lblTitle.grid(row=1,column=2,columnspan=4)
        print(LoginFrame.gsuofficers)
        
        lbllabel0 = Label(self.master,font=('Silkscreen',15,'bold'),text='Candidate',padx=50,pady=30,bg='black',fg='red')
        lbllabel1 = Label(self.master,font=('Silkscreen',15,'bold'),text='1st Preference',padx=50,pady=30,bg='black',fg='red')
        lbllabel2 = Label(self.master,font=('Silkscreen',15,'bold'),text='2nd Preference',padx=50,pady=30,bg='black',fg='red')
        lbllabel3 = Label(self.master,font=('Silkscreen',15,'bold'),text='3rd Preference',padx=50,pady=30,bg='black',fg='red')
        lbllabel4 = Label(self.master,font=('Silkscreen',15,'bold'),text='4th Preference',padx=50,pady=30,bg='black',fg='red')
        print(LoginFrame.facultyofficers)
        lbllabel5 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficers[0],padx=50,pady=30,bg='black',fg='red')
        lbllabel6 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficers[1],padx=50,pady=30,bg='black',fg='red')
        lbllabel7 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficers[2],padx=50,pady=30,bg='black',fg='red')
        lbllabel8 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficers[3],padx=50,pady=30,bg='black',fg='red')
        
        lbllabel9 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficerdict[self.facultyofficers[0]]['preference1'],padx=50,pady=30,bg='black',fg='white')
        lbllabel10 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficerdict[self.facultyofficers[0]]['preference2'],padx=50,pady=30,bg='black',fg='white')
        lbllabel11 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficerdict[self.facultyofficers[0]]['preference3'],padx=50,pady=30,bg='black',fg='white')
        lbllabel12 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficerdict[self.facultyofficers[0]]['preference4'],padx=50,pady=30,bg='black',fg='white')

        lbllabel13 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficerdict[self.facultyofficers[1]]['preference1'],padx=50,pady=30,bg='black',fg='white')
        lbllabel14 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficerdict[self.facultyofficers[1]]['preference2'],padx=50,pady=30,bg='black',fg='white')
        lbllabel15 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficerdict[self.facultyofficers[1]]['preference3'],padx=50,pady=30,bg='black',fg='white')
        lbllabel16 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficerdict[self.facultyofficers[1]]['preference4'],padx=50,pady=30,bg='black',fg='white')

        lbllabel17 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficerdict[self.facultyofficers[2]]['preference1'],padx=50,pady=30,bg='black',fg='white')
        lbllabel18 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficerdict[self.facultyofficers[2]]['preference2'],padx=50,pady=30,bg='black',fg='white')
        lbllabel19 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficerdict[self.facultyofficers[2]]['preference3'],padx=50,pady=30,bg='black',fg='white')
        lbllabel20 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficerdict[self.facultyofficers[2]]['preference4'],padx=50,pady=30,bg='black',fg='white')
        
        lbllabel21 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficerdict[self.facultyofficers[3]]['preference1'],padx=50,pady=30,bg='black',fg='white')
        lbllabel22 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficerdict[self.facultyofficers[3]]['preference2'],padx=50,pady=30,bg='black',fg='white')
        lbllabel23 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficerdict[self.facultyofficers[3]]['preference3'],padx=50,pady=30,bg='black',fg='white')
        lbllabel24 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficerdict[self.facultyofficers[3]]['preference4'],padx=50,pady=30,bg='black',fg='white')

        
        lbllabel0.grid(row=2,column=1)
        lbllabel1.grid(row=2,column=2)
        lbllabel2.grid(row=2,column=3)
        lbllabel3.grid(row=2,column=4)
        lbllabel4.grid(row=2,column=5)
        lbllabel5.grid(row=3,column=1)
        lbllabel6.grid(row=4,column=1)
        lbllabel7.grid(row=5,column=1)
        lbllabel8.grid(row=6,column=1)
        
        lbllabel9.grid(row=3,column=2)
        lbllabel10.grid(row=3,column=3)
        lbllabel11.grid(row=3,column=4)
        lbllabel12.grid(row=3,column=5)
        
        lbllabel13.grid(row=4,column=2)
        lbllabel14.grid(row=4,column=3)
        lbllabel15.grid(row=4,column=4)
        lbllabel16.grid(row=4,column=5)
        
        lbllabel17.grid(row=5,column=2)
        lbllabel18.grid(row=5,column=3)
        lbllabel19.grid(row=5,column=4)
        lbllabel20.grid(row=5,column=5)
        
        lbllabel21.grid(row=6,column=2)
        lbllabel22.grid(row=6,column=3)
        lbllabel23.grid(row=6,column=4)
        lbllabel24.grid(row=6,column=5)
        
        test = self.winner()
        print(LoginFrame.gsuofficers[test])
        
        
        lblres1 = Label(self.master,font=('Silkscreen',15,'bold'),text='Winner:',bg='black',fg='white')
        lblres1.grid(row=7,column=1)
        
        lblres2 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.facultyofficers[test],bg='black',fg='white')
        lblres2.grid(row=7,column=2,columnspan=3)
        
        lblres3 = Label(self.master,font=('Silkscreen',15,'bold'),text='Votes Recieved:',bg='black',fg='white')
        lblres3.grid(row=8,column=1)
        
        lblres4 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.f_maxvotes,bg='black',fg='white')
        lblres4.grid(row=8,column=2,columnspan=3)
        
        lblres5 = Label(self.master,font=('Silkscreen',15,'bold'),text='Total Votes:',bg='black',fg='white')
        lblres5.grid(row=9,column=1)
        
        lblres6 = Label(self.master,font=('Silkscreen',15,'bold'),text=LoginFrame.f_totalvotes,bg='black',fg='white')
        lblres6.grid(row=9,column=2,columnspan=3)
        
        lbltp = Label(self.master,text="",padx=50,bg='black',fg='white')
        lbltp.grid(row=10,column=1)
        
        btnback = Button(self.master,text='Back',padx=10,pady=10,command=self.back)
        btnback.grid(row=11,column=2,columnspan=2)
        
    def back(self):
        self.master.destroy()
        
        # lbllabel24 = Label(self.master,font=('Silkscreen',10,'bold'),text=LoginFrame.president[self.gsupresident[3]]['preference4'],padx=50,pady=30)

        
        
        # lbllabel0.pack()
        # lbllabel1.pack()
        # lbllabel2.pack()
        # lbllabel3.pack()
        # lbllabel4.pack()

    def duplicates(self,lst, item):
        return [i for i, x in enumerate(lst) if x == item]
    
    def winner(self):
        self.pref1=[]
        self.pref2=[]
        self.pref3=[]
        self.pref4=[]
        
                
        for i in LoginFrame.facultyofficers:
            self.pref1.append(LoginFrame.facultyofficerdict[i]['preference1'])
    
        for i in LoginFrame.facultyofficers:
            self.pref2.append(LoginFrame.facultyofficerdict[i]['preference2'])

        for i in LoginFrame.facultyofficers:
            self.pref3.append(LoginFrame.facultyofficerdict[i]['preference3'])

        for i in LoginFrame.facultyofficers:
            self.pref4.append(LoginFrame.facultyofficerdict[i]['preference4'])
        
        for ele in range(0, len(self.pref1)): 
            LoginFrame.f_totalvotes+=self.pref1[ele]

        self.p1 = max(self.pref1)
        self.d1 = self.duplicates(self.pref1,self.p1)
        if len(self.d1) > 1:
            self.p2 = max(self.pref2)
            self.d2 = self.duplicates(self.pref2,self.p2)
            if len(self.d2) > 1:
                self.p3 = max(self.pref3)
                self.d3 = self.duplicates(self.pref3,self.p3)
                if len(self.d3) > 1:
                    self.p4 = max(self.pref4)
                    LoginFrame.f_maxvotes = self.p4
                    return self.pref4.index(self.p4)
                else:
                    LoginFrame.f_maxvotes = self.p3
                    return self.pref3.index(self.p3)
            else:
                LoginFrame.f_maxvotes = self.p2
                return self.pref2.index(self.p2)
        else:
            LoginFrame.f_maxvotes = self.p1
            return self.pref1.index(self.p1)




root = Tk()
lf = LoginFrame(root)
root.mainloop()
