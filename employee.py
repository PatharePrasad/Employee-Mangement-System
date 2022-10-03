
from tkinter import RIDGE, W, Button, Frame, Image, Label, LabelFrame, Tk, font, ttk
from PIL import Image, ImageTk
class Employee(Tk):
    def __init__(self):
        super().__init__()
        
        # Configuring the main window!
        self.title('Employee Management System')
        self.geometry("1530x790+0+0")
        
        # Adding label 
        self.label = Label(self, text="EMPLOYEE MANAGEMENT SYSTEM", font=('times new roman',37,'bold'),fg='cyan',bg='white')
        self.label.place(x=0,y=0,width=1530,height=50)

        # Preparing Image
        img_logo=Image.open('./images/empLogo.png')
        img_logo=img_logo.resize((50,50),Image.Resampling.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        # Placing Image
        self.labelImg = Label(image=self.photo_logo)
        self.labelImg.place(x=270, y=0, width=50, height=50)
        #Add Frame
        img_frame=Frame(self,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)
        
        # image 1  
        img1=Image.open('./images/pic1.png')
        img1=img1.resize((540,160),Image.Resampling.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.labelImg = Label(img_frame, image=self.photo1)
        self.labelImg.place(x=0, y=0, width=460, height=156)

        # image 2
        img2=Image.open('./images/pic2.png')
        img2=img2.resize((540,160),Image.Resampling.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.labelImg = Label(img_frame, image=self.photo2)
        self.labelImg.place(x=440, y=0, width=562, height=156)

        # image 3 
        img3=Image.open('./images/pic3.jpg')
        img3=img3.resize((540,160),Image.Resampling.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.labelImg = Label(img_frame, image=self.photo3)
        self.labelImg.place(x=1000, y=0, width=560, height=156)

        #Main Frame
        Main_frame=Frame(self,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=220,width=1500,height=560)
 
        #upper Frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white', text='Employee Information',font=('times new roman',11,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=270)

        # Labels and Entry fields
        lbl_dep=Label(upper_frame,text='Department',font=('aerial',11,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,font=('aerial',12,'bold'),width=17,state='readonly')
        combo_dep['value']=('Select Depamrtment', 'HR', 'Software Engineer', 'Manager', 'Team Leader', 'Data Scientist')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        lbl_dep=Label(upper_frame,text='Department',font=('aerial',11,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)
        combo_dep=ttk.Combobox(upper_frame,font=("aerial",12,"bold"),width=17,state='readonly')
        
        #Name
        lbl_Name=Label(upper_frame,font=("aerial",12,"bold"),text="Name:",bg="white")
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(upper_frame,width=22,font=("aerial",11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        # lbl_Designition
        lbl_Designition=Label(upper_frame,font=("aerial",12,"bold"),text="Designition:",bg="white")
        lbl_Designition.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_Designition=ttk.Entry(upper_frame,width=22,font=("aerial",11,"bold"))
        txt_Designition.grid(row=1,column=1,padx=2,pady=7)
        
        # Email
        lbl_Email=Label(upper_frame,font=("aerial",12,"bold"),text="Email:",bg="white")
        lbl_Email.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_Email=ttk.Entry(upper_frame,width=22,font=("aerial",11,"bold"))
        txt_Email.grid(row=1,column=3,padx=2,pady=7)

        # Address
        lbl_address=Label(upper_frame,font=("aerial",12,"bold"),text="Address:",bg="white")
        lbl_address.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(upper_frame,width=22,font=("aerial",11,"bold"))
        txt_address.grid(row=2,column=1,padx=2,pady=7)

        # Married
        lbl_married_status=Label(upper_frame,text='Married Status',font=('aerial',12,'bold'),bg='white')
        lbl_married_status.grid(row=2,column=2,padx=2,sticky=W)

        combo_txt_married=ttk.Combobox(upper_frame,font=('aerial',12,'bold'),width=18,state='readonly')
        combo_txt_married['value']=("Married", "Unmarried")
        combo_txt_married.current(0)
        combo_txt_married.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        # DOB
        lbl_dob=Label(upper_frame,font=("aerial",12,"bold"),text="DOB:",bg="white")
        lbl_dob.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_dob=ttk.Entry(upper_frame,width=22,font=("aerial",11,"bold"))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)

        # DOJ
        lbl_doj=Label(upper_frame,font=("aerial",12,"bold"),text="DOJ:",bg="white")
        lbl_doj.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_doj=ttk.Entry(upper_frame,width=22,font=("aerial",11,"bold"))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)

        # ID Proof
        lbl_proof=Label(upper_frame,text='ID Proof',font=('aerial',12,'bold'),bg='white')
        lbl_proof.grid(row=4,column=0,padx=2,sticky=W)

        combo_txt_proof=ttk.Combobox(upper_frame,font=('aerial',12,'bold'),width=18,state='readonly')
        combo_txt_proof['value']=("Select ID Proof", "PAN CARD", "AADHAR CARD", "DRIVING LICENCE")
        combo_txt_proof.current(0)
        combo_txt_proof.grid(row=4,column=1,padx=2,pady=7,sticky=W)

        # Gender
        lbl_gender=Label(upper_frame,text='Gender',font=('aerial',12,'bold'),bg='white')
        lbl_gender.grid(row=4,column=2,padx=2,sticky=W)

        combo_txt_gender=ttk.Combobox(upper_frame,font=('aerial',12,'bold'),width=18,state='readonly')
        combo_txt_gender['value']=("Male", "Female", "Other")
        combo_txt_gender.current(0)
        combo_txt_gender.grid(row=4,column=3,padx=2,pady=7,sticky=W)

         # Phone
        lbl_phone=Label(upper_frame,font=("aerial",12,"bold"),text="Phone:",bg="white")
        lbl_phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_phone=ttk.Entry(upper_frame,width=22,font=("aerial",11,"bold"))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)

        # Country
        lbl_country=Label(upper_frame,font=("aerial",12,"bold"),text="Country:",bg="white")
        lbl_country.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_country=ttk.Entry(upper_frame,width=22,font=("aerial",11,"bold"))
        txt_country.grid(row=1,column=5,padx=2,pady=7)

        # Country
        lbl_country=Label(upper_frame,font=("aerial",12,"bold"),text="Country:",bg="white")
        lbl_country.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_country=ttk.Entry(upper_frame,width=22,font=("aerial",11,"bold"))
        txt_country.grid(row=1,column=5,padx=2,pady=7)

        # CTC
        lbl_ctc=Label(upper_frame,font=("aerial",12,"bold"),text="Salary(CTC):",bg="white")
        lbl_ctc.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        txt_ctc=ttk.Entry(upper_frame,width=22,font=("aerial",11,"bold"))
        txt_ctc.grid(row=2,column=5,padx=2,pady=7)

        #Button Frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1290,y=10,width=170,height=210)

        btn_add=Button(button_frame,text="Save",font=("aerial",15,"bold"),width=13,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)
 
        btn_update=Button(button_frame,text="Update",font=("aerial",15,"bold"),width=13,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=5)

        btn_delete=Button(button_frame,text="Delete",font=("aerial",15,"bold"),width=13,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)

        btn_clear=Button(button_frame,text="Clear",font=("aerial",15,"bold"),width=13,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=1,pady=5)

        #down Frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white', text='Employee Information Table',font=('times new roman',11,'bold'),fg='red')
        down_frame.place(x=10,y=280,width=1480,height=270)
        
if __name__=="__main__":
    app = Employee()
    app.mainloop()
    