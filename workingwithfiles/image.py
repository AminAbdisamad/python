img = 'asalblue.png'
# copy image
with open(img, 'rb') as rImage:  # rb - Read Binary
    with open('updatedLogo.png', 'wb') as wImage:  # wb - Write Binary

        # for img in rImage:
        #     wImage.write(img)
        chunkSize = 4096  # size to read
        # Reading one segment at time
        ReadChunk = rImage.read(chunkSize)
        while len(ReadChunk) > 0:
            wImage.write(ReadChunk)
            ReadChunk = rImage.read(chunkSize)
