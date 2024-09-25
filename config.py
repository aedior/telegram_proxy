#import package
import os


#input vps 
# user = input("server username-->")
# ip = input("server ip-->")

# #try connect vps
# try:
#     os.system(f"ssh {user}@{ip}")
# except:
#     print("cant connect the server")
#     exit()

#installing curl
os.system("sudo apt update")
os.system("sudo apt install git curl -y")
os.system("git clone https://github.com/TelegramMessenger/MTProxy")
os.system('cd ./MTProxy')
os.system("make")



#building secret key
os.system("head -c 16 /dev/urandom | xxd -ps")

print("pleas copy your secret key")


#get telegram servers
os.system("curl -s https://core.telegram.org/getProxyConfig -o proxy-config")
os.system("curl -s https://core.telegram.org/getProxySecret -o proxy-secret")


#start proxy
secretkey = input("pleas enter your secret key-->")
port = input("pleas enter port(defualt'8888')")
os.system(f"./objs/bin/mtproto-proxy -u nobody -p {port} -H 443 -S {secretkey} --aes-pwd proxy-secret proxy-config -M 1")


#for auto start proxy
os.system(f"echo '@reboot root cd /root/MTProxy && ./objs/bin/mtproto-proxy -u nobody -p {port} -H 443 -S {secretkey} --aes-pwd proxy-secret proxy-config -M 1' | sudo tee -a /etc/crontab")


#add sponser channel

chooice = input("do you want add sponser channel?(Y/n)")
choi = chooice.upper()
if choi == "N":
    exit
sponser = input("pleas enter sponser link-->")
os.system(f"./objs/bin/mtproto-proxy -u nobody -p {port} -H 443 -S {secretkey} --aes-pwd proxy-secret proxy-config -M 1 --advertise-for-telegram {sponser}")

#copy proxy link
print("your proxy link pleas copy and save it.")
