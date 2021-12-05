#!/usr/bin/env bash
clear
echo -e "\e[4;31m MrHacker**** \e[0m"
echo -e "\e[1;32m  ◡̈ \e[0m"
echo -e "\e[1;34m"
figlet -f slant ──────
echo "รหัสเข้า ... "
read a10
if [[ -s update.shield.yemen ]];then
echo "พบความต้องการทั้งหมด...."
else
echo 'กำลังติดตั้ง....'
echo .
echo .
apt install figlet toilet python curl ruby -y
apt install python3-pip
gem install lolcat
echo ..
echo ...
echo ....
echo .....
read upd
fi
while :
do
rm *.xxx >/dev/null 2>&1
clear
echo -e "\e[1;31m"
figlet -f slant MrHacker***| lolcat
echo -e "\e[1;34m  Bypass \e[1;32m"  #blue Color
echo -e "\e[4;34m ..... \e[0m" #underline+blue
echo -e "\e[1;34m ......\e[0m"
echo -e "\e[1;32m ....... \e[0m" #yellow
echo -e "\e[1;34m ........ \e[0m"
echo " "
echo -e "\e[4;31m เลือกฟังก์ชั่นแล้วเติมหมายเลข... \e[0m" #red
echo " "
echo "Enter 1 To  Run X-SMS == เรียกใช้ X-SMS"
echo "Enter 2 To  Track X-SMS == ติดตาม X-SMS"  #white
echo "Enter 3 To  Update == อัปเดต"
echo "Enter 4 To  Check Features == ตรวจสอบคุณสมบัติ "
echo "Enter 5 To  Exit - ออก"

read -p  "     หมายเลข :> " menu
if [ $menu = 1 ];then
clear
echo -e "\e[1;32m"
rm *.xxx >/dev/null 2>&1
python3 fakesms.py
rm *.xxx >/dev/null 2>&1
exit 0
elif [ $menu = 2 ];then
clear
echo -e "\e[1;32m"
echo 'Track X-SMS'> call.xxx
python3 fakesms.py track
rm *.xxx >/dev/null 2>&1
exit 0
elif [ $menu = 3 ];then
clear
apt install git -y
echo -e "\e[1;34m กำลังขออัปเดตจากแหล่งที่มา..."
echo -e "\e[1;34m ขอความพยายามสำเร็จ..."
echo -e "\e[1;34m กำลังอัปเดตตอนนี้..."
git clone https://github.com/1337XQ/Termux-X-SMS
if [[ -s Termux-X-SMS/Run.sh ]];then
cd Termux-X-SMS
cp -r -f * .. > temp
cd ..
rm -rf  Termux-X-SMS>> temp
rm update.shield.yemen>> temp
rm temp
chmod +x Run.sh
fi
echo -e "\e[1;32m X-SMS จะรีเฟรชทันที..."
echo -e "\e[1;32m  ติดตั้งแพ็คเกจที่จำเป็นทั้งหมดแล้ว..."
echo -e "\e[1;34m กด Enter เพื่อรีเฟรช..."
read a6
./Run.sh
exit
echo " "
echo " "
elif [ $menu = 4 ];then
clear
echo -e "\e[1;33m"
figlet -f slant X-SMS| lolcat
echo -e "\e[1;34m MrHacker*** \e[1;34m"  #Blue Color
toilet -f mono12 -F border read | lolcat
echo  " "
echo -e "\e[1;32m                   คุณสมบัติ\e[1;34m"
echo "  การส่งที่รวดเร็วเป็นพิเศษ"
echo "  ส่งต่างประเทศ"
echo "  การติดตาม "
echo "  การอัปเดตในอนาคตอัตโนมัติ"
echo "  ใช้งานง่ายและฝังในโค้ด"
echo ""
echo ""
echo -e "\e[1;31m นี้เป็นเพียงเพื่อการศึกษาหรือเพื่อเล่นตลก\e[0m"
echo -e "\e[1;31m อย่าใช้สิ่งนี้เพื่อทำให้ผู้อื่นระคายเคือง \e[0m"
echo -e "\e[1;31m อย่าใช้สิ่งนี้เพื่อทำร้ายผู้อื่น \e[0m"
echo -e "\e[1;31m เราไม่รับผิดชอบต่อการใช้สคริปต์ในทางที่ผิด \e[0m"
echo -e "\e[1;32m อัปเดตหากไม่ได้ผล\e[0m"
echo  " "
echo "กด Enter เพื่อกลับไปยังเมนูหลัก"
read a3
clear
elif [ $menu = 5 ];then
clear
echo -e "\e[1;31m"
figlet -f slant X-SMS| lolcat
echo -e "\e[1;34m MrHacker*** \e[1;32m"
toilet -f sgga -F border MrHacker*** | lolcat
echo -e "\e[1;34m ขอบคุณ !!!\e[0m"
echo -e "\e[1;32m  ◡̈ \e[0m" #yellow
echo -e "\e[1;34m ... \e[0m"
echo " "
exit 0
else
echo -e "\e[4;32m ตรวจพบอินพุตที่ไม่ถูกต้อง !!! \e[0m"
echo "กด Enter เพื่อกลับไปยังเมนูหลัก"
read a3
clear
fi
done
