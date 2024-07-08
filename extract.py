# path
png = "LOGO.png"
result = "output"

filePNG = open(png, "rb")
data = filePNG.read()
filePNG.close()

endBytes = b"\x49\x45\x4E\x44\xAE\x42\x60\x82" # PNG end bytes

data = data[data.find(endBytes)+len(endBytes):]
fileResult = open(result, "wb")
fileResult.write(data)

fileResult.close()