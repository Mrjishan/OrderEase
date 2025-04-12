from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk 
import random,os
from tkinter import messagebox
import tempfile
from time import strftime
from PIL import Image


class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Food Ordering software")

        #============Variables============
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        self.SubCatPerson=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        

        #Product categories list
        self.Category=["Select Option","Khare's Kitchen","Nescafe","Stadium Canteen"]
        self.SubCatClothing=["Select Meal","Fast Food","Tea","Snacks"]
        self.pant=["Burger","French Fries","Sandwich"]
        self.price_peterEngland=50
        self.price_levis=30
        self.price_sparky=40

        self.T_shirt=['Green Tea','Milk Tea','Black Tea']
        self.price_polo=25
        self.price_Roadster=20
        self.price_JackJones=18

        self.Shirt=['Chips','Popcorn','Cookies']
        self.price_peter=20
        self.price_louis=25
        self.price_park=30

        #SubCatLifeStyle
        self.SubCatLifeStyle=["Select Meal",'Coffee','Maggie','Drinks']
        self.Bath_soap=['Hot Coffee','Cold Coffee','Iced coffee','Cappuccino']
        self.price_life=20
        self.price_lux=30
        self.price_santoor=35
        self.price_pearl=50

        self.Face_creame=['Plan Maggie','Masala Maggie','Paneer','Vegetable Maggie']
        self.price_fair=25
        self.price_ponds=35
        self.price_olay=40
        self.price_garnier=25

        self.Hair_oil=['Coca Cola','Water','Sprite']
        self.price_para=25
        self.price_jasmin=20
        self.price_bajaj=30

        #SubCatMobiles(Stadium Canteen)
        self.SubCatMobiles=["Select Meal",'BreakFast','Lunch','Dinner','Soft Drink','Tea']
        self.Iphone=['Samosa','Chola samosa','Tea']
        self.price_ix=10
        self.price_i11=20
        self.price_i12=15

        self.Samsung=['Veg Biryani','Biryani','Salad']
        self.price_sm16=90
        self.price_sm12=110
        self.price_sm21=20

        self.Xiome=['Paneer Tikka','Butter Paneer','Palak Paneer']
        self.price_r11=70
        self.price_r12=100
        self.price_rpro=90

        self.RealMe=['Nimbu Pani','Lassi','Falooda']
        self.price_rel12=15
        self.price_rel13=45
        self.price_relpro=60

        self.OnePlus=['Masala Tea','Adrak Tea','Elaichi Tea']
        self.price_one1=30
        self.price_one12=20
        self.price_one3=25


     # Person 
        self.SubCatPerson=["Select",'Faculty',"Staff","Student"]
        self.SubCatPer=['Faculty',"Staff","Student"]

        #image1
        img = Image.open(r"C:\Users\Jishan\OneDrive\Desktop\Coding\Python\image\logo3.png")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=380,height=130)

        #image2
        img_1 = Image.open(r"C:\Users\Jishan\OneDrive\Desktop\Coding\Python\image\fastfood.jpg")
        img_1=img_1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=380,y=0,width=500,height=130)

        #image3
        img_2 = Image.open(r"C:\Users\Jishan\OneDrive\Desktop\Coding\Python\image\softdrinks.jpg")
        img_2=img_2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=760,y=0,width=500,height=130)

        #image4
        img_3 = Image.open(r"C:\Users\Jishan\OneDrive\Desktop\Coding\Python\image\u10.png")
        img_3=img_3.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        lbl_img_3=Label(self.root,image=self.photoimg_3)
        lbl_img_3.place(x=1140,y=0,width=500,height=130)
        

        lbl_title=Label(self.root,text="OrderEase",font=("times new roman",35,"bold"),bg="grey",fg="yellow")
        lbl_title.place(x=0,y=130,width=1530,height=45)

        def time():
          string = strftime('%H:%M:%S %p')
          lbl.config(text=string)
          lbl.after(1000, time)

        lbl = Label(lbl_title, font = ('times new roman',16, 'bold'),background = 'grey',foreground='yellow')
        lbl.place(x=0,y=0,width=120,height=45)
        time()

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="grey")
        Main_Frame.place(x=0,y=175,width=1530,height=620)

        #Customer labelframe
        Cust_Frame = LabelFrame(Main_Frame,text="Customer details",font=("times new roman",15,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",15,"bold"),bg="white",fg="black")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)


        self.lblCustName=Label(Cust_Frame,font=('arial',12,'bold'),bg="white",text="Customer Name",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=('arial',10,'bold'),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)


        self.lblEmail=Label(Cust_Frame,font=('arial',12,'bold'),bg="white",text="Address",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=('arial',10,'bold'),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #product labelframe
        Product_Frame = LabelFrame(Main_Frame,text="Product",font=("times new roman",15,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=620,height=140)

        #Category
        self.lblCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Select Canteen",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=('arial',10,'bold'),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        #Subcategory
        self.lblSubCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Select Meal",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[""],state="readonly",font=('arial',10,'bold'),width=24)
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        #Product Name
        self.lblproduct=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Menu Card",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,state="readonly",font=('arial',10,'bold'),width=24)
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)

        #Price
        self.lblPrice=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Price",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,state="readonly",textvariable=self.prices,font=('arial',10,'bold'),width=24)
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #Qty
        self.lblQty=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Qty",bd=8)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=('arial',10,'bold'),width=26)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        #Person
        self.lblproduct=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Person",bd=4)
        self.lblproduct.grid(row=2,column=2,sticky=W,padx=5,pady=2)

        self.Combo_Persons=ttk.Combobox(Product_Frame,value=self.SubCatPerson,state="readonly",font=('arial',10,'bold'),width=24)
        self.Combo_Persons.current(0)
        self.Combo_Persons.grid(row=2,column=3,sticky=W,padx=5,pady=2)
        self.Combo_Persons.bind("<<ComboboxSelected>>",self.Person)

        #Midddle frame
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=980,height=340)

        #imagemiddle1
        img_3 = Image.open(r"C:\Users\Jishan\OneDrive\Desktop\Coding\Python\image\Newkhare1.jpg")
        ima_3=img_3.resize((490,340),Image.Resampling.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img_3)

        lbl_img12=Label(MiddleFrame,image=self.photoimg12)
        lbl_img12.place(x=0,y=0,width=490,height=340)

        #imagemiddle2
        img_13=Image.open(r"C:\Users\Jishan\OneDrive\Desktop\Coding\Python\image/nescafe.jpg")
        img_13=img_13.resize((490,447),Image.Resampling.LANCZOS)
        self.photoimg_13=ImageTk.PhotoImage(img_13)

        lbl_img_13=Label(MiddleFrame,image=self.photoimg_13)
        lbl_img_13.place(x=490,y=0,width=500,height=447)

        #Search Area
        Search_Frame=Frame(Main_Frame,bd=2,bg="grey")
        Search_Frame.place(x=1020,y=10,width=500,height=400)

        self.lblBill=Label(Search_Frame,font=('arial',12,'bold'),fg="white",bg="red",text="Bill Number")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=('arial',10,'bold'),width=24)
        self.txt_Entry_search.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',10,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)


        #Right frame bill area 
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",15,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1000,y=45,width=480,height=440)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.Textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",15,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.Textarea.yview)
        self.Textarea.pack(fill=BOTH,expand=1)


        # Bill counter labelframe
        Bottom_Frame = LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",15,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=485,width=1520,height=120)

        self.lblSubTotal=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Sub Total",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=('arial',10,'bold'),width=24)
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lbl_tax=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Gov Tax",bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=('arial',10,'bold'),width=24)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblAmountTotal=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Total",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=('arial',10,'bold'),width=24)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="grey")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add to Cart",font=('arial',17,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=('arial',17,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=('arial',17,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2,text="Order",font=('arial',17,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=('arial',17,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=('arial',17,'bold'),bg="orangered",fg="white",width=13,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()

        self.l=[]
     #======================Function Declaration============================

    # Welcome
    def welcome(self):
         self.Textarea.delete(1.0,END)
         self.Textarea.insert(END,"\t   Welcome to BBD Canteens")
         self.Textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
         self.Textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
         self.Textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
         self.Textarea.insert(END,f"\n Customer Address:{self.c_email.get()}")

         self.Textarea.insert(END,"\n=========================================")
         self.Textarea.insert(END,f"\n Products \t\t\tQTY\t\tprice")
         self.Textarea.insert(END,"\n=========================================\n")



    def AddItem(self):
         Tax=1
         self.n=self.prices.get()
         self.m=self.qty.get()*self.n   
         self.l.append(self.m)
         if self.product.get()=="":
              messagebox.showerror("Error","Please Select Product")
         else:
              self.Textarea.insert(END,f"\n {self.product.get()}\t\t\t{self.qty.get()}\t             {self.m}")
              self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
              self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
              self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))


    def gen_bill(self):
         if self.product.get()=="":
              messagebox.showerror("Error","Please Add To Cart Product")
         elif self.c_phone.get()=="":
              messagebox.showerror("Error","Please Enter Mobile Number")
         elif self.c_name.get()=="":
              messagebox.showerror("Error","Please Enter Name")
         elif self.c_email.get()=="":
              messagebox.showerror("Error","Please Enter Address ")
     #     elif self.SubCatPer.get()=="":
     #          messagebox.showerror("Error","Please Select Who are you ")           
         else:
              text=self.Textarea.get(10.0,(10.0+float(len(self.l))))
              self.welcome()
              self.Textarea.insert(END,text)
              self.Textarea.insert(END,"\n=========================================")
              self.Textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
              self.Textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
              self.Textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
              self.Textarea.insert(END,"\n=========================================")

    def save_bill(self):
         op=messagebox.askyesno("Save bill","Do you want to save the Bill")
         if self.product.get()=="":
              messagebox.showerror("Error","Please Add To Cart Product")
         elif self.c_phone.get()=="":
              messagebox.showerror("Error","Please Enter Mobile Number")
         elif self.c_name.get()=="":
              messagebox.showerror("Error","Please Enter Name")
         elif self.c_email.get()=="":
              messagebox.showerror("Error","Please Enter Address ")
         elif op>0:
              self.bill_data=self.Textarea.get(1.0,END)
              f1=open('bill/'+str(self.bill_no.get())+".txt",'w')
              f1.write(self.bill_data)
              op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} saved successfully")
              f1.close()

    def iprint(self):
         if self.product.get()=="":
              messagebox.showerror("Error","Please Add To Cart Product")
         elif self.c_phone.get()=="":
              messagebox.showerror("Error","Please Enter Mobile Number")
         elif self.c_name.get()=="":
              messagebox.showerror("Error","Please Enter Name")
         elif self.c_email.get()=="":
              messagebox.showerror("Error","Please Enter Address ")
         else:
              op=messagebox.showinfo("Done","Your Order is Done kindly Check your mobile for confirmation")  
               # q=self.Textarea.get(1.0,"end-1c")
               # filename=tempfile.mktemp('.txt')
               # open(filename,'w').write(q)
               # os.startfile(filename,"print")
               # self.kharesKitchenScheen()

    def find_bill(self):
         found="no"
         for i in os.listdir("bill/"):
              if i.split('.')[0]==self.search_bill.get():
                    f1=open(f'bill/{i}','r')
                    self.Textarea.delete(1.0,END)
                    for d in f1:
                         self.Textarea.insert(END,d)
                    f1.close()
                    found="yes"
         if found=='no':
               messagebox.showerror("Error","Invalid Bill No.")

     # Eroor when no name enters


    def clear(self):
         self.Textarea.delete(1.0,END)
         self.c_name.set("")
         self.c_phone.set()
         self.SubCatPerson.set("")
         self.c_email.set("")
         x=random.randint(1000,9999)
         self.bill_no.set(str(x))
         self.search_bill.set("")
         self.product.set("")
         self.prices.set(0)
         self.qty.set(0)
         self.l[0]
         self.sub_total.set("")
         self.tax_input.set("")
         self.total.set('')
         self.welcome()
                   
    def Person(self,event=""):
         if self.Combo_Persons.get()=="Faculty":
              self.SubCatPerson.config(value=self.SubCatPer)
              self.SubCatPerson.current(0)
              

    def Categories(self,event=""):
          if self.Combo_Category.get()=="Khare's Kitchen":
               self.ComboSubCategory.config(value=self.SubCatClothing)
               self.ComboSubCategory.current(0)


          if self.Combo_Category.get()=="Nescafe":
               self.ComboSubCategory.config(value=self.SubCatLifeStyle)
               self.ComboSubCategory.current(0)


          if self.Combo_Category.get()=="Stadium Canteen":
               self.ComboSubCategory.config(value=self.SubCatMobiles)
               self.ComboSubCategory.current(0)


    def Product_add(self,event=""):
          if self.ComboSubCategory.get()=="Fast Food":
               self.ComboProduct.config(value=self.pant)
               self.ComboProduct.current(0)

          if self.ComboSubCategory.get()=="Tea":
               self.ComboProduct.config(value=self.T_shirt)
               self.ComboProduct.current(0)

          if self.ComboSubCategory.get()=="Snacks":
               self.ComboProduct.config(value=self.Shirt)
               self.ComboProduct.current(0)

         #Lifestyle
          if self.ComboSubCategory.get()=="Coffee":
               self.ComboProduct.config(value=self.Bath_soap)
               self.ComboProduct.current(0)

          if self.ComboSubCategory.get()=="Maggie":
               self.ComboProduct.config(value=self.Face_creame)
               self.ComboProduct.current(0)

          if self.ComboSubCategory.get()=="Drinks":
               self.ComboProduct.config(value=self.Hair_oil)
               self.ComboProduct.current(0)

        #Mobiles (Stadium canteen )
          if self.ComboSubCategory.get()=="BreakFast":
               self.ComboProduct.config(value=self.Iphone)
               self.ComboProduct.current(0)

          if self.ComboSubCategory.get()=="Lunch":
               self.ComboProduct.config(value=self.Samsung)
               self.ComboProduct.current(0)

          if self.ComboSubCategory.get()=="Dinner":
               self.ComboProduct.config(value=self.Xiome)
               self.ComboProduct.current(0)

          if self.ComboSubCategory.get()=="Soft Drink":
               self.ComboProduct.config(value=self.RealMe)
               self.ComboProduct.current(0)

          if self.ComboSubCategory.get()=="Tea":
               self.ComboProduct.config(value=self.OnePlus)
               self.ComboProduct.current(0)

    def price(self,event=""):
     # pant(Fast Food)
        if self.ComboProduct.get()=="Burger":
             self.ComboPrice.config(value=self.price_levis)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="French Fries":
             self.ComboPrice.config(value=self.price_peterEngland)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Sandwich":
             self.ComboPrice.config(value=self.price_sparky)
             self.ComboPrice.current(0)
             self.qty.set(1)

     # T-Shirt(Tea)

        if self.ComboProduct.get()=="Green Tea":
             self.ComboPrice.config(value=self.price_polo)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Milk Tea":
             self.ComboPrice.config(value=self.price_Roadster)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Black Tea":
             self.ComboPrice.config(value=self.price_JackJones)
             self.ComboPrice.current(0)
             self.qty.set(1)
     
     # Shirt(Snacks)
        if self.ComboProduct.get()=="Chips":
             self.ComboPrice.config(value=self.price_peter)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Popcorn":
             self.ComboPrice.config(value=self.price_louis)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Cookies":
             self.ComboPrice.config(value=self.price_park)
             self.ComboPrice.current(0)
             self.qty.set(1)

     # Bath soap(Coffee)
        if self.ComboProduct.get()=="Hot Coffee":
             self.ComboPrice.config(value=self.price_life)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Cold Coffee":
             self.ComboPrice.config(value=self.price_lux)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Iced Coffee":
             self.ComboPrice.config(value=self.price_santoor)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Cappuccino":
             self.ComboPrice.config(value=self.price_pearl)
             self.ComboPrice.current(0)
             self.qty.set(1)
       
     # Face creame(Maggie)
        if self.ComboProduct.get()=="Plane Maggie":
             self.ComboPrice.config(value=self.price_fair)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Masala Maggie":
             self.ComboPrice.config(value=self.price_ponds)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Paneer Maggie":
             self.ComboPrice.config(value=self.price_olay)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Vegetable Maggie":
             self.ComboPrice.config(value=self.price_garnier)
             self.ComboPrice.current(0)
             self.qty.set(1)

     # Hair oil(Drinks)

        if self.ComboProduct.get()=="Coca Cola":
             self.ComboPrice.config(value=self.price_para)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Water":
             self.ComboPrice.config(value=self.price_jasmin)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Sprite":
             self.ComboPrice.config(value=self.price_bajaj)
             self.ComboPrice.current(0)
             self.qty.set(1)

     # Mobiles(Stadium Canteen)
       #Iphone(Breakfast)
        if self.ComboProduct.get()=="Samosa":
             self.ComboPrice.config(value=self.price_ix)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Chola samosa":
             self.ComboPrice.config(value=self.price_i11)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Tea":
             self.ComboPrice.config(value=self.price_i12)
             self.ComboPrice.current(0)
             self.qty.set(1)

      # Samsung(Lunch)

        if self.ComboProduct.get()=="Veg Biryani":
             self.ComboPrice.config(value=self.price_sm16)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Biryani":
             self.ComboPrice.config(value=self.price_sm12)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Salad":
             self.ComboPrice.config(value=self.price_sm21)
             self.ComboPrice.current(0)
             self.qty.set(1)

       # Xiome(Dinner)
        if self.ComboProduct.get()=="Paneer Tikka":
             self.ComboPrice.config(value=self.price_r11)
             self.ComboPrice.current(0)
             self.qty.set(1)
        if self.ComboProduct.get()=="Butter Paneer":
             self.ComboPrice.config(value=self.price_r12)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Palak Paneer":
             self.ComboPrice.config(value=self.price_rpro)
             self.ComboPrice.current(0)
             self.qty.set(1)
       # Realme (Soft Drink)
        if self.ComboProduct.get()=="Nimbu Pani":
             self.ComboPrice.config(value=self.price_rel12)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Lassi":
             self.ComboPrice.config(value=self.price_rel13)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Falooda":
             self.ComboPrice.config(value=self.price_relpro)
             self.ComboPrice.current(0)
             self.qty.set(1)
       
       # One plus (Tea)
        if self.ComboProduct.get()=="Masala Tea":
             self.ComboPrice.config(value=self.price_one1)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Adrak Tea":
             self.ComboPrice.config(value=self.price_one12)
             self.ComboPrice.current(0)
             self.qty.set(1)

        if self.ComboProduct.get()=="Elaichi Tea":
             self.ComboPrice.config(value=self.price_one3)
             self.ComboPrice.current(0)
             self.qty.set(1)



if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()