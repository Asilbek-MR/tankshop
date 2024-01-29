# from instabot import Bot
# bot = Bot()

# bot.login(username="asil_bekbaxodirov", password="asilbek99")

# bot.upload_photo("123123.jpg",caption="upodaet by fristly picture")



# from InstagramAPI import InstagramAPI

# def upload_video(username, password, video_path, caption):
#     api = InstagramAPI(username, password)
    
#     # Kirish
#     api.login()

#     # Video yuklash
#     if api.uploadVideo(video_path, caption=caption):
#         print("Video muvaffaqiyatli yuklandi!")
#     else:
#         print("Video yuklashda xatolik yuz berdi.")

#     # Chiqish
#     api.logout()

# # Sizning ma'lumotlaringizni kiriting
# username = "asil_bekbaxodirov"
# password = "asilbek99"
# video_path = "123123.jpg"
# caption = "birinchi bot tomonidan yuklangan video"

# # Skriptni ishga tushirish
# upload_video(username, password, video_path, caption)


from instapy_cli import client

username = 'asilbek_26_'
password = 'asilbek99'
video_path = 'chezol.mp4'
caption = "Upload video"

with client(username, password) as cli:
    cli.upload(video_path, caption)

# Your credentials and video path

# Run the upload function
# upload_video(username, password, video_path, caption)





