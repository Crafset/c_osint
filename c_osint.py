import requests
import os
import colorama
from colorama import Fore, Back, Style
import urllib.parse
import argparse

def check_username(username):
    sites = {
        "Twitter": f"https://twitter.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Github": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "YouTube": f"https://www.youtube.com/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Medium": f"https://medium.com/@{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "VK": f"https://vk.com/{username}",
        "Flickr": f"https://www.flickr.com/people/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "Behance": f"https://www.behance.net/{username}",
        "Bitbucket": f"https://bitbucket.org/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "Keybase": f"https://keybase.io/{username}",
        "About.me": f"https://about.me/{username}",
        "Disqus": f"https://disqus.com/by/{username}",
        "Wattpad": f"https://www.wattpad.com/user/{username}",
    }

    results = {}

    for site, url in sites.items():

        response = requests.get(url)
        if response.status_code == 200:
            results[site] = f"{url}"

    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-help', action='store_true')
    parser.add_argument('-social', action='store_true')
    args = parser.parse_args()

    print(Fore.MAGENTA + "[ " + Fore.YELLOW + "Welcome" + Fore.MAGENTA + " ]> " + Fore.CYAN + "Welcome to Osint Tool by Adam\n")
    colorama.deinit()
    if args.help:
       os.system("cls")
       print(Fore.MAGENTA + "[ " + Fore.YELLOW + "Packages" + Fore.MAGENTA + " ]> " + Fore.CYAN + "-packages\n")
       print(Fore.MAGENTA + "[ " + Fore.YELLOW + "Social" + Fore.MAGENTA + " ]> " + Fore.CYAN + "-social\n")
       colorama.deinit()

    if args.social: 
        colorama.init(autoreset=True)
        os.system("cls")
        username = input(Fore.MAGENTA + "[ " + Fore.YELLOW + "User-Name" + Fore.MAGENTA + " ]> " + Fore.CYAN)
        print(Fore.MAGENTA + "\n[ " + Fore.YELLOW + f"Scan" + Fore.MAGENTA + " ]> " + Fore.CYAN + f"Scanning...\n")
        results = check_username(username)
        for site, result in results.items():
            print(Fore.MAGENTA +"-"*60)
            print(Fore.MAGENTA + "[ " + Fore.YELLOW + f"{site}" + Fore.MAGENTA + " ]> " + Fore.GREEN + f"{result}")
            print(Fore.MAGENTA +"-"*60)
            colorama.deinit()
