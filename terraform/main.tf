provider "aws" {
  region = "ap-southeast-1"
}

resource "aws_instance" "devops_server" {
  ami           = "ami-0a56f8447277affd8"
  instance_type = "t3.micro"
  key_name      = var.key_name

  security_groups = [aws_security_group.devops_sg.name]

  tags = {
    Name = "devops-terraform-server"
  }

  user_data = <<-EOF
              #!/bin/bash
              apt update -y
              apt install -y docker.io awscli
              systemctl start docker
              systemctl enable docker
              usermod -aG docker ubuntu
              EOF
}

resource "aws_security_group" "devops_sg" {
  name = "devops-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}