resource "aws_s3_bucket" "mongodb_backups" {
  bucket        = "wiz-demo-mongodb-backups"
  force_destroy = true
}

resource "aws_s3_bucket_public_access_block" "mongodb_backups" {
  bucket = aws_s3_bucket.mongodb_backups.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_s3_bucket_acl" "mongodb_backups" {
  bucket = aws_s3_bucket.mongodb_backups.id
  acl    = "public-read"
}

resource "aws_s3_bucket_policy" "allow_public_access" {
  bucket = aws_s3_bucket.mongodb_backups.id
  policy = data.aws_iam_policy_document.allow_public_access.json
}

data "aws_iam_policy_document" "allow_public_access" {
  statement {
    principals {
      identifiers = ["*"]
      type        = "*"
    }

    actions = [
      "s3:GetObject"
    ]

    resources = [
      "${aws_s3_bucket.mongodb_backups.arn}/*"
    ]
  }
}
