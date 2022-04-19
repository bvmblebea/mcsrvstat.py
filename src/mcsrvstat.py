from requests import get


class MinecraftServerStatus:
    def __init__(self, address: str):
        self.api = "https://api.mcsrvstat.us"
        self.bedrock_api = "https://api.mcsrvstat.us/bedrock"
        self.address = address
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Android; U; ru-RU) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/33.0",
            "Accept": "application/json"}
        self.server = self.get_server_info()

    def get_server_info(self, is_bedrock: bool = False):
        url = f"{self.api}/2/{self.address}"
        if is_bedrock:
            url = f"{self.bedrock_api}/2/{self.address}"
        return get(url, headers=self.headers).json()

    def lookup_server_icon(self):
        return get(
            f"{self.api}/icon/{self.address}",
            headers=self.headers).json()

    def check_server_status(self, is_bedrock: bool = False):
        url = f"{self.api}/simple/{self.address}"
        if is_bedrock:
            url = f"{self.bedrock_api}/simple/{self.address}"
        return get(url, headers=self.headers).text

    def debug_server(self):
        return get(
            f"{self.api}/debug/ping/{self.address}",
            headers=self.headers).json()

    def debug_bedrock_server(self):
        return get(
            f"{self.api}/debug/bedrock/{self.address}",
            headers=self.headers).json()

    def get_server_motd(
            self,
            is_raw: bool = True,
            is_html: bool = False,
            is_clean: bool = False):
        if is_raw:
            return self.server["motd"]["raw"]
        elif is_html:
            return self.server["motd"]["html"]
        elif is_clean:
            return self.server["motd"]["clean"]

    def get_server_plugins(self):
        if "plugins" in self.server:
            return self.server["plugins"]

    def get_server_debug(self):
        return self.server["debug"]

    def get_online_players(self):
        return self.server["players"]["online"]

    def get_max_players(self):
        return self.server["players"]["max"]

    def get_server_version(self):
        return self.server["version"]

    def get_server_ip(self):
        return self.server["ip"]

    def get_server_hostname(self):
        return self.server["hostname"]

    def get_server_protocol(self):
        return self.server["protocol"]

    def get_server_software(self):
        if "software" in self.server:
            return self.server["software"]

    def get_server_id(self):
        if "serverid" in self.server:
            return self.server["serverid"]

    def get_server_gamemode(self):
        if "gamemode" in self.server:
            return self.server["gamemode"]
