from tkinter import *
from tkinter import messagebox
import random, os
import random, os, tempfile
import smtplib
#


def clear():


    bathsoapEntry.delete(0,END)
    facecreamEntry.delete(0,END)
    facewashEntry.delete(0,END)
    hairgelEntry.delete(0,END)
    hairsprayEntry.delete(0,END)
    bodylotionEntry.delete(0,END)


    daalEntry.delete(0,END)
    wheatEntry.delete(0,END)
    sugarEntry.delete(0,END)
    teaEntry.delete(0,END)
    riceEntry.delete(0,END)
    oilEntry.delete(0,END)


    pepsiEntry.delete(0,END)
    dewEntry.delete(0,END)
    frootiEntry.delete(0,END)
    spriteEntry.delete(0,END)
    cococolaEntry.delete(0,END)
    maazaEntry.delete(0,END)








    bathsoapEntry.insert(0,0)
    facecreamEntry.insert(0,0)
    facewashEntry.insert(0,0)
    hairgelEntry.insert(0,0)
    hairsprayEntry.insert(0,0)
    bodylotionEntry.insert(0,0)


    daalEntry.insert(0,0)
    wheatEntry.insert(0,0)
    sugarEntry.insert(0,0)
    teaEntry.insert(0,0)
    riceEntry.insert(0,0)
    oilEntry.insert(0,0)


    pepsiEntry.insert(0,0)
    dewEntry.insert(0,0)
    frootiEntry.insert(0,0)
    spriteEntry.insert(0,0)
    cococolaEntry.insert(0,0)
    maazaEntry.insert(0,0)


    cosmeticstaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    drinkstaxEntry.delete(0,END)


    cosmeticspriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    drinkspriceEntry.delete(0,END)


    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)


    textarea.delete(1.0,END)







def send_email():

    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderEntry.get(),passwordEntry.get())
            message=email_textarea.get(1.0,END)
            # reciever_address=recieverEntry.get()
            ob.sendmail(senderEntry.get(),recieverEntry.get(),message)
            ob.quit()
            messagebox.showinfo('success', 'Bill is Successfully Send')
        except:
            messagebox.showerror('Error', 'Something went wrong, please try again',parent=root1)
            root1.destroy()
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('SEND GMAIL')
        root1.config(bg='gray20')
        root1.resizable(0,0)
        senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        senderLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bg='gray20',fg='white')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)


        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)


        passwordLabel=Label(senderFrame,text="Password",font=('arial',14,'bold'),bg='gray20',fg='white')
        passwordLabel.grid(row=1,column=0,padx=10,pady=8)


        passwordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
        passwordEntry.grid(row=1,column=1,padx=10,pady=8)



        recipientFrame=LabelFrame(root1,text='RECIPIENT',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        recipientFrame.grid(row=1,column=0,padx=40,pady=20)



        recieverLabel=Label(recipientFrame,text="Email Address",font=('arial',14,'bold'),bg='gray20',fg='white')
        recieverLabel.grid(row=0,column=0,padx=10,pady=8)


        recieverEntry=Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        recieverEntry.grid(row=0,column=1,padx=10,pady=8)



        messageLabel=Label(recipientFrame,text="Message",font=('arial',14,'bold'),bg='gray20',fg='white')
        messageLabel.grid(row=1,column=0,padx=10,pady=8)



        email_textarea=Text(recipientFrame, font=('arial', 14, 'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))




        sendButton=Button(root1,text='SEND', font=('arial', 16, 'bold'),width=15,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=20)








        root1.mainloop()



def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0, END))
        os.startfile(file,'print')




def search_bill():
    for i in os.listdir('bills/'):
        
        if i.split(' .')[0] == billnumberEntry.get():
            f = open(f'bills/{i}', 'r')
            textarea.delete('1.0', END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')



if not os.path.exists('bills'):
    os.mkdir('bills')




def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you Want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber} .txt','w')  
        # .pdf is used for your choise
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f' Bill number {billnumber} is saved successfully')
        billnumber = random.randint(500,15000)

billnumber=random.randint(500,15000)


