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
    print("##########----RESULTADO----##########")
    print("VOLUME DA PILHA")
    volume_pile = f'{volume_pile:.2f}'
    print(f'{float(volume_pile):,}cm3')
    print("#####################################")

