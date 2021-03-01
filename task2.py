"""
Denoise Problem
(Due date: Nov. 25, 11:59 P.M., 2019)
The goal of this task is to denoise image using median filter.

Do NOT modify the code provided to you.
Do NOT import ANY library or API besides what has been listed.
Hint: 
Please complete all the functions that are labeled with '#to do'. 
You are suggested to use utils.zero_pad.
"""


import utils
import numpy as np
import json

def median_filter(img):
    """
    Implement median filter on the given image.
    Steps:
    (1) Pad the image with zero to ensure that the output is of the same size as the input image.
    (2) Calculate the filtered image.
    Arg: Input image. 
    Return: Filtered image.
    """
    # TODO: implement this function.
    filter_size = 3
    img_padded = np.array(utils.zero_pad(img, pwx=1, pwy=1))           #padding the image with one row and column in beginning and end
    filtered_img = img
    for row in range(img_padded.shape[0]-filter_size+1):
        for col in range(img_padded.shape[1]-filter_size+1):
            med_list = np.array([])                                    #list [3x3] that stores the values among which the median is found
            for rk in range(filter_size):
                for ck in range(filter_size):
                    med_list = np.append(med_list, img_padded[row+rk][col+ck])
            filtered_img[row][col] = np.median(med_list)               #median of the filter kernel is found and stored in its center

    return filtered_img.astype(np.uint8)
def mse(img1, img2):
    """
    Calculate mean square error of two images.
    Arg: Two images to be compared.
    Return: Mean square error.
    """    
    # TODO: implement this function.
    img1 = np.array(img1); img2 = np.array(img2)
    squared_diff = (img1 - img2) ** 2                                  #finds the square of difference in each pixel values of given two images
    mean_err = np.mean(squared_diff)                                   #finds the mean of this squared differences

    return mean_err

if __name__ == "__main__":
    img = utils.read_image('lenna-noise.png')
    gt = utils.read_image('lenna-denoise.png')

    result = median_filter(img)
    error = mse(gt, result)

    with open('results/task2.json', "w") as file:
        json.dump(error, file)
    utils.write_image(result,'results/task2_result.jpg')


