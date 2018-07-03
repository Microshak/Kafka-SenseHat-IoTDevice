# Install Dependancies
On your Pi in a terminal run
```sh
sudo apt-get update
sudo apt-get install git
sudo apt-get install sense-hat
sudo pip3 install numpy
sudo pip3 install kafka-python
```

# Git
set up your git credentials
git config --global user.email "you@example.com"

git config credential.helper store


# Start up
You will need to edit startup

sudo nano /etc/rc.local

Then at right befor the exit 0 put in the location of your files



sudo python3 /home/pi/Desktop/RealtimeIoT/PiToKafka.py &
sudo python3 /home/pi/Desktop/RealtimeIoT/KafkaToPi.py &






sudo reboot
