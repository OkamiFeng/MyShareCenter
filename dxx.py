'''
    before use this, please run the follow commands:
        pip install webdav4
        pip install pyperclip
'''

from webdav4.client import Client
import pyperclip

file = 'task1.txt'
client = Client('http://124.221.230.134/dav', auth=("dxxhkbs@163.com","VKxD5WAdbYoj3OyK50YIbnjLLvDstG7n"))

def upload():
    content = pyperclip.paste()
    with open(file, 'w') as f:
        f.write(content)

    if client.exists(file):
        print('exsit')
        return
    client.upload_file(file, file)

def download():
    file1 = "a_" + file
    if not client.exists(file1):
        print('not exsit')
        return
    client.download_file(file1, file1)

    with open(file1, 'r') as f:
        content = f.read()
    pyperclip.copy(content)

# upload() # use this to upload your clipboard
# download() # use this to write your clipboard