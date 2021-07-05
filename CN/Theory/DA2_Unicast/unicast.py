import os
import datetime
import shutil
import csv
import pandas as pd
from pandas.core.frame import DataFrame
#x=datetime.datetime.now()
path=os.getcwd()
path=path+'\Chats'
username=''
password=''
admin_username='Gaurav'
admin_password='19BCE2119'

def display_chats(path_user_logs, To_user, From_user):
    data=pd.read_csv(path_user_logs)
    data['Time']= pd.to_datetime(data['Time'], infer_datetime_format=True)
    data.sort_values(by = 'Time', ascending = True, inplace = True)
    data_user= data.loc[data['From']==From_user]
    print(data_user)

def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list
def display_log(path_user_logs,username):
    data=pd.read_csv(path_user_logs)
    data['Time']= pd.to_datetime(data['Time'], infer_datetime_format=True)
    data.sort_values(by = 'Time', ascending = False, inplace = True)
    data= data.loc[data['From']!=username]
    print(unique(data['From']))
def create_log(path):
    with open(path+"\\"+'log.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "From", "Message"])
        file.close()
def add_log(to_user, from_user, message):
    path_log=path+"\\"+to_user.split(' ')[0]+"\\"+to_user.split(' ')[1]+"\\"+'log.csv'
    with open(path_log, 'a', newline='') as file:
        writer = csv.writer(file)
        x=datetime.datetime.now()
        writer.writerow([x, from_user, message])
        file.close()

def session_init():
    print("\nSession Initialization.....\n")
    subnets = int(input("Enter number of subnets: "))
    for i in range(subnets):
        path_subnet=path+"\\"+chr(65+i)
        os.mkdir(path_subnet)
        users=int(input("Enter number of users in subnet "+chr(65+i)+":"))
        for j in range(users):
            path_user=path_subnet+"\\"+str(j+1)
            os.mkdir(path_user)
            create_log(path_user)

def add_or_delete_user(delU,choice):
    flag=int(1)
    choice=int(choice)
    while(flag==1):
        if (choice==1):
            flag=0
            loc=input("Enter the subnet in which u want to add the user: ")
            if(os.path.exists(path+"\\"+loc)):
                dirlist=os.listdir(path+"\\"+loc)
                for i in range(len(dirlist)):
                    dirlist[i]=int(dirlist[i])
                username = max(dirlist)+1
                os.mkdir(path+"\\"+loc+"\\"+str(username))
                print("User Added... The username for the user is: "+loc+" "+str(username))
            else:
                print("Subnet not found")
        elif(choice==0):
            flag=0
            delU=delU.split(' ')
            shutil.rmtree(path+"\\"+str(delU[0])+"\\"+str(delU[1]), ignore_errors=True)
            print("User removed")
        else:
            print("Enter valid option")
            flag=1

def add_subnet(admin_user, admin_pass):
    if(admin_user==admin_username and admin_pass==admin_password):
        dirlist=os.listdir(path)
        for i in range(len(dirlist)):
            dirlist[i]=int(ord(dirlist[i]))
        subnet_ascii=max(dirlist)+1
        os.mkdir(path+"\\"+str(chr(subnet_ascii)))
        nusers=int(input("Enter number of users in the subnet: "))
        for j in range(nusers):
            path_user=path+"\\"+str(chr(subnet_ascii))+"\\"+str(j+1)
            os.mkdir(path_user)
    else:
        print("Unauthorized user")

def del_subnet(admin_user, admin_pass):
    if(admin_user==admin_username and admin_pass==admin_password):
        sub_del=input("Enter the subnet to be deleted: ")
        dirlist=os.listdir(path)
        if (sub_del in dirlist):
            shutil.rmtree(path+"\\"+str(sub_del), ignore_errors=True)
            print("Subnet removed")
        else:
            print("Subnet not found")
    else:
        print("Unauthorized user")

if (os.path.exists(path)):
    flag=1
    choice=input("Do you want to continue from last session? (y/n): ")
    if (choice=='y'):
        while(flag==1):
            option=input("Do you want to make any changes in the structure of the network? (y/n): ")
            if (option=='y'):
                choice=int(input("Enter 0 to delete a user\nEnter 1 to add a user\nEnter 2 to add a subnet with admin privileges\nEnter 3 to delete a subnet with admin privileges\nEnter 4 to exit:"))
                if (choice==1):
                    add_or_delete_user('none', 1)
                elif (choice==0):
                    print("Login to account to delete.")
                    username=input("Username: ")
                    password=input("Password: ")
                    if (os.path.exists(path+"\\"+username.split(' ')[0]+"\\"+username.split(' ')[1]) and username==password):
                        add_or_delete_user(username,0)
                    else:
                        print("User not found")
                elif (choice==2):
                    admin_u=input("Enter username: ")
                    admin_p=input("Enter password: ")
                    add_subnet(admin_u, admin_p)
                elif(choice==3):
                    admin_u=input("Enter username: ")
                    admin_p=input("Enter password: ")
                    del_subnet(admin_u, admin_p)
                else:
                    pass
                loop=input("Do you want to make more changes? (y/n) ")
                if(loop=='y'):
                    flag=1
                else:
                    flag=0
            elif(option=='n'):
                flag=0
                pass
            else:
                print("Enter valid option.")
                flag=1
        pass
    elif (choice=='n'):
        shutil.rmtree(path, ignore_errors=True)
        print("Previous session deleted...")
        os.mkdir(path)
        print("New session created...")
        session_init()
else:
    os.mkdir(path)
    print("No previous session found... New session created")
    session_init()


print("\n\n\n\n\n------------------------LOGIN------------------------")
username='X1'
password='X2'
login='y'
flag='y'
while(login=='y'):
    flag='y'
    while(username!=password):
        username=input("Enter Username: ")
        password=input("Enter Password: ")
        if(username!=password):
            print("Incorrect username or password")
        else:
            print("Logged in to user "+ username)

    flag_log='y'
    path_user=path+"\\"+username.split(' ')[0]+"\\"+username.split(' ')[1]
    path_user_log=path_user+"\\"+'log.csv'
    
    while(flag=='y'):
        choice=int(input("Enter 0 to get list of users who interacted most recently.\nEnter 1 to send message to another peer\nEnter 2 to logout: "))
        if (choice==0):
            display_log(path_user_log, username)
            read_chat='y'
            while(read_chat=='y'):
                read_chat=input("Do you want to read a chat from any user? (y/n):")
                if(read_chat=='y'):
                    unicasted_chat=input("Enter username of the person whose messages you want to see: ")
                    display_chats(path_user_log, username, unicasted_chat)
                else:
                    read_chat='n'
        elif(choice==1):
            to_user=input("Enter username of recepient: ")
            message=input("Enter your message: ")
            add_log(to_user,username,message)
            add_log(username, username,message)
        elif(choice==2):
            print("Logged out")
            flag_log='n'
            flag='n'
            username='X1'
            password='X2'
        else:
            print("Enter valid option")
        
        if (flag_log=='y'):
            flag=input("Do you want to perform any other function? (y/n) ")
            if (flag=='n'):
                login='n'
        else:
            another_login=input("Do you want to end session (login in again if you want to continue)? (y/n)")
            if(another_login=='y'):
                login='n'