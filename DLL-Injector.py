import os
import requests
from time import sleep

def download_file(url: str, filename: str):
	with open(filename, 'wb') as f:
		with requests.get(url, stream=True) as r:

			r.raise_for_status()
			for chunk in r.iter_content(chunk_size=8192):
				f.write(chunk)

print('''
      ____  __    __       ____        _           __            
     / __ \/ /   / /      /  _/___    (_)__  _____/ /_____  _____
    / / / / /   / /       / // __ \  / / _ \/ ___/ __/ __ \/ ___/
   / /_/ / /___/ /___   _/ // / / / / /  __/ /__/ /_/ /_/ / /  
  /_____/_____/_____/  /___/_/ /_/_/ /\___/\___/\__/\____/_/  
                                                /___/                        

         DLL Injector (LoadLibrary) in C++ (x86 / x64) 
                Full Undetected Injector.
''')
print('\n\n')
dll = input("[#] Введите название DLL(test.dll): ")
proc = input("[#] Введите название процесса(notepad.exe): ")
download_file("https://github.com/adamhlt/DLL-Injector/releases/download/DLL-Injector/Inject-x64.exe", "helper.exe")
sleep(0.5)
os.system(f'helper.exe {dll} {proc}')
sleep(0.5)
os.system('del helper.exe')
input()