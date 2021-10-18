# OpenCV Cheatsheet

## Installing OpenCV

`pip install opencv-python`

## Working on images
  
  1. Read an image from path: <br>
    a. First, find image to use
      - Use wget to retrieve an image using the image's URL.
      - If using Google Colab, you can upload your image to Google Drive. 
      
        Add the following to your Google Colab notebook to let Google Colab access your Googel Drive: <br>
        `from google.colab import drive`

      b. The following code will read an image in from a path: 
      ```
      path = "image.jpg"
      image = cv2.imread(path)
      cv2_imshow(image)
      ```
      If the image is large, use the OpenCV image resize command. [Sample Code](https://github.com/cosmeow/WWCodePython)

  2. Image Resizing
  3. Blurring an Image
  4. Grayscaling of images

## Working with Images

  1. Play videos with OpenCv
  2. Extract frames from a video


