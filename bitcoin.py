import re
import requests

# Copyright (c) 2020 Fernando
# Url: https://github.com/dlfernando/
# License: MIT

# This script monitors bitcoin transaction status using its hash ID and informs if transaction was already completed or not.

hashID = "6f4034e65e69b02d029fda5404c087156e8a896857ef74c92d35a61441e8cf07"

def main():
    try:
        html = requests.get("https://live.blockcypher.com/btc/tx/"+hashID+"/")
        found = re.search('<strong>(.*?)</strong> confirmations.', html.text)
        if found is None:
            print("No status available")
        else:
            status = int(found.group(1).replace('.','').replace(',',''))
            if(status>5):
                print("Bitcoin transaction COMPLETED! " + str(status))
                print("Hash ID: " + hashID)
            else:
                print("Bitcoin transaction NOT completed yet.")
    except:
        print("Error: can not execute script.")         
    
if __name__ == "__main__":


    main()

