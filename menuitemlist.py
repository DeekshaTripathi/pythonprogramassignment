#!/usr/bin/python2
import time,os,webbrowser

x='''
press 1:to check date and time
press 2:reboot your os
press 3:to create new user from your current os
press 4:to search something on google
press 5:to search cpu and memory information
press 6:to login your fb account and update status hello world
'''
print x
choice =raw_input()

#webbrowser.open('https://www.google.co.in/#q=python')
x =int(choice)
new =2
if choice  == '1' :
	print "showing current time"
	print time.ctime()

elif choice == '2' :
	print "system is reboot"
 #os.system('reboot ')
elif choice == '3' :
	print "enter user name "
#x=raw_input()
	os.system('useradd  '+raw_input())
elif choice == '4' :
	
	msg = raw_input("enter anything: ")
	
	taburl="http://www.google.co.in/?#q="
	webbrowser.open(taburl+msg,new = new)
	
elif choice == '5' :
	print "ram size..."
	os.system('free  ')
	print "______________________________________________________________________"
	time.sleep(10)
	print "cpu information..."
	os.system('cat /proc/cpuinfo')	
elif choice == '6':
	tabu="http://www.google.co.in/?#q=http://www.facebook.com"
         
	#msg1=raw_input("enter any")
	webbrowser.open(tabu, new=new)
