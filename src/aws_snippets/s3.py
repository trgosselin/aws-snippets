import boto3
import multiprocessing as mp
from collections.abc import Iterable

def list_objects(
        bucket_name, 
        bucket_prefix,
        profile_name="default", 
        region_name="us-east-1",
        jmes_string="default"
        ):
    session = boto3.Session(profile_name=profile_name)
    client = session.client("s3", region_name=region_name)
    paginator = client.get_paginator("list_objects")
    if bucket_prefix == None:
        bucket_prefix = "" 
    parameters = {
        "Bucket": bucket_name,
        "Prefix": bucket_prefix,
    }
    page_iter = paginator.paginate(**parameters)
    if jmes_string == "default":
        jmes_search_value = "Contents[].Key"
    else:
        jmes_search_value = jmes_string
    data = page_iter.search(jmes_search_value)
    return data

def _read_pages(page):
    contents = page['Contents']
    keys = [c['Key'] for c in contents]
    return keys


if __name__ == "__main__":
    jmes_str = f"Contents[?contains(Key,'145939')].Key"
    data = list_objects(bucket_name="ppmi-500-object-store", bucket_prefix="prod", jmes_string=jmes_str)
    key_list = [d for d in data]
    print(key_list)