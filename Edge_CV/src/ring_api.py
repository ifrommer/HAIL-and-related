# -*- coding: utf-8 -*-
"""
Created on Tue May 16 17:50:19 2023
@author: ifrommer
RUN THIS 1st TO LOG IN AND SET UP TOKEN FOR FUTURE LOG-INS.
This is mostly from the library's test.py
Updating with changes I see there on 10/26/24
"""
import asyncio # new
import json
import getpass
from pathlib import Path
from pprint import pprint

# from ring_doorbell import Ring, Auth # old
from ring_doorbell import Auth, AuthenticationError, Requires2FAError, Ring #new

# old
# from oauthlib.oauth2 import MissingTokenError


#cache_file = Path("test_token.cache")
user_agent = "IanRing-1.0"  
cache_file = Path(user_agent + ".token.cache")

def token_updated(token) -> None:
    cache_file.write_text(json.dumps(token))


def otp_callback():
    auth_code = input("2FA code: ")
    return auth_code

async def do_auth():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    auth = Auth(user_agent, None, token_updated)
    try:
        await auth.async_fetch_token(username, password)
    except Requires2FAError:
        await auth.async_fetch_token(username, password, otp_callback())
    return auth


async def main() -> None:
    if cache_file.is_file():  # auth token is cached
        auth = Auth(user_agent, json.loads(cache_file.read_text()), token_updated)
        ring = Ring(auth)
        try:
            await ring.async_create_session()  # auth token still valid
        except AuthenticationError:  # auth token has expired
            auth = await do_auth()
    else:
        auth = await do_auth()  # Get new auth token
        ring = Ring(auth)

    await ring.async_update_data()

    print(ring.devices())
    await auth.async_close()


if __name__ == "__main__":
    asyncio.run(main())
    
""" OLD
def main():
    if cache_file.is_file():
        
        auth = Auth("NEW_PROJECT/1.0", json.loads(cache_file.read_text()), token_updated)
    else:
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        auth = Auth("NEW_PROJECT/1.0", None, token_updated)
        try:
            auth.fetch_token(username, password)
        except MissingTokenError:
            auth.fetch_token(username, password, otp_callback())

    ring = Ring(auth)
    ring.update_data()

    devices = ring.devices()
    pprint(devices)
    return ring

if __name__ == "__main__":
    ring = main()
"""