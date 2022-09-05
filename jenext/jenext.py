from config import Config
import nextcloud_client
import os
import hashlib

# check connection to server
try:
    nc = nextcloud_client.Client(Config.NEXTCLOUD_URL)

except:
    print(f"[Error]: Cannot connect to ({Config.NEXTCLOUD_URL}), Please check the url or network connection.")
    exit(2)

# connect with user/pass
try:
    nc.login(Config.NEXTCLOUD_USER, Config.NEXTCLOUD_PASS)
    print("[Info]: Client is connected")
except:
    print(f"[Error]: Could not login to Nextcloud server ({Config.NEXTCLOUD_URL}), Check user and password.")
    exit(3)

# check directory existance on nextcloud server
try:
    nc.list(Config.NEXTCLOUD_PATH)
except:
    print(f"[Error]: There is not ({Config.NEXTCLOUD_PATH}) directory on NextCloud, Please create or change it.")
    exit(4)

# check file existance on local system
try:
    os.path.exists(Config.FILE_PATH)
except:
    print(f"[Error]: File or Directory doesn't exist, Please check your path ({Config.FILE_PATH})")
    exit(5)


# delete old file
try:
    nc.delete(f"{Config.NEXTCLOUD_PATH}/{os.path.basename(Config.FILE_PATH)}.old")
    print(f"[Info]: the last version is deleted.")
except:
    pass

# rename remain file to .old
try:
    nc.move(f"{Config.NEXTCLOUD_PATH}/{os.path.basename(Config.FILE_PATH)}", f"{Config.NEXTCLOUD_PATH}/{os.path.basename(Config.FILE_PATH)}.old")
    print(f"[Info]: File is renamed to {os.path.basename(Config.FILE_PATH)}.old")
except:
    pass

# upload new file
try:
    nc.put_file(f"{Config.NEXTCLOUD_PATH}/{os.path.basename(Config.FILE_PATH)}", Config.FILE_PATH)
    print("[Info]: File is uploaded successfully.")
except:
    print(f"[Error]: Failed to upload your file, Try again later.")
    exit(6)

print("[Info]: checking file checksum...")

LOCAL_FILE_MD5 = hashlib.md5(open(Config.FILE_PATH,'rb').read()).hexdigest()

# get uploaded file again to check md5
try:
    nc.get_file(f"{Config.NEXTCLOUD_PATH}/{os.path.basename(Config.FILE_PATH)}", '/tmp/uploaded')    
    REMOTE_FILE_MD5 = hashlib.md5(open('/tmp/uploaded','rb').read()).hexdigest()
except:
    print(f"[Info]: Couldn't check the MD5")
    exit(7)

# compare md5s
if LOCAL_FILE_MD5 == REMOTE_FILE_MD5:
    print(f"[Info]: file's checksum is ok.")
    os.remove("/tmp/uploaded") 
else:
    print(f"[Error]: Upload it again.")
    os.remove("/tmp/uploaded") 
    exit(10)



