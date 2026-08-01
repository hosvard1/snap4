
import requests

TOKEN = "8753863153:AAESoe2pWFsz_bEteF_hFZVM0l9tfwM61ZE"

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

print(requests.get(url).json())