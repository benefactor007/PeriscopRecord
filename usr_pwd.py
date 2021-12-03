# coding=utf-8
import os
import string
import random
import re


def set_pwd_sample_size() -> str:
    # return string.ascii_letters + string.digits + string.punctuation
    ten_special_character = "!@#$%^&*()"
    return string.ascii_letters + string.digits + ten_special_character
    # return string.ascii_letters + string.digits


def getRandomPwd(pwdLen: int = 8) -> str:
    # pwd = ""
    n = 0
    while True:
        result = random.sample(set_pwd_sample_size(), pwdLen)  # Return List
        pwd = "".join(result)
        n += 1
        # print(pwd)
        # print(type(pwd))
        if n > 200:
            print("It's enough, try 200 times, something is going wrong!!!")
            return None
            break
        if re.search("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$", pwd):
            # Minimum eight characters, at least one upper case English letter, one lower case English letter, one number
            # and one special character
            return pwd
            break


def set_usr_sample_size() -> str:
    # return string.ascii_letters + string.digits + string.punctuation
    ten_special_character = "!@#$%^&*()"
    return string.ascii_letters + string.digits + ten_special_character
    # return string.ascii_letters + string.digits


def getRandomUsr(usrLen: int = 6) -> str:
    n = 0
    while True:
        usrName = random.sample(set_usr_sample_size(), 8)
        usrName = "".join(usrName)
        if n > 200:
            print("200 times, something is going wrong!!!")
            return None
            break
        if re.search("^[a-z0-9_-]{3,15}$", usrName):
            return usrName
            break


def getCurrentPWD() -> str:
    current_location = os.popen("echo `pwd`")
    # pwd = current_location.read()
    return current_location.read().strip()


def save_data_in_txt(usr_pwd_dict: dict) -> bool:
    filepath = getCurrentPWD() + "/usr_pwd.txt"
    if not os.path.isfile(filepath):
        mtime_before = 0.0
    else:
        mtime_before = os.stat(filepath).st_mtime
    # Use os.stat(path).st_mtime to check whether the file was modified.
    with open(filepath, 'a+') as f:
        if mtime_before == 0.0:
            f.write("%-20s\t%-20s\t\n" % ("Username", "Password"))
        else:
            for usr,pwd in usr_pwd_dict.items():
                f.write("%-20s\t%-20s\t\n" % (usr, pwd))
    mtime_after = os.stat(filepath).st_mtime
    if mtime_before != mtime_after:
        return True
    else:
        return False
    # return os.path.isfile(filepath)


def main():
    # for i in range(8):
    #     print(getRandomPwd(10))
    # Format string
    # print('%-20s\t\t%-20s\t\t' % (getRandomUsr(8), getRandomPwd(8)))

    timesTry = 8
    # usrNameList = ["Username"]
    # pwdList = ["Password"]
    # for i in range(timesTry):
    #     usrNameList.append(getRandomUsr(6))
    #     pwdList.append(getRandomPwd(8))
    # Create dictionary to save the pair of username and password
    dict = {}
    for i in range(timesTry):
        dict[getRandomUsr()] = getRandomPwd()
    print("%-20s\t%-20s\t" % ("Username", "Password"))
    for usr, pwd in dict.items():
        print("%-20s\t%-20s\t" % (usr, pwd))
    save_data_in_txt(dict)


if __name__ == '__main__':
    main()
