import cv2
from arucomarkercalculate import ArucoMarkerCalculate
from segmentation import segmentation


img1_area = cv2.imread('E:\\IFTO\\Topicos_2\\Projeto\\aruco_marker\\test_02\\measure_object_size\\src\\validate_algorith\\editado\\tst11.jpg')
img2_width = cv2.imread('E:\\IFTO\\Topicos_2\\Projeto\\aruco_marker\\test_02\\measure_object_size\\src\\validate_algorith\\editado\\tst6.jpg')

imgs = img1_area, img2_width

corners = ArucoMarkerCalculate.identify_aruco(imgs)

if corners:
    pixel_white = segmentation(img1_area)
    width_pile = ArucoMarkerCalculate.calculate_width_pile(corners, img2_width)
    area_pile = ArucoMarkerCalculate.calculate_area(corners, pixel_white)
    volume_pile = area_pile * width_pile
print("!!!")
































# print(volume_pile)


#     # get width
#     object_width_pixel = cv2.selectROI("select the area", img1_area, showCrosshair=False)[2]
#     aruco_perimeter = cv2.arcLength(corners[1][0], True)
#     pixel_cm_ratio = aruco_perimeter/40
#     object_width_cm = object_width_pixel/pixel_cm_ratio

#     aruco_width_pixel = cv2.minAreaRect(corners[1][0])[1][0]
#     cv2.polylines(img1_area, np.int0(corners[1][0]), True, (0, 255, 0), 2)
#     aruco_width_cm = aruco_width_pixel / pixel_cm_ratio
#     cv2.imshow("imagem", img1_area)
#     key = cv2.waitKey(1)

#     # get area

