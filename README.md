How to Run the People Counter Project with YOLOv8

Requirements
Python 3.7 or higher
Python packages: ultralytics, opencv-python, pandas, cvzone
Install Dependencies
Run the following command to install all required packages:


pip install ultralytics opencv-python pandas cvzone
Required Files
main.py (main script for detection and tracking)
tracker.py (object tracking module)
yolov8s.pt (pretrained YOLOv8 model)
vidp.mp4 (input video file)
coco.txt (class names file)
Make sure all these files are in the same directory.

Running the Program
Run the following command in your terminal:


python main.py
The program will open a video window showing real-time detection and tracking of people in the video vidp.mp4. You will see bounding boxes, object IDs, and counts of people crossing a designated line going up and down.

Stopping the Program
Press the Esc key in the video window to stop the program and close the window.

This guide will help users run the project from start to finish and see the output of people counting on the video.

Code github by : https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa2w1RFNHM01oUXFUYng3RnhGdDltNzIyZ1lHUXxBQ3Jtc0tsOEV3MC1kZzV3eE5uUTZBRjk3amRBU2ZZc1JOWXhVSTIxeDlGRTBLWUlDTkpxZWREN1hEYWFMc0g3Y3dXd3hrTlV2ZFJtVEgyVUNBSGFNN0JGaFI4eGd4U29rQ1RmUG1CM0R5V0haeXh4eVMwRWI1Zw&q=https%3A%2F%2Fgithub.com%2Ffreedomwebtech%2Fyolov8peoplecounter&v=KxdKcmarZjs
