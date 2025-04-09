import cv2

ref_image = cv2.imread("reference.jpg")
ref_image_gray = cv2.cvtColor(ref_image, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

ref_faces = face_cascade.detectMultiScale(ref_image_gray, 1.3, 5)
(x, y, w, h) = ref_faces[0]
ref_face = ref_image_gray[y:y+h, x:x+w]


cap = cv2.VideoCapture(0)
print("Appuie sur 'q' pour quitter.")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, ref_face.shape[::-1])  
        diff = cv2.absdiff(ref_face, face)
        score = diff.mean()

        label = "Angelina Jolie" if score < 50 else "Inconnu"
        color = (0, 255, 0) if label == "Kawtar" else (0, 0, 255)

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow("Reconnaissance Faciale Simple", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
