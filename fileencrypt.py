  
#Coded By Kral4, BBOD | https://github.com/rootkral4 | https://github.com/1nnr3d
#Educational Purposes Only
#https://github.com/rootkral4/fileencrypt/blob/main/LICENSE

# You should have received a copy of the MIT License
# along with this program.  If not, see <https://github.com/rootkral4/fileencrypt/blob/main/LICENSE>.

import sys
import time
import codecs
from termcolor import colored
from cryptography.fernet import Fernet

print(colored("\n**********************KRAL4**********************\n","cyan"))

if sys.argv[1] == "-h":
    print(colored("Usage :fileencrypt.py FILEPATH OUTPUTPATH ARG\n-d : Decryption mode\npython3 fileencrypt.py secretimage.png secretimage.encpng\npython3 fileencrypt.py secretimage.encpng secretimage.png -d key.key","magenta"))
    sys.exit(0)

try:
    filedest = sys.argv[1]
    outputpath = sys.argv[2]
except IndexError:
    print(colored("Usage :fileencrypt.py FILEPATH OUTPUTPATH ARG\n-d : Decryption mode","magenta"))
    sys.exit(1)
    
try:
    if sys.argv[3] == "-d":
        isdecrypt = "yes"
        keypath = sys.argv[4]
    else:
        print(colored("Usage :fileencrypt.py FILEPATH OUTPUTPATH -d KEYPATH","magenta"))
        sys.exit(1)
except IndexError:
    isdecrypt = "no"
    pass
    
if isdecrypt == "yes":
    try:
        with codecs.open(keypath, 'rb', encoding='utf-8') as f:
            deckey = f.read()
    except FileNotFoundError:
        print(colored("[!]No Such File {}","red").format(keypath))
        sys.exit(1)
    try:
        fernetcrypt = Fernet(deckey)
    except ValueError:
        print(colored("Fernet key must be 32 url-safe base64-encoded bytes.","red"))
        sys.exit(1)
    print(colored("[i]Key :{}","green").format(deckey))
else:
    print(colored("[i]Generating Key","blue"))
    key = Fernet.generate_key()
    keypath = input(colored("[?]Path To Save Key e.g. Desktop/enc.key:","yellow"))
    with codecs.open(keypath, 'wb', encoding='utf-8') as f:
        f.write(key.decode())
    print(colored("[!]Key Saved {} :{}","green").format(keypath,key.decode()))
    fernetcrypt = Fernet(key)
    


print(colored("[i]Reading File {}","blue").format(filedest))

try:
    f = open(filedest, 'rb')
    getdata = f.read()
    f.close()
except FileNotFoundError:
    print(colored("[!]No Such File","red"))
    sys.exit(1)

print(colored("[i]File {} Read Ok","cyan").format(filedest))

if isdecrypt == "no":
    f = open(outputpath,"wb")
    f.write(fernetcrypt.encrypt(getdata))
    f.close()
    print(colored("[!]Done!","green"))
else:
    f = open(outputpath,"wb")
    f.write(fernetcrypt.decrypt(getdata))
    f.close()
    print(colored("[!]Done!","green"))

