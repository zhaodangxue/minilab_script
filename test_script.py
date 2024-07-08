import os
import subprocess
import termcolor as T
def log(s, col="green"):
    print (T.colored(s, col))
def main():
    log("copy test code from github")
    os.system("git clone https://github.com/zhaodangxue/mininetLab.git")
    python3 = "python3 "
    log("run test code")
    os.chdir("mininetLab")
    os.system(python3 + "test_script.py")
    os.system("mv ./data ../data")
    os.chdir("..")
    os.system("rm -rf mininetLab")
    folder_path = "./data"
    new_mode = "777"
    for root, dirs, files in os.walk(folder_path):
    # 设置文件的权限
     for file in files:
        file_path = os.path.join(root, file)
        subprocess.run(['sudo', 'chmod', new_mode, file_path])
if __name__ == "__main__":
    main()