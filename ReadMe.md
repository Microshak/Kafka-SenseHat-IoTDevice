# Install Dependancies
On your Pi in a terminal run
```sh
sudo apt-get update
sudo apt-get install git
sudo apt-get install sense-hat
sudo pip3 install numpy
sudo pip3 install kafka-python

```

# Create a Config.ini file
put in this config file

```config
[device]
deviceId = device1
sendSleep = .25
recieveSleep = .25
[cloud]
bootstrapServers = [Your Kafka IP]:9092
```


# Git
set up your git credentials
```sh
sudo git config --global user.email "you@example.com"
sudo git config --global user.password "ur password"
```


# Start up
You will need to edit startup
```sh
sudo nano /etc/rc.local
```
Then at right befor the exit 0 put in the location of your files


```sh

sudo python3 /home/pi/Desktop/RealtimeIoT/PiToKafka.py &
sudo python3 /home/pi/Desktop/RealtimeIoT/KafkaToPi.py &

```





sudo reboot
