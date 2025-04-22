import json
import boto3

ec2 = boto3.client('ec2')
sns = boto3.client('sns')

SNS_TOPIC_ARN = 'arn:aws:sns:<region>:<account-id>:incident-alerts'

def lambda_handler(event, context):
    instance_id = event['detail']['resource']['instanceDetails']['instanceId']
    region = event['region']
    
    ec2.stop_instances(InstanceIds=[instance_id])
    
    message = f"GuardDuty finding detected! EC2 instance {instance_id} stopped in region {region}."
    sns.publish(TopicArn=SNS_TOPIC_ARN, Subject="EC2 Quarantine Alert", Message=message)
    
    return {
        'statusCode': 200,
        'body': json.dumps(f"Remediation executed. Stopped {instance_id}")
    }
