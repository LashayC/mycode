#!/usr/bin/python3

import numpy as np # number operations
import yaml # pyyaml for yaml
import re  # regex
import paramiko # ssh into servers
from flask import Flask, render_template
import matplotlib.pyplot as plt

def sshlogin(ip, un, passw):
    # creates session
    sshsession = paramiko.SSHClient()
    # auto adds ssh connections so they don't ask if you want to connect everytime
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # what session connects with
    sshsession.connect(hostname=ip, username=un, password=passw)
    # takes all info that is printed to terminal, log, and error log network device
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command("cat /proc/uptime")
    #decodes incoming terminal output from bytes
    sshresult = ssh_stdout.read().decode('utf-8').split()[0]
    
    # write results to file
    with open("sshresult", "w") as myfile:
        myfile.write(sshresult)

    # convert uptime in sec to days
    days = (int(float(sshresult)) / 86400)
    sshsession.close()
    print(days)
    return days

app = Flask(__name__)

@app.route("/graphin")
def graphin():
    with open("/home/student/sshpass.yml") as sshpass: # creds for our servers
        creds = yaml.load(sshpass)
    svruptime = []
    xtick = []

    # loop through credentials
    for cred in creds:
        #append each ip to xtick
        xtick.append(cred['ip'])
        #create resp for credential login to ssh
        resp = sshlogin(cred['ip'], cred['un'], cred['passw'])
        # append resp to svruptime
        svruptime.append(resp)
    xtick = tuple(xtick) # create a tuple
    svruptime = tuple(svruptime)

    # graphin
    N = 3 # total number of bars for each ntwrk device
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence
    p1 = plt.bar(ind, svruptime, width)

    plt.ylabel('Uptime in Days')

    plt.title('Uptime of Servers in Days')
    plt.xticks(ind, xtick)
    plt.yticks(np.arange(0, 20, 1)) # prob want to turn this into a log scale

    plt.savefig('static/status.png') # might want to save this with timestamp for history purposes
    return render_template("graph.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

