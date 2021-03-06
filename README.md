<h1 align="center">Termux-X-SMS</h1>
<p align="center">Anonymous Message Sender for Linux And Termux.</p><br>
## บันทึก:

- สคริปต์ต้องใช้การเชื่อมต่อเครือข่ายในการทำงาน
- จะไม่มีการหักยอดคงเหลือสำหรับการใช้สคริปต์นี้ในการส่ง SMS
- ห้ามเว้นวรรคระหว่างหมายเลขโทรศัพท์ (เช่น 99999 99999)
- ตรวจสอบให้แน่ใจว่าคุณใช้ Termux-X-SMS . เวอร์ชันล่าสุด
- ตรวจสอบให้แน่ใจว่าคุณใช้ Python v3

วิธีตรวจสอบมีดังนี้ พิมพ์คำสั่งนี้ในเทอร์มินัลของคุณ
```
$ หลาม -V
```
หากเอาต์พุตดูเหมือน 'Python 3' หรือสูงกว่า - ยินดีด้วย Python 3 ได้รับการติดตั้งอย่างถูกต้อง

- อย่าใช้สิ่งนี้เพื่อทำร้ายผู้อื่น
- สคริปต์นี้ใช้เพื่อการศึกษาหรือเล่นตลกเท่านั้น
- ** ผู้พัฒนาไม่รับผิดชอบต่อการใช้ Termux-X-SMS ในทางที่ผิด **
<br>

## คุณสมบัติ:

- นี่เป็นเวอร์ชันฟรี
- การส่งข้อความที่เร็วมาก
- มีการส่งข้อความระหว่างประเทศ
- คุณสามารถส่งได้เพียงข้อความเดียวต่อวัน
- การส่งข้อความโดยไม่ระบุชื่อ
- ใช้งานง่ายและฝังในโค้ด

## การใช้งาน:

เรียกใช้คำสั่งเหล่านี้เพื่อส่งข้อความที่ไม่ระบุชื่อ

### > สำหรับ Termux:

**สังเกต:** 

วิธีการติดตั้ง git นั้นไม่เป็นสากลและแตกต่างกันระหว่างการแจกแจง
ดังนั้นการติดตั้ง git ตามคำแนะนำด้านล่างอาจไม่ทำงาน
โปรดตรวจสอบวิธีการติดตั้ง `git' สำหรับการแจกจ่าย Linux ของคุณ
คำสั่งด้านล่างมีคำแนะนำสำหรับระบบที่ใช้เดเบียน

ในการส่งข้อความโดยไม่ระบุชื่อให้พิมพ์คำสั่งต่อไปนี้ใน Termux:
```
pkg ติดตั้ง git
pkg ติดตั้ง python
โคลน git https://github.com/1337XQ/Termux-X-SMS
cd Termux-X-SMS
bash Run.sh
```

### > สำหรับ Linux:

ในการส่งข้อความโดยไม่ระบุชื่อให้พิมพ์คำสั่งต่อไปนี้ในเทอร์มินัล Linux:
```
โคลน git https://github.com/1337XQ/Termux-X-SMS
cd Termux-X-SMS
sudo bash Run.sh
```
 
## อัปเดต:
### V2.1
[+] การเพิ่มคุณสมบัติอัปเดตอัตโนมัติ
