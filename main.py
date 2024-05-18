from pytube import YouTube

link = input("Enter YouTube link: ")
Y_tube = YouTube(link)

print(f'Video Title -> {Y_tube.title}')
stream = Y_tube.streams.filter(progressive="True", res="720p")
video = list(enumerate(stream))

for i in stream:
    print(i)


index = int(input("Enter index: "))
stream[index].download()
print("Download Complete")
