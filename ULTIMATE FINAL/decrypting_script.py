
from cryptography.fernet import Fernet

def decrypt_fb():
    try:
        
        with open ("fb_count_file.txt","r+") as gg:
            p = gg.read()
    except IOError:
        print("ERROR...file not found!!")
        exit()
                
    for b in range(int(p)):
        try:
            
            file=open("key"+"fb"+str(b+1)+".key","rb+")
            key=file.read()
            file.close()
        except IOError:
            print("ERROR...file not found!!")
            break
            
        try:
            
            with open("Theft_data_fb"+(str(b+1))+'.txt.encrypted', 'rb+') as f:
                data = f.read()  
        except IOError:
            print("ERROR...file not found!!")
            break
            
        fernet = Fernet(key)

        decrypted = fernet.decrypt(data)
        print(decrypted)
        try:
            
            with open("fb_dec"+str(b+1)+".txt","a+") as fa:
                cv = decrypted.decode()
                fa.write(cv)
        except IOError:
            print("ERROR...file not found!!")
            
            

        
    



def decrypt_ins():
    try:
        
        with open ("ins_count_file.txt","r+") as gg:
            p = gg.read()
    except IOError:
            print("ERROR...file not found!!")
            exit()
    for b in range(int(p)):
        try:
            
            file=open("key"+"ins"+str(b+1)+".key","rb+")
            key=file.read()
            file.close()
        except IOError:
            print("ERROR...file not found!!")
            break
            
        try:
            
            with open("Theft_data_ins"+(str(b+1))+'.txt.encrypted', 'rb+') as f:
                data = f.read()
        except IOError:
            print("ERROR...file not found!!")
            break

        fernet = Fernet(key)

        decrypted = fernet.decrypt(data)
        print(decrypted)
        try:
            
            with open("ins_dec"+str(b+1)+".txt","a+") as fa:
                cv = decrypted.decode()
                fa.write(cv)
        except IOError:
            print("ERROR...file not found!!")
            


def decrypt_ofn():
    try:
        
        with open ("ofn_count_file.txt","r+") as gg:
            p = gg.read()
    except IOError:
            print("ERROR...file not found!!")
            exit()
    for b in range(int(p)):
        try:
            
            file=open("key"+"ofn"+str(b+1)+".key","rb+")
            key=file.read()
            file.close()
        except IOError:
            print("ERROR...file not found!!")
            break
        try:
            
            with open("Theft_data_ofn"+(str(b+1))+'.txt.encrypted', 'rb+') as f:
                data = f.read()
        except IOError:
            print("ERROR...file not found!!")
            break

        fernet = Fernet(key)

        decrypted = fernet.decrypt(data)
        print(decrypted)
        try:
            
            with open("ofn_dec"+str(b+1)+".txt","a+") as fa:
                cv = decrypted.decode()
                fa.write(cv)
        except IOError:
            print("ERROR...file not found!!")



def decrypt_sp():
    try:
        
        with open ("sp_count_file.txt","r+") as gg:
            p = gg.read()
    except IOError:
            print("ERROR...file not found!!")
            exit()
    for b in range(int(p)):
        try:
            
            file=open("key"+"sp"+str(b+1)+".key","rb+")
            key=file.read()
            file.close()
        except IOError:
            print("ERROR...file not found!!")
            break
        try:
            
            with open("Theft_data_sp"+(str(b+1))+'.txt.encrypted', 'rb+') as f:
                data = f.read()
        except IOError:
            print("ERROR...file not found!!")
            break

        fernet = Fernet(key)

        decrypted = fernet.decrypt(data)
        print(decrypted)

        try:
            
            with open("sp_dec"+str(b+1)+".txt","a+") as fa:
                cv = decrypted.decode()
                fa.write(cv)
        except IOError:
            print("ERROR...file not found!!")


def decrypt_lin():
    try:
        
        with open ("lin_count_file.txt","r+") as gg:
            p = gg.read()
    except IOError:
            print("ERROR...file not found!!")
            exit()
    for b in range(int(p)):
        try:
            
            file=open("key"+"lin"+str(b+1)+".key","rb+")
            key=file.read()
            file.close()
        except IOError:
            print("ERROR...file not found!!")
            break
        try:
            
            with open("Theft_data_lin"+(str(b+1))+'.txt.encrypted', 'rb+') as f:
                data = f.read()
        except IOError:
            print("ERROR...file not found!!")
            break

        fernet = Fernet(key)

        decrypted = fernet.decrypt(data)
        print(decrypted)

        try:
            
            with open("lin_dec"+str(b+1)+".txt","a+") as fa:
                cv = decrypted.decode()
                fa.write(cv)
        except IOError:
            print("ERROR...file not found!!")



def decrypt_tmb():
    try:
        
        with open ("tmb_count_file.txt","r+") as gg:
            p = gg.read()
    except IOError:
            print("ERROR...file not found!!")
            exit()
    for b in range(int(p)):
        try:
            
            file=open("key"+"tmb"+str(b+1)+".key","rb+")
            key=file.read()
            file.close()
        except IOError:
            print("ERROR...file not found!!")
            break
        try:
            
            with open("Theft_data_tmb"+(str(b+1))+'.txt.encrypted', 'rb+') as f:
                data = f.read()
        except IOError:
            print("ERROR...file not found!!")
            break

        fernet = Fernet(key)

        decrypted = fernet.decrypt(data)
        print(decrypted)

        try:
            
            with open("tmb_dec"+str(b+1)+".txt","a+") as fa:
                cv = decrypted.decode()
                fa.write(cv)
        except IOError:
            print("ERROR...file not found!!")

