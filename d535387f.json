{
  "control": "kics",
  "title": "S3 Buckets should not be readable and writable to all users",
  "reason": "Misconfigured s3 bucket that allows public read access can lead to a customer data breach. Second, a misconfigured s3 bucket allowing public write access can be used to serve or control malware, damage a website hosted on a cloud storage service, store any amount of data at your expense, and even encrypt your files for the purposes of demanding a ransom",
  "guidelines": "Consider changing the permissions to private",
  "test_id": "d3b81fde",
  "actions": [
      {
        "action_type": "add_or_replace_value",
        "params": {
          "node": "*.acl",
          "value": "\"private\""
        }
      }
    ]
}