def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details Are Required')
    elif cosmeticspriceEntry.get()=='' or grocerypriceEntry.get()=='' or drinkspriceEntry.get()=='':
         messagebox.showerror('Error','No Product are Selected')
    elif cosmeticspriceEntry.get()=='0 Rs' and grocerypriceEntry.get()=='0 Rs' and drinkspriceEntry.get()=='0 Rs':
        messagebox.showerror('Error','No Product are Selected')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t**WELCOME CUSTOMER**\n')
        textarea.insert(END,f'\nBill Number:{billnumber}\n')
        textarea.insert(END,f'\nCustomer Name:{nameEntry.get()}\n')
        textarea.insert(END,f'\nCustomer Phone Number:{phoneEntry.get()}\n')
        textarea.insert(END,'\n=======================================================')
        textarea.insert(END,f'\nProduct\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END,'\n=======================================================')
        if bathsoapEntry.get()!='0':
            textarea.insert(END,f'\nBath Soap \t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs')
        if facecreamEntry.get()!='0':
            textarea.insert(END,f'\nFace Cream \t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs')
        if facewashEntry.get()!='0':
            textarea.insert(END,f'\nFace Wash \t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs')
        if hairsprayEntry.get()!='0':
            textarea.insert(END,f'\nHair Spray \t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs')
        if hairgelEntry.get()!='0':
            textarea.insert(END,f'\nHair Gel \t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs')
        if bodylotionEntry.get()!='0':
            textarea.insert(END,f'\nBody Lotion \t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Rs')
    


        if riceEntry.get()!='0':
            textarea.insert(END,f'\nRice \t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs')

        if oilEntry.get()!='0':
            textarea.insert(END,f'\nOil \t\t\t{oilEntry.get()}\t\t\t{oilprice } Rs')

        if daalEntry.get()!='0':
            textarea.insert(END,f'\nDaal\t\t\t{daalEntry.get()}\t\t\t{daalprice} Rs')

        if wheatEntry.get()!='0':
            textarea.insert(END,f'\nWheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rs')

        if sugarEntry.get()!='0':
            textarea.insert(END,f'\nSugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Rs')

        if teaEntry.get()!='0':
            textarea.insert(END,f'\nTea \t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs')




        if maazaEntry.get()!='0':
            textarea.insert(END,f'\nMaaza \t\t\t{maazaEntry.get()}\t\t\t{maazaprice} Rs')
        

        if pepsiEntry.get()!='0':
            textarea.insert(END,f'\nPepsi \t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Rs')
        

        if spriteEntry.get()!='0':
            textarea.insert(END,f'\nSprite \t\t\t{spriteEntry.get()}\t\t\t{spriteprice} Rs')

        if dewEntry.get()!='0':
            textarea.insert(END,f'\nDew \t\t\t{dewEntry.get()}\t\t\t{dewprice} Rs')

        if frootiEntry.get()!='0':
            textarea.insert(END,f'\nFrooti \t\t\t{frootiEntry.get()}\t\t\t{frootiprice} Rs')

        if cococolaEntry.get()!='0':
            textarea.insert(END,f'\nCoco Cola \t\t\t{cococolaEntry.get()}\t\t\t{cococolaprice} Rs')

        textarea.insert(END,'\n-------------------------------------------------------')
                            
        if cosmeticstaxEntry.get()!='0.0Rs':
            textarea.insert(END,f'\nCosmetic Tax\t\t\t\t{cosmeticstaxEntry.get()}')

        if grocerytaxEntry.get()!='0.0Rs':
            textarea.insert(END,f'\nGrocery Tax\t\t\t\t{grocerytaxEntry.get()}')

        if drinkstaxEntry.get()!='0.0Rs':
            textarea.insert(END,f'\nDrink Tax\t\t\t\t{drinkstaxEntry.get()}')
        textarea.insert(END,'\n-------------------------------------------------------')

        textarea.insert(END,f'\n\nTotal Bill \t\t\t\t {totalbill}')

        textarea.insert(END,'\n-------------------------------------------------------')

        textarea.insert(END,'\t\t\t**THANKYOU VISIT AGAIN**\n')

        save_bill()




def total():
    global soapprice,facecreamprice,facewashprice,hairsprayprice,hairgelprice,bodylotionprice
    global riceprice,oilprice,daalprice,wheatprice,sugarprice,teaprice
    global maazaprice,pepsiprice,spriteprice,dewprice,frootiprice,cococolaprice
    global totalbill
    #cosmetics price calculation
    soapprice=int(bathsoapEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*50
    facewashprice=int(facewashEntry.get())*100
    hairsprayprice=int(hairsprayEntry.get())*150
    hairgelprice=int(hairgelEntry.get())*80
    bodylotionprice=int(bodylotionEntry.get())*60

    totalcosmeticprice=soapprice+facewashprice+facecreamprice+hairgelprice+hairsprayprice+bodylotionprice
    cosmeticspriceEntry.delete(0,END)
    cosmeticspriceEntry.insert(0,f'{totalcosmeticprice} Rs')
    cosmeticstax=totalcosmeticprice*0.12
    cosmeticstaxEntry.delete(0,END)
    cosmeticstaxEntry.insert(0,str(cosmeticstax)+ 'Rs')
    

    #grocery price calculation
    
    riceprice=int(riceEntry.get())*200
    oilprice=int(oilEntry.get())*150
    daalprice=int(daalEntry.get())*110 
    wheatprice=int(wheatEntry.get())*25
    sugarprice=int(sugarEntry.get())*45
    teaprice=int(teaEntry.get())*55

    totalgroceryprice=riceprice+oilprice+daalprice+wheatprice+sugarprice+teaprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,f'{totalgroceryprice} Rs')

    grocerytax=totalgroceryprice*0.05
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,str( grocerytax)+ 'Rs')

 
    #drinks price colculation
    maazaprice=int(maazaEntry.get())*90   
    pepsiprice=int(pepsiEntry.get())*90  
    spriteprice=int(spriteEntry.get())*95
    dewprice=int(dewEntry.get())*85
    frootiprice=int(frootiEntry.get())*80   
    cococolaprice=int(cococolaEntry.get())*95

    totaldrinksprice= maazaprice+pepsiprice+spriteprice+dewprice+frootiprice+cococolaprice
    drinkspriceEntry.delete(0,END)
    drinkspriceEntry.insert(0,f'{totaldrinksprice} Rs')

    drinkstax=totaldrinksprice*0.08
    drinkstaxEntry.delete(0,END)
    drinkstaxEntry.insert(0,str( drinkstax) + 'Rs')

    totalbill=totalcosmeticprice+totalgroceryprice+totaldrinksprice+cosmeticstax+grocerytax+drinkstax





