import boto3

def get_key(d,k):

    for key, value in d.items():
        if key == k:
          result.append(value)
        if isinstance(value, dict):
          get_key(value,k)
        if isinstance(value, list):
            for item in value:
              if isinstance(item,dict):
                get_key(item,k)

def getInstanceMetadata(instanceIds, key=None):
    global result
    result =[]
    session = boto3.Session(profile_name='Dinesh')

    aws_client = session.client('ec2', 
        region_name = "us-east-1"
    )

    metadata = aws_client.describe_instances(InstanceIds=instanceIds)
    get_key(metadata,key)
    return (result)



# instanceIds =["i-0461e64e9df67518d","i-0ad04bd1cd1163aab"]
instanceIds =["i-0461e64e9df67518d"]
key = "CpuOptions"

print(getInstanceMetadata(instanceIds,key))
