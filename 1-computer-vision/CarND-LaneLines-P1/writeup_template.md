# **Finding Lane Lines on the Road** 

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps. First, I used the gaussian blur filter. Then, I converted the images to grayscale and applied the canny edge detection. The resulting image, I cropped to the region of interest and used it as an input to the hough transformation in order to get the hough lines. Finally I drew the resulting lines on the original image.  

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by an additional processing step. My approach is to fill the holes between the markings by connecting them and filling the hole closest to the car by extending the first line. 

If you'd like to include images to show how the pipeline works, here is how to include an image: 

![alt text][image1]


### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when the car makes a lane change. Then the region of interest would reflect the actual region of interest. 

Another shortcoming could be darker colors of lane markings possibly in other countries or in construction sites.


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to train a neural network on labeled lane markings of different colors and apply it ot the images.

Another potential improvement could be to handengineer the region of interest based on steering angles.
