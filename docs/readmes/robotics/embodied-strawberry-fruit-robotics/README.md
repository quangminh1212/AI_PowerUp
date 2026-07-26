<!-- source: https://github.com/smartfarmdiy/Embodied-Strawberry-Fruit-Robotics.git sha: 9dcc3aeffbc33b4c1c57f8583589caca821df790 readme: main/README.md -->
# smartfarmdiy/Embodied-Strawberry-Fruit-Robotics

Embodied-Strawberry-Fruit-Robotics AI camera

---

นี่คือแบบ จำลองระบบเกษตรอัจฉริยะ (Robotics Arm picking Smart Farming) ที่ใช้ AI ขั้นสูงในการควบคุมหุ่นยนต์เก็บเกี่ยวผลผลิต โดยเน้นไปที่ความแม่นยำในการคัดแยกคุณภาพของผลผลิต สตรอเบอรี่ ripe/ unripe/ overripe

การจำลองอินเทอร์เฟซของระบบ "Embodied Reasoning" ซึ่งเป็นการนำ AI (ในที่นี้คือโมเดล Gemini) มาใช้ควบคุมหุ่นยนต์ในโลกกายภาพเพื่อทำงานที่ซับซ้อนครับ โดยมีรายละเอียดที่น่าสนใจดังนี้ครับ:

1. ส่วนจำลองการทำงาน (ด้านซ้าย)
หุ่นยนต์แขนกล (Yellow Robotic Arm): ติดตั้งบนฐานล้อเลื่อน กำลังจำลองการเก็บผลผลิต (ในภาพระบุว่าเป็นสตรอว์เบอร์รี) จากต้นไม้จำลอง

สภาพแวดล้อม: มีการใช้ Grid เพื่อกำหนดพิกัด และมีกล่องสำหรับใส่ผลผลิตที่เก็บได้

แถบควบคุมด้านล่าง: มีปุ่มควบคุมพื้นฐาน เช่น หยุด (Pause), รีเซ็ต, โหมดกลางคืน, ตั้งค่าคอนฟิก, และโหมดการควบคุมแบบ Manual (รูปจอยเกม)

2. ส่วนควบคุม AI และการประมวลผล (ด้านขวา)
Model: ใช้โมเดล gemini-robotics-er-1.5-preview ซึ่งออกแบบมาเพื่อใช้กับงานด้านหุ่นยนต์โดยเฉพาะ

โหมดการตรวจจับ (Selection Tools): * MASKS: (ที่เลือกอยู่) คือการให้ AI ระบุขอบเขตของวัตถุแบบละเอียดตามรูปทรง

BOXES / POINTS: การระบุตำแหน่งแบบกรอบสี่เหลี่ยมหรือจุดพิกัด

Ripeness Filter: ระบบสามารถแยกแยะ "ความสุก" ของผลไม้ได้ โดยมีตัวเลือกตั้งแต่ All (ทั้งหมด), Ripe (สุก), Unripe (ดิบ), ไปจนถึง Overripe (สุกงอม)

Prompt Command: มีช่องใส่คำสั่งภาษาธรรมชาติ เช่น "ripe, unripe, and overripe strawberries" เพื่อให้ AI เข้าใจว่าต้องมองหาอะไร

3. จุดเด่นที่สำคัญ
Embodied Reasoning: หมายถึงการที่ AI ไม่ได้แค่ "คิด" ในคอมพิวเตอร์ แต่สามารถ "เข้าใจบริบทของโลกจริง" และตัดสินใจสั่งการหุ่นยนต์ให้เคลื่อนที่หรือหยิบจับวัตถุได้ถูกต้องตามเงื่อนไข (เช่น เลือกเก็บเฉพาะลูกที่สุก)

Thinking Checkbox: แสดงให้เห็นว่า AI กำลังใช้กระบวนการ "Chain of Thought" หรือการคิดวิเคราะห์ก่อนจะส่งคำสั่งไปยังหุ่นยนต์

