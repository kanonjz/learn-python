subprocess模块和os模块都可以用来执行shell命令，不同的是subprocess是开启一个子进程来执行
```
def get_git_address( file_name_piece ):
    cur_dir = os.getcwd()
    if "driver" in file_name_piece:
        cur_dir = os.getcwd()
        os.chdir("/home/xiaoju/webroot/gulfstream/application/driver/v2")
        result = subprocess.check_output("git remote -v", shell=True)
        git_address = result.split()[1]
        print("git address of driver module:", git_address)
        os.chdir(cur_dir)
        return git_address
    elif "passenger" in file_name_piece:
        cur_dir = os.getcwd()
        os.chdir("/home/xiaoju/webroot/gulfstream/application/passengerj/v2")
        result = subprocess.check_output("git remote -v", shell=True)
        git_address = result.split()[1]
        print("git address of driver module:", git_address)
        os.chdir(cur_dir)
        return git_address
  ```
