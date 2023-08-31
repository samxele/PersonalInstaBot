from instabot import Bot
myBot = Bot()

myBot = Bot(max_likes_to_like=1000)
myBot.login(username="samspythonbot", password="Samisawesome12")

print("Welcome to Sam's Instagram Bot")
print("What would you like to do?")
menuChoice = int(input("1.Follow a user\n2.Like a post\n3.Comment on a post\n4.Post a photo\n5.Like & comment on post\n"
                       "6.Send a DM\n"))

if menuChoice == 1:
    followAcc = input("Enter the name of the account you would like to follow: ")
    myBot.follow(followAcc)
elif menuChoice == 2:
    mediaLink = input("Enter link to the post: ")
    media = myBot.get_media_id_from_link(mediaLink)
    myBot.like(media)
elif menuChoice == 3:
    mediaLink = input("Enter link to the post: ")
    media = myBot.get_media_id_from_link(mediaLink)
    userComment = input("Enter comment: ")
    myBot.comment(media, userComment)
elif menuChoice == 4:
    imgName = input("Enter the name of the image you would like to post. Include .jpg/.jpeg/: ")
    capChoice = input("Would you like to post a caption? Y/N: ").upper()
    if capChoice == "Y":
        userComm = input("Enter caption: ")
        myBot.upload_photo(imgName,caption=userComm)
    elif capChoice == "N":
        myBot.upload_photo(imgName)
elif menuChoice == 5:
    mediaLink = input("Enter link to the post: ")
    media = myBot.get_media_id_from_link(mediaLink)
    userComment = input("Enter comment: ")
    myBot.comment(media, userComment)
    myBot.like(media)
elif menuChoice == 6:
    dmAcc = input("Enter account you would like to send a DM to: ")
    dmMess = input("Enter message: ")
    myBot.send_message(dmMess, dmAcc)

myBot.logout()
exit()