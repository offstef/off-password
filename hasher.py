import base64
import hashlib
import elara


def get_master_password_hash():
    db = elara.exe_secure("data.db", True)
    return db.get("Masterpassword")


def encode_password(password):
    password_ascii = password.encode("utf-8")
    
    base64_bytes = base64.b64encode(password_ascii)
    base64_string = base64_bytes.decode("utf-8")
    
    concatenated_password = base64_string + get_master_password_hash()
    concatenated_password_ascii = concatenated_password.encode("utf-8")
    
    base64_bytes_concat = base64.b64encode(concatenated_password_ascii)
    base64_string_concat = base64_bytes_concat.decode("utf-8")

    return base64_string_concat


def decode_password(base64_string_concat):
    base64_bytes_concat = base64_string_concat.encode("utf-8")
    
    concatenated_password_ascii = base64.b64decode(base64_bytes_concat)
    password = concatenated_password_ascii.decode("utf-8")
    
    mod_password = password[:-64]
    
    base64_bytes = mod_password.encode("utf-8")

def hash_master_password(master_password):
    encode_master_password_ascii = master_password.encode("utf-8")
    base64_bytes = base64.b64encode(encode_master_password_ascii)
    encode_master_password = base64_bytes.decode("utf-8")
    
    result = hashlib.sha256(encode_master_password.encode())

    # returning the equivalent hexadecimal value.
    hex_result = result.hexdigest()
    return hex_result
