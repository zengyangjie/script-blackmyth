%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"
python -m pip install pyautogui
python -m pip install keyboard
python blackmyrh.py
pause