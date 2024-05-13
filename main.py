from pytube import YouTube

link = input("Enter YouTube link: ")
y_tube = YouTube(link)

print(f'Video Title -> {y_tube.title}')
# Nasim

print("Meaw")