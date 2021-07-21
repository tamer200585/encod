#!/usr/bin/python3
from time import sleep
import sys, os, termcolor, pyfiglet

os.system("clear")
print("Welcome  To My Script")
print(termcolor.colored(pyfiglet.figlet_format("Dev: Tamer"),
color='green'))

try:
    try:
        Input = sys.argv[1]
        # layers = int(input("Enter Number Layers: "))
        layers = int(sys.argv[2])
        if layers >= 30 and int(layers):
            print("Not Allowd\nAlowed 1-30")
            sys.exit()
    except IndexError:
        print("Pleas Enter File")
    except ValueError:
        print("Pleas Enter Integar Number")

    def base(code):
        import base64 as b
        code = code.encode('utf-8')
        return f'import base64 as b\nexec(b.b64decode({b.b64encode(code)}))'


    file = open(Input, 'r')

    sleep(1.0)
    t = file.read()
    new_file = open(f"{Input.strip('.py')}-encoding.py", "w")
    new_file.write(base(t))
    file.close()
    new_file.close()
    for i in range(layers):
        i+=1

        new_file = open(f"{Input.strip('.py')}-encoding.py", "r")
        print("Reading File....")
        sleep(0.4)
        d = base(new_file.read())
        new_file.close()
        
        new_file = open(f"{Input.strip('.py')}-encoding.py", "w")
        new_file.write(d)
        new_file.close()
        print("Encrypted")
        print(f"{i}")
except:
    pass




    