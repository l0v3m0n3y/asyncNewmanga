import aiohttp,asyncio
class asyncNewmanga():
	def __init__(self):
		self.session = aiohttp.ClientSession()
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
		self.api='https://api.newmanga.org/v2'
		self.api_v3='https://api.newmanga.org/v3'
		self.user_id=None
	def __del__(self):
		try:
		          loop = asyncio.get_event_loop()
		          loop.create_task(self._close_session())
		except RuntimeError:
		          loop = asyncio.new_event_loop()
		          loop.run_until_complete(self._close_session())
	async def _close_session(self):
		if not self.session.closed: await self.session.close()
	async def get_account_info(self):
		async with self.session.get(f'{self.api}/user',headers=self.headers) as req:
			return await req.json()
	async def login(self,email,password):
	    data={"credentials":email,"password":password}
	    async with self.session.post(f'{self.api}/login',json=data,headers=self.headers) as req:
	    	self.headers['Cookie']=req.headers['set-cookie']
	    	self.user_id=self.get_account_info()['id']
	    	return await req.json()
	async def friendship_request(self,user_id):
	    async with self.session.post(f'{self.api}/user/friendships/requests?user_id={user_id}',headers=self.headers) as req:
	    	return await req.json()
	async def register(self,login,email,password):
	    data={"login":login,"email":email,"password":password}
	    async with self.session.post(f'{self.api}/register',json=data,headers=self.headers) as req:
	    	return req.text
	async def forgot_password(self,credentials):
	    data={"credentials":credentials}
	    async with self.session.post(f'{self.api}/forgot_password',json=data,headers=self.headers) as req:
	    	return await req
	async def slides(self):
	    async with self.session.get(f'{self.api}/slides',headers=self.headers) as req:
	    	return await req.json()
	async def projects_trending(self):
	    async with self.session.get(f'{self.api}/projects/trending',headers=self.headers) as req:
	    	return await req.json()
	async def tags(self):
	    async with self.session.get(f'{self.api}/tags',headers=self.headers) as req:
	    	return await req.json()
	async def user_subscriptions(self):
	    async with self.session.get(f'{self.api}/user/branches/subscriptions',headers=self.headers) as req:
	    	return await req.json()
	async def user_notifications(self):
	    async with self.session.get(f'{self.api}/user/notifications/',headers=self.headers) as req:
	    	return await req.json()
	async def user_translators(self):
	    async with self.session.get(f'{self.api}/user/translators',headers=self.headers) as req:
	    	return await req.json()
	async def genres(self):
	    async with self.session.get(f'{self.api}/user/translators',headers=self.headers) as req:
	    	return await req.json()
	async def my_statistic(self):
	    async with self.session.get(f'{self.api}/users/{self.user_id}/statistic',headers=self.headers) as req:
	    	return await req.json()
	async def my_badges(self):
	    async with self.session.get(f'{self.api}/users/{self.user_id}/badges',headers=self.headers) as req:
	    	return await req.json()
	async def my_activity(self,scope):
	    async with self.session.get(f'{self.api}/users/{self.user_id}/activity?scope={scope}',headers=self.headers) as req:
	    	return await req.json()
	async def projects_updates(self,only_bookmarks:bool=False,page:int=1,size:int=5):
	    async with self.session.get(f'{self.api}/projects/updates?only_bookmarks={only_bookmarks}&page={page}&size={size}',headers=self.headers) as req:
	    	return await req.json()
	async def projects_popular(self,size:int=5):
	    async with self.session.get(f'{self.api}/projects/popular?size={size}',headers=self.headers) as req:
	    	return await req.json()
	async def search(self,query,size:int=5,page:int=1):
	    async with self.session.get(f'{self.api}/teams/search?query={query}b&page={page}&size={size}',headers=self.headers) as req:
	    	return await req.json()
	async def edit_profile(self,site:str=None,about:str=None,gender:str=None):
	    data={}
	    if gender:data['gender']=gender
	    if about:data['about']=about
	    if site:data['site']=site
	    async with self.session.patch(f'{self.api}/user',json=data,headers=self.headers) as req:
	    	return await req.json()
	async def send_comment(self,patch,text,parent_id:int=None):
	    data={"html":text}
	    if parent_id:data['parent_id']=parent_id
	    async with self.session.post(f'{self.api}/projects/{patch}/comments',json=data,headers=self.headers) as req:
	    	return await req.json()
	async def get_comments(self,patch):
	    async with self.session.get(f'{self.api}/projects/{patch}/comments?sort_by=new',headers=self.headers) as req:
	    	return await req.json()
	async def bookmark(self,type,patch):
	    data={"type":type}
	    async with self.session.post(f'{self.api}/projects/{patch}/bookmark',json=data,headers=self.headers) as req:
	    	return await req.json()
	async def report(self,reason,description,patch):
	    data={"reason":reason,"description":description}
	    async with self.session.post(f'{self.api}/projects/{patch}/report',json=data,headers=self.headers) as req:
	    	return await req.json()
	async def heart(self,comment_id,value:bool=True):
	    data={"value":value}
	    async with self.session.post(f'{self.api}/chapters/{comment_id}/heart',json=data,headers=self.headers) as req:
	    	return await req.json()
	async def mark(self,comment_id,value:bool=True):
	    data={"value":value}
	    async with self.session.post(f'{self.api}/comments/{comment_id}/mark',json=data,headers=self.headers) as req:
	    	return await req.json()
	async def get_friendships_requests(self):
	    async with self.session.get(f'{self.api}/user/friendships/requests?outgoing=true',headers=self.headers) as req:
	    	return await req.json()
	async def get_team_requests(self):
	    async with self.session.get(f'{self.api}/user/teams/requests',headers=self.headers) as req:
	    	return await req.json()
	async def get_team_invites(self):
	    async with self.session.get(f'{self.api}/user/team_invites',headers=self.headers) as req:
	    	return await req.json()