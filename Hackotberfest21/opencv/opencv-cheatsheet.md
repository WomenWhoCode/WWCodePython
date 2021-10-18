# OpenCV Cheatsheet

## Installing OpenCV

`pip install opencv-python`

<br>

## Working on images
	
1. **Read an image from path:**
	1. First upload image to use
		- Use wget to retrieve an image using the image's URL.
		- If using Google Colab, you can upload your image to Google Drive.
		  
			_Add the following to your Google Colab notebook to let Google Colab access your Google Drive:_
				 <br>
				`from google.colab import drive`

	2. The following code will read an image in from a path: 
		```
		path = "image.jpg"
		image = cv2.imread(path)
		cv2_imshow(image)
		```
		_If the image is large, use the OpenCV image resize command. [Sample Code](notebooks/Read_an_image_with_OpenCV.ipynb)_


2. **Image Resizing**
3. **Blurring an Image**
4. **Grayscaling of images**
	``` 
	image_to_greyscale=cv2.imread(path,0)
	cv2_imshow(image_to_greyscale)
	```

## Working with Videos 

1. **Play videos with OpenCv:** <br> 
	* Find a video to use 
	- If using Google Colab upload a video to your google drive to use. Add the following code to let google colab access your google drive:

		`from google.colab import drive` 

	- Find your video url and add into the wget code inside the double quotes: 

		`!wget = "put your video url here"`

	- Also put your ending part of the video url in the cap code inside the parentheses and quote: 
 
		`cap = cv2.VideoCapture('number part.mp4')`

	- It will play the video frame by frame. Warning it will be very slow on Google Colab.
	- [Sample code](notebooks/Play_A_Video_with_OpenCV.ipynb)

<br>

2. **Extract frames from a video**


