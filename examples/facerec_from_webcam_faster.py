import subprocess
import pyglet
import cv2
import face_recognition
# from pptx import Presentation
import os
# import pdb
from pathlib import Path
# pdb.set_trace()

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one
list_of_faces = []
names_of_faces = []
unknown_face_encodings = []
video_capture = cv2.VideoCapture(0)
image_path = "web/known_faces"
unknown_path = "web/unknown_faces"
for file in os.listdir(image_path):
    filename, file_extension = os.path.splitext(file)
    if file_extension == ".jpg":
        face_image = face_recognition.load_image_file(image_path + "/" + file)
        face_encoding = face_recognition.face_encodings(face_image)[0]
        list_of_faces.append(face_encoding)
        names_of_faces.append(filename)
    
print(names_of_faces)

# for file in os.listdir(unknown_path):
    # print(file)
    # filename, file_extension = os.path.splitext(file)
    # if file_extension == ".jpg":
        # unknown_face_image = face_recognition.load_image_file(unknown_path + "/" + file)
        # unknown_face_encoding = face_recognition.face_encodings(unknown_face_image)[0]
        # unknown_face_encodings.append(unknown_face_encoding)

# print(len(unknown_face_encodings))
# Load a sample picture and learn how to recognize it.
#obama_image = face_recognition.load_image_file("web/known_faces/obama.jpg")
#obama_face_encoding = face_recognition.face_encodings(obama_image)[0]


# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
sound = pyglet.media.load('LowerQTrim.wav', streaming=False)
i = 0
j = 0
k = 0
blue = (255, 0, 0)
red = (0, 0, 255)
is_open = 0
sound_played = 0 
exist = 1
exist_name = 1  
# orange = (0, 191, 255)
color = red
while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    name = "Unknown"
    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            sound_played = 0
            face_object = [face_encoding, sound_played]
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces(list_of_faces, face_encoding)
            print(match)
            if match.count(1) > 0:
                # print(face_names)
                print(names_of_faces)
                print(match.index(1))
                name = names_of_faces[match.index(1)]
            else:
                if len(unknown_face_encodings) > 0:
                    unknown_match = face_recognition.compare_faces(unknown_face_encodings, face_encoding)
                    print(unknown_match.count(1))
                    if unknown_match.count(1) > 25:
                        name = "Unnamed"
                    # makeDirectory for "unnamed person"
                    if name != "Unnamed":
                        path = '/Users/vduraphe@tibco.com/node-js-sample/public/face_recognition/examples/web/unknown_faces/Unknown ' + str(i) 
                        while (exist == 1):
                            my_file = Path(path + 'jpg')
                            if my_file.is_file():
                                i += 1
                            else:
                                exist = 0
                        cv2.imwrite(str(path) + '.jpg', small_frame)
                        i += 1
                    else:
                        newpath = r'/Users/vduraphe@tibco.com/node-js-sample/public/face_recognition/examples/web/known_faces/Unnamed ' + str(j)
                        new_name = 'Unnamed ' + str(j)
                        while (exist_name == 1):
                            my_file = Path(newpath + '.jpg')
                            if my_file.is_file():
                                i += 1
                            else:
                                exist_name = 0
                        cv2.imwrite(str(newpath) + '.jpg', small_frame)
                        j += 1
                        new_name_face_encoding = face_recognition.face_encodings(small_frame)[0]
                        list_of_faces.append(new_name_face_encoding)
                        names_of_faces.append(str(new_name))
                        sorted(names_of_faces)
                unknown_face_encodings.append(face_encoding)    
            face_names.append(name)        
            if name == "Unknown" and len(face_encodings) > 0:
                k += 1
                if k > 10 and face_object[1] == 0:
                    print("sound play")
                    sound.play()
                    cap = cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    cv2.imshow('intruder', gray)
                    cv2.waitKey(3000)
                    cv2.destroyWindow('intruder')
                    k = 0
                    face_object[1] == 0
                print("Alert! Unknown Face!")

    process_this_frame = not process_this_frame

    # Display the results
    print(name)
    print(face_names)
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        print(name)
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


    # Display the resulting image
    cv2.imshow('Video', frame)

            
    # *********PRESENTATION PART
    pres_path = "/Users/vduraphe@tibco.com/node-js-sample/face_recognition/examples/presentations" 
    for file in os.listdir(pres_path):
        if file == (name + '.pps'):
            if is_open == 0:
                path_to_presentation = pres_path + '/' + name + '.pps'
                subprocess.call(['open', path_to_presentation])
                is_open = 1
        elif is_open == 1 and name == "Barack":
            print("next slide")
        else:
            print("No presentation for " + name)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

