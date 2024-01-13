# asyncNewmanga.py
Async library for newmanga.org
![b](https://github.com/aminobotskek/newmanga/assets/94906343/c057b187-2821-4bf5-9305-c466065e2686)

# Install
```
git clone https://github.com/aminobotskek/asyncNewmanga
```


### Example
```python3
import asyncNewmanga
import asyncio
async def main():
	client=asyncNewmanga.asyncNewmanga()
	await client.login(email="",password="")
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
