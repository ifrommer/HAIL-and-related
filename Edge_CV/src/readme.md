### Info
**Login credentials**
When you run ring_api.py it checks if there is a test_token.cache file already in the local folder.  If so, it tries to use this.  If it has expired, delete it.  Then running ring_api.py will cause a new login prompt to occur with Python, complete with 2FA, so have your cell phone ready.