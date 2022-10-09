import cv2

cv2.imread("solar-sstem.jpg")

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.Font_HERSHEY_COMPLEX,
            0.5
            (225,225,225)
            )

  cv2.putText(img,
            "Mercury",
            (10,100),
            cv2.Font_HERSHEY_COMPLEX,
            0.5
            (225,225,225)
           )

cv2.putText(img,
            "Venus",
            (150,200),
            cv2.Font_HERSHEY_COMPLEX,
            0.5
            (225,225,225)
           )

cv2.putText(img,
            "Earth",
            (20,250),
            cv2.Font_HERSHEY_COMPLEX,
            0.5
            (225,225,225)
           )

cv2.putText(img,
            "Mars",
            (25,280),
            cv2.Font_HERSHEY_COMPLEX,
            0.5
            (225,225,225)
           )

cv2.putText(img,
            "Jupiter",
            (30,300),
            cv2.Font_HERSHEY_COMPLEX,
            0.5
            (225,225,225)
           )

cv2.putText(img,
            "Saturn",
            (25,300),
            cv2.Font_HERSHEY_COMPLEX,
            0.5
            (225,225,225)
           )

cv2.putText(img,
            "Uranus",
            (15,150),
            cv2.Font_HERSHEY_COMPLEX,
            0.5
            (225,225,225)
           )

cv2.putText(img,
            "Neptune",
            (5,100),
            cv2.Font_HERSHEY_COMPLEX,
            0.5
            (225,225,225)
           )



cv2.imshow("output",img)

cv2.waitKe(0)
