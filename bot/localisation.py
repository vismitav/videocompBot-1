#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "HelloβοΈ, \n\nThis is a Video Compress Bot \n\n<b>π― sent me any Telegram big file I Will compress a small file</b> \n\nπSupport Group :@Binary_bots_Support \n\nCLICK /help FOR MORE DETAILS \n\nPowered By BINARY Tech π±π°"

    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "π₯ Downloading... π₯ \n"
    
    UPLOAD_START = "π€ Uploading... π€ \n"
    
    COMPRESS_START = "π Trying to compress... π"
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "π₯ Downloaded in {}\n\nπ Compressed in {}\n\nπ€ Uploaded in {}\n\nBy @mhd_thanzeer"

    COMPRESS_PROGRESS = "β° ππ¬π­π’π¦ππ­π’π¨π§: {}\nπ Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "β Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "β Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "β Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "β οΈ Already one Process going on! β οΈ \n\nCheck Live Status on Updates Channel."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hi, I am Video Compressor Bot \n\n1. Send me your telegram big video file \n2. Reply to the file with: `/compress 50` \n\n [π ππ π§πππ‘π­πππ₯](https://t.me/mhd_thanzeer)."
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
