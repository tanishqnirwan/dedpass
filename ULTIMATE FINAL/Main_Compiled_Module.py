from admin_script import *
from user_script import *
import stdiomask



print(" \n\n\n\n                                                              **************<< White Hat Bois >>*************")
print("\n\n\n                                                  -----------<CREDENTIAL PHISHING CUM ENCRYPTING MODULE..v1.92>-----------  ")



def us_mm():
    
    print("\n\n\n                                                                               1) ADMIN   ")
    print("\n\n                                                                               2) EMPLOYEE") 



    main_chk=input("\n\n\nSELECT USER MODE :- ")  
    if main_chk == "1":
        admin_pas=stdiomask.getpass(prompt="ENTER PASSWORD TO GAIN ADMIN CONTROL :-")
        
        if admin_pas=="whitehatbois@123":
            print("\n.\n.\n.\n.\n.\n ACCESS GRANTED...")
            admin()
    elif main_chk == "2":
        user()
        
us_mm()

