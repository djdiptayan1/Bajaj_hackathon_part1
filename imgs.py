import requests
import json
from PIL import Image
from io import BytesIO

def search_photo_by_keyword(access_key, keyword):
    api_url = "https://api.unsplash.com/photos/random"
    headers = {
        "Accept-Version": "v1",
        "Authorization": f"Client-ID {access_key}",
    }

    params = {
        "query": keyword,
    }

    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200:
        photo_data = json.loads(response.text)
        photo_url = photo_data["urls"]["regular"]
        return photo_url
    else:
        print(f"Error: {response.status_code}")
        return None

def display_photo(photo_url):
    response = requests.get(photo_url)

    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image.show()
    else:
        print(f"Error downloading image: {response.status_code}")

if __name__ == "__main__":
    # Replace 'YOUR_ACCESS_KEY' with your actual Unsplash Access Key
    access_key = 'h6PEiVZeh5xVqYWN0ou9boqS2c2k1SoPinU9oSaC69c'

    if access_key == 'YOUR_ACCESS_KEY':
        print("Please replace 'YOUR_ACCESS_KEY' with your Unsplash Access Key.")
    else:
        keyword = input("Enter a keyword for the photo search: ")
        photo_url = search_photo_by_keyword(access_key, keyword)

        if photo_url:
            print(f"Photo URL: {photo_url}")
            display_photo(photo_url)
        else:
            print(f"No photo found for the keyword '{keyword}'.")
