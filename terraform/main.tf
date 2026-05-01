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
                # Exit immediately if any command fails
                set -e
                
                apt update -y
                
                apt install -y docker.io
                
                systemctl start docker
                systemctl enable docker
                
                # Install AWS CLI v2
                apt install -y unzip curl
                
                curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
                unzip awscliv2.zip
                # it installs to /usr/local/bin, Without sudo, it can fail silently depending on environment
                sudo ./aws/install
                
                # Add ubuntu to docker group
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