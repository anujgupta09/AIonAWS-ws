import cv2
import boto3

while True:
    try:
        pic_name_webcam="anuuj.jpg"
        cap  = cv2.VideoCapture(0)              # to activate webcam (ON)
        retrn , frame = cap.read()              # to click a pic
        cv2.imwrite(pic_name_webcam , frame)    # to save that pic 
        cap.release()                           # to deactivate webcam (OFF)

        bucket_name="anuj-bucket-9799"       #variables
        region="ap-south-1"
        pic_name_s3="fille.jpg"
        s3 = boto3.resource('s3')         # to connect s3 of aws 
        s3.Bucket(bucket_name).upload_file( pic_name_webcam , pic_name_s3) #connecting to bucket of s3 and uploading image

        rekog = boto3.client('rekognition')
        response=rekog.detect_labels(
            Image={
                  'S3Object': {
                      'Bucket': bucket_name,
                      'Name': pic_name_s3,
                  }
              },
              MaxLabels=30,
              MinConfidence=90
          )
        response           # now from thsi output we can put conditions and flower a usecase
    
        # using the o/p
        most_likely=response["Labels"][0]['Name']
        
        print("\n"+str(most_likely))
    except ValueError:
         print("Oops!  That was no valid number.  Try again...")

        
        
############# step 4 using rsponse or output # v2 try
