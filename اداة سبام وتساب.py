
import os,sys
import random,string
from time import sleep

R = '\x1b[38;5;1m'   # أحمر
M = '\x1b[38;5;244m' # رمادي 
L = '\x1b[38;5;10m' #اخضر 

print(f"{L}={M}="*30)

print(
	
	f"{L}  [1] {R} ==> {L} yopmail.com\n"
	f"{M}{'='*60}\n"
	f"{L}  [2] {R} ==> {L} hi2.in\n"
	f"{M}{'='*60}\n"
	f"{L}  [3] {R} ==> {L} hotmail.com\n"
	f"{M}{'='*60}\n"
	f"{L}  [4] {R} ==> {L} gmail.com\n"
	f"{M}{'='*60}\n"
	f"{L}  [5] {R} ==> {L} telegmail.com\n"
	f"{M}{'='*60}\n"
	f"{L}  [6] {R} ==> {L} yahoo.com\n"
	
)

print(f"{L}={M}="*30)

choice =input(f"{L} [{M} Enter choice {L}] >> {M}")

if not choice:
	print(R+"  لازمك تختار الدومين   ")
	sys.exit()


if choice == "1":
	domain = "@yopmail.com"
elif choice == "2":
	domain = "@hi2.in"
elif choice == "3":
	domain = "@hotmail.com"
elif choice == "4":
	domain = "@gmail.com"
elif choice == "5":
	domain = "@telegmail.com"
elif choice == "6":
	domain = "@yahoo.com"

else:
	print(R+" اختياركك غاللط ❌")
	sys.exit()

i = int(input(f"{L}  [ {M} How emails want ? {L}] {L} >>"))	
		

ibra = "qwertyuioplkjhgfdsamnbvcxz1234567890"
len = random.randint(2,8)

with open("/storage/emulated/0/Download/domain_email.txt", "w") as f:
	for _ in range(i):
		user ="".join(random.choice(ibra) for _ in range(len))
		email = f"{user}{domain}\n"
		f.write(email)
	
	
print(f" 'domain_email.txt' تم حفظ في ملف اسمه")
	
