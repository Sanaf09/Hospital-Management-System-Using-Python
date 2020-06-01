
import getpass
import os
import pickle
import string

import time
import pickle
try:
	os.chdir(os.path.join(os.getcwd(), '../../../../etc'))
	print(os.getcwd())
except:
	pass
class Hospital:
    def _init_(self):
        self.sno=0
        self.name=' '
        self.age=0
        self.sex=""
        self.email=" "
        self.fname=" "
        self.address=''
        self.city=''
        self.state=''
        self.height=0
        self.weight=0
        self.doctor=''
        self.med=''
        self.bill=0
        self.paymethod=''
        self.pno=0
        self.bgroup=''
        self.dname=''

    def Input(self):
        self.sno=input("Enter Serial number:")
        self.name=input("Enter Patinet's Name:")
        self.age=input("Enter Patinet's Age:")
        self.sex=input("Enter Patinet's Sex (Male/Female):")
        self.height=input("Enter Patinet's Height:")
        self.weight=input("Enter Patinet's Weight(In Kgs):")
        self.bgroup=input("Enter Patient's Blood Group:")
        self.fname=input("Enter Fathers Name:")
        self.address=input("Enter Address:")
        self.city=input("Enter City:")
        self.state=input("Enter State:")
        self.pno=input("Enter Phone number:")
        self.email=input("Enter E-Mail:")
        self.doctor=input("Enter Doctor's Name:")
        self.dname=input("Enter Disease Name:")
        self.med=input("Enter Prescribed Medicine:")
        self.bill=input("Enter Bill Amount: Rs.")
        self.paymethod=input("Enter Payment Method(Cash/Cheque/Card):")
    def Output(self):
        print ("\n\nSERIAL NUMBER:-", self.sno)
        print ("PATIENT'S NAME:-",self.name)
        print ("PATIENT'S AGE:-",self.age)
        print ("PATIENT'S SEX:-",self.sex)
        print ("PATIENT'S HEIGHT:-",self.height)
        print ("PATIENT'S WEIGHT:-",self.weight)
        print ("PATIENT'S BLOOD GROUP:-",self.bgroup)
        print ("FATHERS NAME:-",self.fname)
        print ("ADDRESS:-",self.address)
        print ("CITY:-",self.city)
        print ("STATE:-",self.state)
        print ("CONTACT NUMBER:-",self.pno)
        print ("E-MAIL ADDRESS:-",self.email)
        print ("DISEASE NAME:-",self.dname)
        print ("DOCTOR'S NAME:-",self.doctor)
        print ("PRESCRIBED MEDICINES:-",self.med)
        print ("BILL AMOUNT:-",self.bill)
        print ("PAYMENT METHOD:-",self.paymethod)

def WriteHospital():
    fout=open("asd.txt","wb")
    ob=Hospital()
    print ("Enter Details::")
    ob.Input()
    pickle.dump(ob,fout)
    print ("Record Saved")
    fout.close()
def ReadHospital():
    fin=open("asd.txt","rb")
    ob=Hospital()
    try:
        print ("Hospital Details are::")
        while True:
            ob=pickle.load(fin)
            ob.Output()
            print    
    except EOFError:
        fin.close
def SearchHospitalSno(n):       #to search on the basis of sno
    fin=open("asd.txt","rb")
    ob=Hospital()
    flag=False
    try:
        print
        print("\nHospital Details Are:--")
        while True:
            ob=pickle.load(fin)
            if ob.sno==n:
                ob.Output()
                flag=True
    except EOFError:
        if not flag:
            print ("\n")
            print ("\n")
            print ("               ____________________________________________ " )
            print ("               |  ... RECORD... DOES... NOT... EXIST ...  | ")
            print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
        fin.close()
def SearchHospitalemail(n):       #to search on the basis of email
    fin=open("asd.txt","rb")
    ob=Hospital()
    flag=False
    try:
        print("\nHospital Details Are:--")
        while True:
            ob=pickle.load(fin)
            if ob.email==n:
                ob.Output()
                flag=True
                break
    except EOFError:
        if not flag:
            print ("\n")
            print ("\n")
            print ("               ____________________________________________ " )
            print ("               |  ... RECORD... DOES... NOT... EXIST ...  | " )
            print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " )
        fin.close() 
