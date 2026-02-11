import re
while True:
   email=input("enter your email:").strip().lower()
   if " " in email:
       print("Invalid email! Email don't contain spaces ")
       continue
   if email.count("@")!=1:
       print("Invalid email ! Email must contain one @");
       continue
   if email.startswith("@") or email.endswith("@"):
       print("Invalid email ! '@' cannot be at start or end")
       continue
   username,domain_name=email.split("@")
   if len(username)==0:
       print("Invalid email! username cannot be empty")
       continue
   if len(domain_name)==0:
       print("Invalid email ! Domain name cannot be empty")
       continue
   if ".."  in domain_name:
       print("Invalid email ! Domain name do not contain '..'")
       continue
   if ".."  in username:
       print("Invalid email ! username do not contain '..'")
       continue
   if "." not in domain_name:
       print("Invalid email ! Domain name must contain '.'")
       continue
   if(domain_name.startswith('.') or domain_name.endswith('.')):
       print("Invalid email ! Domain name cannot start or and with '.'")
       continue
   if(username.startswith('.') or username.endswith('.')):
       print("Invalid email ! username cannot start or end with '.'")
       continue
   ext=domain_name.split('.')[-1]
   if ext not in ["com","org","net"]:
       print("Invalid domain name ! Domain name must be .com .org .net")
       continue

   if re.fullmatch(r"[a-z0-9._-]+",username):
       print("Congratulation! Your email is correct")
       print("Username: ",username)
       print("Domain name: ",domain_name)
       break
   else:
       print("Invalid email! Username contains invalid characters")
       continue

