[app]

# (str) Title of your application
title = Friday AI

# (str) Package name
package.name = fridayai

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Application version
version = 0.1

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# इकडे आपण आवश्यक लायब्ररीज टाकल्या आहेत
requirements = python3,kivy==2.3.0,kivymd==1.2.0,groq,requests,certifi,urllib3,idna,charset-normalizer

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, RECORD_AUDIO

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android NDK directory (if empty, it will be automatically downloaded)
android.ndk_path = 

# (str) Android SDK directory (if empty, it will be automatically downloaded)
android.sdk_path = 

# (list) Android architectures to build for
# आपण फक्त एकाच आर्किटेक्चरसाठी बनवतोय जेणेकरून बिल्ड फेल होणार नाही
android.archs = arm64-v8a

# (bool) use poseidon to speed up the build
p4a.branch = master

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)

warn_on_root = 1
