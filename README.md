# aws-snippets

## Example
```
jmes_str = f"Contents[?contains(Key,'my_object')].Key"
key_iter = list_objects(bucket_name="my-bucket", bucket_prefix="objects", jmes_string=jmes_str)
key_list = [key for key in key_iter]
print(key_list)
```
