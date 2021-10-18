
# OpenCV Cheatsheet

## Installing OpenCV
    pip install opencv-python

## Import OpenCV
    import cv2

## Working on images
  
  ### 1. Read an image from path
     cv2.imread(path,flag)
  
  **Parameter:**
  - path: Location of image to be read as a string.
  - flag(optional): flag value, that defines the format image to be read. Default value is 1(CV2.IMREAD_COLOR).It value varies from 0, 1, -1.
  
  [Sample Code](https://github.com/JeevaSaravanan/OpenCv-GitCheatSheet/blob/main/OpenCV-ReadImage.ipynb)
  
  ### 2. Image Resizing
      cv2.resize(image,(width,height),fx,fy,interpolation)
  **Parameter:**
  - image: source image read
  - (width,height) : dimension as tuple
  - fx(optional) : scaling along horizontal axis.
  - fy(optional) : scaling along vertical axis.
  - interpolation(optional) : flag value that defines the any following method -INTER_NEAREST, INTER_LINEAR, INTER_AREA, INTER_CUBIC.
  
  [Sample Code](https://github.com/JeevaSaravanan/OpenCv-GitCheatSheet/blob/main/OpenCV%20-%20Resize%20Image.ipynb)
      
  ### 3. Blurring an Image
  **Gaussian Blur:**
  
    cv2.GaussianBlur(image,ksize,sigmaX,sigmaY,borderType)
  **Parameter:**
  - image: source image read
  - ksize: kernel size as tuple
  - sigmaX(optional): kernel standard deviation along x-axis
  - sigmaY(optional): kernel standard deviation along y-axis
  - borderType: specifies image boundaries
  
  **Median Blur:**
  
      cv2.medianBlur(image, ksize)
  **Parameter:**
  - image : source image read
  - ksize: kernel size as integer
  
  **Bilateral Blur:**
  
      cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace, borderType)
  **Parameter:**
  - image: source image read
  - d: diameter of pixel neighbourhood as integer
  - sigmaColor: filter sigma in the color space as integer
  - sigmaSpace: filter sigma in the coordinate space.
  - borderType: specifies image boundaries 
  
  [Sample Code](https://github.com/JeevaSaravanan/OpenCv-GitCheatSheet/blob/main/OpenCV%20-%20Blur%20Image.ipynb)
  
  ### 4. Grayscaling of images
      cv2.cvtColor(image,colorcode)
  **Parameter:**
  - image: source image read
  - colorcode: color space conversion code.
  for grayscale colorcode is *cv2.COLOR_BGR2GRAY*
  
[Sample Code](https://github.com/JeevaSaravanan/OpenCv-GitCheatSheet/blob/main/OpenCV%20-%20Grayscale%20Image.ipynb)

## Working with Images

  1. Play videos with OpenCv
  2. Extract frames from a video


