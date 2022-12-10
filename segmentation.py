import cv2
import numpy as np
import os
import sys
from maskrcnn.m_rcnn import load_inference_model
from maskrcnn.visualize import get_mask_contours, draw_mask
import uuid

def create_directory():
    name_random = uuid.uuid1()
    path = os.getcwd() + "\img_segmentation\img_history" + f"\{str(name_random)}"
    os.mkdir(path)

    img_origin = path + "\\img_origin.jpg"
    img_segmented = path + "\\img_segmented.jpg"

    return img_origin, img_segmented
    
def segmentation(img):
    # Load Image
    path_maskrcnn = os.getcwd()+'\maskrcnn'
    sys.path.append(path_maskrcnn)

    path_model = os.getcwd()+'\model\mask_rcnn_object_0005.h5'
    test_model, inference_config = load_inference_model(1, path_model)
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    # Detect results
    r = test_model.detect([image])[0]


    object_count = len(r["class_ids"])
    a, b, _ = img.shape
    black_img = np.zeros((a,b))

    black_img = np.stack((black_img,)*3, axis=-1)

    for i in range(object_count):
        mask = r["masks"][:, :, i]
        contours = get_mask_contours(mask)
        black_img = draw_mask(black_img, contours, (255,255,255), 1)
    
    img_origin, img_segmented = create_directory()

    # Save image
    cv2.imwrite(img_origin, img)
    cv2.imwrite(img_segmented, black_img)


    count_white_pixel = np.sum(black_img[:,:,0] == 255)
    # count_black_pixel = np.sum(black_img[:,:,0] == 0)

    return count_white_pixel
