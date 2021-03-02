


import utils
import numpy as np
import json
import time


def kmeans(img,k):
    """
    Implement kmeans clustering on the given image.
    Steps:
    (1) Random initialize the centers.
    (2) Calculate distances and update centers, stop when centers do not change.
    (3) Iterate all initializations and return the best result.
    Arg: Input image;
         Number of K. 
    Return: Clustering center values;
            Clustering labels of all pixels;
            Minimum summation of distance between each pixel and its center.  
    """
    # TODO: implement this function.
    img = np.array(img)
    x_img,y_img = img.shape

    dist_list=np.array([]);centroid_list = np.array([]); xl = []
    counts, bins = np.histogram(img, range(256))
    # print(counts)
    x = counts.argsort()[-100:][::-1]               #gets the pixel values with highest number of counts i.e it contains global maxima and other local maximas
    for c, elem in enumerate(x):
        for i in range(c+1,x.size):
            xl.append([elem,x[i]])                  # creates combination of pixel centers
    # print(xl)
    for centroid in xl:
        centroid = np.array(centroid)
        if centroid[0] == centroid[1]:
            continue;
        while (True):
            dist = np.sqrt((img.reshape(x_img * y_img) - centroid[:, np.newaxis]) ** 2)
            nearest_centroid = np.argmin(dist, axis=0).reshape((x_img, y_img))
            new_centroid = np.array([img[nearest_centroid == k].mean(axis=0) for k in range(centroid.shape[0])])  # updating the center
            if (new_centroid.all() == centroid.all()):
                break;
            centroid = new_centroid
        min_dist = np.array(dist.min(axis=0), dtype='float64')
        # print(min_dist.sum(axis=0))
        dist_list = np.append(dist_list, min_dist.sum(axis=0))
        centroid_list = np.append(centroid_list,centroid)
    min_index = np.argmin(dist_list)
    centroid_list = centroid_list.reshape(-1,2)
    centroid = centroid_list[min_index,:].astype(int)

    dist = np.sqrt((img.reshape(x_img * y_img) - centroid[:, np.newaxis]) ** 2)
    nearest_centroid = np.argmin(dist, axis=0).reshape((x_img, y_img))

    return centroid.tolist(), nearest_centroid, int(dist_list[min_index])

def visualize(centers,labels):
    """
    Convert the image to segmentation map replacing each pixel value with its center.
    Arg: Clustering center values;
         Clustering labels of all pixels. 
    Return: Segmentation map.
    """
    # TODO: implement this function.
    labels[labels == 0] = centers[0];
    labels[labels == 1] = centers[1];            #assigning centroid pixel values

    return labels.astype(np.uint8);
     
if __name__ == "__main__":
    img = utils.read_image('lenna.png')
    k = 2

    start_time = time.time()
    centers, labels, sumdistance = kmeans(img,k)
    result = visualize(centers, labels)
    end_time = time.time()

    running_time = end_time - start_time
    print(running_time)

    centers = list(centers)
    with open('results/task1.json', "w") as jsonFile:
        jsonFile.write(json.dumps({"centers":centers, "distance":sumdistance, "time":running_time}))
    utils.write_image(result, 'results/task1_result.jpg')
