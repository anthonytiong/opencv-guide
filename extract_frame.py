# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
import cv2
import os


def video_to_frame(video_path, frame_ext='png', frame_dirname="video-frame", approx_frame_num=None):
    """Extract video frames into a folder.
    Args:
        video_path = {str}, location of the video.
        frame_ext = {str}, saved images extension, default: "png".
        frame_dirname = {str}, folder to save the video frames, default: "video-frame".
        approx_frame_num = {int}, (approx.) number of saved frames, default: all frames.
    """

    vidcap = cv2.VideoCapture(video_path)

    # Name and directory
    vidname = video_path.split("/")[-1].split(".")[0]
    frame_dir = os.path.join(".", frame_dirname)

    if not os.path.isdir(frame_dir):
        os.makedirs(frame_dir)
        print("Creating {} directory...".format(frame_dirname))

    # Find the total number of video frames
    total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    print("The video consists of {} frames.".format(total_frames))

    if approx_frame_num is None:
        approx_frame_num = total_frames

    save_rate = int(total_frames / approx_frame_num)

    # Extract video frames
    step = 0

    while vidcap.isOpened():
        ret, frame = vidcap.read()

        if ret:
            step += 1
            if step % save_rate == 0:
                frame_name = "{}_{}.{}".format(vidname, step, frame_ext)
                frame_path = os.path.join(frame_dir, frame_name)
                cv2.imwrite(frame_path, frame)
                print("Saving {}".format(frame_name))
        else:
            break

    cv2.destroyAllWindows()
    vidcap.release()

    # Expected vs actual number of saved frames
    num_frame_saved = int(step / save_rate)
    print("Approx. saved frames: {}".format(approx_frame_num))
    print("Actual saved frames: {}".format(num_frame_saved))


def main():
    # demo
    video_name = input("Video name including extension: ")
    frame_ext = input("Image extension? Eg. png, jpeg: ")
    frame_dirname = input("Directory name to save the image: ")
    approx_frame_num = int(input("Number of images to be extracted: "))
    video_path = os.path.join(os.getcwd(), "video/", video_name)

    video_to_frame(video_path, frame_ext=frame_ext, frame_dirname=frame_dirname,
                   approx_frame_num=approx_frame_num)


if __name__ == "__main__":
    main()
