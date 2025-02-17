import aiohttp
import asyncio
import json
import re
import os
import random
from colorama import *
from datetime import datetime
import pytz

wib = pytz.timezone('Asia/Jakarta')

class Clayton:
    def __init__(self) -> None:
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Host': 'tonclayton.fun',
            'Origin': 'https://tonclayton.fun',
            'Pragma': 'no-cache',
            'Referer': 'https://tonclayton.fun/?tgWebAppStartParam=1493482017',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
        }
        self.base_url = "https://tonclayton.fun"
        self.api_base_id = None

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Clayton Bot Script by {Fore.BLUE + Style.BRIGHT}HACKER WORLD BD
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Join script channel {Fore.YELLOW + Style.BRIGHT}https://t.me/HACKER_WORLD_BD
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    
    async def find_latest_js_file(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url) as response:
                response.raise_for_status()
                html = await response.text()
                match = re.search(r'\/assets\/index-[^"]+\.js', html)
                return match.group(0).split('/')[-1] if match else None

    async def fetch_api_base_id(self, retries=5, delay=3):
        for attempt in range(retries):
            js_file = await self.find_latest_js_file()
            if js_file:
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(f"{self.base_url}/assets/{js_file}") as response:
                            response.raise_for_status()
                            js_content = await response.text()
                            match = re.search(r'_ge="([^"]+)"', js_content)
                            if match:
                                self.api_base_id = match.group(1)
                                return
                            else:
                                return None
                except (aiohttp.ClientError, aiohttp.ContentTypeError, json.JSONDecodeError) as e:
                    if attempt < retries - 1:
                        await asyncio.sleep(delay)
                    else:
                        return None
            else:
                if attempt < retries - 1:
                    await asyncio.sleep(delay)
                else:
                    return None
    
    async def user_authorization(self, query: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/user/authorization'
        headers = {
            **self.headers,
            'Content-Length': '0',
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
                
    async def daily_claim(self, query: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/user/daily-claim'
        headers = {
            **self.headers,
            'Content-Length': '0',
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
    
    async def all_tasks(self, query: str, type: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/tasks/{type}'
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def start_tasks(self, query: str, task_id: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/tasks/complete'
        data = json.dumps({'task_id': task_id})
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def claim_tasks(self, query: str, task_id: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/tasks/claim'
        data = json.dumps({'task_id': task_id})
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def check_tasks(self, query: str, task_id: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/tasks/check'
        data = json.dumps({'task_id': task_id})
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def user_achievements(self, query: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/user/achievements/get'
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def claim_achievements(self, query: str, type: str, level: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/user/achievements/claim/{type}/{level}'
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def start_game1024(self, query: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/game/start'
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def save_tile(self, query: str, session_id: str, tile: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/game/save-tile'
        data = json.dumps({'session_id':session_id, 'maxTile':tile})
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def over_tile(self, query: str, session_id: str, tile: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/game/over'
        data = json.dumps({'session_id':session_id, 'multiplier':1, 'maxTile':tile})
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
                
    async def start_clayball(self, query: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/clay/start-game'
        data = {}
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, json=data) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
                
    async def end_clayball(self, query: str, score: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/clay/end-game'
        data = json.dumps({'score':score})
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
                
    async def start_gamestack(self, query: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/stack/st-game'
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def upadate_stack(self, query: str, score: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/stack/update-game'
        data = json.dumps({'score':score})
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def end_stack(self, query: str, score: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/stack/en-game'
        data = json.dumps({'score':score, 'multiplier':1})
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
                
    async def process_query(self, query: str):
        user = await self.user_authorization(query)
        if not user:
            self.log(
                f"{Fore.MAGENTA + Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.RED + Style.BRIGHT} Query ID May Invalid {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}or{Style.RESET_ALL}"
                f"{Fore.YELLOW + Style.BRIGHT} Clayton Server Down {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
            )
            return
        
        if user:
            self.log(
                f"{Fore.MAGENTA + Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} {user['user']['first_name']} {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} {user['user']['tokens']} $CLAY {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}] [ Ticket{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} {user['user']['daily_attempts']} {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}] [ Streak{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} {user['dailyReward']['current_day']} day {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
            )
            await asyncio.sleep(1)

            daily = user['dailyReward']['can_claim_today']
            if daily:
                claim = await self.daily_claim(query)
                if claim and claim['message'] == 'Daily reward claimed successfully':
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                        f"{Fore.GREEN + Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} {claim['tokens']} $CLAY {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} Ticket {claim['daily_attempts']} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                    f"{Fore.YELLOW + Style.BRIGHT} Is Already Claimed {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )
            await asyncio.sleep(1)

            for type in ['super-tasks', 'partner-tasks', 'default-tasks', 'daily-tasks']:
                tasks = await self.all_tasks(query, type)
                if tasks:
                    for task in tasks:
                        task_id = task['task_id']
                        is_completed = task['is_completed']
                        is_claimed = task['is_claimed']

                        requires_check = task['task']['requires_check']
                        if not requires_check:
                            if task and not is_completed and not is_claimed:
                                start = await self.start_tasks(query, task_id)
                                if start and start['message'] == 'Task completed':
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                        f"{Fore.GREEN + Style.BRIGHT}Is Started{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )

                                    claim = await self.claim_tasks(query, task_id)
                                    if claim and claim['message'] == 'Reward claimed':
                                        self.log(
                                            f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                            f"{Fore.GREEN + Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} {claim['reward_tokens']} $CLAY {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} {claim['game_attempts']} Ticket {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                        )
                                    else:
                                        self.log(
                                            f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                            f"{Fore.RED + Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                        )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                        f"{Fore.RED + Style.BRIGHT}Isn't Started{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )

                            elif task and is_completed and not is_claimed:
                                claim = await self.claim_tasks(query, task_id)
                                if claim and claim['message'] == 'Reward claimed':
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                        f"{Fore.GREEN + Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {claim['reward_tokens']} $CLAY {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {claim['game_attempts']} Ticket {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                        f"{Fore.RED + Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )
                        else:
                            if task and not is_completed and not is_claimed:
                                check = await self.check_tasks(query, task_id)
                                if check and check['message'] == 'Task completed':
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                        f"{Fore.GREEN + Style.BRIGHT}Is Checked{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )

                                    claim = await self.claim_tasks(query, task_id)
                                    if claim and claim['message'] == 'Reward claimed':
                                        self.log(
                                            f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                            f"{Fore.GREEN + Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} {claim['reward_tokens']} $CLAY {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} {claim['game_attempts']} Ticket {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                        )
                                    else:
                                        self.log(
                                            f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                            f"{Fore.RED + Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                        )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                        f"{Fore.RED + Style.BRIGHT}Isn't Checked{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )

                            elif task and is_completed and not is_claimed:
                                claim = await self.claim_tasks(query, task_id)
                                if claim and claim['message'] == 'Reward claimed':
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                        f"{Fore.GREEN + Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {claim['reward_tokens']} $CLAY {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {claim['game_attempts']} Ticket {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                        f"{Fore.RED + Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                await asyncio.sleep(1)

            user_achievements = await self.user_achievements(query)
            if user_achievements:
                for type, achievements in user_achievements.items():
                    if type in ["friends", "games", "stars"]:
                        for achievement in achievements:
                            level = str(achievement['level'])
                            is_completed = achievement['is_completed']
                            is_rewarded = achievement['is_rewarded']

                            if achievement and is_completed and not is_rewarded:
                                claim = await self.claim_achievements(query, type, level)
                                if claim and claim['reward']:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Achievments{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {type} {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} Level {level} {Style.RESET_ALL}"
                                        f"{Fore.GREEN + Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ][ Reward{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {claim['reward']} $CLAY {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Achievments{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {type} {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} Level {level} {Style.RESET_ALL}"
                                        f"{Fore.RED + Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )

            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Achievments{Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )
            await asyncio.sleep(1)

            user = await self.user_authorization(query)
            ticket = user['user']['daily_attempts']
            if ticket > 0:
                while ticket > 0:
                    game_stack = await self.start_gamestack(query)
                    if game_stack and game_stack['session_id']:
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Game Stack{Style.RESET_ALL}"
                            f"{Fore.GREEN + Style.BRIGHT} Is Started {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}] [ ID{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} {game_stack['session_id']} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                        )

                        score = 10
                        while score <= 90:
                            update = await self.upadate_stack(query, score)
                            if update and update['message'] == 'Score updated successfully':
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Game Stack{Style.RESET_ALL}"
                                    f"{Fore.GREEN + Style.BRIGHT} Success to Update {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}] [ Score{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {score} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Game Stack{Style.RESET_ALL}"
                                    f"{Fore.RED + Style.BRIGHT} Failed to Update {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                                break

                            score += 10
                            await asyncio.sleep(1)

                        if score == 100:
                            end = await self.end_stack(query, score)
                            if end:
                                ticket -= 1
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Game Stack{Style.RESET_ALL}"
                                    f"{Fore.GREEN + Style.BRIGHT} Is Completed {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {end['earn']} $CLAY {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {end['xp_earned']} XP {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Game Stack{Style.RESET_ALL}"
                                    f"{Fore.RED + Style.BRIGHT} Isn't Completed {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                    else:
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Game Stack{Style.RESET_ALL}"
                            f"{Fore.RED + Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                        break

                    await asyncio.sleep(2)

                    start = await self.start_clayball(query)
                    if start and start['session_id']:
                        ticket = start['attempts']
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Game Clayball{Style.RESET_ALL}"
                            f"{Fore.GREEN + Style.BRIGHT} Is Started {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}] [ ID{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} {start['session_id']} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                        )

                        for remaining in range(150, 0, -1):
                            print(
                                f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                                f"{Fore.YELLOW + Style.BRIGHT} {remaining} {Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT}Seconds to Complete Game{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}   ",
                                end="\r",
                                flush=True
                            )
                            await asyncio.sleep(1)

                        score = 1000
                        end = await self.end_clayball(query, score)
                        if end:
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Game Clayball{Style.RESET_ALL}"
                                f"{Fore.GREEN + Style.BRIGHT} Is Completed {Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {end['reward']} $CLAY {Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Game Clayball{Style.RESET_ALL}"
                                f"{Fore.RED + Style.BRIGHT} Isn't Completed {Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}              "
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Game Stack{Style.RESET_ALL}"
                            f"{Fore.RED + Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                        break

                if ticket == 0:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Play Game{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} No Ticket Remaining {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Play Game{Style.RESET_ALL}"
                    f"{Fore.YELLOW + Style.BRIGHT} No Ticket Remaining {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )

    async def main(self):
        try:
            await self.fetch_api_base_id()

            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            while True:
                self.clear_terminal()
                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)

                for query in queries:
                    query = query.strip()
                    if query:
                        await self.process_query(query)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)
                        seconds = random.randint(5, 15)
                        while seconds > 0:
                            formatted_time = self.format_seconds(seconds)
                            print(
                                f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                                f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                                end="\r"
                            )
                            await asyncio.sleep(1)
                            seconds -= 1

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    await asyncio.sleep(1)
                    seconds -= 1

        except FileNotFoundError:
            self.log(f"{Fore.RED}File 'query.txt' tidak ditemukan.{Style.RESET_ALL}")
            return
        except Exception as e:
            self.log(f"{Fore.RED+Style.BRIGHT}Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        bot = Clayton()
        asyncio.run(bot.main())
    except KeyboardInterrupt:
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
            f"{Fore.RED + Style.BRIGHT}[ EXIT ] Clayton - BOT{Style.RESET_ALL}",                                       
        )