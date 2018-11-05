#Contains code for Ceaser Cipher 
def encryption(str1,key):
    l1=[]
    for i in range(len(str1)):
        a=chr((ord(str1[i])+(key-97))%26+97)
        l1.append(a)
    en=(''.join(l1))
    print ("The encrypted key is",en)


def decryption(en,key):
    l2=[]
    for j in range(len(en)):
        new=chr((ord(en[j])-(key-97))%26+97)
        l2.append(new)
        
    dn=(''.join(l2))
    print ("The decrypted key is",dn)


print ("!!!!!Welcome!!!!!!!")
print ("-----------------------------------------")
while True:
    print ("Press 1 for Encryption\nPress 2 for Decryption\nPress 3 for exit")
    choice=int(input("Enter your choice"))
    if choice==1:
        str1=input("Enter string you want to encrypt")
        key=int(input("Enter the key for the string"))
        encryption(str1,key)
        print ("------------------------------------------")
    elif choice==2:
            
        str1=input("Enter string you want to decrypt")
        key=int(input("Enter the key for the string"))
        decryption(str1,key)
        print("---------------------------------------------")
        
    elif choice==3:
        break
    
        

    
