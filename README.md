# aws-snippets

## Example
'''
jmes_str = f"Contents[?contains(Key,'145939')].Key"
data = list_objects(bucket_name="ppmi-500-object-store", bucket_prefix="prod", jmes_string=jmes_str)
key_list = [d for d in data]
print(key_list)
'''