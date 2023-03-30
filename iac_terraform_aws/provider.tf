provider "aws" {
  region = var.aws_region
}

# Centralizar o arquivo de controle de estado do terraform
terraform {
  backend "s3" {
    bucket = "terraform-state-emerson-edc"
    key    = "state/mod1/terraform.tfstate"
    region = "sa-east-1"
  }
}