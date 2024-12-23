#alexis@archlinux
#                .o+`                    ----------------
#               `ooo/                    OS: Arch Linux x86_64
#              `+oooo:                   Host: Vivobook_ASUSLaptop M1502IA_M1502IA (1.0)
#             `+oooooo:                  Kernel: Linux 6.12.4-arch1-1
#             -+oooooo+:                 Uptime: 1 hour, 21 mins
#           `/:-:++oooo+:                Packages: 894 (pacman)
#          `/++++/+++++++:               Shell: bash 5.2.37
#         `/++++++++++++++:              Display (BOE0903): 1920x1080 @ 60 Hz in 15" [Built-in]
#        `/+++ooooooooooooo/`            WM: Hyprland (Wayland)
#       ./ooosssso++osssssso+`           Theme: catppuccin-mocha-flamingo-standard+default [GTK2/3]
#      .oossssso-````/ossssss+`          Icons: Adwaita [GTK2/3]
#     -osssssso.      :ssssssso.         Font: Cantarell (11pt) [GTK2/3]
#    :osssssss/        osssso+++.        Cursor: default (24px)
#   /ossssssss/        +ssssooo/-        Terminal: kitty 0.37.0
# `/ossssso+/:-        -:/+osssso+-      Terminal Font: CaskaydiaCoveNFM-Regular (12pt)
#`+sso+:-`                 `.-/+oso:     CPU: AMD Ryzen 5 4600H (12) @ 4.01 GHz
#`++:.                           `-/+/    GPU: AMD Radeon Vega Series / Radeon Vega Mobile Series [Inte]
#.`                                 `/    Memory: 2.25 GiB / 15.04 GiB (15%)
#                                         Swap: 0 B / 4.00 GiB (0%)
#                                         Disk (/): 24.31 GiB / 475.94 GiB (5%) - btrfs
#                                         Local IP (wlan0): 192.168.18.28/24
#                                         Battery (ASUS Battery): 63% [Discharging]
#                                         Locale: es_PE.UTF-8

USER_NAME=$(whoami)
HOST_NAME=$(uname -n)
OS=$(uname -o)
KERNEL=$(uname -r)
UPTIME=$(uptime -p)
PACKAGES=$(pacman -Qq | wc -l)  
SHELL=$(echo $SHELL)
WM=$(echo $XDG_CURRENT_DESKTOP)
THEME=$(gsettings get org.gnome.desktop.interface gtk-theme)
ICONS=$(gsettings get org.gnome.desktop.interface icon-theme)
FONT=$(gsettings get org.gnome.desktop.interface font-name)
CURSOR=$(gsettings get org.gnome.desktop.interface cursor-theme)
TERMINAL=$(echo $TERM)
TERMINAL_FONT=$(echo $FONT)
CPU=$(lscpu | grep "Model name" | cut -d: -f2)
GPU=$(lspci | grep VGA | cut -d: -f3)
MEMORY=$(free -h | grep Mem | awk '{print $3 " / " $2}')
SWAP=$(free -h | grep Swap | awk '{print $3 " / " $2}')
DISK=$(df -h | grep /dev/sda2 | awk '{print $3 " / " $2 " (" $5 ")"}')
LOCAL_IP=$(ip a | grep inet | grep wlan0 | awk '{print $2}')
#BATTERY=$(acpi | awk '{print $4 " [" $3 "]"}')
LOCALE=$(locale | grep LANG | cut -d= -f2)




echo "$USER_NAME@$HOST_NAME"

