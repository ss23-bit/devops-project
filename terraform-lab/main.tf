provider "aws" {
  region = var.aws_region
}

data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"                         # is like a Key, and values is like a Value
    values = ["amzn2-ami-hvm-*-x86_64-gp2"] # Because Amazon Web Services has hundreds of AMIs
  }
}

resource "aws_instance" "my_server" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"

  key_name = "terraform-key"

  vpc_security_group_ids = [aws_security_group.allow_ssh.id]
}

resource "aws_security_group" "allow_ssh" {
  name = "allow_ssh"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["58.8.249.244/32"]
  }
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "ss23-terraform-lab-1a"
}

resource "aws_s3_bucket" "imported_bucket" {
  bucket = "ss23-manual-bucket-xyz"
}