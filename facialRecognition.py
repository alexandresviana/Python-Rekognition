import boto3

#aws keys to connect
AWS_ACCESS_KEY_ID = 'AWSKEYID'
AWS_SECRET_ACCESS_KEY = 'AWSKEYACCESS'



if __name__ == "__main__":

    bucket='bucket-name'
    sourceFile='image1.jpg'
    targetFile='image2.jpg'

    client = boto3.client('rekognition','us-east-1',
         aws_access_key_id=AWS_ACCESS_KEY_ID,
         aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
 

    response=client.compare_faces(SimilarityThreshold=70,
                                  SourceImage={'S3Object':{'Bucket':bucket,'Name':sourceFile}},
                                  TargetImage={'S3Object':{'Bucket':bucket,'Name':targetFile}})

    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        confidence = str(faceMatch['Face']['Confidence'])
        print('The face at ' +
               str(position['Left']) + ' ' +
               str(position['Top']) +
               ' matches with ' + confidence + '% confidence')