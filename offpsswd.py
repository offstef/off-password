# Gestor de contraseñas
from stdiomask import getpass
import json
import elara
import hashlib
import pyfiglet

from hasher import decode_password, encode_password, hash_master_password
from crud import new_password, view_password, delete_password, update_password


def set_master_password():
    master_password = getpass(prompt = "Establece la contraseña maestra - ", mask = '*')
    return hash_master_password(master_password)



def intialise_db():
    db = elara.exe_secure("data.db", True)
    
    if not db.exists("Masterpassword"):
        db.set("Masterpassword", set_master_password())
    return db



def main():
    db = intialise_db()
    verify_master_password_unhashed = getpass(prompt = "Introduce la contraseña maestra - ", mask = '*' )
    verify_master_password = hash_master_password(verify_master_password_unhashed)
    if verify_master_password == db.get("Masterpassword"): 
        ascii_banner = pyfiglet.figlet_format("OFF//", font="big")
        print(ascii_banner)
        while(1):
            print(" ")
            print("1. Agregar contraseña")
            print("2. Ver contraseña")
            print("3. Borrar contraseña") 
            print("4. Actualizar contraseña") 
            print("5. Exit ")
            print(" ")

            choice = int(input("Escoge una opción - "))
            if choice == 1:
                db = new_password(db)
            elif choice == 2:
                view_password(db)
            elif choice == 3:
                db = delete_password(db)
            elif choice == 4:
                db = update_password(db)
            elif choice == 5:
                print(" ")
                print("Gracias por usar este gestor")
                break
            else:
                print("Vuelve a intentarlo")

            
    else:
        print("Fallo en las credenciales.")

main()