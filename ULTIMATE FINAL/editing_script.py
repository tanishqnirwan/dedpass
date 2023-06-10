import os
def edit():

    a = "1) FACEBOOK  "
    b = "2) INSTAGRAM "
    c = "3) OnlyFans  "
    d = "4) SNAPCHAT  "
    e = "4) LINKDIN  "
    f = "4) TUMBLR  "
    


    print("\n\n\n                                                             + - - - - - - - -+")
    print("                                                              |  a) FACEBOOK   |")
    print("                                                              |                |")
    print("                                                              |  b) INSTAGRAM  |")
    print("                                                              |                |")
    print("                                                              |  c) OnlyFans   |")
    print("                                                              |                |")
    print("                                                              |  d) SNAPCHAT   |")
    print("                                                              |                |")
    print("                                                              |  e) LINKDIN    |")
    print("                                                              |                |")
    print("                                                              |  f) TUMBLR     |")
    print("                                                              + - - - - - - -  +")
    dat=[]
    enbld_mod_no = input("\n\nSELECT THE NUMBER OF  WEBSITES TO BE ENABLED IN THE MODULE :-")
    for enb in range(int(enbld_mod_no)): 
            enbld_mod = input("\n\nSELECT THE WEBSITE :- ")
            if enbld_mod == "a":
                    enbld_mod = a
            elif enbld_mod == "b":
                    enbld_mod = b
            elif enbld_mod == "c":
                    enbld_mod = c
            elif enbld_mod == "d":
                    enbld_mod = d
            elif enbld_mod == "e":
                    enbld_mod = e
            elif enbld_mod == "f":
                    enbld_mod = f
           
           
            
            dat.append(enbld_mod)
    try:
        os.remove("fb_count_file.txt")
        os.remove("ins_count_file.txt")
        os.remove("ofn_count_file.txt")
        os.remove("sp_count_file.txt")
        os.remove("lin_count_file.txt")
        os.remove("tmb_count_file.txt")
    except IOError:
        pass
    
                
                

    for skt in dat:
        if skt=="1) FACEBOOK  ":
           
            f=open("fb_count_file.txt","w+")
            z=str(1)
            f.write(z)
            f.close()


        elif skt=="2) INSTAGRAM ":
            
            f=open("ins_count_file.txt","w+")
            z=str(1)
            f.write(z)
            f.close()

        elif skt=="3) OnlyFans  ":
          
            f=open("ofn_count_file.txt","w+")
            z=str(1)
            f.write(z)
            f.close()

        elif skt=="4) SNAPCHAT  ":
            f=open("sp_count_file.txt","w+")
            z=str(1)
            f.write(z)
            f.close()

        elif skt=="5) LINKDIN  ":
            f=open("lin_count_file.txt","w+")
            z=str(1)
            f.write(z)
            f.close()

        elif skt=="4) TUMBLR  ":
            f=open("tmb_count_file.txt","w+")
            z=str(1)
            f.write(z)
            f.close()

   
                  
                  
                



 
    
    
















    
