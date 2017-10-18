import hashlib
import sys

# Need to run command sudo python -m pip install pysha3
# Run on terminal command line
#

def encrypt_avatarname(avatarname):
    '''

    :param avatarname: string
    :return: uppercase SHA-3 string

    Example:
    encrypt_avatarname("queen123")
    e9a5f8e9acbdbd74f9bc3aeb33ef7728204e7471682ff111915e2cc8

    '''
    enc_s = hashlib.sha256(avatarname.encode('utf-8')).hexdigest()
    return enc_s

def main():
    while True:
        avatarname = str(input('Enter avatarname: '))
        if (avatarname == "stop"):
            break
        encryptedname = encrypt_avatarname(avatarname)
        print (encryptedname)


if __name__ == "__main__":
    main()
