#TASK 3
#Random Password Generator
import string
import random
def pswd(size):
    if size<8:
        print("Password length should be atleast 8 characters long")
        return None
    p1=string.ascii_lowercase
    p2=string.ascii_uppercase
    p3=string.digits
    p4=string.punctuation
    p5=p1+p2+p3+p4
    paswd=''.join(random.choice(p5)for _ in range(size))
    return paswd
def main():
    size=int(input("Enter the length of the password: "))
    password=pswd(size)
    if password:
        print("Generated Password: ",password)
if __name__=="__main__":
    main()
