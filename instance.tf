provider "aws" {
  region     = "${var.region}"
  access_key = "${var.access_key}"
  secret_key = "${var.secret_key}"
}

# EC2 resource

resource "aws_instance" "CustomEC2" {
  ami                    = var.AMI_ID
  instance_type          = "t2.micro"
  security_groups = ["${aws_security_group.SG.name}"]

  tags = {
    Name = "Custom-instance"
  }
}

resource "aws_security_group" "SG" {
  name        = "SG"
  description = "Security Group"

  ingress {
    description = "Allow SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 22
    to_port     = 22
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Custom TCP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 80
    to_port     = 80
