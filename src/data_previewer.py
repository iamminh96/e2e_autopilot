import h5py
import numpy as np
import cv2
import matplotlib.pylab as pl
import utils


def preview(filename):
    log = h5py.File("../data/log/" + str(filename) + ".h5")
    cam = h5py.File("../data/camera/" + str(filename) + ".h5")

    frame_stamp = log['cam1_ptr']

    img = cam['X'][frame_stamp[70100]]
    angle = log['steering_angle'][65100]
    speed = log['speed'][65100]

    img = np.transpose(img, (1, 2, 0))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # img = cv2.resize(img, (80, 40), interpolation=cv2.INTER_CUBIC)
    pl.ion()
    my_img = pl.imshow(img)
    # print(len(frame_stamp))
    # fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    # out_vid = cv2.VideoWriter('../assets/demo.mp4', fourcc, 20.0, (320, 160))

    for i in range(55000, 160000, 20):
        img = cam['X'][frame_stamp[i]]
        angle = log['steering_angle'][i]
        speed = log['speed'][i]

        img = np.transpose(img, (1, 2, 0))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        utils.draw_path_on(img, speed, -angle / 10.0, color=(255, 0, 0))
        # cv2.imwrite("../temp/img{}.png".format(i), img)
        # print(img.shape)
        # img = cv2.flip(img, 180)
        # out_vid.write(img)
        # print(img.shape)

        # resize image
        # img = cv2.resize(img,(2*img.shape[1], 2*img.shape[0]), interpolation = cv2.INTER_CUBIC)
        # edges = cv2.Canny(cv2.cvtColor(img , cv2.COLOR_RGB2GRAY) ,50,150)
        # edges = cv2.GaussianBlur(edges , (3,3) , 0)
        # res = np.hstack((cv2.cvtColor(img , cv2.COLOR_RGB2GRAY) , edges))

        # log details

        if abs(angle) < 30:
            print('{}    Straight    {:.4f}    speed = {:.4f}'.format(i, angle, speed))
        elif angle < 0:
            print('{}    Left        {:.4f}    speed = {:.4f}'.format(i, angle, speed))
        else:
            print('{}    Right       {:.4f}    speed = {:.4f}'.format(i, angle, speed))

        # display

        my_img.set_data(img)
        pl.pause(.0001)
        pl.draw()

    # out_vid.release()


def main():
    preview(2)


if __name__ == '__main__':
    main()
