# KMeansClustering and ImageDenoising
This project consists of two separate tasks- `K-Means Clustering for Image Segmentation` and `Image Denoising using Median Filter`.
## Task 1. K-Means Clustering for Image Segmentation
The goal of this task is to use K-Means Clustering to segment the image `\lenna.png`. Specifically by setting K = 2 and the clustering is only based on the Euclidean distance of pixel values. The output is such that the sum of distances between pixel values and their corresponding centers is minimum. The logic of clustering is implemented in `\kmeans` function which outputs the centers and sum of distances of the best clustering in `\.json` file. The `\visualize` function then uses this output to create a segmentation map replacing the pixel values with the corresponding centers. The program only outputs the best clustering result out of all the possibilities (since initialization of centers in K-means is random, the final result could vary).
![image](https://user-images.githubusercontent.com/36618302/109547484-6a7b9100-7a99-11eb-9092-52093dd91a3f.png)

Input Image (left) and Segmentation Map (right)
## Task 2. Image Denoising
The goal of this task is to use median filter for image denoising. The filter size is set as 3. To ensure the output is of same size as the input it wass required to do zero-padding first. The `\median-filter` function implements median filter on `\lenna-noise.png` and outputs the denoised image. The `\mse` function calculates the Mean Square Error of the result and the provided image "\lenna-denoised.png" for reference, it then outputs the MSE in `\.json` file.
![image](https://user-images.githubusercontent.com/36618302/109548034-2341d000-7a9a-11eb-92e3-09715c87f12f.png)
![image](https://user-images.githubusercontent.com/36618302/109548063-2ccb3800-7a9a-11eb-9a2e-c23af432ac37.png)

Lenna image with noise (left)        Lenna image denoised (right)
