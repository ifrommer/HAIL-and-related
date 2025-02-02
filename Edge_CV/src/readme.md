### Info
**Login credentials**
Run ring_api.py first.  See below - may need to do this from Anaconda prompt.


When you run ring_api.py it checks if there is a test_token.cache file already in the local folder.  If so, it tries to use this.  If it has expired, delete it.  Then running ring_api.py will cause a new login prompt to occur with Python, complete with 2FA, so have your cell phone ready.

After running ring_api.py, you should be able to run ring_my_work_1.py.  

Was getting errors in downloading videos from Son. on 6/7/24. First with 2FA through the code, 2nd just simply logging in on the browser at Son.

Tried updating the code on 10/26/24.  The test.py on the repo now uses asyncio.  This is what is in my ring_api.py now.  1st I got an async error.  Then I ran
it from an Anaconda prompt and got:
AttributeError: 'Auth' object has no attribute 'async_fetch_token'
No idea what this is.

Got it to work by upgrading the ring_doorbell package and then running from Anaconda prompt again:  python ring_api.py

You can also do things from their CLI - see https://github.com/python-ring-doorbell/python-ring-doorbell
I'm having trouble connecting my old code ring_my_work_1.py to this new way of logging in.
I can get ring_api.py to run from Spyder by having it launch in its own terminal window with interactivity.
But I can't get any of the follow-on commands to work then.  
May be stuck with CLI.

