from pytube import YouTube

link = input("Enter YouTube link: ")
y_tube = YouTube(link)

print(f'Video Title -> {y_tube.title}')
stream = y_tube.streams.filter(progressive=True)
video = list(enumerate(stream))

for i in stream:
    print(i)
print("hnjhd")


print("=========================")
index=int(input("Enter index: "))
stream[index].download()
print("Download Complete")