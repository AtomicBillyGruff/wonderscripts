import os

#looks for pods kubernettes
if __name__ == '__main__':
    ip = '10.10.11.113'
    port = '10250'

    os.system(str('curl https://{}:{}/pods -k'.format(ip, port)))
