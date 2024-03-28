import os
import time
from colorama import Fore

from colorama import Fore, Style, init
import time

def print_fading_logo():
    logo = """                                                                                     ⢀⡠⣄⡀⠀⠀⡠⠞⠛⢦⣠⢤⡀⠀
                                                                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢠⠏⠀⠀⢱⡀⣸⠁⠀⡴⠋⠀⠀⣹⠀    
                                                                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠉⢿⢀⡤⠶⣴⠇⣯⠀⣼⠁⠀⢀⡴⠷⣄          
                                                                     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠁⠀⣀⡾⠋⠀⠀⢹⣼⠁⢠⡇⠀⡴⠋⠀⠀⡼     
                                                                     ⠀⠀⠀⠀⢠⠊⠑⢦⠀⡴⠋⢀⣠⠞⠉⠀⠀⠀⣠⣿⠧⣄⡾⠁⡼⠁⣀⣤⠾⡁
                                                                     ⠀⠀⠀⠀⢸⠀⠀⣨⠟⠁⢠⡞⠁⠀⠀⠀⣠⡾⠛⠁⠀⣿⠃⣰⠃⣴⠋⠀⠀⣷
                                                                     ⠀⠀⠀⠀⣸⢠⠞⠁⠀⢠⠏⠀⠀⢀⡴⠋⠁⠀⢀⣠⡴⠿⣶⡇⢰⠇⠀⠀⢠⠇
                                                                     ⠀⠀⠀⢠⢿⠏⠀⠀⠀⠉⠀⠀⣠⠞⠁⠀⡴⠚⠉⠁⠀⢀⡟⠀⣼⠀⠀⠀⢸⠀
                                                                     ⠀⠀⠀⡾⣼⢀⠀⠀⠀⠀⠀⠈⠉⠀⣠⠞⠁⠀⠀⢀⡴⠋⠙⢼⠃⠀⠀⠀⣸⠀
                                                                     ⠀⠀⠀⡇⠉⡎⠀⣰⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⡼⠉⠀⠀⠀⠘⠂⠀⠀⣠⠇⠀
                                                                     ⠀⠀⠀⡇⢸⠀⣰⠃⠀⡴⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⣠⠖⠁⠀⠀
                                                                     ⠀⠀⢸⠁⡏⢠⠃⢀⠞⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⢀⣠⠖⠋⠁⠀⠀⠀⠀
                                                                     ⠀⠀⡞⠀⠃⡎⢀⠏⠀⠀⠀⠀⠀⠀⢀⡏⠀⣀⡤⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀
                                                                     ⡴⢺⠇⠀⠀⠀⠞⠀⠀⠀⠀⠀⠀⢀⡾⠒⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                     ⡇⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                     ⢳⡀⠘⢦⡀⠀⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                     ⠀⠳⣄⠀⠙⠲⣤⣀⣠⠴⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                     ⠀⠀⠈⠓⠦⣄⣀⡠⠎⠀⠀
                                                                     [+[+[+ created by annymous_coder +]+]+]
                                                                     [+[+[+ github.com/Dhdh2k +]+]+]
                                                                     [+[+[+ version 2.0.0 +]+]+]
"""

    init()

    start_color = Fore.RED
    end_color = Fore.GREEN
    lines = logo.split('\n')
    num_lines = len(lines)
    color_range = list(range(0, 255, 255 // num_lines))
    gradients = [start_color + Style.BRIGHT + f'\033[38;2;{r};{g};0m'
                 for r, g in zip(color_range, reversed(color_range))]
    max_line_length = max(len(line) for line in lines)
    padding = (max_line_length - len(lines[0])) // 2
    for line, gradient in zip(lines, gradients):
        centered_line = ' ' * padding + line
        print(gradient + centered_line)
        time.sleep(0.2)
    print(Style.RESET_ALL)
print_fading_logo()
def print_fading_menu(menu_options):
    init()
    start_color = Fore.RED
    end_color = Fore.GREEN
    num_options = len(menu_options)
    color_range = list(range(0, 255, 255 // num_options))
    gradients = [start_color + Style.BRIGHT + f'\033[38;2;{r};{g};0m' for r, g in zip(color_range, reversed(color_range))]
    for option, gradient in zip(menu_options, gradients):
        print(gradient + option)
    print(Style.RESET_ALL)
menu_options = [
    '[1] learn coding                                 [2] learn hacking                           [3] kali tools                        [4] free movies',
    '[5] ai                                           [6] websites to cure bordem                 [7] camera hacking                    [8] grab gps',
    '[9] grab ip                                      [10] track ip                               [11] track phonenumber                [12] free books',
    '[13] hacking courses                             [14] get location from image                [15] free games                       [16] property info',
    '[17] phishing                                    [18] wifi hacking                           [19] info gathering                   [20] virus scaning',
    '[21] url scan                                    [22] port scanners                          [23] operating systems                [24] brute force accounts',
    '[25] brute force files                           [26] brute force phones                     [27] DDoS                             [28] DoS',
    '[29] meta data                                   [30] program alternatives                   [31] web scraping                     [32] beef',
    '[33] social engineering                          [34] custom search                          [35] passowrd generator               [36] games',
    '[37] free books                                  [38] open youtube                           [39] open soundcloud                  [40] cool commands', 
    '[41] motivation                                  [42] psyhology                              [43] minecraft                        [99] exit'
]

print_fading_menu(menu_options)

menuchoice = input(Fore.RED + 'Enter your choice: ')
