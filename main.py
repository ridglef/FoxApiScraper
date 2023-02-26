#Fox API downloader
import requests

#Get Number of foxes from https://randomfox.ca/ and check the thing that says fox count
fox_count = 123


progress = 1
while progress < fox_count + 1:
    print("Downloading Image " + str(progress))
    url = "https://randomfox.ca/images/" + str(progress) + ".jpg"
    response = requests.get(url)
    filename = (str(progress) + ".jpg")
    with open(filename, 'wb') as f:
        f.write(response.content)

    progress = progress + 1
