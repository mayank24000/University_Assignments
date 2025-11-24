from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def print_header(text):
    """Print colored header"""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}{text.center(60)}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")

def print_section(title):
    """Print section title"""
    print(f"\n{Fore.YELLOW}▶ {title}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'-'*50}{Style.RESET_ALL}")

def print_info(label, value, color=Fore.GREEN):
    """Print label-value pair"""
    print(f"{Fore.WHITE}{label:.<30} {color}{value}{Style.RESET_ALL}")

def print_list(items, bullet="  •"):
    """Print list of items"""
    for item in items:
        print(f"{Fore.GREEN}{bullet} {item}{Style.RESET_ALL}")

def validate_hostname(hostname):
    """Basic hostname validation"""
    # Remove protocol if present
    hostname = hostname.replace('https://', '').replace('http://', '')
    # Remove path if present
    hostname = hostname.split('/')[0]
    return hostname