from singbusbot import send_message_to_owner, get_url

def check_commands(message):
    message = message.split(" ")
    if message[0] == "/help":
        return "*Help Menu*\n/help - For a list of commands\n/about - About page\n/feedback - Send feedback straight to the developer by using this format - /feedback [text]"
    elif message[0] == "/about":
        return "*About Page*\nThank you for using SingBusBot. \nPlease do check out the code at https://github.com/errorfourten/singbusbot and new ideas are always welcome."
    elif message[0] == "/start":
        return "Welcome to Singapore Bus Bot! Just enter a bus stop code and find the next bus. For example, try entering 53009 or Bishan Int. /help for more information"
    elif message[0] == "/feedback":
        send_message_to_owner(" ".join(message[1:]))
        return "Thank you for your feedback! \"{}\"".format(" ".join(message[1:]))
    else:
        return False