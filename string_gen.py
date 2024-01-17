import pyrogram

print("You've selected pyrogram\n")
APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")
with pyrogram.Client("memory", api_id=APP_ID, api_hash=API_HASH) as app:
    session_str = app.export_session_string()
    if app.get_me().is_bot:
        user_name = input("Enter the username: ")
        msg = app.send_message(user_name, session_str)
    else:
        msg = app.send_message("me", session_str)
    msg.reply_text(
        "⬆️ This String Session is generated using https://trtechguide.wordpress.com\nPlease subscribe @trtechguide ",
        quote=True,
    )
    print(
        "please check your Telegram Saved Messages/user's PM for the StringSession "
    )