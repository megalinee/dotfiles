exit_message="󰌑 Exit Menu"
logout_message="󰗽 Logout"
reboot_message=" Reboot"
shutdown_message="⏻ Shutdown"

# if [ x"$@" = x"exit_message" ]
# then
#     exit 0
# fi


if [ x"$@" = x"$logout_message" ]
then
    hyprlock || exit 0
    
fi


if [ x"$@" = x"$reboot_message" ]
then
    reboot
    exit 0 
fi


if [ x"$@" = x"$shutdown_message" ]
then
    shutdown now
    exit 0 
fi

# echo "󰌑 Exit Menu"
echo "$logout_message"
echo "$reboot_message"
echo "$shutdown_message"