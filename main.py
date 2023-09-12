from instabot import Bot, utils
myBot = Bot() # Creation of bot object

myBot = Bot(max_likes_to_like=1000) # Limits the max number of posts the bot can like to be 1K

print("Welcome to Sam's Instagram Bot")

# Login to account
accUser = input("Enter username: ")
accPass = input("Enter password: ")
myBot.login(username=accUser, password=accPass)

menuChoice = 0 # Initializes menu choice to 0 so that the while loop is ran

while menuChoice != 100:
    print("What would you like to do?")
    menuChoice = int(
        input("1.Follow a user\n2.Like a post\n3.Comment on a post\n4.Post a photo\n5.Like & comment on post\n"
              "6.Send a DM\n7.Post story\n8.See those that aren't following back\n100.Logout and exit program\n"))

    # Follows User
    if menuChoice == 1:
        followAcc = input("Enter the name of the account you would like to follow: ")
        myBot.follow(followAcc)

    # Likes a post
    elif menuChoice == 2:
        mediaLink = input("Enter link to the post: ")
        media = myBot.get_media_id_from_link(mediaLink)
        myBot.like(media)

    # Comments on a post
    elif menuChoice == 3:
        mediaLink = input("Enter link to the post: ")
        media = myBot.get_media_id_from_link(mediaLink)
        userComment = input("Enter comment: ")
        myBot.comment(media, userComment)

    # Posts a photo
    elif menuChoice == 4:
        imgName = input("Enter the name of the image you would like to post. Include .jpg/.jpeg/: ")
        capChoice = input("Would you like to post a caption? Y/N: ").upper()
        if capChoice == "Y":
            userComm = input("Enter caption: ")
            myBot.upload_photo(imgName, caption=userComm)
        elif capChoice == "N":
            myBot.upload_photo(imgName)

    # Like and comment on a post
    elif menuChoice == 5:
        mediaLink = input("Enter link to the post: ")
        media = myBot.get_media_id_from_link(mediaLink)
        userComment = input("Enter comment: ")
        myBot.comment(media, userComment)
        myBot.like(media)

    # Send a dm to a user
    elif menuChoice == 6:
        dmAcc = input("Enter account you would like to send a DM to: ")
        picChoice = input("Would you like to send an immage? Y/N: ").upper()
        if picChoice == "Y":
            dmMess = input("Enter message: ")
            dmPic = input("Enter image name")
            myBot.send_message(dmMess, dmAcc)
            myBot.send_photo(dmAcc, dmPic)
        if picChoice == "N":
            dmMess = input("Enter message: ")
            myBot.send_message(dmMess, dmAcc)

    elif menuChoice == 7:
        imgName = input("Enter the name of the image you would like to post. Include .jpg/.jpeg/: ")
        myBot.upload_story_photo(imgName)

    # See those who aren't following you back
    elif menuChoice == 8:
        file = utils.file("config/non-followers.txt")
        nonFollowers = set(myBot.following) - set(myBot.followers) - myBot.friends_file.set
        nonFollowers = list(nonFollowers)
        nonFollowersNames = []

        for user in nonFollowers:
            name = myBot.get_username_from_user_id(user)
            nonFollowersNames.append(name)
            print(name)
            myBot.small_delay()
        file.save_list(nonFollowersNames)

if menuChoice == 100:
    myBot.logout()
    exit()
