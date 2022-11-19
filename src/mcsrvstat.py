from requests import get


class McSrvStat:
	def __init__(
			self,
			address: str,
			is_bedrock: bool = False) -> None:
		self.api = "https://api.mcsrvstat.us"
		self.bedrock_api = "https://api.mcsrvstat.us/bedrock"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Android; U; ru-RU) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/33.0",
			"accept": "application/json"
		}
		self.address = address
		self.is_bedrock = is_bedrock
		self.server = self.get_server_info()

	def get_server_info(self) -> dict:
		url = f"{self.api}/2/{self.address}"
		if self.is_bedrock:
			url = f"{self.bedrock_api}/2/{self.address}"
		return get(url, headers=self.headers).json()

	def lookup_server_icon(self) -> dict:
		return get(
			f"{self.api}/icon/{self.address}",
			headers=self.headers).json()

	def check_server_status(self) -> str:
		url = f"{self.api}/simple/{self.address}"
		if self.is_bedrock:
			url = f"{self.bedrock_api}/simple/{self.address}"
		return get(url, headers=self.headers).text

	def debug_server(self) -> dict:
		return get(
			f"{self.api}/debug/ping/{self.address}",
			headers=self.headers).json()

	def debug_bedrock_server(self) -> dict:
		return get(
			f"{self.api}/debug/bedrock/{self.address}",
			headers=self.headers).json()

	def get_server_motd(
			self,
			is_raw: bool = False,
			is_html: bool = False,
			is_clean: bool = False) -> list:
		if is_raw:
			return self.server["motd"]["raw"]
		if is_html:
			return self.server["motd"]["html"]
		if is_clean:
			return self.server["motd"]["clean"]

	def get_server_plugins(self) -> str:
		if "plugins" in self.server:
			return self.server["plugins"]

	def get_server_debug(self) -> str:
		return self.server["debug"]

	def get_online_players(self) -> int:
		return self.server["players"]["online"]

	def get_max_players(self) -> int:
		return self.server["players"]["max"]

	def get_server_version(self) -> int:
		return self.server["version"]

	def get_server_ip(self) -> str:
		return self.server["ip"]

	def get_server_hostname(self) -> str:
		return self.server["hostname"]

	def get_server_protocol(self) -> int:
		return self.server["protocol"]

	def get_server_software(self) -> str:
		if "software" in self.server:
			return self.server["software"]

	def get_server_id(self) -> str:
		if "serverid" in self.server:
			return self.server["serverid"]

	def get_server_gamemode(self) -> str:
		if "gamemode" in self.server:
			return self.server["gamemode"]
		
