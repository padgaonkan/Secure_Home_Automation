#!/bin/bash
    ifconfig
    echo
    echo "------------------"
    echo "IoT Server Started"
    echo  "-----------------"
    echo
    mosquitto -c password.conf -v