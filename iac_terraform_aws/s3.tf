resource "aws_s3_bucket" "dl" {
  bucket = "datalake-emerson-edc-tf"
  acl    = "private"

  tags = {
    curso = "EDC"
  }

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}
