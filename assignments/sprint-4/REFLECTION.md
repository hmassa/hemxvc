# REFLECTION

When deciding which SSO open source project to use, I first looked into Gluu and ORY Hydra.
Since I have absolutely no idea what I'm doing, I decided to use Gluu because I found
the docs for this system to be much more helpful. However, I still was not able to get
Gluu running on my ec2 instance, so in hindsight this was really not as good of a decision
as I thought. The first issue I encountered while trying to set up Gluu was that Amazon
Linux AMI was not a supported operating system. To get around this issue, I made another
ec2 instance that runs Ubuntu, which is one of Gluu's supported operating systems. However,
while installing Gluu on this server, I learned that you need 40GB of disk space available
for Gluu to work and the free tier of AWS only allows for 30GB max. So, I looked into a few 
more projects and I found an open source social sign on project called Hybridauth
(https://github.com/hybridauth/hybridauth). Hybridauth is a PHP library that acts "as an
abstract API between your application and various social APIs and identities providers
such as Facebook, Twitter and Google." With this library, I was able to build a very basic
web app that allows users to login by signing in through GitHub.
