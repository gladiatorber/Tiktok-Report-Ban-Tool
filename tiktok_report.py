import requests
import time
import os
from colorama import Fore, init

# Initialize colorama for colored text
init(autoreset=True)

# Banner
BANNER = f"""
{Fore.RED}╔════════════════════════════════════════════════╗
{Fore.RED}║                                                ║
{Fore.RED}║            {Fore.WHITE}🚀 TIKTOK REPORT BAN {Fore.RED}🚀           ║
{Fore.RED}║         {Fore.YELLOW}(Free Version - Local IP Only)         {Fore.RED}║
{Fore.RED}║                                                ║
{Fore.RED}╚════════════════════════════════════════════════╝
"""

# Pro Version Ad
PRO_AD = f"""
{Fore.GREEN}🔥 {Fore.CYAN}UPGRADE TO {Fore.RED}PRO VERSION {Fore.CYAN}FOR MORE POWER! 🔥
{Fore.YELLOW}✅ Private Proxy Support (SOCKS5/HTTP)
{Fore.YELLOW}✅ Auto-Scrape Fresh Proxies
{Fore.YELLOW}✅ Mass Report Users/Videos
{Fore.YELLOW}✅ Multi-Account Mode
{Fore.YELLOW}✅ Comment Spam Tool
{Fore.RED}📢 Telegram Contact: {Fore.WHITE}@vintok666    {Fore.RED}Link: {Fore.WHITE}https://t.me/vintok666
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def report_user(user_id, reason=90097, delay=5):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "Referer": f"https://www.tiktok.com/@{user_id}",
    }
    
    params = {
        "aid": 1988,
        "app_language": "en",
        "report_type": "user",
        "object_id": user_id,
        "reason": reason,
    }
    
    try:
        response = requests.post(
            "https://www.tiktok.com/api/report/",
            params=params,
            headers=headers,
            proxies={"http": None, "https": None}
        )
        print(f"{Fore.GREEN}[+] Reported {Fore.WHITE}@{user_id} {Fore.GREEN}| Status: {response.status_code}")
        time.sleep(delay)
    except Exception as e:
        print(f"{Fore.RED}[-] Error: {e}")

def main():
    clear_screen()
    print(BANNER)
    print(PRO_AD)
    
    # User input
    target = input(f"{Fore.CYAN}[?] Enter TikTok Username to Report: {Fore.WHITE}@").strip()
    delay = int(input(f"{Fore.CYAN}[?] Delay between reports (seconds): {Fore.WHITE}") or 5)
    count = int(input(f"{Fore.CYAN}[?] Number of reports: {Fore.WHITE}") or 1)
    
    print(f"\n{Fore.YELLOW}[~] Starting reports for @{target}...\n")
    
    for i in range(count):
        report_user(target, delay=delay)
        print(f"{Fore.BLUE}[{i+1}/{count}] Waiting {delay} seconds...")
    
    print(f"\n{Fore.GREEN}[✔] Done! Check results above.")

if __name__ == "__main__":
    main()