![li](https://github.com/user-attachments/assets/0a763d5e-d40b-4a0a-834e-c151a6480639)


MOVE CAMERA


![ki](https://github.com/user-attachments/assets/72e9fb5e-1735-4495-b827-ef4e2a29d3f4)


Video Demonstration

https://www.facebook.com/share/v/1BAoj2Wrdj/


การเชื่อมต่อระบบ Embodied Reasoning หรือ AI ขั้นสูงเข้ากับฮาร์ดแวร์อย่าง ESP32, Raspberry Pi 5 และ AI Camera เพื่อสร้างระบบเกษตรอัจฉริยะ

![mv](https://github.com/user-attachments/assets/b86bc5fc-128d-4c15-964e-4fa4d2cdf23b)


สามารถแบ่งโครงสร้างการเชื่อมต่อได้เป็น 3 ส่วนหลัก

1. การแบ่งหน้าที่ของฮาร์ดแวร์ (System Architecture)
เพื่อให้ระบบทำงานได้ลื่นไหล เราจะแบ่งหน้าที่ตามระดับการประมวลผลดังนี้:

Raspberry Pi 5 (The Brain): ทำหน้าที่เป็น Hub กลาง เชื่อมต่อกับอินเทอร์เน็ตเพื่อส่งข้อมูลไปหา Gemini API และรับคำสั่งมาประมวลผล รวมถึงจัดการเรื่อง Logic หลักของหุ่นยนต์

ESP32 (The Muscles): ทำหน้าที่ควบคุม Motor, Servo หรือระบบปั๊มน้ำ/วาล์วไฟฟ้า โดยรับคำสั่งจาก Raspberry Pi ผ่านโปรโตคอลสื่อสาร

AI Camera (The Eyes): ใช้ Camera Module (เช่น IMX219) หรือ USB Camera ส่งภาพสดให้ Raspberry Pi เพื่อให้ AI วิเคราะห์ความสุกของผลผลิต

2. วิธีการเชื่อมต่อทางกายภาพ (Hardware Connection)
   อุปกรณ์,การเชื่อมต่อ,หน้าที่
Pi 5 ↔ ESP32,UART / I2C / Wi-Fi (MQTT),ส่งคำสั่งควบคุมล้อหรือแขนกล
Pi 5 ↔ AI Camera,CSI Port / USB,ส่ง Input ภาพเข้าสู่โมเดล AI
ESP32 ↔ Motor Driver,PWM Pins,ควบคุมความเร็วและทิศทางของมอเตอร์

3. ขั้นตอนการเชื่อมต่อซอฟต์แวร์ (Software Integration)
Step A: รับภาพจาก Camera
ใช้ Library อย่าง OpenCV ใน Raspberry Pi เพื่อดึงเฟรมภาพ:

import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
# ส่ง frame นี้ไปประมวลผลต่อด้วย Gemini API

Step B: ส่งคำสั่งให้ Gemini AI
ใช้ Google AI Edge หรือ Gemini API โดยส่งภาพไปพร้อมกับ Prompt เช่น "ระบุตำแหน่งสตรอว์เบอร์รีที่สุก (Ripe) ในพิกัด X, Y" เพื่อให้ AI ส่งค่าพิกัดกลับมา

Step C: สั่งการ ESP32 (Micro-ROS หรือ MQTT)
เมื่อได้พิกัดจาก AI แล้ว Raspberry Pi จะส่งข้อมูลให้ ESP32 ผ่าน MQTT (แนะนำเพราะเสถียรสำหรับงาน IoT):

Raspberry Pi: ส่งข้อความ "MOVE_TO_X10_Y20" ไปยัง Topic ใน Broker

ESP32: Subscribe Topic นั้น แล้วสั่งให้ Motor หมุนแขนกลไปที่จุดหมาย

4. ตัวอย่างลำดับการทำงาน (Workflow)
AI Camera จับภาพต้นสตรอว์เบอร์รี

Raspberry Pi 5 ส่งภาพไปให้ Gemini วิเคราะห์ (Embodied Reasoning)

Gemini ตอบกลับมาว่า "ลูกสีแดงทางขวาสุกแล้ว ให้ใช้แขนกลคีบที่พิกัด (120, 85)"

Raspberry Pi 5 คำนวณองศาของมอเตอร์ แล้วส่งคำสั่งผ่าน UART ไปที่ ESP32

ESP32 ขยับแขนกลและคีบผลไม้ลงกล่อง

รายละเอียดการเชื่อมต่อรายส่วน
1. ส่วนรับข้อมูลภาพ (Visual Input)
AI Camera (เช่น Raspberry Pi Camera Module 3 หรือ USB Cam):

เชื่อมต่อเข้ากับ CSI Port หรือ USB Port ของ Raspberry Pi 5

หน้าที่: ถ่ายภาพสดของผลผลิต (สตรอว์เบอร์รี) ส่งเข้า Pi 5 เพื่อรอการประมวลผล

2. ส่วนประมวลผลหลัก (The Brain - Raspberry Pi 5)
การเชื่อมต่อเครือข่าย: เชื่อมต่อ Wi-Fi/Ethernet เพื่อคุยกับ Gemini API ผ่านอินเทอร์เน็ต

ซอฟต์แวร์ภายใน: รัน Python Script เพื่อดึงภาพจากกล้อง -> ส่งไปให้ Gemini วิเคราะห์ (Embodied Reasoning) -> รับพิกัด (X, Y, Z) กลับมา

การส่งคำสั่ง: คำนวณค่าองศามอเตอร์แล้วส่งต่อให้ ESP32

3. ส่วนควบคุมการเคลื่อนที่ (The Muscle - ESP32)
Interface: เชื่อมต่อกับ Pi 5 ผ่านสาย UART (TX/RX) หรือ I2C (แนะนำ UART สำหรับระยะใกล้ หรือ MQTT/Wi-Fi หากแยกบอร์ดกันไกล)

Hardware Control: * Pins: เชื่อมต่อเข้ากับ Motor Driver (เช่น L298N หรือ TB6600)

หน้าที่: รับตัวเลขพิกัดจาก Pi 5 แล้วสั่งให้ Stepper Motor หรือ Servo Motor ของแขนกลขยับไปคีบเป้าหมาย

จาก (Raspberry Pi 5),ไปยัง (ESP32),ประเภทสัญญาณ
GND (Pin 6),GND,Ground (ต้องต่อร่วมกัน)
TX (GPIO 14 - Pin 8),RX (GPIO 16),ส่งคำสั่งควบคุม
RX (GPIO 15 - Pin 10),TX (GPIO 17),รับสถานะตอบกลับ

----------------------------------------------------------------------------------------------------------------

ลำดับการไหลของข้อมูล (Data Flow)

กล้อง $\rightarrow$ ส่งรูปภาพ $\rightarrow$ Raspberry Pi 5Raspberry Pi 5 $\rightarrow$ ส่ง Prompt + รูป $\rightarrow$ Gemini Cloud (AI)Gemini Cloud $\rightarrow$ ส่ง JSON พิกัดวัตถุ $\rightarrow$ Raspberry Pi 5Raspberry Pi 5 $\rightarrow$ ส่งคำสั่ง Serial $\rightarrow$ ESP32ESP32 $\rightarrow$ ปล่อยกระแสไฟฟ้า $\rightarrow$ มอเตอร์แขนกล


Diagram แสดงการทำงานของระบบที่ใช้ ROS2 (Robot Operating System 2) รันบน Raspberry Pi 5 เพื่อจัดการระบบ Inverse Kinematics ของแขนกล ซึ่งออกแบบมาให้สอดคล้องกับภาพจำลองการทำงานและ Diagram การเชื่อมต่อฮาร์ดแวร์

![70](https://github.com/user-attachments/assets/f49b4d12-7fc3-4843-a490-8f47adf07f41)


Diagram นี้จะเน้นให้เห็นถึง Architecture การสื่อสารภายใน (ROS2 Nodes & Topics) ของ Raspberry Pi 5

ภาพ ROS2 Software Architecture Diagram สำหรับแขนกล Smart Farmรายละเอียดการทำงานภายใน Raspberry Pi 5 (รัน ROS2 Humble/Jazzy)Diagram แบ่งออกเป็น 4 ชั้นหลัก เพื่อแสดงลำดับการประมวลผล:
1. ชั้นรับข้อมูล (Perception & AI - อินพุต)Gemini Vision Bridge Node: รับภาพสดจากกล้อง (Vision Input) และทำหน้าที่เป็นตัวกลางในการส่งรูปภาพไปประมวลผลกับ Gemini AI (Cloud) จากนั้นจะรับผลลัพธ์ที่เป็นพิกัดพิกเซลของผลไม้ (เช่น X, Y) ส่งต่อผ่าน Topic /ai/detection_data

2. ชั้นวางแผนการเคลื่อนที่ (Planning - หัวใจหลัก)นี่คือส่วนที่ทำงานสอดคล้องกับ "Robot Logic Engine" ใน Diagram การเชื่อมต่อ:Coordinate Transformer Node: รับพิกัดพิกเซล (Camera Frame) แล้วแปลงให้เป็นพิกัดเชิงมุม/ระยะทางจริงในโลกกายภาพ (Robot Base Frame) เพื่อส่งต่อให้ระบบคำนวณระยะKinematics (IK) Server Node: นี่คือส่วนที่คุณถามถึง โหนดนี้ทำหน้าที่คำนวณ Inverse Kinematics (IK) โดยรับ "เป้าหมายที่ปลายแขน" (Target End-Effector Pose) แล้วใช้สมการคณิตศาสตร์ขั้นสูงคำนวณหา "องศาที่มอเตอร์แต่ละตัวต้องหมุน" (Joint Angles) ของแขนกล (เช่น $q_1, q_2, q_3$ สำหรับแขนกล 3 ข้อต่อ)

3. ชั้นควบคุมฮาร์ดแวร์ (Control)Arm Controller Node: รับ Joint Angles จาก IK Server แล้วสร้างโปรไฟล์การเคลื่อนที่ (Trajector Planning) เพื่อให้แขนกลขยับได้อย่างนุ่มนวล จากนั้นจะส่งคำสั่งเป็นตัวเลขมุมมอเตอร์ที่คำนวณได้ไปยัง Topic /hardware/joint_commands

4. ชั้นการสื่อสารระดับล่าง (Hardware I/O)Serial Communications Node: นี่คือส่วนที่เชื่อมต่อไปยัง Diagram การเชื่อมต่อของคุณ ทำหน้าที่เป็นบริดจ์ในการแปลงคำสั่ง ROS2 เป็นข้อมูล Serial String (เช่น "G0 X120 Y85 Z40") ส่งออกทาง UART ไปยังบอร์ด ESP32 เพื่อขับมอเตอร์จริง5. ส่วนแสดงผล (Visualization)rviz2 (PC/Interface): เป็น Tool ของ ROS2 ที่ใช้แสดงผลจำลอง (Simulated View) ของแขนกลในแบบ 3D แบบเรียลไทม์ ซึ่งจะมีลักษณะใกล้เคียงกับภาพจำลองการทำงาน


ทำไม Architecture นี้ถึงทำงานได้ดีที่สุด?
แบ่งหน้าที่ชัดเจน: แต่ละโหนดทำงานเฉพาะทาง ทำให้ระบบเสถียรและแก้ไขง่าย

ประสิทธิภาพสูงบน Pi 5: Pi 5 มี RAM และ CPU เพียงพอที่จะรันโหนดคณิตศาสตร์ IK และ Coordinate Transform ควบคู่กับการประมวลผลภาพ

ความแม่นยำ: การใช้ IK Server บน ROS2 ช่วยให้การขยับแขนกลเข้าหาผลไม้มีความแม่นยำสูงกว่าการใช้โค้ดขยับทีละข้อต่อด้วยมือ

ความยืดหยุ่น: สามารถเปลี่ยนรุ่นของ AI Model หรือรุ่นของแขนกลได้ง่ายโดยการแก้ไขแค่โหนดเดียว โดยไม่ต้องเขียนระบบใหม่ทั้งหมด


---------------------------------------------------------------------------------------------------------------

# Run and deploy your app

This contains everything you need to run your app locally.

View your app 

## Run Locally

**Prerequisites:**  Node.js


1. Install dependencies:
   `npm install`
2. Set the `GEMINI_API_KEY` in [.env.local](.env.local) to your Gemini API key
3. Run the app:
   `npm run dev`
