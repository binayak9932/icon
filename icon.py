import  winreg

path = winreg.HKEY_LOCAL_MACHINE

def rege(k = '29', v ='%windir%\System32\shell32.dll,-50'):
    try:
        key = winreg.OpenKeyEx(path, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\")
        newKey = winreg.CreateKey(key,"Shell Icons")
        winreg.SetValueEx(newKey, k, 0, winreg.REG_SZ, str(v))
        if newKey:
            winreg.CloseKey(newKey)
            print("Done sucessfully!!!!!")
        return True
    except Exception as e:
        print(e)
        print("ERROR!!!!!")
    return False


rege()
