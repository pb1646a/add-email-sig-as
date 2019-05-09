#!/bin/bash
# get profile
currentuser=`stat -f "%Su" /dev/console`
echo $currentuser
sudo -u $(ls -l /dev/console | awk '{print $3}') osascript /Applications/email_signatures/set_email_signature.scpt
echo $(ls -l /dev/console | awk '{print $3}')
