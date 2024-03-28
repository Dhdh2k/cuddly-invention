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
    '[1] Learn Coding',
    '[2] Learn Hacking',
    '[3] Kali Tools',
    '[4] Free Movies',
    '[5] AI',
    '[6] Websites for Cure Boredom',
    '[7] Camera Hacking',
    '[8] Grab GPS',
    '[9] Grab IP Address',
    '[10] Track IP Address',
    '[11] Track Phone Number',
    '[12] Free Books',
    '[13] Hacking Courses',
    '[14] Get Location from Image',
    '[15] Free Games',
    '[16] Property Info',
    '[17] Phishing',
    '[18] WiFi Hacking',
    '[19] Information Gathering',
    '[20] Virus Scanning',
    '[21] URL Scan',
    '[22] Port Scanners',
    '[23] Operating Systems',
    '[24] Brute Force Accounts',
    '[25] Brute Force Files',
    '[26] Brute Force Phones',
    '[27] DDoS (Distributed Denial of Service)',
    '[28] DoS (Denial of Service)',
    '[29] Metadata',
    '[30] Program Alternatives',
    '[31] Web Scraping',
    '[32] Beef (Browser Exploitation Framework)',
    '[33] Social Engineering',
    '[34] Custom Search',
    '[35] Password Generator',
    '[36] Games',
    '[37] VPN (Virtual Private Network)',
    '[38] Open YouTube',
    '[39] Open SoundCloud',
    '[40] Cool Commands',
    '[41] Motivation',
    '[42] Psychology',
    '[43] Minecraft',
    '[99] Exit'
]

print_fading_menu(menu_options)

menuchoice = input(Fore.RED + 'Enter your choice: ')

