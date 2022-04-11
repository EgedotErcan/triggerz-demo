import boto3
import os

## S3 request ve response
s3 = boto3.client("s3",
                region_name="us-east-1",
                aws_access_key_id="AKIAUQUQBNZUWY4J4ZJR",
                aws_secret_access_key="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")


### Bucket işlemleri 
s3.create_bucket(Bucket='myexpertunity') # Bucket oluşturduk 

# Yerel pcde mevcut olan mp3 ve txt formatındaki dosyayı s3'e transfer ettik
##s3.upload_file('./q1.mp3', 'myexpertunity', 'q1.mp3', ExtraArgs={'ACL': 'public-read', 'ContentType': 'audio/mp3'})
s3.upload_file('./transcription.txt','myexpertunity','transcription.txt',ExtraArgs={'ACL': 'public-read', 'ContentType': 'text/plain'})

## Bu dosya formatlarını yerel pcye s3'ten çekip geri gönderdik 
response1 = s3.get_object(Bucket="myexpertunity",Key="transcription.txt")
data1 = response1['Body'].read() # txt

## Bu dosya formatlarını yerel pcye s3'ten çekip geri gönderdik 
s3.download_file('myexpertunity','q1.mp3',os.path.join(os.getcwd(),'testq1.mp3'))# mp3
print(data1)




