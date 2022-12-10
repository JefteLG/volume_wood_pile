import cv2

class ArucoMarkerCalculate():
    parameters = cv2.aruco.DetectorParameters_create()
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
    
    @staticmethod
    def aruco_perimeter_cm(corner):
        aruco_perimeter = cv2.arcLength(corner, True)
        # return aruco_perimeter/76
        return aruco_perimeter/40

    @classmethod
    def identify_aruco(cls, image):
        corners_images = []
        for i in image:
            corners, _, _ = cv2.aruco.detectMarkers(i, cls.aruco_dict, parameters=cls.parameters)
            corners_images.append(corners) if corners else ...
        return corners_images if len(corners_images) == 2 else False

    @classmethod
    def calculate_width_pile(cls, corners, img2_width):
        pixel_2_cm = cls.aruco_perimeter_cm(corners[1][0])
        object_dimension_pixel = cv2.selectROI("select the area", img2_width, showCrosshair=False)
        object_dimension_cm = (object_dimension_pixel[2]/pixel_2_cm, object_dimension_pixel[3]/pixel_2_cm)
        print("!!!")

        return object_dimension_cm[0]

    @classmethod
    def calculate_dimension_aruco_area(cls, corners):
        pixel_2_cm = cls.aruco_perimeter_cm(corners[0][0])
        aruco_dimension_pixel = (cv2.minAreaRect(corners[0][0])[1][0], cv2.minAreaRect(corners[0][0])[1][1])
        # cv2.polylines(img1_area, np.int0(corners[1][0]), True, (0, 255, 0), 2)
        aruco_dimension_cm = (aruco_dimension_pixel[0]/pixel_2_cm, aruco_dimension_pixel[1]/pixel_2_cm)

        print("!!!")

        return aruco_dimension_cm, aruco_dimension_pixel

    @classmethod
    def calculate_area(cls, corners, pixel_object):
        aruco_dimension_cm, aruco_dimension_pixel = cls.calculate_dimension_aruco_area(corners)
        aruco_area_pixel = aruco_dimension_pixel[0] * aruco_dimension_pixel[1]
        aruco_are_cm = aruco_dimension_cm[0] * aruco_dimension_cm[1]

        area_object_cm = (aruco_are_cm * pixel_object) / aruco_area_pixel

        print("!!!")

        return area_object_cm
































# if __name__ == "__main__":
#     img1_area = cv2.imread('E:\\IFTO\\Topicos_2\\Projeto\\aruco_marker\\test_02\\measure_object_size\\imgs\\l_armario\\img_01.jpg')
#     img2_width = cv2.imread('E:\\IFTO\\Topicos_2\\Projeto\\aruco_marker\\test_02\\measure_object_size\\imgs\\l_armario\\img_01.jpg')
#     # img3_segmentation = cv2.imread('E:\\IFTO\\Topicos_2\\Projeto\\aruco_marker\\test_02\\measure_object_size\\src\\img_segmentation\\img1b.png')
#     imgs = img1_area, img2_width
#     corners = ArucoMarker().identify_aruco(imgs)

#     # if corners:
#     #     # get width
#     #     object_width_pixel = cv2.selectROI("select the area", img1_area, showCrosshair=False)[2]
#     #     aruco_perimeter = cv2.arcLength(corners[1][0], True)
#     #     pixel_cm_ratio = aruco_perimeter/40
#     #     object_width_cm = object_width_pixel/pixel_cm_ratio

#     #     aruco_width_pixel = cv2.minAreaRect(corners[1][0])[1][0]
#     #     cv2.polylines(img1_area, np.int0(corners[1][0]), True, (0, 255, 0), 2)
#     #     aruco_width_cm = aruco_width_pixel / pixel_cm_ratio
#     #     cv2.imshow("imagem", img1_area)
#     #     key = cv2.waitKey(1)

#     #     # get area



#     # Segmentation


#     # Load Image
#     path_maskrcnn = os.getcwd()+'\src\maskrcnn'
#     sys.path.append(path_maskrcnn)
#     file = os.getcwd()+'\src\img_segmentation\img_origin\img.png'
#     img = cv2.imread(file)
#     print(sys.path)

#     path_model = os.getcwd()+'\src\model\mask_rcnn_object_0005.h5'
#     test_model, inference_config = load_inference_model(1, path_model)
#     image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


#     # Detect results
#     r = test_model.detect([image])[0]
#     colors = random_colors(80)


#     object_count = len(r["class_ids"])
#     a, b, _ = img.shape
#     black_img = np.zeros((a,b))

#     black_img = np.stack((black_img,)*3, axis=-1)

#     for i in range(object_count):
#         mask = r["masks"][:, :, i]
#         contours = get_mask_contours(mask)
#         black_img = draw_mask(black_img, contours, (255,255,255), 1)


#     # Create DIR
#     name_random = uuid.uuid1()
#     path = os.getcwd() + "\src\img_segmentation\img_history" + f"\{str(name_random)}"
#     os.mkdir(path)

#     img_origin = path + "\\img_origin.jpg"
#     img_segmented = path + "\\img_segmented.jpg"

#     # Save image
#     cv2.imwrite(img_origin, img)
#     cv2.imwrite(img_segmented, black_img)


#     count_white_pixel = np.sum(black_img[:,:,0] == 255)
#     count_black_pixel = np.sum(black_img[:,:,0] == 0)
