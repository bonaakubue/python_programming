# Fetching multiple images in a website using asyncio
import requests
import asyncio

def fetch_image(url):
    response = requests.get(url)
    return response.content
async def download_images(urls):
    loop = asyncio.get_event_loop()
    tasks = []
    for url in urls:
        task = loop.run_in_executor(None, fetch_image, url)
        tasks.append(task)
    images = await asyncio.gather(*tasks)
    return images
async def main():
    image_urls = [
"https://images.pexels.com/photos/1595104/pexels-photo-1595104.jpeg",

"https://images.pexels.com/photos/221016/pexels-photo-221016.jpeg",

"https://images.pexels.com/photos/348689/pexels-photo-348689.jpeg"
    ]
    images = await download_images(image_urls)
    for i, image in enumerate(images, start=1):
        filename = f"image{i}.jpg"
        with open(filename, "wb") as file:
            file.write(image)
        print(f"Downloaded {filename}")

loop = asyncio.new_event_loop()
loop.run_until_complete(main())
