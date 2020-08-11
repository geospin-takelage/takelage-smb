#!/usr/bin/env bash

echo "Changing password for user $USER."
read -s -p "New password: " PASSWORD_0
echo -ne "\n"
read -s -p "Retype new password: " PASSWORD_1
echo -ne "\n"


if [ "$PASSWORD_0" != "$PASSWORD_1" ]
then
    echo "Sorry, passwords do not match."
elif [ ${#PASSWORD_0} -le 3 ]
then
    echo "The length of the password is to short."
elif [ "$PASSWORD_0" == "$USER" ]
then
    echo "It's not allowed to set the password to the username."
else
    echo "$PASSWORD_0" | sudo passwd -f $USER --stdin >> /dev/null
    (echo -e "$PASSWORD_0"; echo -e "$PASSWORD_0") | sudo smbpasswd -s $USER
    echo "Password updated successfully."
fi
