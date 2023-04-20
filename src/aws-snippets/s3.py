import boto3

def s3_list(
        bucket_name, 
        bucket_prefix, 
        profile_name="default", 
        region_name="us-east-1"
        ):
    session = boto3.Session(profile_name=profile_name)
    client = session.client("s3", region_name=region_name)
    paginator = client.get_paginator("list_objects")
    parameters = {
        "Bucket": bucket_name,
        "Prefix": bucket_prefix,
    }
    page_iter = paginator.paginate(**parameters)