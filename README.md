# AWS Cloud Incident Response Automation Platform 🚨☁️

This project demonstrates a security automation framework on AWS that detects threats using GuardDuty and responds automatically using Lambda functions. It integrates services like Security Hub, Config, CloudTrail, CloudWatch, and SNS for comprehensive incident handling.

## 🧱 Architecture
![Architecture](architecture/incident-response-architecture.png)

## 🛠️ Services Used
- Amazon GuardDuty
- AWS Lambda
- AWS Config
- AWS CloudTrail
- Amazon SNS
- AWS Security Hub
- Amazon CloudWatch
- AWS EventBridge

## ⚙️ Features
- Threat detection using GuardDuty
- Auto-remediation via Lambda (e.g., EC2 quarantine, IAM revocation)
- Real-time alerts via SNS
- Centralized visibility in Security Hub
- Configuration auditing with AWS Config

## 📂 Directory Structure
- `lambda/`: All remediation Lambda functions
- `eventbridge-rules/`: EventBridge rules to trigger Lambda
- `cloudformation/`: (Optional) IaC template to deploy everything
- `sns/`: SNS topic + subscription setup docs
- `testing/`: Steps to simulate GuardDuty findings
- `docs/`: Full implementation walkthrough

## 🧪 How to Test
1. Deploy using the CloudFormation template (optional)
2. Simulate findings: `aws guardduty create-sample-findings`
3. Watch Lambda respond and SNS send alerts
4. Review logs in CloudWatch
