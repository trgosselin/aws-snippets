from aws_snippets.s3 import list_objects

def test_list_objects():
    data = list_objects(bucket_name="invicro-quilt", bucket_prefix=None)
    assert data == "x"