#GUI part

#header sections start
root=Tk()
root.title('Billing System')
root.geometry('1270x685')
root.iconbitmap('icon.ico')
headingLabel=Label(root,text='BILLING SYSTEM',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

#header sections end

# customer details start

customer_details_frame=LabelFrame(root,text='Customer Deatils',font=('times new roman',15,'bold'),fg='gold',bd=12,relief=GROOVE,bg='gray20')
customer_details_frame.pack(fill=X)

#Name Label start

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='gray20',fg='white')
nameLabel.grid(row=0,column=0,padx=20,pady=2)


nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

#Name Label end



#Phone Label start
phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=20)


phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

#Phone Label end


#Bill number Label start

billnumberLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)


billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

#Bill number Label end
# customer details end

#button class start
searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)

#button class end


#products Frame section start

productsFrame=Frame(root)
productsFrame.pack()


#cosmeticsFrame sections start

cosmeticsFrame=LabelFrame(productsFrame,text='cosmetics',font=('times new roman',15,'bold'),fg='gold',bd=12,relief=GROOVE,bg='gray20')
cosmeticsFrame.grid(row=0,column=0)


bathsoapLabel=Label(cosmeticsFrame,text='Bath Soap',font=('times new roman',15,'bold'),bg='gray20',fg='white')

bathsoapLabel.grid(row=0,column=0,pady=9,padx=10)

bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,padx=10)
bathsoapEntry.insert(0,0)



facecreamLabel=Label(cosmeticsFrame,text='Face Cream',font=('times new roman',15,'bold'),bg='gray20',fg='white')

facecreamLabel.grid(row=1,column=0,pady=9,padx=10)

facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,padx=10)
facecreamEntry.insert(0,0)




facewashLabel=Label(cosmeticsFrame,text='Face Wash',font=('times new roman',15,'bold'),bg='gray20',fg='white')

facewashLabel.grid(row=2,column=0,pady=9,padx=10)

facewashEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,padx=10)
facewashEntry.insert(0,0)



hairsprayLabel=Label(cosmeticsFrame,text='Hair Spray',font=('times new roman',15,'bold'),bg='gray20',fg='white')

hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

hairsprayEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,padx=10)
hairsprayEntry.insert(0,0)



hairgelLabel=Label(cosmeticsFrame,text='Hair Gel',font=('times new roman',15,'bold'),bg='gray20',fg='white')

hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

hairgelEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,padx=10)
hairgelEntry.insert(0,0)




bodylotionLabel=Label(cosmeticsFrame,text='Body Lotion',font=('times new roman',15,'bold'),bg='gray20',fg='white')

bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,padx=10)
bodylotionEntry.insert(0,0)


#cosmeticsFrame sections end



#groceryFrame sections start

groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),fg='gold',bd=12,relief=GROOVE,bg='gray20')
groceryFrame.grid(row=0,column=1)


riceLabel=Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),bg='gray20',fg='white')

riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

riceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,padx=10)
riceEntry.insert(0,0)



