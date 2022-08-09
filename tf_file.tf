resource "aws_cloudtrail" "positive1" {
  kms_key_id = "arn:aws:kms:<Your KMS Key>"
  name                          = "npositive_1"
  s3_bucket_name                = "bucketlog_1"
}
