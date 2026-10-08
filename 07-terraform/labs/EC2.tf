resource "aws_instance" "this" {
  ami                     = "ami-06b9219be654efe2b"
  instance_type           = "t3.micro"
}