def SearchHospitalcontact(n):      #to search on the basis of Contact Number
    fin=open("asd.txt","rb")
    ob=Hospital()
    flag=False
    try:
        print("\nHospital Details Are:--")
        while True:
            ob=pickle.load(fin)
            if ob.pno==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print ("\n")
                print ("\n")
                print ("               ____________________________________________ " )
                print ("               |  ... RECORD... DOES... NOT... EXIST ...  | " )
                print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " )
            fin.close()

def SearchBloodgroup(n):             #to search on the basis of Blood Group
    fin=open("asd.txt","rb")
    ob=Hospital()
    flag=False
    try:
        print("\nHospital Details are:")
        while True:
            ob=pickle.load(fin)
            if ob.bgroup==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print ("\n")
                print ("\n")
                print ("               ____________________________________________ ") 
                print ("               |  ... RECORD... DOES... NOT... EXIST ...  | ")
                print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
            fin.close()

def SearchAge(n):                        #to search on the basis of Age
    fin=open("asd.txt","rb")
    ob=Hospital()
    flag=False
    try:
        print("\nHospital Details are:")
        while True:
            ob=pickle.load(fin)
            if ob.age==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print ("\n")
                print ("\n")
                print ("               ____________________________________________ ") 
                print ("               |  ... RECORD... DOES... NOT... EXIST ...  | ")
                print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
            fin.close()
            
def SearchSex(n):                         #to search on the basis of Sex
    fin=open("asd.txt","rb")
    ob=Hospital()
    flag=False
    try:
        print("\nHospital Details are:")
        while True:
            ob=pickle.load(fin)
            if ob.sex==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print ("\n")
                print ("\n")
                print ("               ____________________________________________ ") 
                print ("               |  ... RECORD... DOES... NOT... EXIST ...  | ")
                print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
            fin.close()

def SearchDName(n):                         #to search on the basis of Disease Name
    fin=open("asd.txt","rb")
    ob=Hospital()
    flag=False
    try:
        print("\nHospital Details are:")
        while True:
            ob=pickle.load(fin)
            if ob.dname==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print ("\n")
                print ("\n")
                print ("               ____________________________________________ ") 
                print ("               |  ... RECORD... DOES... NOT... EXIST ...  | ")
                print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
            fin.close()

def SearchDoctor(n):                         #to search on the basis of Doctors Name
    fin=open("asd.txt","rb")
    ob=Hospital()
    flag=False
    try:
        print("\nHospital Details are:")
        while True:
            ob=pickle.load(fin)
            if ob.doctor==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print ("\n")
                print ("\n")
                print ("               ____________________________________________ " )
                print ("               |  ... RECORD... DOES... NOT... EXIST ...  | " )
                print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " )
            fin.close()

def SearchPayment(n):                          #to search on the basis of Payment Method
    fin=open("asd.txt","rb")
    ob=Hospital()
    flag=False
    try:
        print("\nHospital Details are:")
        while True:
            ob=pickle.load(fin)
            if ob.paymethod==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print ("\n")
                print ("\n")
                print ("               ____________________________________________ " )
                print ("               |  ... RECORD... DOES... NOT... EXIST ...  | " )
                print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " )
            fin.close()

