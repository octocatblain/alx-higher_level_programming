#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that get the message You got me!
curl -s -o /dev/null -w "You got me!" 127.0.0.1:5000/catch_me
