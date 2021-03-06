import paramiko
import subprocess

import view

hostname = "169.254.35.144"
username = "pi"
password = "raspberry"
commands = [
    "python3 recorde.py"
]

def main():
    # initialize the SSH client
    client = paramiko.SSHClient()
    # add to known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, username=username, password=password)
    except:
        print("[!] Cannot connect to the SSH Server")
        exit()

    # execute the commands
    for command in commands:
        print("=" * 50, command, "=" * 50)
        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read().decode())
        err = stderr.read().decode()
        if err:
            print(err)
    # in this stage we can take videos form the local pc that sync with the raspberry folder
    # but now we entered sample video
    subprocess.call(['opencv-test.exe', 'C:\\Users\\ddkil\\PycharmProjects\\Raspberry_project\\test_video.mp4', 'result.txt', 'C:\\Users\ddkil\\PycharmProjects\\Raspberry_project\\images', '5'])
    view.run()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
