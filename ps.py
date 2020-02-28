#!/bin/python
import optparse
import os

parser = optparse.OptionParser() 
parser.add_option('-u','--utilisateur',action="store_const", default=False)
parser.add_option('-a','--all',action="store_true", default=False)
parser.add_option('-x','--x',action="store_true", default=False)
options=parser.parse_args()

def deuxCaractere(arg): ## fonction pour mettre au bon format le TIME
    if arg<10:
        return '0'+str(arg)
    return str(arg)

def time(seconde): # fonction pour transformer les secondes en HH:MM:SS
    heure = int(seconde //3600)
    seconde %= 3600
    minute = int(seconde//60)
    seconde%=60
    return (deuxCaractere(heure)+':'+deuxCaractere(minute)+':'+deuxCaractere(seconde))

e=False
a=os.listdir('/proc')
utilisateurCourant=os.geteuid()
res=[]
if options[0].utilisateur==None and options[1]==[]: # creation de la premiere ligne selon la commande
    res.append(['USER      ','PID','%CPU','%MEM','VSZ','RSS',' TTY ','STAT','START',' TIME ','    CMD'])
elif options[0].x:
    res.append(['PID','  TTY ','STAT',' TIME ','   CMD'])
else:
    res.append(['PID','  TTY ',' TIME ','   CMD'])
for i in a:
    try: # test pour n'avoir que les dossiers des processus
        int(i)
        e=True
    except:
        pass
    if e:
        cmd=open('/proc/'+str(i)+'/stat','r')
        status=open('/proc/'+str(i)+'/status','r')
        status1=status.read().split()
        cmd1=cmd.read()
        cmd1=cmd1.split()
        seconde=int(cmd1[14])/int(os.sysconf(2)) # le temps en jiffies converti en secondes grace aux informations donnees par os
        userProc=status1[17]
        tty=int(cmd1[6])
        if os.major(tty)==136: #decodage du TTY
            tty="pts/"+str(os.minor(tty))
        elif os.major(tty)==4:
            tty="tty"+str(os.minor(tty))+' '
        else:
            tty="?    "
        
        if options[0].utilisateur==None: # pour savoir si -x est suivi d'un argument
            if options[1]==[userProc]:
                    res.append([i,tty,time(seconde),cmd1[1]])
            else:
                if int(cmd1[7])==os.getppid():
                    res.append([userProc,i,'    ','    ','   ','   ',tty,cmd1[2],'        ',time(seconde),cmd1[1]])
        elif options[0].all:
            if int(cmd1[7])==os.getppid() and i!=cmd1[5]:
                res.append([i,tty,time(seconde),cmd1[1]])
        elif options[0].x:
            if int(userProc)==utilisateurCourant:
                res.append([i,tty,cmd1[2],time(seconde),cmd1[1]])
        else:
            if int(cmd1[7])==os.getppid():
                res.append([i,tty,time(seconde),cmd1[1]])
    
        
        cmd.close()
        status.close()

if options[0].utilisateur==None and options[1]==[]: ## affichage des informations suivant les arguments rentres
    for i in res:
        i[10]=i[10].replace('(','')
        i[10]=i[10].replace(')','')
        print(i[0]+' '+i[1]+' '+i[2]+' '+i[3]+' '+i[4]+' '+i[5]+' '+i[6]+' '+i[7]+' '+i[8]+' '+i[9]+' '+i[10])

elif options[0].x:
    for i in res:
        i[4]=i[4].replace('(','')
        i[4]=i[4].replace(')','')
        print(i[0]+' '+i[1]+' '+i[2]+'        '+i[3]+'   '+i[4])
        
else:
    for i in res:
        i[3]=i[3].replace('(','')
        i[3]=i[3].replace(')','')
        print(i[0]+' '+i[1]+' '+i[2]+' '+i[3])

    




