from nonfig.sdk import Nonfig

options = {
  "app_id": "c1e8293f-58be-4c55-9db4-b1c39cbc1dcb", # Replace with your App ID
  "app_secret": "XuuhXorEZqeRTJjHumGCgnPuZMdQgVvu", # Replace with your App Secret
  "debug": True,
  "cache_enable": True,
  "cache_ttl": 60
}
nonfig = Nonfig(app_id="APP-ID", app_secret="APP-SECRET")
# configurations = nonfig.find_by_path("india")
configurations = nonfig.find_by_name("india/city")

print(configurations)

for configuration in configurations:
  print("------ \n")
  print(configuration)