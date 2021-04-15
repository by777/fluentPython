"""
   Tracking of rotating point.
   Rotation speed is constant.
   Both state and measurements vectors are 1D (a point angle),
   Measurement is the real point angle + gaussian noise.
   The real and the estimated points are connected with yellow line segment,
   the real and the measured points are connected with red line segment.
   (if Kalman filter works correctly,
    the yellow segment should be shorter than the red one).
   Pressing any key (except ESC) will reset the tracking with a different speed.
   Pressing ESC will stop the program.
"""

import cv2 as cv
from math import cos, sin, sqrt
import numpy as np

if __name__ == "__main__":

    img_height = 500
    img_width = 500
    # 创建卡尔曼滤波器对象
    kalman = cv.KalmanFilter(2, 1, 0)

    code = -1

    cv.namedWindow("Kalman")

    while True:
        # state(角度，△角度)
        state = 0.1 * np.random.randn(2, 1)

        #  转移矩阵A[1,1;0,1]
        kalman.transitionMatrix = np.array([[1., 1.], [0., 1.]])
        # 测量矩阵
        kalman.measurementMatrix = 1. * np.ones((1, 2))
        # 系统噪声方差阵
        kalman.processNoiseCov = 1e-5 * np.eye(2)
        # 量测噪声方差阵
        kalman.measurementNoiseCov = 1e-1 * np.ones((1, 1))
        # 后验错误估计协方差矩阵P
        kalman.errorCovPost = 1. * np.ones((2, 2))
        # x(0)初始化
        kalman.statePost = 0.1 * np.random.randn(2, 1)

        while True:
            def calc_point(angle):
                return (np.around(img_width / 2 + img_width / 3 * cos(angle), 0).astype(int),
                        np.around(img_height / 2 - img_width / 3 * sin(angle), 1).astype(int))


            # 1. 首先获取当前的真实状态
            # 跟踪点的角度
            state_angle = state[0, 0]
            # 跟踪点坐标statePt
            state_pt = calc_point(state_angle)

            # 2. 预测
            # 计算预测值，返回x'
            prediction = kalman.predict()
            # 预测点的角度
            predict_angle = prediction[0, 0]
            # 预测点坐标predictPt
            predict_pt = calc_point(predict_angle)

            # 3. 更新
            # measurement是量测值
            measurement = kalman.measurementNoiseCov * np.random.randn(1, 1)

            # generate measurement, z = z + H*x
            measurement = np.dot(kalman.measurementMatrix, state) + measurement

            measurement_angle = measurement[0, 0]
            measurement_pt = calc_point(measurement_angle)


            # plot points
            # 在屏幕上画个十字
            def draw_cross(center, color, d):
                cv.line(img,
                        (center[0] - d, center[1] - d), (center[0] + d, center[1] + d),
                        color, 1, cv.LINE_AA, 0)
                cv.line(img,
                        (center[0] + d, center[1] - d), (center[0] - d, center[1] + d),
                        color, 1, cv.LINE_AA, 0)


            img = np.zeros((img_height, img_width, 3), np.uint8)
            draw_cross(np.int32(state_pt), (255, 255, 255), 3)
            draw_cross(np.int32(measurement_pt), (0, 0, 255), 3)
            draw_cross(np.int32(predict_pt), (0, 255, 0), 3)

            cv.line(img, state_pt, measurement_pt, (0, 0, 255), 3, cv.LINE_AA, 0)
            cv.line(img, state_pt, predict_pt, (0, 255, 255), 3, cv.LINE_AA, 0)

            # 调用kalman这个类的correct方法得到加入观察值校正后的状态变量值矩阵
            kalman.correct(measurement)

            process_noise = sqrt(kalman.processNoiseCov[0, 0]) * np.random.randn(2, 1)
            state = np.dot(kalman.transitionMatrix, state) + process_noise

            cv.imshow("Kalman", img)

            code = cv.waitKey(100)
            if code != -1:
                break

        if code in [27, ord('q'), ord('Q')]:
            break

    cv.destroyWindow("Kalman")
