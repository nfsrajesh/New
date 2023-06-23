from pypylon import pylon
import cv2,time

fourcc = cv2.VideoWriter_fourcc(*'XVID')
width,height=2590,1942
out = cv2.VideoWriter('model2b2.avi', fourcc, 20.0, (width, height))


tl_factory = pylon.TlFactory.GetInstance()
camera = pylon.InstantCamera()
try:
    camera.Attach(tl_factory.CreateFirstDevice())
except:
    print("Can to FInd The Device\nProgram Will run After 3 seconds .......... ")
converter = pylon.ImageFormatConverter()
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
camera.Open()
try:
    pylon.FeaturePersistence.Load("nodemap.pfs", camera.GetNodeMap(), True)
    print("Reading file back to camera's node map...")
except:
    print("file not load ...........")
while camera.IsGrabbing():
    t0 = time.time()
    try:
        grab = camera.RetrieveResult(1000, pylon.TimeoutHandling_ThrowException)
    except:
        print("Time Out ")
        continue
    if grab.GrabSucceeded():
        image = converter.Convert(grab)
        img = image.GetArray()
        print(img.shape)
        out.write(img)
        cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
        cv2.imshow("frame", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("! !! Stop Graping and close Camera ...")
            cv2.destroyAllWindows()
            break
            grabResult.Release()
            out.release()
            camera.Close()


# cap.release()
# out.release()
# cv2.destroyAllWindows()
