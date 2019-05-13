# builds openocd for arm/pi

sudo apt install git htop build-essential fakeroot devscripts
sudo apt-get build-dep openocd
wget https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/openocd/0.10.0-1build1/openocd_0.10.0.orig.tar.bz2
wget https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/openocd/0.10.0-1build1/openocd_0.10.0-1build1.debian.tar.xz
tar xvf openocd_0.10.0.orig.tar.bz2
cd openocd-0.10.0/
tar ../xvf openocd_0.10.0-1build1.debian.tar.xz
debchange -i
dpkg-source --commit
debuild -us -uc -i -I

