import os
import requests
from sys import *
from urllib.parse import urlparse

def is_downloadable(url):
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')

    if 'text' in content_type.lower():
        return False

    if 'html' in content_type.lower():
        return False

    return True

def get_filename_from_cd(cd):
    a = urlparse(cd)
    return os.path.basename(a.path)

def MarvellousDownload(url):
    allowed = is_downloadable(url)

    if allowed:
       try:
            res = requests.get(url, allow_redirects=True)
            filename = get_filename_from_cd(url)
            fd = open(filename, "wb")
            for buffer in res.iter_content(1024):
                fd.write(buffer)

            fd.close()
            return True

       except Exception as E:
            return False

    else:
        return False

def main():
    print("Marvellous Infosystems by Piyush Khairnar")

    print("Application name : " +argv[0])

    if (len(argv)) == 2:
        if (argv[1]=="-h" ) or (argv[1] == "-H"):
            print("This Script is used to download file")
            exit()

        if (argv[1]=="-u" ) or (argv[1] == "-U"):
            print("Usage:DownloadFile")
            exit()
    


    url='https://images.rawpixel.com/image_png_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcm0zNTUtcGYtczczLWNhcmQtbGFwdG9wLTAxLnBuZw.png'
    result=MarvellousDownload(url)

    if result:
        print("File succesfully downloaded")
    else:
        print("Failed to download")


if __name__=="__main__":
    main()
        


    

 