from .session import create_session

@create_session
def list_objects(
        bucket_name, 
        session,
        bucket_prefix="",
        jmes_string="default"
        ):
    client = session.client("s3")
    paginator = client.get_paginator("list_objects")
    parameters = {
        "Bucket": bucket_name,
        "Prefix": bucket_prefix,
    }
    page_iter = paginator.paginate(**parameters)
    if jmes_string == "default":
        jmes_search_value = "Contents[].Key"
    else:
        jmes_search_value = jmes_string
    key_iter = page_iter.search(jmes_search_value)
    return key_iter