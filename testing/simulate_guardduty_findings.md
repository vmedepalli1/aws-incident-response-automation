# Simulate GuardDuty Findings

1. Get your GuardDuty Detector ID:
   aws guardduty list-detectors

2. Simulate sample findings:
   aws guardduty create-sample-findings --detector-id <your-detector-id>

3. Confirm automation triggered:
   - EC2 instance is stopped
   - SNS email is received
