import os
from pyngrok import ngrok, conf

# Step 1: Permission error se bachne ke liye local path set karein
# Ye ngrok ko aapke desktop folder me hi download karega
bin_path = os.path.join(os.getcwd(), "ngrok_bin")
if not os.path.exists(bin_path):
    os.makedirs(bin_path)

pyngrok_config = conf.PyngrokConfig(ngrok_path=os.path.join(bin_path, "ngrok.exe"))

# Step 2: Auth Token set karein 
# (Mene aapka naya token update kar diya hai)
token = "38yKHeRG9bz7FkIw3r6kcMIhuNo_3bj4mQRiV4x57Rx1Ag2rw"
ngrok.set_auth_token(token, pyngrok_config=pyngrok_config)

print("Starting Ngrok tunnel...")

# Step 3: Tunnel start karein (Port 3000 ke liye - Frontend with Proxy)
try:
    url = ngrok.connect(3000, pyngrok_config=pyngrok_config).public_url
    print("\n" + "="*30)
    print(f"NGROK LIVE: {url}")
    print("="*30)
    print("\nIs terminal ko band MAT karna, warna link kaam nahi karega.")
except Exception as e:
    print(f"ERROR: {e}")
    print("\nAgar error aa raha hai, toh terminal ko 'Run as Administrator' karke chalaein.")

# Tunnel ko chalta rakhne ke liye pause
import time
while True:
    time.sleep(1)