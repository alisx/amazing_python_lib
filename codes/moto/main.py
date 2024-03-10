# pip install 'moto[ec2,s3,all]'

import boto3
from moto import mock_s3

@mock_s3
def test_my_model_save():
    # 设置 
    s3 = boto3.resource('s3')
    s3.create_bucket(Bucket='mybucket')

    # 假设这是你的代码中的实际操作
    # 这里不会实际创建  bucket，因为我们有了  Moto
    my_model.save()

    # 验证 
    body= s3.Object('mybucket', 'file.txt').get()['Body'].read().decode("utf-8") 
    assert body == 'my data'
    
@mock_s3
def test_s3_operations():
    # 一系列的  S3  操作模拟 
    pass