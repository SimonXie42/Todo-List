import cv2

# TODO 读取图片
img = cv2.imread('zzz1.png')
# 显示图片
# cv2.imshow('img', img)


# TODO 灰度转换
# gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 灰度显示
# cv2.imshow('gray',gray_img)
# 保存
# cv2.imwrite('gray1.png',gray_img)

# TODO 修改尺寸
# resize = cv2.resize(img,dsize=(200,200))
# 显示图片
# cv2.imshow('200x200',resize)
# 打印原大小
# print('未修改',img.shape)
# 打印修改后大小
# print('修改后',resize.shape)

# TODO 绘制矩形
# 坐标
# x, y, w, h = 100,100,100,100
# 绘制矩形
# cv2.rectangle(img, (x, y, x + w, y + h), color=(0, 0, 255), thickness=1)
# 绘制圆形
# cv2.circle(img, center=(x + w, w + h), radius=100, color=(255, 0, 0),thickness=2)
# 显示
# cv2.imshow('re_img',img)

# TODO 人脸检测
def face_detect_demo(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_detect = cv2.CascadeClassifier('D:/OPENCV/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
    face = face_detect.detectMultiScale(gray,1.01,5,0,(200,200),(800,800))
    for x, y, w, h in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
    cv2.imshow('result', img)

#face_detect_demo(img)
#while True:
#    if ord('q')==cv2.waitKey(0):
#       break

# TODO 摄像头/视频读取
cap = cv2.VideoCapture('3.mp4')

# 按键退出
while True:
    # 摄像头flag
    flag, frame = cap.read()
    if not flag:
        break
    face_detect_demo(frame)
#    cv2.imshow('video', frame)
    if ord('q') == cv2.waitKey(1):
        break
    # 等待
    # cv2.waitKey(0)'''

# TODO 截图
'''
cap = cv2.VideoCapture('porn.mp4')
flag = 1
num = 10
while cap.isOpened():
    ret_flag, Vshow = cap.read()
    cv2.imshow('test', Vshow)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('s'):
        cv2.imwrite('D:/Users/User/PycharmProjects/img' + str(num) + '.jpg', Vshow)
        print('------------------------------')
        print(str(num) + '.jpg' + ' has been stored in: D:/Users/User/PycharmProjects/img')
        num += 1

    elif k == ord(' '):
        break
        '''
# 解放内存
cv2.destroyAllWindows()
# cap.release()
