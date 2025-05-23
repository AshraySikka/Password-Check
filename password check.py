pass1=input("Enter a password: ")
pass2=input("Enter password to confirm: ")
if pass1==pass2:
    print("All Set")
elif pass1.casefold()==pass2.casefold():
    print("Passwords do not match - check the case")
else:
    print("Passwords do not match")
