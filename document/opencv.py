import  cv2
img = cv2.imread('hh.jpg', -1)



cv2.imshow("image", img)
k  = cv2.waitKey(0)


if k == 27:
    print('cancel')
    cv2.destroyAllWindows()
elif k == ord('s'):
  print('d')
  cv2.destroyAllWindows()
  cv2.imwrite('image.png', img)