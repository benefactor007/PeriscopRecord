# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os
import re


def greenFont(str):
    return "\033[32m" + str + "\033[0m"


def catFazitInfo(str):
    # p1 = re.search("2093[0-9]{4}",str)
    # X9G-101[0-9\.]{8}9[0-9]{3}[0-9]{4}
    p1 = re.search("X9G-101[0-9\.]{8}9[0-9]{3}[0-9]{4}", str)
    return p1.group()


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.

def setLogFile():
    scanQR = input("Please scan the QR image:")
    suffix = '.txt'
    current_location = os.popen("echo `pwd`")
    pwd = current_location.read()
    print("Print working directory:", pwd)
    filepath = pwd.strip() + '/' + catFazitInfo(scanQR) + suffix
    print('The serial num is', catFazitInfo(scanQR))
    print('File name is', filepath)
    """
    判断文件是否存在
        os.path.isfile(path)
    """
    if os.path.isfile(filepath):
        print(greenFont("Log file is created!!!"))
        return True
    else:
        return False


def setLogDirectory(dirName: str) -> bool:
    os.system("sudo mkdir " + dirName)
    return os.path.isdir(getCurrentPWD() + "/" + dirName)


def getCurrentPWD() -> str:
    current_location = os.popen("echo `pwd`")
    pwd = current_location.read()
    return pwd.strip()


def main1():
    if setLogFile():
        # os.system("sudo sh -c ./SWDL.exp " + formatSerialNum(case_serialNum) + "|tee -a " + fileName)
        os.system("sudo ./persistence")
        # sudo ./periscope -u serial:/dev/ttyUSB0 -l
    else:
        print("Record File is not created!!!")


def main2():
    scanQR = input("Please scan the QR image:")
    # if os.path.isdir(pwd.strip() + '/' + catFazitInfo(scanQR)):
    if setLogDirectory(catFazitInfo(scanQR)):
        print(greenFont("PASS"))
        os.system("sudo ./periscope -u serial:/dev/ttyUSB0 -l "+catFazitInfo(scanQR))
    else:
        print("Periscope Log directory is not created")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    main2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
