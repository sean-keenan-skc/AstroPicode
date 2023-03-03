from picamera import PiCamera
from time import sleep
import time
from orbit import ISS


def take_photos():
    
    camera = PiCamera()
    camera.resolution = (4056, 3040)
    camera.start_preview()
    sleep(5)
# Camera warm-up time

    for i in range(170):
#        execute the following loop 170 times over next 3 hours
        txtfile = (open('location info.txt', 'a')) # write or append txt file
        location = ISS.coordinates() # get location
        txtfile.writelines(f'{location} {i:03d}') # write a line with location info and loop no (in 3 digits)
        txtfile.writelines('\n') # new line
        txtfile.close() # close the file
        
        current_time = time.time() # get current time
        camera.capture(f'image_{i:03d}_{current_time}.jpg')
# capture image and save as image_000_1643366165.jpg
        sleep(60) # sleep for 60 seconds before reentering loop
        
take_photos()



# camera turns on warms up for 5 secs
# gets location of ISS and saves it on text file
# gets time
# takes a photo saves it with above file name and time and does nothing for 60 secs

# result will be one text file with 170 lines of location info
# on return we will amend it to a more readible and workable version on excel
# we will also have 170 images
# the image will be timestamped and the location will be available from the loop number saved on text file
# each image can be location checked as it has the same loop number as corresponding info on text file
# websites will verify info is correct and convert time