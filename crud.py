from hasher import decode_password, encode_password, hash_master_password
import elara
from stdiomask import getpass

def new_password(db):
    
    website = input("Web y usuario para añadir : ")
    password = getpass(prompt = "Introduce nueva contraseña - ", mask = '*')
    db.set(website, encode_password(password))
    print("Contraseña añadida correctamente.")
    return db


def view_password(db):
    print("Web y usuario :")
    keys = db.getkeys()
    keys.remove("Masterpassword")
    len_keys = len(keys)
    j = 1
    for i in keys:
        print(j, ". ", i)
        j+=1
        
    index = int(input("Introduce el número deseado - "))
    if index>0 and index<=len(keys): 
        print("Contraseña - ",decode_password(db.get(keys[index-1])))

    
def delete_password(db):
    print("Web y usuario que desees eliminar: ")
    keys = db.getkeys()
    keys.remove("Masterpassword")
    len_keys = len(keys)
    j = 1
    for i in keys:
        print(j, ". ", i)
        j+=1
    
    index = int(input("Introduce el número correspondiente- "))
    verify_master_password_unhashed = getpass(prompt = "Contraseña maestra para proseguir - ", mask = '*')
    verify_master_password = hash_master_password(verify_master_password_unhashed)
    if verify_master_password == db.get("Masterpassword"):
        if index>0 and index<=len(keys):
            db.rem(keys[index-1])
            # Del website and password from dict
            print("Contraseña borrada.")
    else:
        print("Fallo de autentificación, contraseña no borrada.")

    return db

def update_password(db):
    print("Web y usuario :")
    keys = db.getkeys()
    keys.remove("Masterpassword")
    len_keys = len(keys)
    j = 1
    for i in keys:
        print(j, ". ", i)
        j+=1
    
    index = int(input("Introduce el número correspondiente- "))
    verify_master_password_unhashed = getpass(prompt = "Contraseña maestra para proseguir - ", mask = '*')
    verify_master_password = hash_master_password(verify_master_password_unhashed)
    if verify_master_password == db.get("Masterpassword"):
        if index>0 and index<=len(keys):
            newpass = getpass(prompt = "Nueva contraseña - ", mask = '*')
            db.set(keys[index-1], encode_password(newpass))
            print("Ha sido actualizada correctamente.")
            
        else:
            print("Fallo de autentificación, contraseña no actualizada.")

    return db