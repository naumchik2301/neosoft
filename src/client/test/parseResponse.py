'''
Created on 2016. gada 22. marts

@author: olegs.naumenko
'''
import io

responseBody = '''
POST /getAgent HTTP/1.1
Accept-Encoding: identity
User-Agent: Python-urllib/3.4
Host: dci1-pbi-001:8888
Content-Length: 42
Connection: close
Content-Type: application/x-www-form-urlencoded

    HTTP/1.1 200 OK
    Hello, World!

'''

if __name__ == '__main__':
    buf = io.StringIO(responseBody)
    for response_line in buf.readlines():
        print (response_line)
        if response_line.startswith('POST'):
            print(response_line.split(' ')[1])
            print ('POST')
        if response_line.startswith('GET'):            
            print ('GET') 
