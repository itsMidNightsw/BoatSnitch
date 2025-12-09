from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from PIL import Image
import io
import numpy as np
import matplotlib.pyplot as plt
##import getpass TODO



CLIENT_ID = input("client_id : ")
print("Client ID reçu.")

CLIENT_SECRET = input("client_secret : ")
print("Client secret reçu.")



# set up credentials
client = BackendApplicationClient(client_id=CLIENT_ID)
oauth = OAuth2Session(client=client)

# get an authentication token
token = oauth.fetch_token(
    token_url='https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token',
    client_secret=CLIENT_SECRET,
    include_client_id=True
)


bbox = [9.915802, 42.613701, 10.651816, 42.976512]
start_date = "2025-11-10"
end_date = "2025-12-09"
collection_id = "sentinel-1-grd"


evalscript = """
//VERSION=3
return [2*VV, dataMask];
"""


# request body/payload

json_request = {
  "input": {
    "bounds": {
      "bbox": [
        9.915802,
        42.613701,
        10.651816,
        42.976512
      ]
    },
    "data": [
      {
        "dataFilter": {
          "timeRange": {
            "from": f'{start_date}T00:00:00Z',
            "to": f'{end_date}T23:59:59Z'
          }
        },
        "processing": {
          "orthorectify": "false"
        },
        "type": "sentinel-1-grd"
      }
    ]
  },
  "output": {
    "width": 512,
    "height": 342.946,
    "responses": [
      {
        "identifier": "default",
        "format": {
          "type": "image/jpeg"
        }
      }
    ]
  },
  "evalscript": evalscript
}

# Set the request URL and headers
url_request = "https://sh.dataspace.copernicus.eu/api/v1/process"
headers_request = {
    "Authorization": f"Bearer {token['access_token']}"
}

# Send the request
response = oauth.post(url_request, headers=headers_request, json=json_request)


print(response)

# read the image as numpy array
image_arr = np.array(Image.open(io.BytesIO(response.content)))

# plot the image for visualization
plt.figure(figsize=(16,16))
plt.axis('off')
plt.tight_layout()
plt.imshow(image_arr)
plt.show()