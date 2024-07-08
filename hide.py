# path
hiddenPath = "File.7z"
pngPath = "LOGO.png"

fileHidden = open(hiddenPath, "rb")
filePNG = open(pngPath, "ab")
filePNG.write(fileHidden.read())

filePNG.close()
fileHidden.close()