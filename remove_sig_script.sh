#/user/bin/perl

UserName=$(ls -l /dev/console | awk '{print $3}')
echo $UserName
if [ -d /Users/$UserName/temp/ ]; then rm -Rf  /Users/$UserName/temp/ ; fi

if [ -d /Applications/email_signatures ]; then rm -Rf  /Applications/email_signatures ; fi