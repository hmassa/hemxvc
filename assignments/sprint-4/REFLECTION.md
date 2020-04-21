Include a REFLECTION.md file that includes:
* A description of which projects you looked at
* Why you chose the one you did
* How far you got in making it work and
* What obstacles you encountered in the process

# REFLECTION

When deciding which SSO open source project to use, I looked into Gluu and ORY Hydra.
Since I have absolutely no idea what I'm doing, I decided to use Gluu because I found
the docs for this system to be much more helpful. However, I still was not able to get
Gluu running on my ec2 instance, so in hindsight this was really not the best decision.
The first issue I encountered while trying to set up Gluu was that Amazon Linux AMI was
not a supported operating system. To get around that, I tried installing Docker and
then installing Gluu but something wasn't working so I gave up and decided to make another
ec2 instance that runs ubuntu, which is one of Gluu's supported operating systems. However,
it turns out you need 40GB of disk space in order to install Gluu and the free tier of AWS
only allows for 30GB max. So, I have now lost all hope for Gluu and have not been able to
find another open source SSO software project that I understand enough to try to implement.
But, here is the link to the ec2 instance I created so you at least know I gave it the ol'
college try:

http://ec2-3-134-97-105.us-east-2.compute.amazonaws.com/
