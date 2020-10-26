from cryptography.fernet import Fernet
import codecs

def decrypT(outputfile, decfile, keypath):
    with codecs.open(keypath, "rb") as f:
        key = f.read()
    fernetcrypt = Fernet(key)
    with codecs.open(decfile, "rb") as f:
        data = f.read()
    data = fernetcrypt.decrypt(data)
    with codecs.open(outputfile, "wb") as f:
        f.write(data)
