import aiohttp
import asyncio
import os
import colorama
from colorama import Fore, Style
import argparse

async def fetch(session, site, url):
    try:
        async with session.get(url, timeout=10) as response:
            if response.status == 200:
                return site, url
            else:
                return site, None
    except Exception as e:
        return site, None

async def check_username(username):
    sites = {
        "Twitter": f"https://twitter.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Github": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "YouTube": f"https://www.youtube.com/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
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
        "Patreon": f"https://www.patreon.com/{username}",
        "PayPal.Me": f"https://www.paypal.me/{username}",
        "Slack": f"https://{username}.slack.com",
        "TripAdvisor": f"https://www.tripadvisor.com/members/{username}",
        "Angellist": f"https://angel.co/{username}",
        "Goodreads": f"https://www.goodreads.com/{username}",
        "Instructables": f"https://www.instructables.com/member/{username}",
        "Codepen": f"https://codepen.io/{username}",
        "Tripit": f"https://www.tripit.com/people/{username}",
        "Bandcamp": f"https://bandcamp.com/{username}",
        "Spotify": f"https://open.spotify.com/user/{username}",
        "Pastebin": f"https://pastebin.com/u/{username}",
        "Wattpad": f"https://www.wattpad.com/user/{username}",
        "Canva": f"https://www.canva.com/{username}",
        "HubPages": f"https://hubpages.com/@{username}",
        "Contently": f"https://{username}.contently.com",
        "Houzz": f"https://www.houzz.com/user/{username}",
        "Imgur": f"https://imgur.com/user/{username}",
        "Flipboard": f"https://flipboard.com/@{username}",
        "SlideShare": f"https://www.slideshare.net/{username}",
        "Fotolog": f"https://fotolog.com/{username}",
        "Gumroad": f"https://gumroad.com/{username}",
        "Wikidot": f"http://www.wikidot.com/user:{username}",
        "Behance": f"https://www.behance.net/{username}",
        "Slack": f"https://{username}.slack.com",
        "Couchsurfing": f"https://www.couchsurfing.com/people/{username}",
        "We Heart It": f"https://weheartit.com/{username}",
        "Carbonmade": f"https://{username}.carbonmade.com",
        "ReverbNation": f"https://www.reverbnation.com/{username}",
        "Badoo": f"https://www.badoo.com/en/{username}",
        "Kongregate": f"https://www.kongregate.com/accounts/{username}",
        "Last.fm": f"https://www.last.fm/user/{username}",
        "MyAnimeList": f"https://myanimelist.net/profile/{username}",
        "Newgrounds": f"https://{username}.newgrounds.com",
        "Wattpad": f"https://www.wattpad.com/user/{username}",
    }

    async with aiohttp.ClientSession() as session:
        tasks = []
        for site, url in sites.items():
            tasks.append(fetch(session, site, url))

        results = await asyncio.gather(*tasks)
        return {site: result for site, result in results if result}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-help', action='store_true')
    parser.add_argument('-social', action='store_true')
    args = parser.parse_args()

    colorama.init(autoreset=True)
    print(Fore.MAGENTA + "[ " + Fore.YELLOW + "Welcome" + Fore.MAGENTA + " ]> " + Fore.CYAN + "Welcome to OSINT Tool by Adam\n")
    colorama.deinit()
    
    if args.help:
        os.system("clear" if os.name == "nt" else "clear")
        print(Fore.MAGENTA + "[ " + Fore.YELLOW + "Packages" + Fore.MAGENTA + " ]> " + Fore.CYAN + "-packages\n")
        print(Fore.MAGENTA + "[ " + Fore.YELLOW + "Social" + Fore.MAGENTA + " ]> " + Fore.CYAN + "-social\n")
        colorama.deinit()

    if args.social: 
        colorama.init(autoreset=True)
        os.system("clear" if os.name == "nt" else "clear")
        username = input(Fore.MAGENTA + "[ " + Fore.YELLOW + "User-Name" + Fore.MAGENTA + " ]> " + Fore.CYAN)
        print(Fore.MAGENTA + "\n[ " + Fore.YELLOW + "Scan" + Fore.MAGENTA + " ]> " + Fore.CYAN + "Scanning...\n")

        results = asyncio.run(check_username(username))

        for site, result in results.items():
            print(Fore.MAGENTA + "-" * 60)
            print(Fore.MAGENTA + "[ " + Fore.YELLOW + f"{site}" + Fore.MAGENTA + " ]> " + Fore.GREEN + f"{result}")
            print(Fore.MAGENTA + "-" * 60)
        
        colorama.deinit()

if __name__ == "__main__":
    main()