def ModiHospital(b,a):#to modify details
    fin=open("asd.txt","rb")
    fout = open ("temp.txt","a")
    ob=Hospital()
    flag = False
    try:
        while True :
            ob=pickle.load(fin)
            if ob.sno==b:
                flag=True
                if n==1:
                    a=input("ENTER NEW PATIENT'S NAME::")
                    ob.name=a
                    pickle.dump(ob,fout)
                elif n==2: 
                    a=input("ENTER NEW PATIENT'S AGE:-->")
                    ob.age=a
                    pickle.dump(ob,fout)
                elif n==3:
                    a=input("ENTER NEW PATIENT'S SEX(Male/Female):-->")
                    ob.sex=a
                    pickle.dump(ob,fout)
                elif n==4:
                    a=input("ENTER NEW PATIENT'S HEIGHT:-->")
                    ob.height=a
                    pickle.dump(ob,fout)
                elif n==5:
                    a=input("ENTER NEW PATIENT'S WEIGHT(In Kgs):-->")
                    ob.weight=a
                    pickle.dump(ob,fout)
                elif n==6:
                    a=input("ENTER NEW PATIENT'S BLOOD GROUP:-->")
                    ob.bgroup=a
                    pickle.dump(ob,fout)
                elif n==7:
                    a=input("ENTER NEW FATHERS NAME:-->")
                    ob.fname=a
                    pickle.dump(ob,fout)
                elif n==8:
                    a=input("ENTER NEW ADDRESS:-->")
                    ob.address=a
                    pickle.dump(ob,fout)
                elif n==9:
                    a=input("ENTER NEW CITY:-->")
                    ob.city=a
                    pickle.dump(ob,fout)
                elif n==10:
                    a=input("ENTER NEW STATE:-->")
                    ob.state=a
                    pickle.dump(ob,fout)
                elif n==11:
                    a=input("ENTER NEW CONTACT NUMBER:-->")
                    ob.pno=a
                    pickle.dump(ob,fout)
                elif n==12:
                    a=input("ENTER NEW E-MAIL ADDRESS:-->")
                    ob.email=a
                    pickle.dump(ob,fout)
                elif n==13:
                    a=input("ENTER NEW DISEASE NAME:-->")
                    ob.dname=a
                    pickle.dump(ob,fout)
                elif n==14:
                    a=input("ENTER NEW DOCTOR'S NAME:-->")
                    ob.doctor=a
                    pickle.dump(ob,fout)
                elif n==15:
                    a=input("ENTER NEW PRESCRIBED MEDICINE:-->")
                    ob.med=a
                    pickle.dump(ob,fout)
                elif n==16:
                    a=input("ENTER NEW BILL AMOUNT:--> Rs.")
                    ob.bill=a
                    pickle.dump(ob,fout)
                elif n==17:
                    a=input("ENTER NEW PAYMENT METHOD(Cash\Cheque\Card):-->")
                    ob.paymethod=a
                    pickle.dump(ob,fout)
                
                elif n==18:
                    print ("__________________ENTER THE NEW DETAILS__________________")
                    ob.Input() 
                    pickle.dump(ob,fout)
                else:
                    print("Enter Valid Choice!")
            else:
                pickle.dump(ob,fout)
            
    except EOFError:
        if not flag:
            print ("\n")
            print ("\n")
            print ("               ____________________________________________ " )
            print ("               |  ... RECORD... DOES... NOT... EXIST ...  | " )
            print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " )
        fin.close()

    fout.close()
    os.remove("asd.txt")
    os.rename("temp.txt","asd.txt")

def DelHospital(n):
    fin=open("asd.txt","rb")
    fout=open("temp.txt","wb")
    ob=Hospital()
    Flag=False
    try:
        while True:
            ob=pickle.load(fin)
            if ob.sno==n:
                Flag=True
                print("Rcord Deleted")
            else:
                
                pickle.dump(ob,fout)
    except EOFError:
        if not Flag:
            print("Record Does Not Exit")
        fin.close()
        fout.close()
        os.remove("asd.txt")
        os.rename("temp.txt","asd.txt")

#MAIN PROGRAM

    
        
        
        
print("PROGECT MADE BY sanaf momin")

# creatinga lists of users/admins their PINs
users = ['sanaf', 'abc', 'xyz']
pins = ['1234', '2222', '3333']

count = 0
# while loop checks existance of the enterd username
while True:
	user = input('\nENTER USER NAME: ')
	user = user.lower()
	if user in users:
		if user == users[0]:
			n = 0
		elif user == users[1]:
			n = 1
		else:
			n = 2
		break
	else:
	
		
		print('INVALID USERNAME')
		

# comparing pin
while count < 3:
	
	pin = str(getpass.getpass('PLEASE ENTER PIN: '))
	
	if pin.isdigit():
		if user == 'sanaf':
			if pin == pins[0]:
				break
			else:
				count += 1
			
				print('INVALID PIN')
				
				print()

		if user == 'abc':
			if pin == pins[1]:
				break
			else:
				count += 1
				
				print('INVALID PIN')
				
				print()
				
		if user == 'xyz':
			if pin == pins[2]:
				break
			else:
				count += 1
				
				print('INVALID PIN')
				
				print()
	else:
	
		print('PIN CONSISTS OF 4 DIGITS')
		
		count += 1
	
# in case of a valid pin- continuing, or exiting
if count == 3:
	
	
	print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
	
	exit()


print('LOGIN SUCCESFUL, CONTINUE')


