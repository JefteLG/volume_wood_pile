import cv2

class ArucoMarkerCalculate():
    parameters = cv2.aruco.DetectorParameters_create()
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
    
    @staticmethod
    def aruco_perimeter_cm(corner):
        aruco_perimeter = cv2.arcLength(corner, True)
        return aruco_perimeter/76 # Aruco 19x19
        # return aruco_perimeter/40 # Aruco 10x10

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

        return object_dimension_cm[0]

    @classmethod
    def calculate_dimension_aruco_area(cls, corners):
        pixel_2_cm = cls.aruco_perimeter_cm(corners[0][0])
        aruco_dimension_pixel = (cv2.minAreaRect(corners[0][0])[1][0], cv2.minAreaRect(corners[0][0])[1][1])
        # cv2.polylines(img1_area, np.int0(corners[1][0]), True, (0, 255, 0), 2)
        aruco_dimension_cm = (aruco_dimension_pixel[0]/pixel_2_cm, aruco_dimension_pixel[1]/pixel_2_cm)

        return aruco_dimension_cm, aruco_dimension_pixel

    @classmethod
    def calculate_area(cls, corners, pixel_object):
        aruco_dimension_cm, aruco_dimension_pixel = cls.calculate_dimension_aruco_area(corners)
        aruco_area_pixel = aruco_dimension_pixel[0] * aruco_dimension_pixel[1]
        aruco_are_cm = aruco_dimension_cm[0] * aruco_dimension_cm[1]

        area_object_cm = (aruco_are_cm * pixel_object) / aruco_area_pixel

        return area_object_cm
