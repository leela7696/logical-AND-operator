# write a python script develop one meaningful usecase using logical and operator?

import time
print()

print("===============NETFLIX===============")
print()
print("Please enter correct login details")
print('----------------------------------')
print()
user_id=input('Enter the number or gmail:  ')
print()
password=input('Enter the password:  ')
print()
confirm_password=input('Enter confirm_password:  ')
print()
if(user_id=="leela0006" and password=="Leela@2099"and confirm_password=="Leela@2099"):
    print("=========✅✅Login Sucessfull✅✅==========")
    print()
    print()
    print("*********ENJOY YOUR OTT HERE**********")
else:
    print("❌❌❌❌❌Invaid Details Please Enter Correct Details❌❌❌❌❌")
print()
time.sleep(2)
print('End of an application')