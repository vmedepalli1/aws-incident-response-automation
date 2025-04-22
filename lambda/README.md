# Lambda Functions

This folder contains AWS Lambda functions used for incident response automation.  
These functions are triggered by Amazon EventBridge when GuardDuty detects threats.

## Included Scripts:
- `quarantine_ec2_instance.py`: Stops a compromised EC2 instance and sends an alert via SNS.

All functions are designed to be serverless and integrate with other AWS security services.
