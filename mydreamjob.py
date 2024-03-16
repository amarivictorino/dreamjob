from colorama import Fore, Style   # Import libraries for colored text

name = input("What's your name?")
dream_job = input("What's your dream job?")

print(Fore.MAGENTA + "~" * 30 + Style.RESET_ALL)  # Print magenta border
print(f"{Fore.YELLOW}{name:>{30}}{Style.RESET_ALL}")  # Right-align name in yellow
print(f"{Fore.CYAN}Aspiring {dream_job:>{30}}{Style.RESET_ALL}")  # Right-align dream job in cyan
print(Fore.MAGENTA + "~" * 30 + Style.RESET_ALL)  # Print magenta border again






