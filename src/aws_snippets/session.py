import boto3

def create_session(function, profile_name="default", region_name="us-east-1"):
    def session_wrapper(**kwargs):
        session = boto3.Session(profile_name=profile_name)
        return function(session=session, **kwargs)
    return session_wrapper
