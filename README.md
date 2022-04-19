# mcsrvstat.py
Web-API for [mcsrvstat.su](https://mcsrvstat.us) website to get info about minecraft server's

## Example
```python3
import mcsrvstat
mcsrvstat = mcsrvstat.MinecraftServerStatus(address="")
online_players = mcsrvstat.get_online_players()
print(f"-- Current online in server is::: {online_players}")
```
