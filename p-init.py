import os
import datetime;
from dotenv import load_dotenv;

def python_init():
    # ______________ Load Env Vars ______________
    load_dotenv()
    NEWEST_QID = int(os.getenv("NEWEST_QID"))
    MAX_QID = int(os.getenv("MAX_QID"))
    BUCKET_SIZE = os.getenv("BUCKET_SIZE")

    # ______________ Declare Used Variables ______________
    Q_STRING = ""
    splt = 0
    QID = ""
    QStatement = ""
    QBKT = ""

    # ______________ User Input ______________
    Q_STRING = input()#<QID>.<QStatement>
    splt = Q_STRING.find('.')
    QID = Q_STRING[:splt]
    QStatement = Q_STRING[splt+1:]


    if(NEWEST_QID>MAX_QID):
        print("Update Leetcode.xlsl and MAX_QID")
        exit()

    if(len(Q_STRING)==0 or Q_STRING.find(".")==-1 or QID.isdecimal() is False):
        print("Bad String")
        exit()

    for i in range(1,MAX_QID,100):
        path = os.path.join(os.getcwd(),"Q"+str(i)+"-"+str(i+99))
        if(os.path.exists(path) is False): os.mkdir(path)
        if(i<=int(QID) and int(QID)<=i+100): QBKT = path

    log_path = os.path.join(os.getcwd(), "Q_log.txt")
    if(os.path.isfile(log_path) is False): open(log_path, "x")

    do_path = os.path.join(os.getcwd(), "Q_do.txt")
    if(os.path.isfile(do_path) is False): open(do_path, "x")

    did_path = os.path.join(os.getcwd(), "Q_did.txt")
    if(os.path.isfile(did_path) is False): open(did_path, "x")

    log = open(log_path,'a')
    log.write("INIT,{},{}\n".format(QID,datetime.datetime.now()))
    log.close()

    do = open(do_path,'a')
    do.write("{},{}\n".format(QID,datetime.datetime.now()))
    do.close()



    




python_init()