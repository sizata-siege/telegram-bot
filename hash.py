import hashlib

def encoder_md5(password):
    md5 = hashlib.md5(password.encode('utf-8')).hexdigest()
    return md5

def encoder_sha384(password):
    sha = hashlib.sha512(password.encode('utf-8')).hexdigest()
    return sha

def encoder_sha1(password):
    sha = hashlib.sha1(password.encode('utf-8')).hexdigest()
    return sha
# pss = "1234"

# sha384 = hashlib.sha384(pss.encode('utf-8')).hexdigest()

# print(pss)
# print(pss.encode('utf-8'))
# print(pss.encode('utf-8').hex())
# print(sha384)

f = open("data1.csv")

def check():
    for line in f:
        for i in range(0, 10000):
            tmp_pass = str.format("%04d"%i)
            tmp_hash = line.split(",")
            if encoder_md5(tmp_pass) == tmp_hash[1].strip():
                print("pass of %s is %s" %(tmp_hash[0], tmp_pass))

# check()
text = "Amirhosseyn Shakeri"
# print(encoder_sha384(text))
print(encoder_sha1(text))
# print(len(text))