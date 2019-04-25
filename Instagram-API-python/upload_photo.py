#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("film_x_frame", "icanCode69")
InstagramAPI.login()  # login

photo_path = '/Users/maxepstein/Dropbox/Art/experiments/IG_BOT/FOXNEWS_GIRLS.jpg'
caption = "beautiful ladies of fox"
InstagramAPI.uploadPhoto(photo_path, caption=caption)
