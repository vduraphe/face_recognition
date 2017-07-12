import subprocess
import pyglet
import cv2
import face_recognition


# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# austin
austin_image = face_recognition.load_image_file("austin.jpg")
austin_face_encoding = face_recognition.face_encodings(austin_image)[0]
# vaidehi
vaidehi_image = face_recognition.load_image_file("vaidehi.jpg")
vaidehi_face_encoding = face_recognition.face_encodings(vaidehi_image)[0]
# xiang
xiang_image = face_recognition.load_image_file("xiang.jpg")
xiang_face_encoding = face_recognition.face_encodings(xiang_image)[0]
# iris
# iris_image = face_recognition.load_image_file("iris.jpg")
# iris_face_encoding = face_recognition.face_encodings(iris_image)[0]

list_of_faces = [obama_face_encoding, vaidehi_face_encoding, austin_face_encoding, xiang_face_encoding]#, iris_face_encoding]
names_of_faces = ['Barack', 'Vaidehi', 'Austin', 'Xiang']#, 'Tigress']

# Initialize some variables
face_locations = []
face_encodings = []
unknown_face_encodings = []
face_names = []
process_this_frame = True
i = 0
j = 0
k = 0
blue = (255, 0, 0)
red = (0, 0, 255)
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

            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces(list_of_faces, face_encoding)
            print(match)
            if match.count(1) > 0:
                # print(face_names)
                name = names_of_faces[match.index(1)]
            else:
                unknown_face_encodings.append(face_encoding)
                if len(unknown_face_encodings) > 0:
                    unknown_match = face_recognition.compare_faces(unknown_face_encodings, face_encoding)
                    if unknown_match.count(1) > 50:
                        name = "Unnamed"
                    # makeDirectory for "unnamed person"
                    if name != "Unnamed":
                        path = '/Users/vduraphe@tibco.com/face_recognition/examples/unknown_faces/'
                        cv2.imwrite(str(path) + str(i) + 'unknown.jpg', small_frame)
                        i += 1
                    else:
                        newpath = r'/Users/vduraphe@tibco.com/face_recognition/examples/unnamed' + str(j)
                        new_name = 'unnamed' + str(j)
                        cv2.imwrite(str(newpath) + '.jpg', small_frame)
                        j += 1
                        new_name_face_encoding = face_recognition.face_encodings(small_frame)[0]
                        list_of_faces.append(new_name_face_encoding)
                        names_of_faces.append(str(new_name))
                unknown_face_encodings.append(face_encoding)
            face_names.append(name)
            if name == "Unknown":
                print("Alert! Unknown Face!")

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
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
    if name == "Unknown" and len(face_encodings) > 0:
        k += 1
        if k > 10:
            sound = pyglet.media.load('LowerQTrim.wav', streaming=False)
            print("sound play")
            sound.play()
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            cv2.imshow('intruder', gray)
            cv2.waitKey(3000)
            cv2.destroyWindow('intruder')
           	# cv2.imshow('image', cap.read())
           	# cv2.waitKey(3000)
            # sound = 'LowerQ.mp3'
            # subprocess.Popen(['player', sound])
            # playsound('/Users/vduraphe@tibco.com/face_recognition/LowerQ.wav')
            k = 0
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