print("\n\n\t\t\t\t\t\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        
print("\n\t\t\t\t\t\t_____________________________________________________________________________________")
print ("\n\t\t\t\t\t\t\t\tWELCOME TO THE HOSPITAL MANAGEMENT SYSTEM USING PYTHON")
print("\n\t\t\t\t\t\t_____________________________________________________________________________________")
print("\n\t\t\t\t\t\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("\n\n==>>>PRESS ENTER TO CONTINUE")
    #print("\n")
print("1.WRITE RECORD\n2.SHOW ALL RECORDS\n3.SEARCH BY SERIAL NUMBER")
print("4.SEARCH BY CONTACT NUMBER\n5.SEARCH BY BLOOD GROUP\n6.SEARCH BY AGE\n7.SEARCH BY SEX")
print("8.SEARCH BY DISEASE NAME\n9.SEARCH BY DOCTORS NAME\n10.SEARCH BY PAYMENT METHOD\n11.SEARCH BY E-MAIL")
print("12.MODIFY RECORD\n13.DELETE RECORD\n14.EXIT")

print('\n')
localtime=time.asctime(time.localtime(time.time()))
print(localtime)


while True:
    print("\n")
    
    ch=int(input("\nPLEASE ENTER YOUR CHOICE:--"))
    if ch==1:
        WriteHospital()
    elif ch==2:
        ReadHospital()
    elif ch==3:
        n=input("PLEASE ENTER SERIAL NUMBER TO SEARCH:--")
        SearchHospitalSno(n)
    elif ch==4:
        n=input("PLEASE ENTER CONTACT NUMBER TO SEARCH:--")
        SearchHospitalcontact(n)
    elif ch==5:
        n=input("PLEASE ENTER BLOOD GROUP TO SEARCH:--")
        SearchBloodgroup(n)
    elif ch==6:
        n=input("PLEASE ENTER AGE TO SEARCH:--")
        SearchAge(n)
    elif ch==7:
        n=input("PLEASE ENTER SEX TO SEARCH:--")
        SearchSex(n)
    elif ch==8:
        n=input("PLEASE ENTER DISEASE NAME TO SEARCH:--")
        SearchDName(n)
    elif ch==9:
        n=input("PLEASE ENTER DOCTORS NAME TO SEARCH:--")
        SearchDoctor(n)
    elif ch==10:
        n=input("PLEASE ENTER PAYMENT METHOD TO SEARCH:--")
        SearchPayment(n)
    elif ch==11:
        n=input("PLEASE ENTER E-MAIL ADDRESS TO SEARCH:--")
        SearchHospitalemail(n)
    elif ch==12:
        m=input("ENTER SERIAL NUMBER TO MODIFY:--")
        print ("\n")
        print ("____________________________________________ " )
        print ("|  ......... ENTER YOUR CHOICE ..........  | " )
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " )
        print ("\n")
        print ("WHAT DO YOU WANT TO MODIFY:")
        print 
        print ("1.PATIENT'S NAME")
        print ("2.PATIENT'S AGE")
        print ("3.PATIENT'S SEX")
        print ("4.PATIENT'S HEIGHT")
        print ("5.PATIENT'S WEIGHT")
        print ("6.PATIENT'S BLOOD GROUP:-")
        print ("7.FATHERS NAME:-")
        print ("8.ADDRESS:-")
        print ("9.CITY:-")
        print ("10.STATE:-")
        print ("11.CONTACT NUMBER:-")
        print ("12.E-MAIL ADDRESS:-")
        print ("13.DISEASE NAME:-")
        print ("14.DOCTOR'S NAME:-")
        print ("15.PRESCRIBED MEDICINES:-")
        print ("16.BILL AMOUNT:-")
        print ("17.PAYMENT METHOD:-")
        print ("18.ALL")
        n=input("::--")
        ModiHospital(m,n)
    elif ch==13:
        n=input("ENTER SERIAL NUMBER TO DELETE:-")
        DelHospital(n)
    elif ch==14:
        print ("\n")
        print ("EXITING"),
        time.sleep(.8)
        print ("."),
        time.sleep(.8)
        print ("."),
        time.sleep(.8)
        print ("."),
        time.sleep(.8)
        print ("."),
        time.sleep(.8)
        print (".")
        break
    else:
        print ("Analysing your input."),
        time.sleep(1)
        print ("."),
        time.sleep(1)
        print ("."),
        time.sleep(1)
        print ("."),
        time.sleep(.6)
        print ("."),
        time.sleep(.6)
        print (".")
        print("\n\n\n~~~~~~~~~~~~~~~~~~~~WRONG CHOICE!!!~~~~~~~~~~~~~~~~~~~\n\n\n")
        
            


class Hospital:
    def _init_(self):
        self.sno=0,
        self.name=' ',
        self.age=0,
        self.sex="",
        self.email=" ",
        self.fname=" ",
        self.address='',
        self.city='',
        self.state='',
        self.height=0,
        self.weight=0,
        self.doctor='',
        self.med='',
        self.bill=0,
        self.paymethod='',
        self.pno=0,
        self.bgroup='',
        self.dname=''

    def Input(self):
        self.sno=input("Enter Serial number:")
        self.name=input("Enter Patinet's Name:")
        self.age=input("Enter Patinet's Age:")
        self.sex=input("Enter Patinet's Sex (Male/Female):")
        self.height=input("Enter Patinet's Height:")
        self.weight=input("Enter Patinet's Weight(In Kgs):")
        self.bgroup=input("Enter Patient's Blood Group:")
        self.fname=input("Enter Fathers Name:")
        self.address=input("Enter Address:")
        self.city=input("Enter City:")
        self.state=input("Enter State:")
        self.pno=input("Enter Phone number:")
        self.email=input("Enter E-Mail:")
        self.doctor=input("Enter Doctor's Name:")
        self.dname=input("Enter Disease Name:")
        self.med=input("Enter Prescribed Medicine:")
        self.bill=input("Enter Bill Amount: Rs.")
        self.paymethod=input("Enter Payment Method(Cash/Cheque/Card):")
    def Output(self):
        print ("\n\nSERIAL NUMBER:-", self.sno)
        print ("PATIENT'S NAME:-",self.name)
        print ("PATIENT'S AGE:-",self.age)
        print ("PATIENT'S SEX:-",self.sex)
        print ("PATIENT'S HEIGHT:-",self.height)
        print ("PATIENT'S WEIGHT:-",self.weight)
        print ("PATIENT'S BLOOD GROUP:-",self.bgroup)
        print ("FATHERS NAME:-",self.fname)
        print ("ADDRESS:-",self.address)
        print ("CITY:-",self.city)
        print ("STATE:-",self.state)
        print ("CONTACT NUMBER:-",self.pno)
        print ("E-MAIL ADDRESS:-",self.email)
        print ("DISEASE NAME:-",self.dname)
        print ("DOCTOR'S NAME:-",self.doctor)
        print ("PRESCRIBED MEDICINES:-",self.med)
        print ("BILL AMOUNT:-",self.bill)
        print ("PAYMENT METHOD:-",self.paymethod)

def WriteHospital():
    fout=open("asd.txt","wb")
    ob=Hospital()
    print ("Enter Details::")
    ob.Input()
    pickle.dump(ob,fout)
    print ("Record Saved")
    fout.close()
def ReadHospital():
    fin=open("asd.txt","rb")
    ob=Hospital()
    try:
        print ("Hospital Details are::")
        while True:
            ob=pickle.load(fin)
            ob.Output()
            print    
    except EOFError:
        fin.close
def SearchHospitalSno(n):       #to search on the basis of sno
    fin=open("asd.txt","rb")
    ob=Hospital()
    flag=False
    try:
        print
        print("\nHospital Details Are:--")
        while True:
            ob=pickle.load(fin)
            if ob.sno==n:
                ob.Output()
                flag=True
    except EOFError:
        if not flag:
            print ("\n")
            print ("\n")
            print ("               ____________________________________________ " )
            print ("               |  ... RECORD... DOES... NOT... EXIST ...  | ")
            print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
        fin.close()
def SearchHospitalemail(n):       #to search on the basis of email
    fin=open("asd.txt","rb")
    ob=Hospital()
    flag=False
    try:
        print("\nHospital Details Are:--")
        while True:
            ob=pickle.load(fin)
            if ob.email==n:
                ob.Output()
                flag=True
                break
    except EOFError:
        if not flag:
            print ("\n")
            print ("\n")
            print ("               ____________________________________________ " )
            print ("               |  ... RECORD... DOES... NOT... EXIST ...  | " )
            print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " )
        fin.close() 
def SearchHospitalcontact(n):      #to search on the basis of Contact Number
    fin=open("asd.txt","rb")
    ob=Hospital()
    flag=False
    try:
        print("\nHospital Details Are:--")
        while True:
            ob=pickle.load(fin)
            if ob.pno==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print ("\n")
                print ("\n")
                print ("               ____________________________________________ " )
                print ("               |  ... RECORD... DOES... NOT... EXIST ...  | " )
                print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " )
            fin.close()

def SearchBloodgroup(n):             #to search on the basis of Blood Group
    fin=open("asd.txt","rb")
    ob=Hospital()
    flag=False
    try:
        print("\nHospital Details are:")
        while True:
            ob=pickle.load(fin)
            if ob.bgroup==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print ("\n")
                print ("\n")
                print ("               ____________________________________________ ") 
                print ("               |  ... RECORD... DOES... NOT... EXIST ...  | ")
                print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
            fin.close()

def SearchAge(n):                        #to search on the basis of Age
    fin=open("asd.txt","rb")
    ob=Hospital()
    flag=False
    try:
        print("\nHospital Details are:")
        while True:
            ob=pickle.load(fin)
            if ob.age==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print ("\n")
                print ("\n")
                print ("               ____________________________________________ ") 
                print ("               |  ... RECORD... DOES... NOT... EXIST ...  | ")
                print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
            fin.close()
            
def SearchSex(n):                         #to search on the basis of Sex
    fin=open("asd.txt","rb")
    ob=Hospital()
    flag=False
    try:
        print("\nHospital Details are:")
        while True:
            ob=pickle.load(fin)
            if ob.sex==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print ("\n")
                print ("\n")
                print ("               ____________________________________________ ") 
                print ("               |  ... RECORD... DOES... NOT... EXIST ...  | ")
                print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
            fin.close()

def SearchDName(n):                         #to search on the basis of Disease Name
    fin=open("asd.txt","rb")
    ob=Hospital()
    flag=False
    try:
        print("\nHospital Details are:")
        while True:
            ob=pickle.load(fin)
            if ob.dname==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print ("\n")
                print ("\n")
                print ("               ____________________________________________ ") 
                print ("               |  ... RECORD... DOES... NOT... EXIST ...  | ")
                print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
            fin.close()

def SearchDoctor(n):                         #to search on the basis of Doctors Name
    fin=open("asd.txt","rb")
    ob=Hospital()
    flag=False
    try:
        print("\nHospital Details are:")
        while True:
            ob=pickle.load(fin)
            if ob.doctor==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print ("\n")
                print ("\n")
                print ("               ____________________________________________ " )
                print ("               |  ... RECORD... DOES... NOT... EXIST ...  | " )
                print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " )
            fin.close()

def SearchPayment(n):                          #to search on the basis of Payment Method
    fin=open("asd.txt","rb")
    ob=Hospital()
    flag=False
    try:
        print("\nHospital Details are:")
        while True:
            ob=pickle.load(fin)
            if ob.paymethod==n:
                ob.Output()
                flag=True
                
    except EOFError:
            if not flag:
                print ("\n")
                print ("\n")
                print ("               ____________________________________________ " )
                print ("               |  ... RECORD... DOES... NOT... EXIST ...  | " )
                print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " )
            fin.close()

def ModiHospital(b,a):#to modify details
    fin=open("asd.txt","rb")
    fout = open ("temp.txt","wb")
    ob=Hospital()
    flag = False
    try:
        while True :
            ob=pickle.load(fin)
            if ob.sno==b:
                flag=True
                if n==1:
                    a=input("ENTER NEW PATIENT'S NAME::")
                    ob.name=a
                    pickle.dump(ob,fout)
                elif n==2: 
                    a=input("ENTER NEW PATIENT'S AGE:-->")
                    ob.age=a
                    pickle.dump(ob,fout)
                elif n==3:
                    a=input("ENTER NEW PATIENT'S SEX(Male/Female):-->")
                    ob.sex=a
                    pickle.dump(ob,fout)
                elif n==4:
                    a=input("ENTER NEW PATIENT'S HEIGHT:-->")
                    ob.height=a
                    pickle.dump(ob,fout)
                elif n==5:
                    a=input("ENTER NEW PATIENT'S WEIGHT(In Kgs):-->")
                    ob.weight=a
                    pickle.dump(ob,fout)
                elif n==6:
                    a=input("ENTER NEW PATIENT'S BLOOD GROUP:-->")
                    ob.bgroup=a
                    pickle.dump(ob,fout)
                elif n==7:
                    a=input("ENTER NEW FATHERS NAME:-->")
                    ob.fname=a
                    pickle.dump(ob,fout)
                elif n==8:
                    a=input("ENTER NEW ADDRESS:-->")
                    ob.address=a
                    pickle.dump(ob,fout)
                elif n==9:
                    a=input("ENTER NEW CITY:-->")
                    ob.city=a
                    pickle.dump(ob,fout)
                elif n==10:
                    a=input("ENTER NEW STATE:-->")
                    ob.state=a
                    pickle.dump(ob,fout)
                elif n==11:
                    a=input("ENTER NEW CONTACT NUMBER:-->")
                    ob.pno=a
                    pickle.dump(ob,fout)
                elif n==12:
                    a=input("ENTER NEW E-MAIL ADDRESS:-->")
                    ob.email=a
                    pickle.dump(ob,fout)
                elif n==13:
                    a=input("ENTER NEW DISEASE NAME:-->")
                    ob.dname=a
                    pickle.dump(ob,fout)
                elif n==14:
                    a=input("ENTER NEW DOCTOR'S NAME:-->")
                    ob.doctor=a
                    pickle.dump(ob,fout)
                elif n==15:
                    a=input("ENTER NEW PRESCRIBED MEDICINE:-->")
                    ob.med=a
                    pickle.dump(ob,fout)
                elif n==16:
                    a=input("ENTER NEW BILL AMOUNT:--> Rs.")
                    ob.bill=a
                    pickle.dump(ob,fout)
                elif n==17:
                    a=input("ENTER NEW PAYMENT METHOD(Cash\Cheque\Card):-->")
                    ob.paymethod=a
                    pickle.dump(ob,fout)
                
                elif n==18:
                    print ("__________________ENTER THE NEW DETAILS__________________")
                    ob.Input() 
                    pickle.dump(ob,fout)
                else:
                    print("Enter Valid Choice!")
            else:
                pickle.dump(ob,fout)
            
    except EOFError:
        if not flag:
            print ("\n")
            print ("\n")
            print ("               ____________________________________________ " )
            print ("               |  ... RECORD... DOES... NOT... EXIST ...  | " )
            print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " )
        fin.close()

    fout.close()
    os.remove("asd.txt")
    os.rename("temp.txt","asd.txt")

def DelHospital(n):
    fin=open("asd.txt","rb")
    fout=open("temp.txt","wb")
    ob=Hospital()
    Flag=False
    try:
        while True:
            ob=pickle.load(fin)
            if ob.sno==n:
                Flag=True
                print("Rcord Deleted")
            else:
                
                pickle.dump(ob,fout)
    except EOFError:
        if not Flag:
            print("Record Does Not Exit")
        fin.close()
        fout.close()
        os.remove("asd.txt")
        os.rename("temp.txt","asd.txt")

#MAIN PROGRAM

    
        
        
        
print("PYTHON PROJECTS")

# creatinga lists of users/admins & their PINs
users = ['sanaf', 'abc', 'xyz']
pins = ['1234', '5678', '1111']

count = 0
# while loop checks existance of the enterd username
while True:
	user = input('\nENTER USER NAME: ')
	user = user.lower()
	if user in users:
		if user == users[0]:
			n = 0
		elif user == users[1]:
			n = 1
		else:
			n = 2
		break
	else:
	
		
		print('INVALID USERNAME')
		

# comparing pin
while count < 3:
	
	pin = str(getpass.getpass('PLEASE ENTER PIN: '))
	
	if pin.isdigit():
		if user == 'sanaf':
			if pin == pins[0]:
				break
			else:
				count += 1
			
				print('INVALID PIN')
				
				print()

		if user == 'abc':
			if pin == pins[1]:
				break
			else:
				count += 1
				
				print('INVALID PIN')
				
				print()
				
		if user == 'xyz':
			if pin == pins[2]:
				break
			else:
				count += 1
				
				print('INVALID PIN')
				
				print()
	else:
	
		print('PIN CONSISTS OF 4 DIGITS')
		
		count += 1
	
# in case of a valid pin- continuing, or exiting
if count == 3:
	
	
	print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
	
	exit()


print('LOGIN SUCCESFUL, CONTINUE')


print("\n\n\t\t\t\t\t\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        
print("\n\t\t\t\t\t\t_________________________________________________________________________")
print ("\n\t\t\t\t\t\t\t\tWELCOME TO THE HOSPITAL MANAGEMENT SYSTEM USING PYTHON")
print("\n\t\t\t\t\t\t_________________________________________________________________________")
print("\n\t\t\t\t\t\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("\n\n==>>>PRESS ENTER TO CONTINUE")
    #print("\n")
print("1.WRITE RECORD\n2.SHOW ALL RECORDS\n3.SEARCH BY SERIAL NUMBER")
print("4.SEARCH BY CONTACT NUMBER\n5.SEARCH BY BLOOD GROUP\n6.SEARCH BY AGE\n7.SEARCH BY SEX")
print("8.SEARCH BY DISEASE NAME\n9.SEARCH BY DOCTORS NAME\n10.SEARCH BY PAYMENT METHOD\n11.SEARCH BY E-MAIL")
print("12.MODIFY RECORD\n13.DELETE RECORD\n14.EXIT")

print('\n')
localtime=time.asctime(time.localtime(time.time()))
print(localtime)


while True:
    print("\n")
    
    ch=int(input("\nPLEASE ENTER YOUR CHOICE:--"))
    if ch==1:
        WriteHospital()
    elif ch==2:
        ReadHospital()
    elif ch==3:
        n=input("PLEASE ENTER SERIAL NUMBER TO SEARCH:--")
        SearchHospitalSno(n)
    elif ch==4:
        n=input("PLEASE ENTER CONTACT NUMBER TO SEARCH:--")
        SearchHospitalcontact(n)
    elif ch==5:
        n=input("PLEASE ENTER BLOOD GROUP TO SEARCH:--")
        SearchBloodgroup(n)
    elif ch==6:
        n=input("PLEASE ENTER AGE TO SEARCH:--")
        SearchAge(n)
    elif ch==7:
        n=input("PLEASE ENTER SEX TO SEARCH:--")
        SearchSex(n)
    elif ch==8:
        n=input("PLEASE ENTER DISEASE NAME TO SEARCH:--")
        SearchDName(n)
    elif ch==9:
        n=input("PLEASE ENTER DOCTORS NAME TO SEARCH:--")
        SearchDoctor(n)
    elif ch==10:
        n=input("PLEASE ENTER PAYMENT METHOD TO SEARCH:--")
        SearchPayment(n)
    elif ch==11:
        n=input("PLEASE ENTER E-MAIL ADDRESS TO SEARCH:--")
        SearchHospitalemail(n)
    elif ch==12:
        m=input("ENTER SERIAL NUMBER TO MODIFY:--")
        print ("\n")
        print ("____________________________________________ " )
        print ("|  ......... ENTER YOUR CHOICE ..........  | " )
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " )
        print ("\n")
        print ("WHAT DO YOU WANT TO MODIFY:")
        print 
        print ("1.PATIENT'S NAME")
        print ("2.PATIENT'S AGE")
        print ("3.PATIENT'S SEX")
        print ("4.PATIENT'S HEIGHT")
        print ("5.PATIENT'S WEIGHT")
        print ("6.PATIENT'S BLOOD GROUP:-")
        print ("7.FATHERS NAME:-")
        print ("8.ADDRESS:-")
        print ("9.CITY:-")
        print ("10.STATE:-")
        print ("11.CONTACT NUMBER:-")
        print ("12.E-MAIL ADDRESS:-")
        print ("13.DISEASE NAME:-")
        print ("14.DOCTOR'S NAME:-")
        print ("15.PRESCRIBED MEDICINES:-")
        print ("16.BILL AMOUNT:-")
        print ("17.PAYMENT METHOD:-")
        print ("18.ALL")
        n=input("::--")
        ModiHospital(m,n)
    elif ch==13:
        n=input("ENTER SERIAL NUMBER TO DELETE:-")
        DelHospital(n)
    elif ch==14:
        print ("\n")
        print ("EXITING"),
        time.sleep(.8)
        print ("."),
        time.sleep(.8)
        print ("."),
        time.sleep(.8)
        print ("."),
        time.sleep(.8)
        print ("."),
        time.sleep(.8)
        print (".")
        break
    else:
        print ("Analysing your input."),
        time.sleep(1)
        print ("."),
        time.sleep(1)
        print ("."),
        time.sleep(1)
        print ("."),
        time.sleep(.6)
        print ("."),
        time.sleep(.6)
        print (".")
        print("\n\n\n~~~~~~~~~~~~~~~~~~~~WRONG CHOICE!!!~~~~~~~~~~~~~~~~~~~\n\n\n")
        
            


#%%
