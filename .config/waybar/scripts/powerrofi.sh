

if [ x"$@" = x"󰌑 Exit Menu" ]
then
    exit 0
fi


if [ x"$@" = x"󰗽 Logout" ]
then
    hyprlock || exit 0
    
fi


if [ x"$@" = x" Reboot" ]
then
    reboot
    exit 0 
fi


if [ x"$@" = x"⏻ Shutdown" ]
then
    shutdown now
    exit 0 
fi

echo "󰌑 Exit Menu"
echo "󰗽 Logout"
echo " Reboot"
echo "⏻ Shutdown"