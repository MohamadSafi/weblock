import time
from datetime import datetime as dt


#change the host path as u want
host_path = "/etc/hosts"
redirect = "127.0.0.1"
wepsite_list = ["www.facebook.com", "www.example.com"]

while True:
    if dt(dt.now().year,
          dt.now().month,
          dt.now().day, 8) < dt(dt.now().year,
                                dt.now().month,
                                dt.now().day,7):
        with open(host_path, 'r+') as file:
            lines = file.read()
            for website in wepsite_list:
                if website in lines:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        lines=[]
        with open(host_path, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            content=file.read()
            n_sites = len(wepsite_list)
            if wepsite_list[0] in content:
                for n in range(0,n_sites):
                    lines.pop()
                
        with open(host_path, 'w') as file:
            for line in lines:
                file.write(line)
        

    time.sleep(5)
