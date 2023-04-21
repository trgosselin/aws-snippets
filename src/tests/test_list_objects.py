from aws_snippets.s3 import list_objects
import os
import pytest
from moto import mock_s3
import boto3
import types

@pytest.fixture
def s3_fixture():
    s3 = boto3.client("s3", region_name="us-east-1")
    return s3

@mock_s3
def test_list_objects(s3_fixture):
    os.environ['AWS_ACCESS_KEY_ID'] = "fakeaccesskey"
    os.environ['AWS_SECRET_ACCESS_KEY'] = "fakesecretkey"
    os.environ['AWS_DEFAULT_REGION'] = "us-east-1"

    # Setup test mock
    bucket_name = "testbucket"
    keys = ["test_object_" + str(i) for i in range(100)]
    body = "nothing"
    s3_fixture.create_bucket(Bucket=bucket_name)
    for k in keys:
        s3_fixture.put_object(Bucket=bucket_name, Key=k, Body=body)

    data = list_objects(bucket_name=bucket_name)  
    keys = [d for d in data]

    assert isinstance(data, types.GeneratorType)
    assert all(isinstance(i, str) for i in keys)
    
    data2 = list_objects(
        bucket_name=bucket_name, 
        jmes_string="Contents[?contains(Key, 'test_object_2')].Key"
        )
    keys2 = [d for d in data2]

    assert keys2[0] == "test_object_2"
    