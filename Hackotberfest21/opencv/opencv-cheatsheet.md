# OpenCV Cheatsheet

## Installing OpenCV

`pip install opencv-python`

## Working on images
  
  1. Read an image from path
    a. !wget is command to get image from path. 
    b. cv2.imread is command to read the image. 
    c. cv2_imshow is command to show the image. 
    d. Example: 
#get image from path 
!wget "https://cdn.mos.cms.futurecdn.net/bsvoRNpjSTZt8BeiirNKmD.jpg"
#read an image from path
path="bsvoRNpjSTZt8BeiirNKmD.jpg"
img=cv2.imread(path)
#show the image
cv2_imshow(img)
  2. Image Resizing
  3. Blurring an Image
  4. Grayscaling of images

## Working with Images

  1. Play videos with OpenCv
  2. Extract frames from a video


