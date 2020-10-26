from cryptography.fernet import Fernet
import codecs

def encrypT(outputpath, getdata, keypath):
    key = Fernet.generate_key()
    fernetcrypt = Fernet(key)
    f = codecs.open(outputpath, "wb", encoding="utf-8")
    f.write(fernetcrypt.encrypt(getdata))
    f.close()
    with codecs.open(keypath, 'wb', encoding='utf-8') as f:
        f.write(key.decode())
