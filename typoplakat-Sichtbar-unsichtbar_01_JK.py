# # Set the size of the canvas
# newPage(1080, 1080)

# # Set the number of lines
# lineAmount = 70

# # Calculate the distance between each line
# distance = 1080 / lineAmount

# # Draw the lines
# for i in range(lineAmount):
#     stroke(0.2)
#     line((0.2, i * distance), (1080, i * distance))


# Canvas Größe
newPage(1080, 1080)


im = ImageObject()



# draw in the image
# the 'with' statement will create a custom context
# only drawing in the image object
with im:
    # set a size for the image
    size(1080, 1080)
    # draw something
    fill(1)
    rect(0, 0, width(), height())
    fill(0)
    fontSize(900)
    text("s", (300, 330))

# apply some filters
im.gaussianBlur(9)

# get the offset (with a blur this will be negative)
x, y = im.offset()
w, h = imageSize(im)

s = 15
# for x in range(0, int(w), int(s)):
#     # loop of the height of the image
#     for y in range(0, int(h), int(s)):
#         # get the color
#         color = imagePixelColor(im, (x, y))
#         if color:
#             r, g, b, a = color
#             # set the color
#             strokeWidth(r/100)
#             # draw some text
#             rect(x,y,50,50)
# # draw in the image in the main context
# image(im, (0+x, 0+y))

# Set the number of lines and segments

lineAmount = 90
segmentAmount = 10

# Distanz zu den Linien
lineDistance = 1080 / lineAmount
segmentDistance = 1080 / segmentAmount

# Linien werden gezeichnet
for i in range(lineAmount):
    stroke(0.2)
    
    for j in range(segmentAmount):
        color = imagePixelColor(im, (x, y))
        r, g, b, a = color
        strokeWidth(r)
        line((j * segmentDistance, i * lineDistance), ((j + 1) * segmentDistance, i * lineDistance))