oilLabel=Label(groceryFrame,text='Oil',font=('times new roman',15,'bold'),bg='gray20',fg='white')

oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

oilEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,padx=10)
oilEntry.insert(0,0)



daalLabel=Label(groceryFrame,text='Daal',font=('times new roman',15,'bold'),bg='gray20',fg='white')

daalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

daalEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
daalEntry.grid(row=2,column=1,padx=10)
daalEntry.insert(0,0)



wheatLabel=Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold'),bg='gray20',fg='white')

wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

wheatEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
wheatEntry.grid(row=3,column=1,padx=10)
wheatEntry.insert(0,0)




sugarLabel=Label(groceryFrame,text='Sugar',font=('times new roman',15,'bold'),bg='gray20',fg='white')

sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

sugarEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sugarEntry.grid(row=4,column=1,padx=10)
sugarEntry.insert(0,0)


teaLabel=Label(groceryFrame,text='Tea',font=('times new roman',15,'bold'),bg='gray20',fg='white')

teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

teaEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
teaEntry.grid(row=5,column=1,padx=10)
teaEntry.insert(0,0)


#groceryFrame sections end




#drinksFrame sections start

drinksFrame=LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',15,'bold'),fg='gold',bd=12,relief=GROOVE,bg='gray20')
drinksFrame.grid(row=0,column=2)


maazaLabel=Label(drinksFrame,text='Maaza',font=('times new roman',15,'bold'),bg='gray20',fg='white')

maazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

maazaEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
maazaEntry.grid(row=0,column=2,padx=10)
maazaEntry.insert(0,0)



pepsiLabel=Label(drinksFrame,text='Pepsi',font=('times new roman',15,'bold'),bg='gray20',fg='white')

pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

pepsiEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=1,column=2,padx=10)
pepsiEntry.insert(0,0)


spriteLabel=Label(drinksFrame,text='Sprite',font=('times new roman',15,'bold'),bg='gray20',fg='white')

spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

spriteEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=2,column=2,padx=10)
spriteEntry.insert(0,0)





dewLabel=Label(drinksFrame,text='Dew',font=('times new roman',15,'bold'),bg='gray20',fg='white')

dewLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

dewEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
dewEntry.grid(row=3,column=2,padx=10)
dewEntry.insert(0,0)





frootiLabel=Label(drinksFrame,text='Frooti',font=('times new roman',15,'bold'),bg='gray20',fg='white')

frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

frootiEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
frootiEntry.grid(row=4,column=2,padx=10)
frootiEntry.insert(0,0)




cococolaLabel=Label(drinksFrame,text='Coco Cola',font=('times new roman',15,'bold'),bg='gray20',fg='white')

cococolaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

cococolaEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cococolaEntry.grid(row=5,column=2,padx=10)
cococolaEntry.insert(0,0)

#drinksFrame sections end



#products Frame section end

#billframe section start

billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)



billareaLabel=Label(billframe,text='Bill Area',font=('times new roman',15,'bold'),bd=8,relief=GROOVE)
billareaLabel.pack(fill=X)

#VERTICAL view of text area 

Scrollbar=Scrollbar(billframe,orient=VERTICAL)
Scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=16,width=55,yscrollcommand=Scrollbar.set)
textarea.pack()

#Scrollbar config

Scrollbar.config(command=textarea.yview)
#billframe section start





billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),fg='gold',bd=12,relief=GROOVE,bg='gray20')
billmenuFrame.pack()


cosmeticspriceLabel=Label(billmenuFrame,text='Cosmetic Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')

cosmeticspriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')

cosmeticspriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cosmeticspriceEntry.grid(row=0,column=1,padx=10,pady=6)



grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')

grocerypriceLabel.grid(row=1,column=0,pady=6,padx=10,sticky='w')

grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,padx=10,pady=6)


drinkspriceLabel=Label(billmenuFrame,text='Cold Drink Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')

drinkspriceLabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')

drinkspriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
drinkspriceEntry.grid(row=2,column=1,padx=10,pady=6)






cosmeticstaxLabel=Label(billmenuFrame,text='Cosmetic Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')

cosmeticstaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')

cosmeticstaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cosmeticstaxEntry.grid(row=0,column=3,padx=10,pady=6)



grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')

grocerytaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')

grocerytaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,padx=10,pady=6)


drinkstaxLabel=Label(billmenuFrame,text='Cold Drink Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')

drinkstaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')

drinkstaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
drinkstaxEntry.grid(row=2,column=3,padx=10,pady=6)






buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)


totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)


billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=5)


printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=5)




clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)




root.mainloop()