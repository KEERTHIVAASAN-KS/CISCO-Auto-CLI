import serial
import sys
import pexpect
import paramiko
import tkinter  

def serialcon(prt,baud,commands):
    
    ser = serial.Serial(port=prt,baudrate=baud,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,timeout=1)
    
    for command in commands:
        content=ser.read_until(b"\r\n")
        content=content.decode("utf-8")
        print(content)
            
        command=command+"\r\n"
        ser.write(bytes(command.encode("utf-8")))

    content=ser.read_until(b"\r\n")
    content=content.decode("utf-8")
    print(content)
        
    ser.close()
    
def telnetcon(host,commands):
    tel=pexpect.spawn(f"telnet {host}",encoding="utf-8",timeout=10)
    
    for command in commands:
        content=tel.expect("\r\n")
        print(content)    
        command=command+"\r\n"
        tel.sendline(command)
    
    content=tel.expect("\r\n")
    print(content)
    tel.close()

def sshcon(host,user,passwd,commands):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=user, password=passwd, timeout=10)
    shell=ssh.invoke_shell()
    
    for command in commands:
        content=""
        while True:
            charac=shell.recv(1)
            charac=charac.decode("utf-8")
            if charac=="\r\n":
                break
            content=content+charac
        print(content)
            
        command=command+"\r\n"
        shell.send(bytes(command.encode("utf-8")))
    content=""
    while True:
        charac=shell.recv(1)
        charac=charac.decode("utf-8")
        if charac=="\r\n":
            break
        content=content+charac
    print(content)
        
    ssh.close()


entry=None
content=None    
def run():
    content=entry.get("1.0","end-1c")
    content=content.split("\n")
    if content[-1]=="":
        content.pop()
    if sys.argv[1]=="serial":
        serialcon(sys.argv[2],sys.argv[3],content)
    if sys.argv[1]=="ssh":
        sshcon(sys.argv[2],sys.argv[3],sys.argv[4],content)
    if sys.argv[1]=="telnet":
        telnetcon(sys.argv[2],content)
    
def gui():  
    window=tkinter.Tk()
    window.title("CISCO AUTOMATION TOOL")
    window.geometry("400x400")

    mainframe=tkinter.Frame(window)
    mainframe.pack(fill="both",expand=True,padx=10,pady=10)
    global entry
    entry=tkinter.Text(mainframe,height=10)
    entry.pack(fill="both",expand=True)

    button=tkinter.Button(window,text="RUN",command=run)
    button.pack(padx=10,pady=10)


    window.mainloop()

gui()






    
    


