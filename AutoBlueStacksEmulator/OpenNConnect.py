import psutil
import os
def findProcessPidByName(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return proc
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

os.startfile('C:\Program Files\BlueStacks_nxt\HD-Player.exe')
#print(findProcessPidByName("HD-Player.exe"))
os.system(r'cmd /c "%LocalAppData%\Android\sdk\platform-tools\adb connect localhost:5555"')
