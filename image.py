import cv2

img = cv2.imread("solar-system.jpg")

sun = "SUN"
cv2.putText(
    img,
    sun,
    (90,70),
    fontFace = cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=1,
    color=(0,0,255)
)

mercury = "MERCURY"
cv2.putText(
    img,
    mercury,
    (120,190),
    fontFace = cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=0.3,
    color=(0,0,255)
)

venus = "VENUS"
cv2.putText(
    img,
    venus,
    (200,170),
    fontFace = cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=0.3,
    color=(0,0,255)
)

earth = "EARTH"
cv2.putText(
    img,
    earth,
    (290,160),
    fontFace = cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=0.3,
    color=(0,0,255)
)

m = "MARS"
cv2.putText(
    img,
    m,
    (390,170),
    fontFace = cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=0.3,
    color=(0,0,255)
)

j = "JUPITER"
cv2.putText(
    img,
    j,
    (510,60),
    fontFace = cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=0.5,
    color=(0,0,255)
)

s = "SATURN"
cv2.putText(
    img,
    s,
    (720,120),
    fontFace = cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=0.5,
    color=(0,0,255)
)


u = "URANUS"
cv2.putText(
    img,
    u,
    (940,130),
    fontFace = cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=0.5,
    color=(0,0,255)
)

n = "NEPTUNE"
cv2.putText(
    img,
    n,
    (1100,130),
    fontFace = cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=0.5,
    color=(0,0,255)
)



cv2.imshow("Display image:",img)
print(img)
cv2.waitKey(0)