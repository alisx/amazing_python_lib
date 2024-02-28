# pip install colorama

from colorama import init

# 初始化
init()

# 在 Windows 系统上，它将转换这些序列以修改终端的状态
#from colorama import just_fix_windows_console
#just_fix_windows_console()

# 打印彩色文本
from colorama import Fore, Back, Style
print(Fore.RED + '这是一段红色文本')
print(Back.GREEN + '并有一个绿色背景')
print(Style.DIM + '文字变得暗淡')
print(Style.RESET_ALL)
print('现在又回到了正常文本')

# 可用的格式化常量
'''
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''
