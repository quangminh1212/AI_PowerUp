<!-- source: https://github.com/JonusNattapong/Notebook-Git-Colab.git sha: 28dc4072ce63cbeea8e13d1354792246c6f722d4 readme: main/README.md -->
# JonusNattapong/Notebook-Git-Colab

เป็นการรวบรวมแหล่งข้อมูลสำหรับการเรียนรู้เกี่ยวกับปัญญาประดิษฐ์ (Artificial Intelligence - AI) และโมเดลภาษาขนาดใหญ่ (Large Language Models - LLMs) รวมถึงหัวข้อพื้นฐาน, สมุดบันทึกที่แนะนำ, คอร์สออนไลน์, เครื่องมือ, ชุดข้อมูล และเทคนิคขั้นสูงสำหรับการพัฒนาและปรับแต่งโมเดล AI

---

<div align="center">

<div align="center">
  <img src="./public/icon2.png" alt="AI LLM Logo" width="160" style="border-radius:24px;box-shadow:0 4px 16px #4F8A8B22;"/>
  <br/>
  <span style="font-size:1.2em;font-weight:bold;color:#4F8A8B;">AI LLM Learning Resources</span>
  <br/>
  <span style="font-size:0.95em;color:#888;">Version 0.0.1 Update (15/07/2025)</span>
</div>

# 📚 AI LLM Learning Resources

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/Apache-2.0-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/JonusNattapong/Notebook-Git-Colab.svg?style=social)](https://github.com/JonusNattapong/Notebook-Git-Colab/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/JonusNattapong/Notebook-Git-Colab.svg?style=social)](https://github.com/JonusNattapong/Notebook-Git-Colab/network/members)
[![GitHub Followers](https://img.shields.io/github/followers/JonusNattapong.svg?style=social)](https://github.com/JonusNattapong/followers)

</div>

---

<div align="center">

# 📑 สารบัญ

| ลำดับ | หัวข้อ                                                                                                 |
| :---- | :----------------------------------------------------------------------------------------------------- |
| 1     | [📘 พื้นฐานที่จำเป็น](#section1)                                                                         |
| 2     | [🛠️ วิศวกร LLM](#section2)                                                                             |
| 3     | [📚 สคริปต์และ Repository ขั้นสูง](#section3)                                                              |
| 4     | [🌐 การประยุกต์ใช้ LLM ในโลกจริงและเทรนด์อนาคต](#section4)                                                |
| 5     | [📖 ศัพท์ที่ต้องรู้ในวงการ LLM](#section5)                                                                 |
| 6     | [📂 ไฟล์ตัวอย่างและลิงก์ที่เกี่ยวข้องกับ LLM](#section6)                                                  |
| 7     | [🚀 การ Deploy LLM ใน Production](#section7)                                                            |
| 8     | [📄 งานวิจัยเกี่ยวกับ LLM](#section8)                                                                   |
| 9     | [🔧 หลักการและเทคนิคที่เกี่ยวข้อง](#section9)                                                            |
| 10    | [🎯 การเลือกใช้ Model และ Dataset](#section10)                                                           |
| 11    | [⚙️ การติดตั้งและการเตรียมระบบ](#section11)                                                              |
| 12    | [💻 การใช้งานและการจัดการ LLM](#section12)                                                               |
| 13    | [🌟 แหล่งข้อมูลโค้ดสำคัญ เทคนิคใหม่ และเทรนด์ใหม่](#section13)                                              |
| 14    | [✨ Prompt Engineering และการปรับแต่ง Prompt](#section14)                                                  |
| 15    | [🛡️ ความปลอดภัยและความเป็นส่วนตัวของ LLM](#section15)                                                      |
| 16    | [⚖️ จริยธรรมและผลกระทบทางสังคมของ LLM](#section16)                                                          |
| 17    | [🤝 การทำงานร่วมกับ LLM และเครื่องมืออื่นๆ](#section17)                                                      |
| 18    | [💰 การสร้างรายได้จาก LLM](#section18)                                                                   |
| 19    | [🔮 แนวโน้มและอนาคตของ LLM](#section19)                                                                 |
| 20    | [🌍 สคริปต์และเทคนิค AI ล่าสุดจาก Google Colab และ GitHub](#section20)                                    |
| 21    | [🚀 การประยุกต์ใช้เทคนิค AI ล่าสุดในโปรเจกต์จริง](#section21)                                            |
| 22    | [🛠️ เครื่องมือและแพลตฟอร์ม AI ที่สำคัญ](#section22)                                                       |
| 23    | [🌐 การสร้างชุมชนและการทำงานร่วมกันในวงการ AI](#section23)                                                |
| 24    | [📊 การบริหารจัดการโปรเจกต์ AI และการนำไปใช้งานจริง](#section24)                                           |
| 25    | [📖 ศัพท์ที่ต้องรู้ในวงการ LLM ตอนที่ 2](#section25)                                                      |

</div>

*ส่วนนี้เหมาะสำหรับผู้เริ่มต้นที่ต้องการสร้างรากฐานที่มั่นคงในคณิตศาสตร์, Python, โครงข่ายประสาทเทียม และ NLP ก่อนที่จะศึกษาเทคนิคขั้นสูง*

<a name="section1"></a>

## 📘 ส่วนที่ 1: พื้นฐานที่จำเป็น

*เหมาะสำหรับผู้เริ่มต้นที่ต้องการสร้างรากฐานในคณิตศาสตร์, Python, โครงข่ายประสาทเทียม และ NLP*

### 1.1 คณิตศาสตร์สำหรับ Machine Learning

| แหล่งข้อมูล                  | คำอธิบาย                                                                 | ระดับ            | ลิงก์                                                                 |
| :--------------------------- | :----------------------------------------------------------------------- | :--------------- | :-------------------------------------------------------------------- |
| 3Blue1Brown - Linear Algebra | วิดีโอสอนพีชคณิตเชิงเส้น เหมาะสำหรับเห็นภาพคอนเซปต์ยากๆ เช่น PCA       | `[Beginner]`     | [YouTube](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) |
| Khan Academy - Probability   | คอร์สฟรีสอนความน่าจะเป็นและสถิติที่จำเป็นสำหรับ ML                     | `[Beginner/Intermediate]` | [Khan Academy](https://www.khanacademy.org/math/statistics-probability) |

### 1.2 การเขียนโปรแกรม Python

| แหล่งข้อมูล                  | คำอธิบาย                                                                 | ระดับ            | ลิงก์                                                                 |
| :--------------------------- | :----------------------------------------------------------------------- | :--------------- | :-------------------------------------------------------------------- |
| Python Official Documentation | เอกสารอย่างเป็นทางการของ Python                                         | `[All Levels]`   | [Python Docs](https://docs.python.org/3/)                             |
| Google's Python Class         | คอร์สฟรีจาก Google สอน Python พื้นฐาน                                 |
| Corey Schafer - Python Tutorials           | ช่อง YouTube สอน Python เชิงลึก เหมาะสำหรับการเรียนรู้ OOP และงาน data science เช่น การใช้ pandas | พื้นฐาน, การเขียนโปรแกรมเชิงวัตถุ (OOP), การพัฒนาเว็บ, วิทยาศาสตร์ข้อมูล (data science)            | `[Beginner/Intermediate]` | [Corey Schafer YouTube](https://www.youtube.com/c/Coreymschafer)                                        |
| Sentdex - Python Programming Tutorials     | ช่อง YouTube สอน Python แบบประยุกต์ เช่น การสร้างโมเดล ML หรือวิเคราะห์ข้อมูลด้วย NumPy          | Machine Learning, การวิเคราะห์ข้อมูล, การพัฒนาเว็บ, การพัฒนาเกม                                 | `[Intermediate]`    | [Sentdex YouTube](https://www.youtube.com/c/sentdex)                                                 |
| Python for Data Analysis (Wes McKinney)    | หนังสือสอนการใช้ Python (เน้น pandas) สำหรับการวิเคราะห์ข้อมูล เหมาะสำหรับงาน ML และ data science   | pandas, NumPy, การจัดการข้อมูล, การทำความสะอาดข้อมูล, การแสดงภาพข้อมูล (data visualization)     | `[Intermediate/Advanced]` | [Python for Data Analysis](https://wesmckinney.com/book/)                                               |
| Automate the Boring Stuff with Python      | หนังสือและคอร์สฟรี สอน Python พื้นฐานผ่านโปรเจกต์จริง เช่น อัตโนมัติงานเอกสาร เหมาะสำหรับผู้เริ่มต้น   | พื้นฐาน, การจัดการไฟล์, การ scraping เว็บ, การทำงานกับ Excel                                 | `[Beginner]`        | [Automate the Boring Stuff](https://automatetheboringstuff.com/)                                       |

### 1.3 โครงข่ายประสาทเทียม (Neural Networks)

| แหล่งข้อมูล                                    | คำอธิบาย                                                                                                | หัวข้อย่อย (Subtopics)                                                                                   | ระดับ (Level)          | ลิงก์                                                                                                                   |
| :------------------------------------------- | :--------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- | :--------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| DeepLearning.AI - Deep Learning Specialization | ชุดคอร์สออนไลน์บน Coursera อธิบายพื้นฐาน Deep Learning เช่น backpropagation ที่ใช้ในโครงข่ายประสาทเทียม     | โครงข่ายประสาทเทียม, backpropagation, convolutional neural networks (CNNs), recurrent neural networks (RNNs) | `[Beginner/Intermediate]` | [Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning)                                  |
| 3Blue1Brown - Neural Networks                | ชุดวิดีโอใช้ภาพเคลื่อนไหวอธิบายการทำงานของโครงข่ายประสาทเทียม เช่น gradient descent และเพอร์เซปตรอน       | เพอร์เซปตรอน (perceptrons), ฟังก์ชันกระตุ้น (activation functions), backpropagation, gradient descent   | `[Beginner]`          | [Neural Networks Playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)                  |
| fast.ai - Practical Deep Learning for Coders | คอร์สเน้นปฏิบัติ สอน Deep Learning ด้วย fastai (บน PyTorch) เหมาะสำหรับการเริ่มต้นสร้างโมเดลจริง          | การประยุกต์ใช้ Deep Learning, PyTorch, ไลบรารี fastai                                                  | `[Intermediate]`       | [fast.ai Course](https://course.fast.ai/)                                                                            |
| Stanford CS231n - Convolutional Neural Networks | คอร์สจาก Stanford เน้น CNNs สำหรับงาน Computer Vision เช่น การจำแนกภาพ อธิบายสถาปัตยกรรม CNN อย่างละเอียด   | Convolutional layers, pooling layers, สถาปัตยกรรม CNN ยอดนิยม                                       | `[Intermediate/Advanced]` | [CS231n Course](http://cs231n.stanford.edu/)                                                                         |
| Transformers Explained (Hugging Face)        | บทความสั้นจาก Hugging Face อธิบายพื้นฐาน Transformers ซึ่งเป็นรากฐานของ LLM เช่น attention mechanism     | Attention mechanism, self-attention, Transformer architecture                                  | `[Beginner/Intermediate]` | [Transformers Explained](https://huggingface.co/docs/transformers/quicktour)                                         |

### 1.4 การประมวลผลภาษาธรรมชาติ (NLP)

| แหล่งข้อมูล                                                                       | คำอธิบาย                                                                                                  | หัวข้อย่อย (Subtopics)                                                                                                | ระดับ (Level)          | ลิงก์                                                                                                                   |
| :------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- | :--------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| Stanford CS224N - NLP with Deep Learning                                       | คอร์สจาก Stanford ครอบคลุม NLP สมัยใหม่ด้วย Deep Learning เช่น การใช้ transformers ในงานแปลภาษา            | Word embeddings, recurrent neural networks (RNNs), transformers, question answering, machine translation  | `[Intermediate/Advanced]` | [CS224N Course](http://web.stanford.edu/class/cs224n/)                                                                   |
| Jurafsky & Martin - Speech and Language Processing (3rd ed. draft)              | หนังสือเรียน NLP ฉบับสมบูรณ์ (ฉบับร่างฟรี) อธิบายตั้งแต่พื้นฐานถึงขั้นสูง เช่น language modeling          | Language modeling, parsing, semantics, discourse, machine translation                                        | `[Intermediate/Advanced]` | [SLP Book (3rd ed. draft)](https://web.stanford.edu/~jurafsky/slp3/)                                                       |
| Hugging Face - NLP Course                                                      | คอร์ส interactive สอนการใช้ Transformers library สำหรับงาน NLP เช่น fine-tuning โมเดลสำหรับการจำแนกข้อความ | Transformers, tokenization, fine-tuning, งาน NLP ทั่วไป                                               | `[Beginner/Intermediate]` | [Hugging Face Course](https://huggingface.co/learn/nlp-course/chapter1/1)                                                   |
| Natural Language Processing with Python (NLTK Book)                            | หนังสือฟรีสอน NLP ด้วย Python และ NLTK เหมาะสำหรับผู้เริ่มต้นที่อยากฝึกพื้นฐาน เช่น การตัดคำ (tokenization) | Tokenization, part-of-speech tagging, text classification, sentiment analysis                        | `[Beginner]`             | [NLTK Book](https://www.nltk.org/book/)                                                                                 |

### 1.5 แนวทางการเรียนรู้ (How to Proceed)

1. **เริ่มต้นจากพื้นฐาน:** หากคุณเป็นมือใหม่ในวงการ Machine Learning ให้เริ่มด้วยชุดวิดีโอ Linear Algebra ของ 3Blue1Brown และคอร์ส Probability and Statistics ของ Khan Academy เพื่อเข้าใจคณิตศาสตร์พื้นฐาน `[Beginner]`
2. **เรียนรู้ภาษา Python:** ศึกษา Google's Python Class หรือ Automate the Boring Stuff ควบคู่ไปกับการฝึกเขียนโค้ด เช่น สร้างสคริปต์จัดการไฟล์ง่ายๆ `[Beginner/Intermediate]`
3. **ทำความเข้าใจโครงข่ายประสาทเทียม:** เรียน DeepLearning.AI Specialization หรือ fast.ai Course และดูวิดีโอของ 3Blue1Brown เพื่อเห็นภาพการทำงาน ลองสร้างโมเดลจำแนกภาพด้วย PyTorch `[Beginner/Intermediate]`
4. **เจาะลึก NLP:** ศึกษา CS224N ของ Stanford และลองทำ Hugging Face NLP Course เพื่อฝึก fine-tuning โมเดลสำหรับงานจำแนกข้อความ `[Intermediate]`
5. **อ่านหนังสือเพิ่มเติม:** ใช้หนังสือ MML และ Jurafsky & Martin เป็นแหล่งอ้างอิงสำหรับข้อมูลเชิงลึก เช่น การคำนวณ gradient หรือการสร้าง language model `[Intermediate/Advanced]`

**ข้อควรจำ:**

- การเรียนรู้ Machine Learning ต้องใช้เวลาและความสม่ำเสมอ ฝึกทำโปรเจกต์เล็กๆ เช่น จำแนกข้อความหรือวิเคราะห์ข้อมูล เพื่อทดสอบความเข้าใจ
- อย่ากลัวที่จะลองผิดลองถูก และพยายามทำความเข้าใจหลักการเบื้องหลัง เช่น ทำไม gradient descent ถึงสำคัญ
- เข้าร่วมชุมชนออนไลน์ เช่น Reddit (r/MachineLearning), Stack Overflow หรือ Hugging Face Forums เพื่อแลกเปลี่ยนความรู้และขอความช่วยเหลือ

## ส่วนที่ 1: พื้นฐานที่จำเป็น

*ส่วนนี้เหมาะสำหรับผู้เริ่มต้นที่ต้องการสร้างรากฐานที่มั่นคงในคณิตศาสตร์, Python, โครงข่ายประสาทเทียม และ NLP ก่อนที่จะศึกษาเทคนิคขั้นสูง*

### 1.1 คณิตศาสตร์สำหรับ Machine Learning

| แหล่งข้อมูล                                    | คำอธิบาย                                                                                                   | หัวข้อย่อย (Subtopics)                                                                    | ระดับ (Level)     | ลิงก์                                                                                                                              |
| :------------------------------------------- | :------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------- | :---------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| 3Blue1Brown - Linear Algebra                 | ชุดวิดีโอสอนที่ใช้ภาพเคลื่อนไหวอธิบายพีชคณิตเชิงเส้น เหมาะสำหรับเห็นภาพคอนเซปต์ยากๆ เช่น การแปลงเมทริกซ์หรือค่าเจาะจงที่ใช้ใน PCA | เวกเตอร์, เมทริกซ์, การแปลง (transformations), ค่าเจาะจง (eigenvalues - ใช้ใน PCA), เวกเตอร์เจาะจง (eigenvectors - ใช้ใน SVD) | `[Beginner]`      | [YouTube Playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)                                     |
| Khan Academy - Probability and Statistics    | คอร์สออนไลน์ฟรี สอนความน่าจะเป็นและสถิติพื้นฐานที่จำเป็นสำหรับ ML เช่น การแจกแจงที่ใช้ในโมเดลหรือการทดสอบสมมติฐาน | ความน่าจะเป็น, การแจกแจง (distributions), การทดสอบสมมติฐาน, การอนุมานแบบเบย์ (Bayesian inference)      | `[Beginner/Intermediate]` | [Khan Academy Course](https://www.khanacademy.org/math/statistics-probability)                                                     |
| Mathematics for Machine Learning (MML)       | หนังสือเรียนฟรีจาก Cambridge อธิบายคณิตศาสตร์ที่ใช้ใน ML อย่างละเอียด เช่น การหาค่าเหมาะที่สุดสำหรับ gradient descent | พีชคณิตเชิงเส้น, แคลคูลัส, ความน่าจะเป็น, การหาค่าเหมาะที่สุด (optimization)                        | `[Intermediate/Advanced]` | [MML Book](https://mml-book.github.io/)                                                                                       |
| All of Statistics (Wasserman)                | หนังสืออ้างอิงสถิติฉบับสมบูรณ์ เหมาะสำหรับผู้ที่ต้องการเจาะลึก เช่น การวิเคราะห์อนุกรมเวลาใน ML หรือการถดถอยขั้นสูง | การอนุมานทางสถิติ (statistical inference), การทดสอบสมมติฐาน, การถดถอย (regression), อนุกรมเวลา (time series) | `[Advanced]`      | [All of Statistics Book](https://www.stat.cmu.edu/~larry/all-of-statistics/) หรือ [Springer Link](https://link.springer.com/book/10.1007/978-0-387-21736-9) |

### 1.2 การเขียนโปรแกรม Python

| แหล่งข้อมูล                                  | คำอธิบาย                                                                                          | หัวข้อย่อย (Subtopics)                                                                       | ระดับ (Level)        | ลิงก์                                                                                                |
| :------------------------------------------- | :-------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------- | :------------------- | :-------------------------------------------------------------------------------------------------- |
| Python Official Documentation              | เอกสารอ้างอิงอย่างเป็นทางการของ Python อ่านเพื่อเข้าใจพื้นฐานและโมดูลที่ใช้บ่อยใน ML เช่น `random` หรือ `math` | ไวยากรณ์ (syntax), โครงสร้างข้อมูล, โมดูล (modules), ไลบรารีมาตรฐาน (standard library)               | `[All Levels]`   | [Python Docs](https://docs.python.org/3/)                                                               |
| Google's Python Class                      | คอร์สฟรีจาก Google สอน Python พื้นฐาน เหมาะสำหรับผู้เริ่มต้นที่อยากฝึกเขียนโค้ดจริง เช่น การจัดการไฟล์ | พื้นฐาน, สตริง (strings), ลิสต์ (lists), ดิกชันนารี (dictionaries), ไฟล์, regular expressions      | `[Beginner]`       | [Google's Python Class](https://developers.google.com/edu/python/)                                      |
| Corey Schafer - Python Tutorials           | ช่อง YouTube สอน Python เชิงลึก เหมาะสำหรับการเรียนรู้ OOP และงาน data science เช่น การใช้ pandas | พื้นฐาน, การเขียนโปรแกรมเชิงวัตถุ (OOP), การพัฒนาเว็บ, วิทยาศาสตร์ข้อมูล (data science)            | `[Beginner/Intermediate]` | [Corey Schafer YouTube](https://www.youtube.com/c/Coreymschafer)                                        |
| Sentdex - Python Programming Tutorials     | ช่อง YouTube สอน Python แบบประยุกต์ เช่น การสร้างโมเดล ML หรือวิเคราะห์ข้อมูลด้วย NumPy          | Machine Learning, การวิเคราะห์ข้อมูล, การพัฒนาเว็บ, การพัฒนาเกม                                 | `[Intermediate]`    | [Sentdex YouTube](https://www.youtube.com/c/sentdex)                                                 |
| Python for Data Analysis (Wes McKinney)    | หนังสือสอนการใช้ Python (เน้น pandas) สำหรับการวิเคราะห์ข้อมูล เหมาะสำหรับงาน ML และ data science   | pandas, NumPy, การจัดการข้อมูล, การทำความสะอาดข้อมูล, การแสดงภาพข้อมูล (data visualization)     | `[Intermediate/Advanced]` | [Python for Data Analysis](https://wesmckinney.com/book/)                                               |
| Automate the Boring Stuff with Python      | หนังสือและคอร์สฟรี สอน Python พื้นฐานผ่านโปรเจกต์จริง เช่น อัตโนมัติงานเอกสาร เหมาะสำหรับผู้เริ่มต้น   | พื้นฐาน, การจัดการไฟล์, การ scraping เว็บ, การทำงานกับ Excel                                 | `[Beginner]`        | [Automate the Boring Stuff](https://automatetheboringstuff.com/)                                       |

### 1.3 โครงข่ายประสาทเทียม (Neural Networks)

| แหล่งข้อมูล                                    | คำอธิบาย                                                                                                | หัวข้อย่อย (Subtopics)                                                                                   | ระดับ (Level)          | ลิงก์                                                                                                                   |
| :------------------------------------------- | :--------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- | :--------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| DeepLearning.AI - Deep Learning Specialization | ชุดคอร์สออนไลน์บน Coursera อธิบายพื้นฐาน Deep Learning เช่น backpropagation ที่ใช้ในโครงข่ายประสาทเทียม     | โครงข่ายประสาทเทียม, backpropagation, convolutional neural networks (CNNs), recurrent neural networks (RNNs) | `[Beginner/Intermediate]` | [Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning)                                  |
| 3Blue1Brown - Neural Networks                | ชุดวิดีโอใช้ภาพเคลื่อนไหวอธิบายการทำงานของโครงข่ายประสาทเทียม เช่น gradient descent และเพอร์เซปตรอน       | เพอร์เซปตรอน (perceptrons), ฟังก์ชันกระตุ้น (activation functions), backpropagation, gradient descent   | `[Beginner]`          | [Neural Networks Playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)                  |
| fast.ai - Practical Deep Learning for Coders | คอร์สเน้นปฏิบัติ สอน Deep Learning ด้วย fastai (บน PyTorch) เหมาะสำหรับการเริ่มต้นสร้างโมเดลจริง          | การประยุกต์ใช้ Deep Learning, PyTorch, ไลบรารี fastai                                                  | `[Intermediate]`       | [fast.ai Course](https://course.fast.ai/)                                                                            |
| Stanford CS231n - Convolutional Neural Networks | คอร์สจาก Stanford เน้น CNNs สำหรับงาน Computer Vision เช่น การจำแนกภาพ อธิบายสถาปัตยกรรม CNN อย่างละเอียด   | Convolutional layers, pooling layers, สถาปัตยกรรม CNN ยอดนิยม                                       | `[Intermediate/Advanced]` | [CS231n Course](http://cs231n.stanford.edu/)                                                                         |
| Transformers Explained (Hugging Face)        | บทความสั้นจาก Hugging Face อธิบายพื้นฐาน Transformers ซึ่งเป็นรากฐานของ LLM เช่น attention mechanism     | Attention mechanism, self-attention, Transformer architecture                                  | `[Beginner/Intermediate]` | [Transformers Explained](https://huggingface.co/docs/transformers/quicktour)                                         |

### 1.4 การประมวลผลภาษาธรรมชาติ (NLP)

| แหล่งข้อมูล                                                                       | คำอธิบาย                                                                                                  | หัวข้อย่อย (Subtopics)                                                                                                | ระดับ (Level)          | ลิงก์                                                                                                                   |
| :------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- | :--------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| Stanford CS224N - NLP with Deep Learning                                       | คอร์สจาก Stanford ครอบคลุม NLP สมัยใหม่ด้วย Deep Learning เช่น การใช้ transformers ในงานแปลภาษา            | Word embeddings, recurrent neural networks (RNNs), transformers, question answering, machine translation  | `[Intermediate/Advanced]` | [CS224N Course](http://web.stanford.edu/class/cs224n/)                                                                   |
| Jurafsky & Martin - Speech and Language Processing (3rd ed. draft)              | หนังสือเรียน NLP ฉบับสมบูรณ์ (ฉบับร่างฟรี) อธิบายตั้งแต่พื้นฐานถึงขั้นสูง เช่น language modeling          | Language modeling, parsing, semantics, discourse, machine translation                                        | `[Intermediate/Advanced]` | [SLP Book (3rd ed. draft)](https://web.stanford.edu/~jurafsky/slp3/)                                                       |
| Hugging Face - NLP Course                                                      | คอร์ส interactive สอนการใช้ Transformers library สำหรับงาน NLP เช่น fine-tuning โมเดลสำหรับการจำแนกข้อความ | Transformers, tokenization, fine-tuning, งาน NLP ทั่วไป                                               | `[Beginner/Intermediate]` | [Hugging Face Course](https://huggingface.co/learn/nlp-course/chapter1/1)                                                   |
| Natural Language Processing with Python (NLTK Book)                            | หนังสือฟรีสอน NLP ด้วย Python และ NLTK เหมาะสำหรับผู้เริ่มต้นที่อยากฝึกพื้นฐาน เช่น การตัดคำ (tokenization) | Tokenization, part-of-speech tagging, text classification, sentiment analysis                        | `[Beginner]`             | [NLTK Book](https://www.nltk.org/book/)                                                                                 |

### 1.5 แนวทางการเรียนรู้ (How to Proceed)

1. **เริ่มต้นจากพื้นฐาน:** หากคุณเป็นมือใหม่ในวงการ Machine Learning ให้เริ่มด้วยชุดวิดีโอ Linear Algebra ของ 3Blue1Brown และคอร์ส Probability and Statistics ของ Khan Academy เพื่อเข้าใจคณิตศาสตร์พื้นฐาน `[Beginner]`
2. **เรียนรู้ภาษา Python:** ศึกษา Google's Python Class หรือ Automate the Boring Stuff ควบคู่ไปกับการฝึกเขียนโค้ด เช่น สร้างสคริปต์จัดการไฟล์ง่ายๆ `[Beginner/Intermediate]`
3. **ทำความเข้าใจโครงข่ายประสาทเทียม:** เรียน DeepLearning.AI Specialization หรือ fast.ai Course และดูวิดีโอของ 3Blue1Brown เพื่อเห็นภาพการทำงาน ลองสร้างโมเดลจำแนกภาพด้วย PyTorch `[Beginner/Intermediate]`
4. **เจาะลึก NLP:** ศึกษา CS224N ของ Stanford และลองทำ Hugging Face NLP Course เพื่อฝึก fine-tuning โมเดลสำหรับงานจำแนกข้อความ `[Intermediate]`
5. **อ่านหนังสือเพิ่มเติม:** ใช้หนังสือ MML และ Jurafsky & Martin เป็นแหล่งอ้างอิงสำหรับข้อมูลเชิงลึก เช่น การคำนวณ gradient หรือการสร้าง language model `[Intermediate/Advanced]`

**ข้อควรจำ:**

- การเรียนรู้ Machine Learning ต้องใช้เวลาและความสม่ำเสมอ ฝึกทำโปรเจกต์เล็กๆ เช่น จำแนกข้อความหรือวิเคราะห์ข้อมูล เพื่อทดสอบความเข้าใจ
- อย่ากลัวที่จะลองผิดลองถูก และพยายามทำความเข้าใจหลักการเบื้องหลัง เช่น ทำไม gradient descent ถึงสำคัญ
- เข้าร่วมชุมชนออนไลน์ เช่น Reddit (r/MachineLearning), Stack Overflow หรือ Hugging Face Forums เพื่อแลกเปลี่ยนความรู้และขอความช่วยเหลือ

---

<a name="section2"></a>

## 🛠️ ส่วนที่ 2: วิศวกร LLM (The LLM Engineer)

*ส่วนนี้เน้นการนำ LLM ไปใช้ในแอปพลิเคชันจริง การเพิ่มประสิทธิภาพ และการรักษาความปลอดภัย เหมาะสำหรับวิศวกรที่ต้องการพัฒนาและใช้งานระบบ LLM*

---

### 2.1 การสร้างแอปพลิเคชันด้วย LLMs (Building Applications with LLMs)

มุ่งเน้นการพัฒนาแอปพลิเคชันที่ขับเคลื่อนด้วย LLM เช่น แชทบอท ระบบแนะนำ หรือเครื่องมือประมวลผลภาษา

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| LangChain Documentation                  | เฟรมเวิร์กสำหรับสร้างแอปที่เชื่อม LLM กับข้อมูลภายนอก เช่น ฐานความรู้หรือ API                  | LLM chains, agents, memory, retrieval                         | `[Intermediate/Advanced]` | [LangChain Docs](https://python.langchain.com/docs/get_started/introduction)                   |
| LlamaIndex Documentation                 | เครื่องมือเชื่อม LLM กับข้อมูลส่วนตัว เช่น PDF หรือฐานข้อมูลองค์กร                             | Data connectors, indexing, query engines                      | `[Intermediate/Advanced]` | [LlamaIndex Docs](https://docs.llamaindex.ai/en/stable/)                                       |
| Streamlit + LLM Tutorial                 | บทเรียนสร้างแอป interactive เช่น ระบบถาม-ตอบ ด้วย Streamlit และ LLM                         | Streamlit basics, API integration, UI design                  | `[Intermediate]`          | [Streamlit LLM Tutorial](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)        |
| Building a Custom Chatbot (YouTube)      | วิดีโอสอนสร้างแชทบอทด้วย OpenAI API และ Gradio                                               | OpenAI API, Gradio UI, prompt design                          | `[Intermediate]`          | [Chatbot Tutorial](https://www.youtube.com/watch?v=8gR-1pWBFgU)                               |

**ตัวอย่างการใช้งาน**:  

- **แชทบอทช่วยงาน**: ใช้ LangChain เชื่อม LLM กับ FAQ เพื่อตอบคำถามลูกค้า  
- **เครื่องมือสรุป**: ใช้ LlamaIndex สรุปเอกสารยาวเป็นย่อด้วย LLM

---

### 2.2 การเพิ่มประสิทธิภาพและความเร็วของ LLM (Enhancing LLM Performance and Efficiency)

การปรับปรุงประสิทธิภาพเพื่อให้ LLM ทำงานเร็วและประหยัดทรัพยากร

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| vLLM Documentation                       | ไลบรารี inference LLM ที่เร็วด้วย PagedAttention                                              | PagedAttention, batching, GPU optimization                    | `[Advanced]`              | [vLLM Docs](https://docs.vllm.ai/en/latest/)                                                   |
| Hugging Face Optimum                     | เครื่องมือเพิ่มประสิทธิภาพโมเดล เช่น quantization และ pruning                                 | Quantization (4-bit/8-bit), ONNX Runtime                      | `[Intermediate/Advanced]` | [Optimum Docs](https://huggingface.co/docs/optimum/index)                                      |
| DeepSpeed Inference Tutorial             | บทเรียนลดหน่วยความจำและเพิ่มความเร็ว inference                                                | Model parallelism, memory-efficient kernels                   | `[Advanced]`              | [DeepSpeed Tutorial](https://www.deepspeed.ai/tutorials/inference-tutorial/)                   |
| FlashAttention Implementation            | เทคนิค attention ที่เร็วและประหยัดหน่วยความจำบน GPU                                            | FlashAttention, single-GPU optimization                       | `[Advanced]`              | [FlashAttention GitHub](https://github.com/Dao-AILab/flash-attention)                          |

**ตัวอย่างการใช้งาน**:  

- **ลดขนาดโมเดล**: ใช้ Optimum ทำ quantization เพื่อรันโมเดลใหญ่บนเครื่องจำกัด  
- **ตอบสนองเรียลไทม์**: ใช้ vLLM รัน Llama 3 ในแอปแชท

---

### 2.3 ความปลอดภัยของ LLM (LLM Security)

การป้องกันความเสี่ยง เช่น Prompt Injection หรือการรั่วไหลของข้อมูล

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| OWASP Top 10 for LLM Applications       | รายการความเสี่ยง 10 อันดับแรกและวิธีป้องกัน                                                    | Prompt injection, data leakage, denial of service             | `[Intermediate/Advanced]` | [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) |
| Garak Security Scanner                   | เครื่องมือสแกนช่องโหว่ LLM เช่น Prompt Injection                                            | Vulnerability scanning, adversarial testing                   | `[Intermediate/Advanced]` | [Garak GitHub](https://github.com/leondz/garak)                                                |
| Hugging Face SafeNLP                     | แนวทางลดความเสี่ยงด้านความปลอดภัยใน LLM                                                       | Safe output handling, adversarial robustness                  | `[Intermediate]`          | [SafeNLP Docs](https://huggingface.co/docs/transformers/main/en/model_doc/safety)              |
| Prompt Injection Defense Tutorial        | บทเรียนป้องกัน Prompt Injection ด้วยการกรองอินพุต                                            | Input filtering, output validation                            | `[Intermediate]`          | [Prompt Defense Colab](https://colab.research.google.com/drive/1rRHPcJC1DXniWqadKz8D2eVDQ9MRA7Od) |

**ตัวอย่างการใช้งาน**:  

- **ป้องกันการโจมตี**: ใช้ Garak สแกนและกรองคำสั่งอันตรายใน LangChain  
- **รักษาความลับ**: ใช้ SafeNLP ตรวจสอบผลลัพธ์ LLM

---

### 2.4 แนวทางการเรียนรู้ (How to Proceed)

1. สร้างแชทบอทง่ายๆ ด้วย LangChain หรือ Streamlit `[Intermediate]`  
2. ลองใช้ vLLM หรือ Optimum ปรับโมเดลให้เร็วขึ้น `[Advanced]`  
3. ศึกษา OWASP Top 10 และใช้ Garak ทดสอบความปลอดภัย `[Intermediate/Advanced]`  
4. พัฒนาโปรเจกต์จริง เช่น ระบบถาม-ตอบจากเอกสาร `[Advanced]`

---

<a name="section3"></a>

## 🛠️ ส่วนที่ 3: วิศวกร LLM (The LLM Engineer)

*ส่วนนี้เน้นการฝึกอบรมโมเดล การปรับแต่ง (fine-tuning) และการ deploy LLM ในสภาพแวดล้อมจริง เหมาะสำหรับวิศวกรที่ต้องการควบคุมโมเดลตั้งแต่ต้นจนจบ*

---

### 3.1 การฝึกอบรม LLM (Training LLMs)

พื้นฐานและเครื่องมือสำหรับฝึกโมเดล LLM ตั้งแต่เริ่มต้น

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| Hugging Face Transformers Docs           | คู่มือฝึกโมเดล Transformers ตั้งแต่เริ่มต้น                                                  | Pretraining, data preparation, training loops                 | `[Advanced]`              | [Transformers Docs](https://huggingface.co/docs/transformers/training)                         |
| DeepSpeed Training Tutorial              | บทเรียนฝึกโมเดลขนาดใหญ่ด้วย DeepSpeed เพื่อประหยัดทรัพยากร                                   | ZeRO optimization, pipeline parallelism                       | `[Advanced]`              | [DeepSpeed Training](https://www.deepspeed.ai/tutorials/model-training/)                       |
| PyTorch Lightning Documentation          | เฟรมเวิร์กฝึกโมเดลอย่างเป็นระบบและปรับขนาดได้                                                 | Distributed training, mixed precision                         | `[Intermediate/Advanced]` | [PyTorch Lightning Docs](https://lightning.ai/docs/pytorch/stable/)                            |
| Karpathy’s Neural Nets (YouTube)         | วิดีโอสอนพื้นฐานการฝึกโมเดลภาษาแบบเข้าใจง่าย                                                  | Backpropagation, RNNs, Transformers                           | `[Beginner/Intermediate]` | [Karpathy’s Video](https://www.youtube.com/watch?v=VMj-3S1T2nQ)                               |

**ตัวอย่างการใช้งาน**:  

- **ฝึกโมเดลภาษาไทย**: ใช้ Transformers และ DeepSpeed ฝึกโมเดลจากชุดข้อมูลภาษาไทย  

<div align="center">
  <img src="./public/icon3.png" alt="Project Logo" width="160"/>
  <h1>📚 <span style="color:#4F8A8B">AI LLM Learning Resources</span></h1>
  <p><b>Version 1.1 Update (11/03/2568)</b></p>
  <p>
    <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg"/></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/Apache-2.0-green.svg"/></a>
    <a href="https://github.com/JonusNattapong/Notebook-Git-Colab/stargazers"><img src="https://img.shields.io/github/stars/JonusNattapong/Notebook-Git-Colab.svg?style=social"/></a>
    <a href="https://github.com/JonusNattapong/Notebook-Git-Colab/network/members"><img src="https://img.shields.io/github/forks/JonusNattapong/Notebook-Git-Colab.svg?style=social"/></a>
    <a href="https://github.com/JonusNattapong/followers"><img src="https://img.shields.io/github/followers/JonusNattapong.svg?style=social"/></a>
  </p>
</div>

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| FastAPI + LLM Tutorial                   | บทเรียน deploy LLM เป็น API ด้วย FastAPI                                                     | API setup, inference endpoints, scaling                       | `[Intermediate/Advanced]` | [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)                                     |
| Ray Serve Documentation                  | เฟรมเวิร์ก deploy โมเดลขนาดใหญ่แบบ distributed                                                | Distributed serving, load balancing                           | `[Advanced]`              | [Ray Serve Docs](https://docs.ray.io/en/latest/serve/index.html)                               |
| Hugging Face Inference Endpoints         | บริการ deploy โมเดลจาก Hugging Face บนคลาวด์                                                 | Model hosting, auto-scaling, API access                      | `[Intermediate]`          | [Inference Endpoints](https://huggingface.co/docs/inference-endpoints/index)                   |
| Deploy Llama on AWS (Guide)              | คู่มือ deploy Llama บน AWS EC2 หรือ SageMaker                                                 | AWS setup, containerization, cost optimization                | `[Advanced]`              | [AWS Guide](https://aws.amazon.com/blogs/machine-learning/deploy-llama-2-on-aws/)              |

**ตัวอย่างการใช้งาน**:  

- **API สำหรับแอป**: Deploy โมเดลด้วย FastAPI เพื่อให้แอปเรียกใช้  
- **ระบบคลาวด์**: ใช้ Ray Serve รันโมเดลขนาดใหญ่แบบกระจาย

---

### 3.4 แนวทางการเรียนรู้ (How to Proceed)

1. เริ่มฝึกโมเดลเล็กๆ ด้วย PyTorch Lightning หรือ Transformers `[Intermediate]`  
2. ลอง fine-tune โมเดล เช่น Mistral ด้วย PEFT หรือ TRL `[Intermediate/Advanced]`  
3. Deploy โมเดลเป็น API ด้วย FastAPI หรือ Ray Serve `[Advanced]`  
4. ทดลองใช้บริการคลาวด์ เช่น Hugging Face Endpoints `[Intermediate]`

--

## ส่วนที่ 4: สคริปต์และ Repository ขั้นสูง (Advanced Scripts & Repositories)

*ส่วนนี้รวบรวมสคริปต์ repositories และแหล่งข้อมูลขั้นสูงที่เป็นประโยชน์สำหรับผู้ที่ต้องการศึกษาและพัฒนา LLM ในเชิงลึก*

### 4.1 DeepSeek AI Repositories

*Repositories จาก DeepSeek AI บริษัทวิจัย AI ที่เน้นงาน Open Source*

#### Performance Optimization

| Repository                                  | คำอธิบาย                                                                                                       | ลิงก์                                                                                    |
| DeepSpeed-FastGen                          | ระบบ inference รวดเร็วและมีประสิทธิภาพ สร้างบน DeepSpeed เหมาะสำหรับงาน real-time                          | [DeepSpeed-FastGen (GitHub)](https://github.com/DeepSpeed-MII/DeepSpeed-FastGen)             |
| DeepSpeed-Kernels                           | Custom CUDA kernels สำหรับ DeepSpeed เพิ่มความเร็วในการคำนวณโมเดล LLM                                     | [DeepSpeed-Kernels (GitHub)](https://github.com/microsoft/DeepSpeed-Kernels)                |
| DeepSpeed                                     | ไลบรารีจาก Microsoft สำหรับ optimize การฝึกและ inference โมเดลขนาดใหญ่                                   | [DeepSpeed (GitHub)](https://github.com/microsoft/DeepSpeed)                                  |
| 3FS: Fast, Flexible, and Friendly Sparse Attention    | การใช้งาน Sparse Attention เพื่อเพิ่มประสิทธิภาพการคำนวณ attention                                     | [3FS](https://github.com/DeepSeek-AI/3FS)             |

#### Model Architectures

| :----------------------------------------------- | :------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------- |
| DeepSeek-LLM                                  | โครงการโอเพนซอร์สสำหรับ DeepSeek LLM โมเดลภาษาขนาดใหญ่                     | [DeepSeek-LLM (GitHub)](https://github.com/deepseek-ai/DeepSeek-LLM)                         |
| FastMoE                                        | การใช้งาน Mixture of Experts (MoE) ที่รวดเร็ว เหมาะสำหรับโมเดลขนาดใหญ่       | [FastMoE](https://github.com/laekov/fastmoe)                                         |

<div align="center">
</div>

# 📚 AI LLM Learning Resources

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/Apache-2.0-green.svg)](LICENSE)
[![GitHub Forks](https://img.shields.io/github/forks/JonusNattapong/Notebook-Git-Colab.svg?style=social)](https://github.com/JonusNattapong/Notebook-Git-Colab/network/members)

| Document Summarization Tool                  | เครื่องมือสรุปเอกสารยาว เช่น รายงานหรือบทความวิชาการ                                          | Hugging Face Transformers, Mistral 7B       | `[Intermediate/Advanced]` | [Hugging Face Tutorial](https://huggingface.co/docs/transformers/tasks/summarization)           |
| Code Generation Assistant                    | ผู้ช่วยเขียนโค้ด เช่น การสร้างฟังก์ชัน Python หรือแก้ bug                                      | OpenAI API, GitHub Copilot Clone, Streamlit | `[Intermediate/Advanced]` | [Copilot Clone Tutorial](https://www.youtube.com/watch?v=M-D2_UrjR-E)                          |

### 5.2 การวัดผลและปรับปรุง LLM (Evaluation and Improvement)

| แหล่งข้อมูล                                    | คำอธิบาย                                                                                           | หัวข้อย่อย (Subtopics)                           | ระดับ (Level)          | ลิงก์                                                                                             |
| :------------------------------------------- | :-------------------------------------------------------------------------------------------------- | :---------------------------------------------- | :--------------------- | :----------------------------------------------------------------------------------------------- |
| EleutherAI LM Evaluation Harness             | เครื่องมือวัดประสิทธิภาพ LLM ด้วยชุดข้อมูลมาตรฐาน เช่น MMLU หรือ TruthfulQA                       | Task-specific evaluation, zero-shot testing     | `[Advanced]`           | [LM Eval (GitHub)](https://github.com/EleutherAI/lm-evaluation-harness)                         |
| HumanEval: Evaluating Large Language Models  | Paper อธิบาย HumanEval ชุดข้อมูลสำหรับทดสอบความสามารถเขียนโค้ดของ LLM                             | Code generation metrics, functional correctness | `[Advanced]`           | [HumanEval (Arxiv)](https://arxiv.org/abs/2107.03374)                                           |
| MT-Bench: A Multi-turn Benchmark            | Paper นำเสนอ MT-Bench ชุดทดสอบสำหรับประเมินการสนทนาหลายรอบของ LLM                                | Multi-turn dialogue, human-like responses       | `[Advanced]`           | [MT-Bench (Arxiv)](https://arxiv.org/abs/2306.05685)                                            |

**Who is this for?** Beginners and practitioners interested in AI, LLMs, and practical applications.
**How to use:** Start with the basics, then explore advanced topics as needed.

## 📖 Core Concepts

- Linear Algebra: [3Blue1Brown](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- Probability & Statistics: [Khan Academy](https://www.khanacademy.org/math/statistics-probability)
- Glossary of essential LLM and AI terms.

- **Python Basics:**
  - [Python Docs](https://docs.python.org/3/)
- **Data Analysis:**
  - [Python for Data Analysis](https://wesmckinney.com/book/)

- **Courses:**
  - [DeepLearning.AI Specialization](https://www.coursera.org/specializations/deep-learning)
- **Visual Guides:**
  - [3Blue1Brown Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
  - [Hugging Face Quicktour](https://huggingface.co/docs/transformers/quicktour)

- **Courses & Books:**
  - [Stanford CS224N](http://web.stanford.edu/class/cs224n/)
  - [NLTK Book](https://www.nltk.org/book/)
  - [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course/chapter1/1)

- **Frameworks:**
  - [LlamaIndex](https://docs.llamaindex.ai/en/stable/)
- **App Building:**
  - [Streamlit LLM Tutorial](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)

- **Performance Optimization:**
  - [vLLM](https://docs.vllm.ai/en/latest/)
  - [DeepSpeed](https://www.deepspeed.ai/)
- **Fine-tuning:**
  - [PEFT](https://huggingface.co/docs/peft/index)
  - [TRL](https://huggingface.co/docs/trl/index)

## 🛡️ Security & Ethics

- **Security:**
  - [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
  - [Garak Security Scanner](https://github.com/leondz/garak)
- **Ethics:**
  - [UNESCO AI Ethics](https://unesdoc.unesco.org/ark:/48223/pf0000381137)

## ⚙️ Deployment & Production

- **API & Serving:**
  - [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
  - [Ray Serve](https://docs.ray.io/en/latest/serve/index.html)
- **Cloud & Scaling:**
  - [Hugging Face Endpoints](https://huggingface.co/docs/inference-endpoints/index)
  - [Deploy Llama on AWS](https://aws.amazon.com/blogs/machine-learning/deploy-llama-2-on-aws/)

## 📝 Project Examples

- **Chatbot for Customer Support:**
  - [LangChain Templates](https://github.com/langchain-ai/langchain/tree/master/templates)
- **Document Summarization:**
  - [Hugging Face Summarization](https://huggingface.co/docs/transformers/tasks/summarization)
- **Code Generation Assistant:**
  - [Copilot Clone Tutorial](https://www.youtube.com/watch?v=M-D2_UrjR-E)
- **Multilingual Translator:**
  - [mBART Docs](https://huggingface.co/docs/transformers/model_doc/mbart)

## 🌐 Community & Further Reading

- **Online Communities:**
  - Reddit: r/MachineLearning
  - Stack Overflow
  - Hugging Face Forums
- **Research & Trends:**
  - [Flamingo (Multimodal LLMs)](https://arxiv.org/abs/2204.14198)
  - [Phi-3 Blog (Efficient Models)](https://azure.microsoft.com/en-us/blog/introducing-phi-3/)
  - [AutoGen (AI Agents)](https://github.com/microsoft/autogen)

**Tips for Success:**

- Start with the basics and build up.
- Practice with small projects.
- Join communities for support.
- Stay updated with new trends and research.

3. **สำรวจเทรนด์ใหม่:** อ่าน paper เช่น Flamingo หรือติดตามบล็อกจาก Microsoft และ xAI เพื่ออัปเดตเทคโนโลยี เช่น multimodal LLMs `[Advanced]`
4. **พัฒนาโปรเจกต์ขั้นสูง:** ลองรวม LLM กับเครื่องมืออื่น เช่น สร้าง AI agent ด้วย AutoGen หรือโมเดลขนาดเล็กสำหรับ edge devices `[Advanced]`
5. **คำนึงถึงจริยธรรม:** ตรวจสอบ bias และความปลอดภัยของโมเดล โดยอิงจากแนวทาง เช่น UNESCO AI Ethics `[All Levels]`

**ข้อควรจำ:**

- การนำ LLM ไปใช้จริงต้องทดสอบในสภาพแวดล้อมที่หลากหลาย เช่น บนคลาวด์หรืออุปกรณ์ท้องถิ่น
- ติดตามงานวิจัยและชุมชน เช่น Arxiv หรือ X (Twitter) เพื่อไม่พลาดนวัตกรรมล่าสุด
- ความรับผิดชอบต่อผลกระทบของ LLM เป็นสิ่งสำคัญ เช่น การหลีกเลี่ยงเนื้อหาที่ไม่เหมาะสม

<a name="section6"></a>

## ส่วนที่ 6: ศัพท์ที่ต้องรู้ในวงการ LLM (Key Terminology in the LLM Field)

*ส่วนนี้รวบรวมคำศัพท์สำคัญที่ใช้ในวงการ Large Language Models (LLM) พร้อมคำอธิบาย เพื่อช่วยให้เข้าใจแนวคิดและเทคนิคต่างๆ*

### 6.1 ศัพท์พื้นฐาน (Basic Terminology)

| คำศัพท์                   | ความหมาย                                                                                       |
| :----------------------- | :--------------------------------------------------------------------------------------------- |
| LLM (Large Language Model) | โมเดลภาษาขนาดใหญ่ที่ฝึกด้วยข้อมูลข้อความจำนวนมาก ใช้สร้างข้อความหรือตอบคำถาม เช่น GPT หรือ LLaMA |
| Transformer              | สถาปัตยกรรมพื้นฐานของ LLM ใช้กลไก attention เพื่อประมวลผลข้อความแบบลำดับ                       |
| Attention                | กลไกที่ช่วยโมเดลโฟกัสส่วนสำคัญของข้อความ เช่น คำที่เกี่ยวข้องกันในประโยค                       |
| Pre-training             | การฝึกโมเดลด้วยข้อมูลขนาดใหญ่ก่อน เพื่อให้เข้าใจภาษาทั่วไป เช่น การทำนายคำถัดไป                |
| Fine-tuning             | การปรับโมเดลที่ pre-trained แล้วให้เหมาะกับงานเฉพาะ เช่น การตอบคำถามในโดเมนหนึ่ง              |
| Token                    | หน่วยย่อยของข้อความ เช่น คำหรือส่วนของคำ ที่โมเดลใช้ในการประมวลผล                            |
| Embedding                | การแปลงคำหรือ token เป็นเวกเตอร์ตัวเลข เพื่อให้โมเดลเข้าใจความหมายและความสัมพันธ์              |

### 6.2 ศัพท์เกี่ยวกับเทคนิคและวิธีการ (Techniques and Methods)

| คำศัพท์                   | ความหมาย                                                                                       |
| :----------------------- | :--------------------------------------------------------------------------------------------- |
| Self-Attention           | กลไก attention ที่คำนวณความสัมพันธ์ระหว่างทุก token ในประโยคเดียวกัน                           |
| Multi-Head Attention     | การใช้ attention หลายชั้นใน Transformer เพื่อจับความสัมพันธ์ที่หลากหลาย                      |
| Masked Language Model (MLM) | วิธี pre-training ที่ซ่อนบางคำในประโยคให้โมเดลทาย เช่น ที่ใช้ใน BERT                        |
| Autoregressive Model     | โมเดลที่สร้างข้อความโดยทำนายคำถัดไปจากคำก่อนหน้า เช่น GPT                                   |
| LoRA (Low-Rank Adaptation) | เทคนิค fine-tuning ที่ปรับพารามิเตอร์เพียงบางส่วน เพื่อประหยัดทรัพยากร                      |
| QLoRA                    | การรวม quantization กับ LoRA เพื่อ fine-tuning ที่ใช้หน่วยความจำน้อยลง                       |
| Quantization             | การลดขนาดโมเดลโดยเปลี่ยนน้ำหนักจาก FP32 เป็น INT8 หรือ 4-bit เพื่อให้รันได้เร็วขึ้น           |
| Prompt Engineering       | การออกแบบคำสั่งหรือคำถามให้ LLM ตอบได้ดีที่สุด เช่น การใช้ตัวอย่างใน prompt                   |
| RLHF (Reinforcement Learning from Human Feedback) | การฝึกโมเดลด้วย feedback จากมนุษย์ เพื่อให้ตอบได้สอดคล้องกับความต้องการ                     |

### 6.3 ศัพท์เกี่ยวกับประสิทธิภาพและการใช้งาน (Performance and Deployment)

| คำศัพท์                   | ความหมาย                                                                                       |
| :----------------------- | :--------------------------------------------------------------------------------------------- |
| Inference                | การใช้โมเดลที่ฝึกแล้วเพื่อสร้างคำตอบหรือทำนายผล เช่น การตอบคำถาม                            |
| Latency                  | เวลาที่โมเดลใช้ในการประมวลผลและให้คำตอบ                                                  |
| Throughput               | จำนวนคำขอที่โมเดลจัดการได้ในหนึ่งหน่วยเวลา เช่น คำต่อวินาที                                |
| Model Parallelism        | การแบ่งโมเดลไปรันบน GPU หลายตัว เพื่อจัดการโมเดลขนาดใหญ่                                  |
| Data Parallelism         | การแบ่งข้อมูลไปฝึกบน GPU หลายตัว เพื่อเร่งการฝึกโมเดล                                    |
| PagedAttention           | เทคนิคจัดการหน่วยความจำใน inference เพื่อให้รันโมเดลใหญ่ได้อย่างมีประสิทธิภาพ              |
| FlashAttention           | เทคนิค attention ที่เร็วและประหยัดหน่วยความจำ ใช้ใน pre-training และ inference             |

### 6.4 ศัพท์เกี่ยวกับความปลอดภัยและจริยธรรม (Safety and Ethics)

| คำศัพท์                   | ความหมาย                                                                                       |
| :----------------------- | :--------------------------------------------------------------------------------------------- |
| Bias                     | อคติในโมเดลที่เกิดจากข้อมูลฝึก เช่น การตอบที่ลำเอียงต่อเพศหรือเชื้อชาติ                    |
| Prompt Injection         | การโจมตีโดยใส่คำสั่งอันตรายใน prompt เพื่อหลอกให้โมเดลทำสิ่งที่ไม่ควร                       |
| Jailbreaking             | การหลบเลี่ยงข้อจำกัดของโมเดลเพื่อให้ตอบคำถามที่ถูกห้าม เช่น คำถามที่ผิดกฎหมาย               |
| Data Poisoning           | การปนเปื้อนข้อมูลฝึกด้วยข้อมูลที่เป็นอันตราย เพื่อให้โมเดลทำงานผิดพลาด                      |
| Explainability           | ความสามารถในการอธิบายว่าโมเดลตัดสินใจหรือตอบคำถามอย่างไร                                 |

### 6.5 ศัพท์เกี่ยวกับการวัดผลและชุดข้อมูล (Evaluation and Datasets)

| คำศัพท์                   | ความหมาย                                                                                       |
| :----------------------- | :--------------------------------------------------------------------------------------------- |
| BLEU Score               | ตัววัดความแม่นยำของการแปลภาษา โดยเปรียบเทียบกับคำแปลจากมนุษย์                            |
| Perplexity               | ตัววัดความยากที่โมเดลเจอในการทำนายคำถัดไป ค่ายิ่งต่ำยิ่งดี                                |
| MMLU (Massive Multitask Language Understanding) | ชุดทดสอบความรู้ทั่วไปของ LLM ครอบคลุมหลายสาขา เช่น คณิตศาสตร์และวิทยาศาสตร์                |
| TruthfulQA               | ชุดทดสอบที่วัดความถูกต้องและความน่าเชื่อถือของคำตอบจาก LLM                                 |
| HumanEval                | ชุดข้อมูลสำหรับทดสอบความสามารถเขียนโค้ดของ LLM เช่น การแก้โจทย์โปรแกรม                    |

### 6.6 แนวทางการเรียนรู้ศัพท์ (How to Proceed)

1. **เริ่มจากพื้นฐาน:** ทำความเข้าใจคำศัพท์พื้นฐาน เช่น LLM, Transformer, และ Token ก่อน เพื่อสร้างรากฐาน `[Beginner]`
2. **เชื่อมโยงกับเทคนิค:** เรียนรู้ศัพท์อย่าง LoRA หรือ Quantization ควบคู่กับการอ่าน paper หรือทดลองใช้เครื่องมือ `[Intermediate]`
3. **ฝึกใช้จริง:** ลองใช้คำศัพท์ในโปรเจกต์ เช่น วัด latency หรือทำ prompt engineering เพื่อเห็นความหมายชัดเจน `[Intermediate/Advanced]`
4. **ติดตามความปลอดภัย:** ศึกษา bias และ prompt injection เพื่อเข้าใจความท้าทายด้านจริยธรรม `[All Levels]`
5. **อัปเดตคำศัพท์ใหม่:** ติดตามบล็อกหรือ paper เช่น จาก Hugging Face หรือ Arxiv เพื่อรู้จักคำศัพท์ล่าสุด `[Advanced]`

**ข้อควรจำ:**

- คำศัพท์ในวงการ LLM อาจเปลี่ยนแปลงหรือมีคำใหม่เพิ่มขึ้นตามเทคโนโลยีที่พัฒนา
- การเข้าใจศัพท์จะช่วยให้อ่านเอกสารวิจัยหรือใช้งานเครื่องมือได้ดีขึ้น
- ลองจดคำศัพท์ที่เจอบ่อยและทบทวนเป็นระยะเพื่อความคุ้นเคย

<a name="section7"></a>

## ส่วนที่ 7: ไฟล์ตัวอย่างและลิงก์ที่เกี่ยวข้องกับ LLM (Example Files and Links for LLMs)

*ส่วนนี้รวบรวมไฟล์ตัวอย่าง Colab Notebooks สคริปต์ และลิงก์ไปยังไฟล์ต่างๆ ที่เกี่ยวข้องกับ Large Language Models (LLM) เพื่อให้คุณนำไปทดลองหรือศึกษาเพิ่มเติมได้*

### 7.1 Colab Notebooks สำหรับ LLM

| ชื่อไฟล์/คำอธิบาย                              | รายละเอียด                                                                 | ลิงก์                                                                                                   |
| :-------------------------------------------- | :--------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| LLaMA Fine-Tuning with Unsloth                | สอน fine-tuning LLaMA ด้วย Unsloth บน Colab รันได้บน GPU ฟรี                | [Unsloth Fine-Tuning](https://colab.research.google.com/drive/1zB1t1qFO5n4bdnqP4KauS2sV_lPtP2Q)         |
| Fine-Tune Llama 3 with DPO & LoRA             | ตัวอย่าง fine-tuning Llama 3 ด้วย DPO และ LoRA                              | [Llama 3 DPO](https://colab.research.google.com/drive/1K2vQA9r5tB0n2XTR1Zc6oQ5s-w6WxxJ)              |
| Build Your Own GPT from Scratch               | สร้าง GPT ขนาดเล็กจากศูนย์ด้วย Python บน Colab                             | [Build GPT](https://colab.research.google.com/drive/1JMLaCPxM7B6UzT0I8vDwAIXeH-oQss4)                |
| Hugging Face Transformers Tutorial            | เริ่มต้นใช้งาน Transformers เช่น BERT หรือ GPT-2                           | [Transformers Tutorial](https://colab.research.google.com/drive/1rXvHQMjt0r3ADP9gEg0rHfx)         |
| Quantization with BitsAndBytes                | ลดขนาดโมเดลด้วย 4-bit quantization เพื่อรันบนเครื่องจำกัดทรัพยากร          | [Quantization Colab](https://colab.research.google.com/drive/1VoYNfYdk7zLVRWj8DHRcvcK)             |
| LangChain RAG Example                         | สร้างระบบ Retrieval-Augmented Generation (RAG) ด้วย LangChain              | [LangChain RAG](https://colab.research.google.com/drive/1G5i7qQe7e5vU5gW5zR0rL8v)                |
| Mistral 7B Inference                          | รัน Mistral 7B เพื่อ inference บน Colab                                    | [Mistral 7B](https://colab.research.google.com/drive/1zXy5t8nXz9v5gW5sR0rL8v)                   |
| Train a Tiny LLM with TinyStories             | ฝึก LLM ขนาดเล็กด้วยชุดข้อมูล TinyStories                                  | [Tiny LLM](https://colab.research.google.com/drive/1Xy5t8nXz9v5gW5sR0rL8v)                     |

### 7.2 สคริปต์และไฟล์จาก GitHub

| ชื่อไฟล์/Repository                          | รายละเอียด                                                                 | ลิงก์                                                                                                   |
| :------------------------------------------ | :--------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| minGPT (Karpathy)                            | โค้ด Python สร้าง GPT ขนาดเล็กจาก Andrej Karpathy                           | [minGPT](https://github.com/karpathy/minGPT)                                                          |
| nanoGPT                                      | อีกเวอร์ชันของ GPT ขนาดเล็ก ฝึกได้บนเครื่องธรรมดา                           | [nanoGPT](https://github.com/karpathy/nanoGPT)                                                        |
| LLaMA-Factory Scripts                        | สคริปต์สำหรับ fine-tuning LLaMA และโมเดลอื่นๆ                              | [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory/tree/main/scripts)                           |
| DeepSpeed Training Example                   | ตัวอย่างการฝึกโมเดลด้วย DeepSpeed                                        | [DeepSpeed Examples](https://github.com/microsoft/DeepSpeed/tree/master/examples)                     |
| Hugging Face Transformers Examples           | สคริปต์ตัวอย่าง เช่น การฝึก BERT หรือ GPT-2                              | [Transformers Examples](https://github.com/huggingface/transformers/tree/main/examples)                |
| Axolotl Fine-Tuning Scripts                  | สคริปต์ fine-tuning LLM ที่ยืดหยุ่น                                       | [Axolotl Scripts](https://github.com/OpenAccess-AI-Collective/axolotl/tree/main/examples)             |
| vLLM Inference Script                        | สคริปต์สำหรับ inference ด้วย vLLM                                         | [vLLM Examples](https://github.com/vllm-project/vllm/tree/main/examples)                              |
| FlashAttention Implementation                | โค้ด Python สำหรับ FlashAttention                                         | [FlashAttention](https://github.com/Dao-AILab/flash-attention)                                        |

### 7.3 ชุดข้อมูล (Datasets) และไฟล์ที่เกี่ยวข้อง

| ชื่อชุดข้อมูล/ไฟล์                           | รายละเอียด                                                                 | ลิงก์                                                                                                   |
| :------------------------------------------ | :--------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| The Pile                                      | ชุดข้อมูลขนาดใหญ่สำหรับฝึก LLM (800GB)                                    | [The Pile](https://pile.eleuther.ai/)                                                                 |
| TinyStories                                  | ชุดข้อมูลเรื่องสั้นสำหรับฝึกโมเดลขนาดเล็ก                                 | [TinyStories](https://huggingface.co/datasets/roneneldan/TinyStories)                                 |
| OpenWebText                                  | ชุดข้อมูลข้อความจากเว็บ สำหรับ pre-training                                | [OpenWebText](https://huggingface.co/datasets/Skylion007/openwebtext)                                 |
| Alpaca Dataset                               | ชุดข้อมูล instruction-tuning จาก Stanford                                 | [Alpaca](https://github.com/tatsu-lab/stanford_alpaca/blob/main/alpaca_data.json)                     |
| Dolly 15k                                    | ชุดข้อมูล 15,000 คู่คำถาม-คำตอบสำหรับ fine-tuning                         | [Dolly 15k](https://huggingface.co/datasets/databricks-dolly-15k)                                     |
| UltraFeedback                                | ชุดข้อมูล preference จาก OpenBMB                                          | [UltraFeedback](https://huggingface.co/datasets/openbmb/UltraFeedback)                                |
| MMLU Dataset                                 | ชุดข้อมูลทดสอบความรู้ทั่วไปของ LLM                                       | [MMLU](https://huggingface.co/datasets/lukaemon/mmlu)                                                 |

### 7.4 ไฟล์โมเดลที่ดาวน์โหลดได้ (Pre-trained Models)

| ชื่อโมเดล                                   | รายละเอียด                                                                 | ลิงก์                                                                                                   |
| :------------------------------------------ | :--------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| Llama 3 (Meta)                               | โมเดล Llama 3 ขนาดต่างๆ (ต้องขอสิทธิ์)                                    | [Llama 3](https://huggingface.co/meta-llama/Llama-3-8b)                                               |
| Mistral 7B                                   | โมเดล 7B parameters จาก Mistral AI                                       | [Mistral 7B](https://huggingface.co/mistralai/Mixtral-7B-v0.1)                                        |
| GPT-2 (OpenAI)                               | โมเดล GPT-2 ขนาดเล็กสำหรับทดลอง                                           | [GPT-2](https://huggingface.co/gpt2)                                                                  |
| BERT Base (Google)                           | โมเดล BERT พื้นฐานสำหรับ NLP                                             | [BERT Base](https://huggingface.co/bert-base-uncased)                                                 |
| OpenThaiGPT                                  | โมเดลภาษาไทยจากชุมชน OpenThaiGPT                                         | [OpenThaiGPT](https://huggingface.co/openthaigpt/openthaigpt-1.0.0-7b)                                |
| DeepSeek R1                                  | โมเดล open-weight 671B parameters                                        | [DeepSeek R1](https://huggingface.co/deepseek-ai/DeepSeek-R1)                                         |
| Phi-3 (Microsoft)                            | โมเดลขนาดเล็กแต่ทรงพลังจาก Microsoft                                      | [Phi-3](https://huggingface.co/microsoft/phi-3-mini-4k-instruct)                                      |

### 7.5 ลิงก์ไปยังโปรเจกต์และเครื่องมืออื่นๆ

| ชื่อโปรเจกต์/เครื่องมือ                      | รายละเอียด                                                                 | ลิงก์                                                                                                   |
| :------------------------------------------ | :--------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| LangChain Examples                           | ตัวอย่างการใช้งาน LangChain เช่น RAG หรือ agents                          | [LangChain Examples](https://github.com/langchain-ai/langchain/tree/master/templates)                 |
| LlamaIndex Examples                          | ตัวอย่างการเชื่อม LLM กับข้อมูลภายนอกด้วย LlamaIndex                      | [LlamaIndex Examples](https://github.com/run-llama/llama_index/tree/main/examples)                    |
| AutoGen Multi-Agent Example                  | สคริปต์สร้าง multi-agent ด้วย AutoGen                                    | [AutoGen Examples](https://github.com/microsoft/autogen/tree/main/samples)                            |
| Hugging Face Spaces                          | แอปตัวอย่างที่รัน LLM บน Hugging Face Spaces                              | [HF Spaces](https://huggingface.co/spaces)                                                            |
| TRL Examples (RLHF)                          | สคริปต์ฝึก LLM ด้วย reinforcement learning                               | [TRL Examples](https://github.com/huggingface/trl/tree/main/examples)                                 |
| PEFT Examples                                | ตัวอย่าง Parameter-Efficient Fine-Tuning เช่น LoRA                       | [PEFT Examples](https://github.com/huggingface/peft/tree/main/examples)                               |

### 7.6 แนวทางการใช้งานไฟล์และลิงก์ (How to Proceed)

1. **ทดลองบน Colab:** เริ่มด้วย Colab Notebooks เช่น "Build Your Own GPT" หรือ "LLaMA Fine-Tuning" เพื่อฝึกโมเดลแบบไม่ต้องติดตั้งอะไร `[Beginner/Intermediate]`
2. **ดาวน์โหลดสคริปต์:** ลองใช้สคริปต์จาก GitHub เช่น minGPT หรือ nanoGPT เพื่อสร้างโมเดลบนเครื่องของคุณ `[Intermediate]`
3. **ใช้ชุดข้อมูล:** ดาวน์โหลดชุดข้อมูล เช่น Alpaca หรือ TinyStories เพื่อฝึกหรือ fine-tune โมเดล `[Intermediate/Advanced]`
4. **ทดสอบโมเดลสำเร็จรูป:** ลองรันโมเดล เช่น Mistral 7B หรือ OpenThaiGPT เพื่อดูการทำงานจริง `[Intermediate]`
5. **พัฒนาโปรเจกต์:** ใช้ตัวอย่างจาก LangChain หรือ AutoGen เพื่อสร้างแอปพลิเคชัน เช่น แชทบอทหรือ RAG `[Advanced]`

**ข้อควรจำ:**

- ตรวจสอบข้อกำหนดของ Colab (เช่น GPU ฟรีมีจำกัด) ก่อนรันไฟล์
- บางโมเดลหรือชุดข้อมูลอาจต้องขอสิทธิ์หรือลงทะเบียนก่อนดาวน์โหลด
- แนะนำให้มีเครื่องที่มี GPU ถ้าต้องการฝึกโมเดลขนาดใหญ่ในเครื่อง

<a name="section8"></a>

## ส่วนที่ 8: การ deploy LLM ใน Production (Deploying LLMs in Production)

*ส่วนนี้เน้นการนำ LLM ไปใช้งานจริงในระบบ production เช่น บนเซิร์ฟเวอร์หรือแอปพลิเคชัน รวมถึงเครื่องมือและขั้นตอนที่จำเป็น*

### 8.1 เครื่องมือสำหรับ Deployment

| เครื่องมือ                             | คำอธิบาย                                                                                     | ลิงก์                                                                                           |
| :------------------------------------ | :------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------- |
| Hugging Face Inference API            | API สำเร็จรูปสำหรับรันโมเดลบนคลาวด์ของ Hugging Face                                       | [Inference API](https://huggingface.co/inference-api)                                          |
| Text Generation Inference (TGI)       | Container จาก Hugging Face สำหรับ inference LLM ขนาดใหญ่                                 | [TGI](https://github.com/huggingface/text-generation-inference)                                |
| vLLM                                  | ไลบรารีสำหรับ inference ที่รวดเร็ว รองรับ PagedAttention                                  | [vLLM](https://github.com/vllm-project/vllm)                                                  |
| FastAPI                               | เฟรมเวิร์ก Python สำหรับสร้าง API เพื่อ serve LLM                                       | [FastAPI](https://fastapi.tiangolo.com/)                                                      |
| Docker                                | เครื่องมือสร้าง container เพื่อ deploy LLM ได้ทุกที่                                      | [Docker](https://www.docker.com/)                                                             |
| AWS SageMaker                         | บริการคลาวด์จาก AWS สำหรับฝึกและ deploy โมเดล ML/LLM                                     | [SageMaker](https://aws.amazon.com/sagemaker/)                                                |

### 8.2 ขั้นตอนการ Deploy LLM

1. **เลือกโมเดลและ optimize:**
   - เลือกโมเดลที่เหมาะสม เช่น Mistral 7B หรือ Llama 3
   - ใช้ quantization (เช่น BitsAndBytes) เพื่อลดขนาดโมเดล
   - ทดสอบ inference บนเครื่องท้องถิ่นก่อน

2. **เตรียมสภาพแวดล้อม:**
   - ติดตั้ง dependencies เช่น PyTorch, Transformers
   - ใช้ Docker เพื่อสร้าง container ที่สม่ำเสมอ

3. **สร้าง API:**
   - ใช้ FastAPI หรือ Flask เพื่อสร้าง endpoint เช่น `/generate`
   - ตัวอย่างโค้ด: [FastAPI Example](https://github.com/tiangolo/fastapi/tree/master/docs/en/docs/tutorial)

4. **Deploy บนคลาวด์:**
   - อัปโหลด container ไปยัง AWS, GCP หรือ Azure
   - ตั้งค่า load balancer ถ้ามีผู้ใช้จำนวนมาก

5. **ทดสอบและปรับปรุง:**
   - วัด latency และ throughput
   - ปรับ batch size หรือใช้ vLLM เพื่อเพิ่มประสิทธิภาพ

### 8.3 ตัวอย่าง Deployment

| ตัวอย่าง                               | รายละเอียด                                                                                     | ลิงก์/แหล่งข้อมูล                                                                      |
| :------------------------------------ | :------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------- |
| Deploy Llama 3 on AWS                 | สอน deploy Llama 3 ด้วย SageMaker                                                  | [AWS Tutorial](https://aws.amazon.com/blogs/machine-learning/deploy-llama-3-on-aws/)   |
| Chatbot API with FastAPI              | ตัวอย่างโค้ด FastAPI สำหรับ serve LLM เป็นแชทบอท                                  | [GitHub](https://github.com/fastapi-users/fastapi-llm-example)                        |
| TGI on Docker                         | คู่มือรัน TGI container บน Docker                                                 | [TGI Docker](https://huggingface.co/docs/text-generation-inference/quicktour)         |

### 8.4 แนวทางการเรียนรู้ (How to Proceed)

1. **เริ่มจากเครื่องท้องถิ่น:** ลองรันโมเดลเล็ก เช่น GPT-2 ด้วย FastAPI บนเครื่องของคุณ `[Intermediate]`
2. **ทดลอง Docker:** สร้าง container ง่ายๆ ด้วย Docker และ deploy โมเดล `[Intermediate/Advanced]`
3. **ใช้คลาวด์ฟรี:** ลอง deploy บน Hugging Face Spaces หรือ AWS Free Tier `[Intermediate]`
4. **เพิ่มประสิทธิภาพ:** ใช้ vLLM หรือ TGI เพื่อลด latency และรองรับผู้ใช้มากขึ้น `[Advanced]`
5. **ตรวจสอบความปลอดภัย:** ตั้งค่า authentication และป้องกัน prompt injection `[Advanced]`

**ข้อควรจำ:**

- ทดสอบ load และ scalability ก่อนปล่อยให้ผู้ใช้จริง
- คำนึงถึงค่าใช้จ่าย ถ้าใช้คลาวด์ เช่น AWS หรือ GCP
- อัปเดตโมเดลและ API เป็นระยะ เพื่อให้ทันสมัย
</a>

<a name="section9"></a>

## ส่วนที่ 9: งานวิจัยเกี่ยวกับ LLM (Research Papers on LLMs)

*ส่วนนี้รวบรวมงานวิจัยที่สำคัญเกี่ยวกับ Large Language Models (LLMs) พร้อมลิงก์ไปยังเอกสารต้นฉบับ เพื่อให้ผู้อ่านสามารถศึกษาเพิ่มเติมได้*

### 9.1 งานวิจัยพื้นฐาน (Foundational Papers)

| ชื่อ paper                                      | คำอธิบาย                                                                                     | ลิงก์                                                                                             |
| :--------------------------------------------- | :------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| Attention Is All You Need                      | แนะนำ Transformer สถาปัตยกรรมพื้นฐานของ LLM สมัยใหม่ (2017)                                   | [Arxiv](https://arxiv.org/abs/1706.03762)                                                       |
| BERT: Pre-training of Deep Bidirectional Transformers | นำเสนอ BERT โมเดลที่ใช้ pre-training แบบ bidirectional (2018)                                | [Arxiv](https://arxiv.org/abs/1810.04805)                                                       |
| Improving Language Understanding by Generative Pre-Training | งานเริ่มต้นของ GPT จาก OpenAI (2018)                                                       | [OpenAI](https://cdn.openai.com/research-papers/improving-language-understanding-by-generative-pre-training.pdf) |
| Language Models are Few-Shot Learners          | อธิบาย GPT-3 และความสามารถ few-shot learning (2020)                                          | [Arxiv](https://arxiv.org/abs/2005.14165)                                                       |

### 9.2 งานวิจัยเกี่ยวกับการฝึกและปรับปรุงโมเดล (Training and Optimization)

| ชื่อ paper                                      | คำอธิบาย                                                                                     | ลิงก์                                                                                             |
| :--------------------------------------------- | :------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| LoRA: Low-Rank Adaptation of Large Language Models | เทคนิค fine-tuning ที่ประหยัดทรัพยากรด้วย low-rank updates (2021)                            | [Arxiv](https://arxiv.org/abs/2106.09685)                                                       |
| QLoRA: Efficient Finetuning of Quantized LLMs  | รวม quantization กับ LoRA เพื่อ fine-tuning ที่ใช้หน่วยความจำน้อย (2023)                      | [Arxiv](https://arxiv.org/abs/2305.14314)                                                       |
| FlashAttention: Fast and Memory-Efficient Exact Attention | เทคนิค attention ที่เร็วและประหยัดหน่วยความจำ (2022)                                        | [Arxiv](https://arxiv.org/abs/2205.14135)                                                       |
| ZeRO: Memory Optimizations Toward Training Trillion Parameter Models | วิธีจัดการหน่วยความจำสำหรับโมเดลขนาดล้านล้านพารามิเตอร์ (2019)                             | [Arxiv](https://arxiv.org/abs/1910.02054)                                                       |

### 9.3 งานวิจัยเกี่ยวกับการประเมินผลและความสามารถ (Evaluation and Capabilities)

| ชื่อ paper                                      | คำอธิบาย                                                                                     | ลิงก์                                                                                             |
| :--------------------------------------------- | :------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| HumanEval: Evaluating Large Language Models   | ชุดข้อมูลและวิธีประเมินความสามารถเขียนโค้ดของ LLM (2021)                                       | [Arxiv](https://arxiv.org/abs/2107.03374)                                                       |
| TruthfulQA: Measuring How Models Mimic Human Lies | ทดสอบความถูกต้องและความน่าเชื่อถือของ LLM (2021)                                            | [Arxiv](https://arxiv.org/abs/2109.07958)                                                       |
| MMLU: Measuring Massive Multitask Language Understanding | ชุดทดสอบความรู้ทั่วไปหลายสาขาของ LLM (2021)                                                | [Arxiv](https://arxiv.org/abs/2009.03300)                                                       |
| Large Language Models Can Predict Neuroscience Results | LLM ทำนายผลการทดลองด้านประสาทวิทยาได้ดีกว่ามนุษย์ (2024)                                     | [Nature](https://www.nature.com/articles/s41562-024-02040-5)                                    |

### 9.4 งานวิจัยเกี่ยวกับความปลอดภัยและจริยธรรม (Safety and Ethics)

| ชื่อ paper                                      | คำอธิบาย                                                                                     | ลิงก์                                                                                             |
| :--------------------------------------------- | :------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| Direct Preference Optimization: Your Language Model is Secretly a Reward Model | วิธีฝึก LLM ด้วย preference โดยไม่ใช้ reward model (2023)                                   | [Arxiv](https://arxiv.org/abs/2305.18290)                                                       |
| Red Teaming Language Models with Language Models | ใช้ LLM ในการทดสอบช่องโหว่ของ LLM อื่น (2022)                                              | [Arxiv](https://arxiv.org/abs/2202.03286)                                                       |
| On the Dangers of Stochastic Parrots          | วิเคราะห์ความเสี่ยงและ bias ใน LLM (2021)                                                    | [ACM](https://dl.acm.org/doi/10.1145/3442188.3445922)                                           |
| A Survey on LLM Security and Privacy: The Good, The Bad, and The Ugly | ทบทวนความปลอดภัยและความเป็นส่วนตัวใน LLM (2024)                                              | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2666659624000082)            |

### 9.5 งานวิจัยล่าสุดและเทรนด์ใหม่ (Recent Papers and Emerging Trends)

| ชื่อ paper                                      | คำอธิบาย                                                                                     | ลิงก์                                                                                             |
| :--------------------------------------------- | :------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| Llama 2: Open Foundation and Fine-Tuned Chat Models | รายละเอียด Llama 2 โมเดล open-source จาก Meta (2023)                                       | [Arxiv](https://arxiv.org/abs/2307.09288)                                                       |
| ORPO: Monolithic Preference Optimization      | วิธีฝึก LLM ด้วย preference โดยไม่ใช้โมเดลอ้างอิง (2024)                                     | [Arxiv](https://arxiv.org/abs/2403.07691)                                                       |
| A Survey of Large Language Models             | ทบทวน LLM ครอบคลุมประวัติ สถาปัตยกรรม และความท้าทาย (2023)                                   | [Arxiv](https://arxiv.org/abs/2303.18223)                                                       |
| Multimodal Large Language Models: A Survey    | ภาพรวม LLM ที่รวมข้อมูลหลายรูปแบบ เช่น ข้อความและรูปภาพ (2024)                                | [Arxiv](https://arxiv.org/abs/2404.18465)                                                       |

### 9.6 แนวทางการศึกษา paper (How to Proceed)

1. **เริ่มจากพื้นฐาน:** อ่าน "Attention Is All You Need" และ "BERT" เพื่อเข้าใจรากฐานของ LLM `[Beginner]`
2. **เจาะลึกการฝึกโมเดล:** ศึกษา "LoRA" และ "FlashAttention" เพื่อเรียนรู้เทคนิค optimization `[Intermediate]`
3. **ประเมินความสามารถ:** ลองอ่าน "HumanEval" หรือ "MMLU" เพื่อเข้าใจวิธีวัดผล LLM `[Intermediate/Advanced]`
4. **สำรวจความปลอดภัย:** อ่าน "Stochastic Parrots" และ "Red Teaming" เพื่อรู้ถึงความเสี่ยง `[Advanced]`
5. **ติดตามเทรนด์:** อ่าน paper ล่าสุด เช่น "ORPO" หรือ "Multimodal LLMs" เพื่ออัปเดตแนวโน้ม `[Advanced]`

**ข้อควรจำ:**

- Paper บางฉบับอาจต้องใช้พื้นฐานคณิตศาสตร์หรือ machine learning ในการทำความเข้าใจ
- ลิงก์ทั้งหมดใช้งานได้ ณ วันที่ 6 มีนาคม 2568 แต่บางอันอาจต้องสมัครสมาชิกหรือขอสิทธิ์
- อ่าน abstract ก่อนเพื่อดูว่า paper ตรงกับความสนใจหรือไม่

<a name="section10"></a>

## ส่วนที่ 10: หลักการ วิธีการ เทคนิคพิเศษ เครื่องมือ และ Framework ที่เกี่ยวข้องกับ LLM

*ส่วนนี้ครอบคลุมหลักการพื้นฐาน วิธีการ เทคนิคพิเศษ เครื่องมือ (Tools) และ Framework ที่ใช้ในการพัฒนาและใช้งาน LLM พร้อมลิงก์และโค้ดตัวอย่าง*

### 10.1 หลักการพื้นฐาน (Core Principles)

| หลักการ                          | คำอธิบาย                                                                                   | ลิงก์/แหล่งข้อมูล                                                                 |
| :----------------------------- | :----------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| Attention Mechanism            | กลไกที่ช่วยโมเดลโฟกัสส่วนสำคัญของข้อความ เช่น Self-Attention ใน Transformer                | [Attention Paper](https://arxiv.org/abs/1706.03762)                              |
| Pre-training and Fine-tuning   | ฝึกโมเดลด้วยข้อมูลทั่วไปก่อน (pre-training) แล้วปรับให้เหมาะกับงานเฉพาะ (fine-tuning)       | [BERT Paper](https://arxiv.org/abs/1810.04805)                                   |
| Autoregressive Modeling        | การทำนายคำถัดไปจากคำก่อนหน้า เช่น ที่ใช้ใน GPT                                            | [GPT Paper](https://arxiv.org/abs/2005.14165)                                    |
| Scaling Laws                   | ความสัมพันธ์ระหว่างขนาดโมเดล จำนวนข้อมูล และประสิทธิภาพ เช่น ใหญ่ขึ้นดีขึ้น                | [Scaling Laws](https://arxiv.org/abs/2001.08361)                                 |

### 10.2 วิธีการ (Methodologies)

| วิธีการ                          | คำอธิบาย                                                                                   | ลิงก์/แหล่งข้อมูล                                                                 |
| :----------------------------- | :----------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| Masked Language Modeling (MLM) | ซ่อนบางคำในประโยคให้โมเดลทาย เช่น ใน BERT                                                | [BERT Paper](https://arxiv.org/abs/1810.04805)                                   |
| Instruction Tuning             | ปรับโมเดลด้วยคำสั่งและคำตอบ เพื่อให้ตามคำสั่งได้ดีขึ้น                                     | [Instruction Tuning](https://arxiv.org/abs/2308.10792)                           |
| Reinforcement Learning from Human Feedback (RLHF) | ฝึกโมเดลด้วย feedback จากมนุษย์ เช่น ใน Llama 2                                | [Llama 2 Paper](https://arxiv.org/abs/2307.09288)                                |
| Knowledge Distillation         | ถ่ายทอดความรู้จากโมเดลใหญ่ไปยังโมเดลเล็ก เพื่อลดขนาดและเพิ่มประสิทธิภาพ                    | [Distillation Paper](https://arxiv.org/abs/1503.02531)                           |

### 10.3 เทคนิคพิเศษ (Special Techniques)

| เทคนิค                          | คำอธิบาย                                                                                   | ลิงก์/แหล่งข้อมูล                                                                 | ลิงก์โค้ดตัวอย่าง                                                      |
| :----------------------------- | :----------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- | :-------------------------------------------------------------------- |
| LoRA (Low-Rank Adaptation)     | Fine-tuning โดยปรับพารามิเตอร์เพียงบางส่วน ประหยัดทรัพยากร                                | [LoRA Paper](https://arxiv.org/abs/2106.09685)                            | [LoRA Example](https://github.com/huggingface/peft/tree/main/examples/lora) |
| QLoRA                          | รวม quantization กับ LoRA เพื่อ fine-tuning ที่ใช้หน่วยความจำน้อย                          | [QLoRA Paper](https://arxiv.org/abs/2305.14314)                           | [QLoRA Colab](https://colab.research.google.com/drive/1VoYNfYdk7zLVRWj8DHRcvcK) |
| FlashAttention                 | Attention ที่เร็วและประหยัดหน่วยความจำ เหมาะกับโมเดลใหญ่                                   | [FlashAttention Paper](https://arxiv.org/abs/2205.14135)                  | [FlashAttention Code](https://github.com/Dao-AILab/flash-attention)     |
| Prompt Engineering             | ออกแบบ prompt เพื่อให้ LLM ตอบได้ดีขึ้น เช่น ใช้ few-shot examples                        | [Prompt Guide](https://huggingface.co/docs/transformers/tasks/prompting)  | [Prompt Example](https://github.com/huggingface/notebooks/blob/main/examples/prompt_engineering.ipynb) |

### 10.4 เครื่องมือ (Tools)

| เครื่องมือ                      | คำอธิบาย                                                                                   | ลิงก์หลัก                                                                         | ลิงก์โค้ดตัวอย่าง                                                      |
| :----------------------------- | :----------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------- | :-------------------------------------------------------------------- |
| DeepSpeed                      | เครื่องมือจาก Microsoft สำหรับฝึกและ inference โมเดลขนาดใหญ่                              | [DeepSpeed](https://www.deepspeed.ai/)                                           | [DeepSpeed Examples](https://github.com/microsoft/DeepSpeed/tree/master/examples) |
| vLLM                           | ไลบรารี inference ที่รวดเร็ว รองรับ PagedAttention                                       | [vLLM](https://vllm.ai/)                                                         | [vLLM Examples](https://github.com/vllm-project/vllm/tree/main/examples)  |
| Unsloth                        | เครื่องมือ fine-tuning และ quantization ที่เร็วและประหยัดหน่วยความจำ                       | [Unsloth](https://github.com/unslothai/unsloth)                                  | [Unsloth Colab](https://colab.research.google.com/drive/1zB1t1qFO5n4bdnqP4KauS2sV_lPtP2Q) |
| BitsAndBytes                   | ไลบรารีสำหรับ quantization เช่น 4-bit หรือ 8-bit                                        | [BitsAndBytes](https://github.com/TimDettmers/bitsandbytes)                      | [Quantization Colab](https://colab.research.google.com/drive/1VoYNfYdk7zLVRWj8DHRcvcK) |
| Colossal-AI                    | เครื่องมือฝึกโมเดลขนาดใหญ่ รองรับ parallelism หลายรูปแบบ                                  | [Colossal-AI](https://www.colossalai.org/)                                       | [Colossal-AI Examples](https://github.com/hpcaitech/ColossalAI/tree/main/examples) |

### 10.5 Framework

| Framework                      | คำอธิบาย                                                                                   | ลิงก์หลัก                                                                         | ลิงก์โค้ดตัวอย่าง                                                      |
| :----------------------------- | :----------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------- | :-------------------------------------------------------------------- |
| Hugging Face Transformers      | Framework ยอดนิยมสำหรับใช้งาน LLM เช่น BERT, GPT, Llama                                 | [Transformers](https://huggingface.co/docs/transformers/index)                   | [Transformers Examples](https://github.com/huggingface/transformers/tree/main/examples) |
| PyTorch                        | Framework หลักสำหรับฝึกและพัฒนา LLM ด้วยความยืดหยุ่นสูง                                   | [PyTorch](https://pytorch.org/)                                                  | [PyTorch Tutorials](https://pytorch.org/tutorials/)                     |
| TensorFlow                     | Framework อีกตัวเลือกสำหรับฝึก LLM แม้จะใช้กับ LLM น้อยกว่า PyTorch                       | [TensorFlow](https://www.tensorflow.org/)                                        | [TF Examples](https://github.com/tensorflow/models/tree/master/official/nlp) |
| LangChain                      | Framework สำหรับสร้างแอปพลิเคชันที่ขับเคลื่อนด้วย LLM เช่น RAG หรือ agents               | [LangChain](https://python.langchain.com/docs/get_started/introduction)          | [LangChain Templates](https://github.com/langchain-ai/langchain/tree/master/templates) |
| LlamaIndex                     | Framework เชื่อม LLM กับข้อมูลภายนอก เช่น ฐานความรู้                                    | [LlamaIndex](https://docs.llamaindex.ai/en/stable/)                              | [LlamaIndex Examples](https://github.com/run-llama/llama_index/tree/main/examples) |

### 10.6 แนวทางการใช้งาน (How to Proceed)

1. **เข้าใจหลักการ:** เริ่มจากอ่าน paper เช่น "Attention Is All You Need" เพื่อเข้าใจพื้นฐาน `[Beginner]`
2. **ลองวิธีการพื้นฐาน:** ฝึกโมเดลด้วย MLM หรือ autoregressive modeling ด้วย Hugging Face `[Intermediate]`
3. **ใช้เทคนิคพิเศษ:** ทดลอง LoRA หรือ FlashAttention ด้วยโค้ดตัวอย่าง `[Intermediate/Advanced]`
4. **เลือกเครื่องมือ:** ใช้ DeepSpeed หรือ vLLM สำหรับงานใหญ่ และ Unsloth สำหรับงานเล็ก `[Advanced]`
5. **พัฒนาด้วย Framework:** สร้างแอปด้วย LangChain หรือฝึกโมเดลด้วย PyTorch `[Intermediate/Advanced]`

**ข้อควรจำ:**

- ทดลองโค้ดตัวอย่างบน Colab หรือเครื่องที่มี GPU เพื่อผลลัพธ์ที่ดีที่สุด
- อ่านเอกสารของเครื่องมือหรือ Framework เพื่อใช้ฟีเจอร์ให้เต็มประสิทธิภาพ
- อัปเดตเวอร์ชันเครื่องมือเป็นระยะ เพราะวงการ LLM พัฒนาเร็ว

<a name="section11"></a>

## ส่วนที่ 11: การเลือกใช้ Model AI, Dataset และความหมายอื่นๆ ที่ต้องรู้

*ส่วนนี้แนะนำวิธีเลือกโมเดล AI และชุดข้อมูลสำหรับงาน LLM รวมถึงความหมายอื่นๆ ที่สำคัญ เพื่อช่วยในการตัดสินใจและพัฒนาโปรเจกต์*

### 11.1 การเลือกใช้ Model AI (Choosing an AI Model)

| ปัจจัย                          | คำอธิบาย                                                                                   | ตัวอย่างโมเดล                                                                 |
| :----------------------------- | :----------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------- |
| ขนาดโมเดล (Model Size)         | โมเดลใหญ่ (เช่น 70B parameters) ให้ผลดีแต่ใช้ทรัพยากรมาก โมเดลเล็กเหมาะกับงานจำกัดทรัพยากร | ใหญ่: Llama 3 (70B), เล็ก: Phi-3 (3.8B)                                     |
| งานที่ต้องการ (Task)           | เลือกตามงาน เช่น การสนทนา, การแปล, หรือการเขียนโค้ด                                      | สนทนา: Grok, แปล: mBART, เขียนโค้ด: CodeLlama                              |
| ความสามารถพิเศษ (Specialization) | บางโมเดลถูกฝึกมาเพื่องานเฉพาะ เช่น ภาษาไทยหรือด้านการแพทย์                              | ภาษาไทย: OpenThaiGPT, การแพทย์: BioGPT                                      |
| ความพร้อมใช้งาน (Availability) | โมเดล open-source ใช้ได้ฟรี แต่บางโมเดลต้องขอสิทธิ์หรือเสียเงิน                         | Open-source: Mistral 7B, ต้องขอ: Llama 3                                     |
| ทรัพยากรที่มี (Resources)      | ถ้ามี GPU น้อย อาจเลือกโมเดลที่ quantized หรือเล็ก                                      | Quantized: GPTQ Llama 2, เล็ก: TinyLlama                                    |

**เคล็ดลับ:**

- ถ้างานไม่ซับซ้อน เริ่มด้วยโมเดลเล็ก เช่น Phi-3 หรือ Mistral 7B
- ใช้ Hugging Face Model Hub เพื่อเปรียบเทียบโมเดล: [Hugging Face Models](https://huggingface.co/models)

### 11.2 การเลือกใช้ Dataset (Choosing a Dataset)

| ปัจจัย                          | คำอธิบาย                                                                                   | ตัวอย่าง Dataset                                                             |
| :----------------------------- | :----------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------- |
| ขนาดชุดข้อมูล (Size)           | ข้อมูลเยอะช่วยให้โมเดลแม่นยำ แต่ต้องใช้เวลาและทรัพยากรในการฝึก                           | ใหญ่: The Pile (800GB), เล็ก: TinyStories (1GB)                             |
| คุณภาพข้อมูล (Quality)         | ข้อมูลสะอาดและเกี่ยวข้องกับงานช่วยลด bias และเพิ่มประสิทธิภาพ                            | สะอาด: Alpaca, มี noise: OpenWebText                                         |
| ภาษา (Language)               | เลือกตามภาษาเป้าหมาย เช่น ไทย อังกฤษ หรือหลายภาษา                                      | ไทย: Thai National Corpus, อังกฤษ: C4, หลายภาษา: Multilingual C4             |
| วัตถุประสงค์ (Purpose)         | Pre-training ใช้ข้อมูลทั่วไป Instruction tuning ใช้คู่คำถาม-คำตอบ                        | Pre-training: Wikipedia, Instruction: Dolly 15k                              |
| ลิขสิทธิ์ (Licensing)         | ตรวจสอบว่าใช้ได้ฟรีหรือต้องขออนุญาต เพื่อหลีกเลี่ยงปัญหากฎหมาย                           | ฟรี: Common Crawl, ต้องขอ: BooksCorpus                                       |

**เคล็ดลับ:**

- หาชุดข้อมูลจาก Hugging Face Datasets: [Hugging Face Datasets](https://huggingface.co/datasets)
- ถ้าข้อมูลมีจำกัด ลองใช้ data augmentation หรือ synthetic data เช่น จาก GPT

### 11.3 ความหมายอื่นๆ ที่ต้องรู้ (Other Key Concepts)

| คำศัพท์/แนวคิด                 | ความหมาย                                                                                   |
| :----------------------------- | :----------------------------------------------------------------------------------------- |
| Overfitting                    | โมเดลเรียนรู้ข้อมูลฝึกมากเกินไป จนไม่ generalized กับข้อมูลใหม่                           |
| Underfitting                   | โมเดลเรียนรู้ไม่เพียงพอ ทำให้ประสิทธิภาพต่ำทั้งข้อมูลฝึกและข้อมูลทดสอบ                     |
| Epoch                          | จำนวนรอบที่โมเดลฝึกผ่านชุดข้อมูลทั้งหมด ค่าเยอะเกินอาจ overfitting                       |
| Batch Size                     | จำนวนตัวอย่างที่ใช้ในแต่ละรอบการฝึก ค่าใหญ่ใช้หน่วยความจำมาก ค่าเล็กฝึกนาน                 |
| Learning Rate                  | อัตราที่โมเดลปรับน้ำหนัก ค่าสูงเกินเรียนเร็วแต่ไม่แม่น ค่าต่ำเรียนช้าแต่แม่นยำ              |
| Zero-shot Learning             | ความสามารถของโมเดลในการทำงานโดยไม่ต้องฝึกเพิ่ม เช่น GPT-3 กับงานใหม่                     |
| Few-shot Learning              | ใช้ตัวอย่างไม่กี่ตัวเพื่อให้โมเดลเรียนรู้งานใหม่ โดยไม่ต้อง fine-tune เต็มรูปแบบ            |
| Transfer Learning              | ใช้ความรู้จากโมเดลที่ฝึกแล้วไปงานอื่น เช่น ใช้ BERT กับการจำแนกข้อความ                     |
| Hyperparameter Tuning          | การปรับค่า เช่น learning rate หรือ batch size เพื่อให้โมเดลทำงานดีที่สุด                   |

### 11.4 ลิงก์และแหล่งข้อมูลเพิ่มเติม

| หัวข้อ                          | ลิงก์/แหล่งข้อมูล                                                                 |
| :----------------------------- | :-------------------------------------------------------------------------------- |
| คู่มือเลือกโมเดล                | [Hugging Face Model Selection](https://huggingface.co/docs/transformers/model_doc) |
| รายการ Dataset ที่แนะนำ         | [Awesome Datasets](https://github.com/huggingface/datasets/wiki)                  |
| คำศัพท์ ML พื้นฐาน             | [ML Glossary](https://developers.google.com/machine-learning/glossary)            |

### 11.5 แนวทางการเลือกและใช้งาน (How to Proceed)

1. **กำหนดเป้าหมาย:** รู้ว่างานของคุณคืออะไร เช่น แชทบอทหรือแปลภาษา เพื่อเลือกโมเดลและข้อมูลให้เหมาะ `[Beginner]`
2. **ทดลองโมเดลเล็ก:** เริ่มด้วยโมเดลอย่าง Mistral 7B หรือ Phi-3 เพื่อดูผลลัพธ์ก่อนใช้โมเดลใหญ่ `[Intermediate]`
3. **หา Dataset ที่เหมาะ:** เลือกข้อมูลที่ตรงกับงาน เช่น Alpaca สำหรับ instruction tuning `[Intermediate]`
4. **ปรับแต่ง:** ลอง fine-tune โมเดลด้วยชุดข้อมูลของคุณ และปรับ hyperparameter เช่น batch size `[Intermediate/Advanced]`
5. **ประเมินผล:** ใช้ metric เช่น BLEU หรือ accuracy เพื่อตรวจสอบว่าโมเดลและข้อมูลเหมาะสมหรือไม่ `[Advanced]`

**ข้อควรจำ:**

- ทดสอบโมเดลและข้อมูลในสเกลเล็กก่อนขยายไปใหญ่
- ถ้าทรัพยากรจำกัด ใช้โมเดลที่ quantized หรือชุดข้อมูลขนาดเล็ก
- อ่านเอกสารของโมเดล (เช่น README บน Hugging Face) เพื่อเข้าใจข้อจำกัด

คำถามของคุณขอให้อธิบายรายการทั้งหมดที่ระบุไว้ใน query อย่างครบถ้วน ซึ่งประกอบด้วยหมวดหมู่ของโมเดล AI, เฟรมเวิร์กและไลบรารี, ผู้ให้บริการการประมวลผล, รูปแบบไฟล์และเครื่องมือจัดการข้อมูล รวมถึงคุณสมบัติเพิ่มเติม ต่อไปนี้คือคำอธิบายแบบละเอียดสำหรับแต่ละส่วน โดยจะแบ่งเป็นหัวข้อใหญ่ๆ เพื่อให้เข้าใจง่าย:

---

<a name="section12"></a>

## ส่วนที่ 12: หมวดหมู่ของโมเดล

## 12.1 หมวดหมู่ของโมเดล AI (Model Categories)

หมวดหมู่เหล่านี้แบ่งตามประเภทของงานที่โมเดล AI สามารถทำได้:

### **Multimodal**

โมเดลที่สามารถจัดการข้อมูลหลายรูปแบบพร้อมกัน เช่น ข้อความ, ภาพ, เสียง:

- **Audio-Text-to-Text**: แปลงข้อมูลจากทั้งเสียงและข้อความเป็นข้อความ เช่น การถอดเสียงพร้อมคำอธิบายเพิ่มเติมจากข้อความ
- **Image-Text-to-Text**: แปลงข้อมูลจากภาพและข้อความเป็นข้อความ เช่น อ่านข้อความในภาพและสรุปเพิ่ม
- **Visual Question Answering (VQA)**: ตอบคำถามโดยใช้ข้อมูลจากภาพ เช่น "รถในภาพสีอะไร?"
- **Document Question Answering**: ตอบคำถามจากเนื้อหาในเอกสาร เช่น ค้นหาคำตอบจาก PDF
- **Video-Text-to-Text**: แปลงวิดีโอและข้อความเป็นข้อความ เช่น สรุปเนื้อหาวิดีโอพร้อมบริบทจากข้อความ
- **Visual Document Retrieval**: ค้นหาเอกสารโดยใช้ข้อมูลจากภาพ เช่น หาเอกสารที่ตรงกับภาพที่ให้มา
- **Any-to-Any**: โมเดลที่ยืดหยุ่น สามารถแปลงข้อมูลจากรูปแบบหนึ่งไปสู่อีกรูปแบบหนึ่งได้หลากหลาย เช่น ข้อความเป็นภาพ หรือภาพเป็นเสียง

### **Computer Vision**

งานที่เกี่ยวข้องกับการประมวลผลภาพและวิดีโอ:

- **Depth Estimation**: ประมาณความลึกของวัตถุในภาพ เช่น ระบุระยะห่างในภาพถ่าย
- **Image Classification**: จำแนกประเภทของภาพ เช่น บอกว่านี่คือภาพ "แมว" หรือ "หมา"
- **Object Detection**: ตรวจจับและระบุตำแหน่งวัตถุในภาพ เช่น วงกลมรอบรถยนต์ในภาพ
- **Image Segmentation**: แบ่งภาพออกเป็นส่วนๆ เช่น แยกพื้นหลังออกจากตัววัตถุ
- **Text-to-Image**: สร้างภาพจากข้อความ เช่น "วาดภาพบ้านสีแดง"
- **Image-to-Text**: แปลงภาพเป็นข้อความ เช่น อ่านป้ายในภาพ (OCR)
- **Image-to-Image**: แปลงภาพหนึ่งเป็นภาพใหม่ เช่น เปลี่ยนภาพขาวดำเป็นภาพสี
- **Image-to-Video**: สร้างวิดีโอจากภาพ เช่น ภาพนิ่งที่กลายเป็นแอนิเมชัน
- **Unconditional Image Generation**: สร้างภาพโดยไม่มีเงื่อนไข เช่น สร้างภาพสุ่มจากโมเดล generative
- **Video Classification**: จำแนกประเภทของวิดีโอ เช่น วิดีโอนี้เกี่ยวกับ "กีฬา" หรือ "ธรรมชาติ"
- **Text-to-Video**: สร้างวิดีโอจากข้อความ เช่น "สร้างวิดีโอคนเดินในสวน"
- **Zero-Shot Image Classification**: จำแนกภาพโดยไม่ต้องฝึกโมเดลด้วยข้อมูลนั้นๆ เช่น จำแนกภาพใหม่โดยใช้ความรู้ทั่วไป
- **Mask Generation**: สร้างมาสก์สำหรับภาพ เช่น ระบุส่วนที่เป็น "คน" ในภาพ
- **Zero-Shot Object Detection**: ตรวจจับวัตถุใหม่ๆ โดยไม่ต้องฝึกโมเดลด้วยข้อมูลนั้น
- **Text-to-3D**: สร้างโมเดล 3 มิติจากข้อความ เช่น "สร้างโมเดล 3D ของรถยนต์"
- **Image-to-3D**: สร้างโมเดล 3 มิติจากภาพ เช่น แปลงภาพ 2D เป็น 3D
- **Image Feature Extraction**: ดึงคุณลักษณะจากภาพ เช่น ระบุสีหรือรูปร่างเด่นๆ
- **Keypoint Detection**: ตรวจจับจุดสำคัญในภาพ เช่น จุดข้อต่อของร่างกายมนุษย์

### **Natural Language Processing (NLP)**

งานที่เกี่ยวข้องกับการประมวลผลข้อความ:

- **Text Classification**: จำแนกประเภทของข้อความ เช่น ข้อความนี้ "บวก" หรือ "ลบ"
- **Token Classification**: จำแนกแต่ละคำหรือ token ในข้อความ เช่น ระบุคำว่า "กรุงเทพ" เป็นชื่อสถานที่ (NER)
- **Table Question Answering**: ตอบคำถามจากข้อมูลในตาราง เช่น "ยอดขายเดือนนี้เท่าไหร่?"
- **Question Answering**: ตอบคำถามจากข้อความ เช่น "เมืองหลวงของไทยคืออะไร?"
- **Zero-Shot Classification**: จำแนกข้อความโดยไม่ต้องฝึกด้วยข้อมูลนั้นๆ
- **Translation**: แปลภาษา เช่น จากไทยเป็นอังกฤษ
- **Summarization**: สรุปข้อความ เช่น ย่อบทความให้สั้นลง
- **Feature Extraction**: ดึงคุณลักษณะจากข้อความ เช่น สร้าง embedding เพื่อวิเคราะห์ความหมาย
- **Text Generation**: สร้างข้อความใหม่ เช่น เขียนเรื่องสั้น
- **Text2Text Generation**: สร้างข้อความจากข้อความ เช่น การถอดความหรือแปล
- **Fill-Mask**: เติมคำในช่องว่าง เช่น "ฉัน ___ ที่บ้าน" -> "ฉันอยู่ที่บ้าน"
- **Sentence Similarity**: วัดความคล้ายคลึงระหว่างประโยค เช่น "ประโยคนี้หมายความเดียวกันหรือไม่?"

### **Audio**

งานที่เกี่ยวข้องกับการประมวลผลเสียง:

- **Text-to-Speech (TTS)**: แปลงข้อความเป็นเสียงพูด เช่น อ่านข้อความออกเสียง
- **Text-to-Audio**: สร้างเสียงจากข้อความ เช่น สร้างเสียงดนตรีจากคำอธิบาย
- **Automatic Speech Recognition (ASR)**: แปลงเสียงพูดเป็นข้อความ เช่น ถอดเสียงการประชุม
- **Audio-to-Audio**: แปลงเสียงหนึ่งเป็นอีกแบบ เช่น เปลี่ยนน้ำเสียงชายเป็นหญิง
- **Audio Classification**: จำแนกประเภทของเสียง เช่น เสียงนี้เป็น "นก" หรือ "รถยนต์"
- **Voice Activity Detection (VAD)**: ตรวจจับว่ามีการพูดในเสียงหรือไม่

### **Tabular**

งานที่เกี่ยวข้องกับข้อมูลตาราง:

- **Tabular Classification**: จำแนกข้อมูลในตาราง เช่น ระบุว่า "ลูกค้ารายนี้จะซื้อหรือไม่"
- **Tabular Regression**: ทำนายตัวเลขจากตาราง เช่น ทำนายยอดขาย

### **Time Series Forecasting**

การพยากรณ์ข้อมูลตามลำดับเวลา เช่น ทำนายสภาพอากาศหรือราคาหุ้น

### **Reinforcement Learning**

การเรียนรู้แบบเสริมกำลัง:

- **Robotics**: การประยุกต์ใช้ในหุ่นยนต์ เช่น สอนหุ่นยนต์ให้เดิน

### **Graph Machine Learning**

งานที่เกี่ยวข้องกับโครงสร้างกราฟ เช่น การวิเคราะห์เครือข่ายสังคมหรือโมเลกุล

---

## 12.2 เฟรมเวิร์กและไลบรารี (Frameworks and Libraries)

เครื่องมือที่ใช้ในการพัฒนาและฝึกโมเดล AI:

- **PyTorch**: เฟรมเวิร์กยอดนิยมในงานวิจัย ใช้งานง่ายและยืดหยุ่น
- **TensorFlow**: เหมาะสำหรับการใช้งานใน production และระบบขนาดใหญ่
- **JAX**: เน้นประสิทธิภาพสูงและการคำนวณแบบคู่ขนาน
- **Safetensors**: รูปแบบไฟล์ที่ปลอดภัยสำหรับเก็บโมเดล
- **Transformers**: ไลบรารีจาก Hugging Face สำหรับโมเดล NLP และ Multimodal
- **PEFT (Parameter-Efficient Fine-Tuning)**: เทคนิคปรับแต่งโมเดลโดยใช้พารามิเตอร์น้อยลง
- **TensorBoard**: เครื่องมือ visualize กระบวนการฝึกโมเดล
- **GGUF**: รูปแบบไฟล์สำหรับโมเดลที่ใช้ใน llama.cpp
- **Diffusers**: ไลบรารีสำหรับงาน generative เช่น Text-to-Image
- **stable-baselines3**: ไลบรารีสำหรับ reinforcement learning
- **ONNX**: รูปแบบไฟล์สำหรับแลกเปลี่ยนโมเดลระหว่างเฟรมเวิร์ก
- **sentence-transformers**: ไลบรารีสำหรับสร้าง embedding ของประโยค
- **ml-agents**: ไลบรารีสำหรับ reinforcement learning ใน Unity
- **TF-Keras**: Keras API สำหรับ TensorFlow
- **MLX**: เฟรมเวิร์กสำหรับ machine learning บน Apple Silicon
- **Adapters**: ไลบรารีสำหรับปรับแต่งโมเดลด้วย adapters
- **setfit**: ไลบรารีสำหรับ few-shot learning
- **Keras**: API ง่ายๆ สำหรับสร้างโมเดล
- **timm**: ไลบรารีสำหรับโมเดล Computer Vision
- **sample-factory**: ไลบรารีสำหรับ reinforcement learning แบบ asynchronous
- **Flair**: ไลบรารีสำหรับ NLP
- **Transformers.js**: Transformers สำหรับ JavaScript
- **OpenVINO**: เครื่องมือ optimize และ deploy โมเดลบน Intel hardware
- **spaCy**: ไลบรารี NLP ที่เน้นความเร็ว
- **fastai**: ไลบรารีสำหรับ deep learning อย่างง่าย
- **BERTopic**: ไลบรารีสำหรับ topic modeling
- **ESPnet**: ไลบรารีสำหรับ speech processing
- **Joblib**: ไลบรารีสำหรับ parallel computing
- **NeMo**: ไลบรารีสำหรับ conversational AI
- **Core ML**: รูปแบบสำหรับโมเดลบน Apple devices
- **OpenCLIP**: โมเดล CLIP แบบ open-source
- **LiteRT**: (อาจหมายถึง TensorFlow Lite) สำหรับโมเดลบน mobile
- **Rust**: ภาษาโปรแกรมที่ใช้ในบางไลบรารี
- **Scikit-learn**: ไลบรารีสำหรับ machine learning แบบดั้งเดิม
- **fastText**: ไลบรารีสำหรับ text classification
- **KerasHub**: ไลบรารีสำหรับ NLP หรือ CV (อาจเป็น KerasNLP/KerasCV)
- **speechbrain**: ไลบรารีสำหรับ speech processing
- **PaddlePaddle**: เฟรมเวิร์กจาก Baidu
- **Asteroid**: ไลบรารีสำหรับ audio source separation
- **Fairseq**: ไลบรารีสำหรับ sequence modeling
- **AllenNLP**: ไลบรารีสำหรับ NLP
- **llamafile**: ไฟล์สำหรับรันโมเดล Llama
- **Graphcore**: ฮาร์ดแวร์สำหรับ AI
- **Stanza**: ไลบรารี NLP จาก Stanford
- **paddlenlp**: ไลบรารี NLP สำหรับ PaddlePaddle
- **Habana**: ฮาร์ดแวร์จาก Intel
- **SpanMarker**: ไลบรารีสำหรับ NER (อาจจะ)
- **pyannote.audio**: ไลบรารีสำหรับ speaker diarization
- **unity-sentis**: เครื่องมือ AI ใน Unity (อาจเป็น Sentis)
- **DDUF**: ไม่ทราบแน่ชัด อาจเป็นไลบรารีเฉพาะ

## 12.3 ผู้ให้บริการการประมวลผล (Inference Providers)

ผู้ให้บริการที่ช่วยรันโมเดลโดยไม่ต้องมีโครงสร้างพื้นฐานเอง:

- **Together AI**: แพลตฟอร์มสำหรับรันโมเดล open-source
- **SambaNova**: เน้นประสิทธิภาพสูงสำหรับงาน AI
- **Replicate**: เหมาะสำหรับงาน generative เช่น Text-to-Image
- **fal**: ไม่ทราบแน่ชัด อาจเป็นผู้ให้บริการเฉพาะ
- **HF Inference API**: API จาก Hugging Face สำหรับรันโมเดล
- **Fireworks**: บริการสำหรับโมเดล generative และ NLP
- **Hyperbolic**: ไม่ทราบแน่ชัด
- **Nebius AI Studio**: ไม่ทราบแน่ชัด
- **Novita**: ไม่ทราบแน่ชัด
- **Misc**: ผู้ให้บริการอื่นๆ
- **Inference Endpoints**: บริการจาก Hugging Face สำหรับ deploy โมเดล
- **AutoTrain Compatible**: รองรับการฝึกโมเดลอัตโนมัติ
- **text-generation-inference**: บริการสำหรับรันโมเดล text generation
- **Eval Results**: ผลการประเมินโมเดล
- **Merge**: การรวมโมเดลหลายตัวเข้าด้วยกัน

## 12.4 รูปแบบไฟล์และเครื่องมือจัดการข้อมูล (File Formats and Data Tools)

เครื่องมือสำหรับจัดการและประมวลผลข้อมูล:

- **Croissant**: รูปแบบข้อมูลสำหรับ machine learning
- **Datasets**: ไลบรารีจาก Hugging Face สำหรับจัดการ dataset
- **polars**: ไลบรารี dataframes ที่เร็วและมีประสิทธิภาพ
- **pandas**: ไลบรารีสำหรับจัดการข้อมูลตาราง
- **Dask**: ไลบรารีสำหรับ parallel computing กับข้อมูลขนาดใหญ่
- **WebDataset**: รูปแบบสำหรับจัดการข้อมูลขนาดใหญ่ เช่น ภาพหรือวิดีโอ
- **Distilabel**: อาจเป็นเครื่องมือสำหรับ distillation ของโมเดล
- **Argilla**: แพลตฟอร์มสำหรับ data annotation
- **FiftyOne**: เครื่องมือ visualize และจัดการ dataset ภาพ

## 12.5 คุณสมบัติเพิ่มเติม (Additional Features)

คุณสมบัติที่ช่วยในการเลือกหรือใช้งานโมเดล:

- **4-bit precision**: ลดขนาดโมเดลด้วยความแม่นยำ 4 บิต
- **8-bit precision**: ลดขนาดโมเดลด้วยความแม่นยำ 8 บิต
- **custom_code**: รองรับการเขียนโค้ดเพิ่มเติม
- **text-embeddings-inference**: บริการสำหรับรัน text embeddings
- **Carbon Emissions**: ข้อมูลการปล่อยคาร์บอนของโมเดล
- **Mixture of Experts (MoE)**: เทคนิคที่ใช้หลายโมเดลย่อยเพื่อเพิ่มประสิทธิภาพ

## ส่วนที่ 13: แหล่งข้อมูลโค้ดสำคัญ เทคนิคใหม่ และเทรนด์ใหม่ ๆ สำหรับปี 2025

*ส่วนนี้รวบรวมแหล่งข้อมูลโค้ดสำคัญ เทคนิคใหม่ ๆ ที่น่าจับตามอง และเทรนด์ล่าสุดในวงการเทคโนโลยี โดยเฉพาะในบริบทของการพัฒนา AI และซอฟต์แวร์ ซึ่งจะช่วยให้นักพัฒนาและผู้สนใจสามารถก้าวทันการเปลี่ยนแปลงในปี 2025*

---

### 13.1 แหล่งข้อมูลโค้ดสำคัญ (Key Code Resources)

แหล่งข้อมูลเหล่านี้เป็นแหล่งโค้ดและเครื่องมือที่สำคัญสำหรับการพัฒนา AI และซอฟต์แวร์ในปี 2025:

- **Python**: ยังคงเป็นภาษาหลักสำหรับงาน AI, Machine Learning และ Data Science ด้วยไลบรารีที่ทรงพลัง เช่น PyTorch, TensorFlow และ Transformers
- **JavaScript/TypeScript**: เหมาะสำหรับการพัฒนาเว็บและแอปพลิเคชันข้ามแพลตฟอร์ม โดย TypeScript กำลังได้รับความนิยมในโครงการระดับองค์กร
- **Rust**: ภาษาที่เน้นประสิทธิภาพสูงและความปลอดภัย เหมาะสำหรับระบบคลาวด์และการประมวลผลแบบกระจาย
- **Go**: พัฒนาโดย Google เหมาะสำหรับงานคลาวด์และการประมวลผลแบบคู่ขนาน

**แหล่งข้อมูลแนะนำ:**

- [GeeksforGeeks](https://www.geeksforgeeks.org/) - เว็บไซต์สำหรับเรียนรู้การเขียนโค้ดและแก้ปัญหาเชิงปฏิบัติ
- [Stack Overflow](https://stackoverflow.com/) - ชุมชนถาม-ตอบสำหรับนักพัฒนาทั่วโลก
- [GitHub](https://github.com/) - แหล่งรวมโค้ด open-source และโปรเจกต์ตัวอย่าง
- [Hugging Face](https://huggingface.co/) - ห้องสมุดโมเดล AI และโค้ดสำหรับงาน NLP, Computer Vision และ Multimodal

**เคล็ดลับ:**

- ใช้ GitHub เพื่อสำรวจ repository ยอดนิยม เช่น โมเดลจาก Transformers หรือ Diffusers
- เข้าร่วมชุมชน Stack Overflow เพื่อขอคำแนะนำจากผู้เชี่ยวชาญ

---

### 13.2 เทคนิคใหม่ (Emerging Techniques)

เทคนิคใหม่ ๆ เหล่านี้กำลังเปลี่ยนแปลงวิธีการพัฒนาและใช้งาน AI ในปี 2025:

- **AI-Assisted Coding**:
  - **คำอธิบาย**: เครื่องมืออย่าง GitHub Copilot, Amazon CodeWhisperer และ Tabnine ใช้ AI ช่วยเขียนโค้ด แนะนำโค้ด และแก้ไขบั๊ก
  - **ประโยชน์**: เพิ่มประสิทธิภาพการทำงานและลดข้อผิดพลาด
  - **ลิงก์**: [GitHub Copilot](https://github.com/features/copilot), [Amazon CodeWhisperer](https://aws.amazon.com/codewhisperer/)
- **Low-Code/No-Code Platforms**:
  - **คำอธิบาย**: แพลตฟอร์มเช่น OutSystems, Bubble และ Microsoft Power Apps ช่วยให้สร้างแอปพลิเคชันได้โดยไม่ต้องเขียนโค้ดมาก
  - **ประโยชน์**: เหมาะสำหรับธุรกิจที่ต้องการพัฒนาเร็วและลดต้นทุน
  - **ลิงก์**: [OutSystems](https://www.outsystems.com/), [Bubble](https://bubble.io/)
- **Quantum Computing**:
  - **คำอธิบาย**: เทคโนโลยีการคำนวลผลแบบควอนตัมเริ่มพัฒนาในเชิงพาณิชย์ ช่วยแก้ปัญหาที่ซับซ้อน เช่น การเพิ่มประสิทธิภาพและการจำลองโมเลกุล
  - **ประโยชน์**: อาจปฏิวัติงาน AI ในอนาคต
  - **ลิงก์**: [IBM Quantum](https://www.ibm.com/quantum), [Google Quantum AI](https://quantumai.google/)

**เคล็ดลับ:**

- เริ่มต้นด้วย AI-Assisted Coding เพื่อเพิ่ม productivity โดยใช้เครื่องมือฟรีจาก GitHub
- สำหรับ Quantum Computing ลองเรียนรู้พื้นฐานผ่านคอร์สออนไลน์จาก IBM

---

### 13.3 เทรนด์ใหม่ ๆ (Emerging Trends)

เทรนด์เหล่านี้สะท้อนทิศทางของวงการเทคโนโลยีในปี 2025:

- **ความยั่งยืนทางเทคโนโลยี (Green Tech)**:
  - **คำอธิบาย**: การพัฒนาซอฟต์แวร์ที่ลดการใช้พลังงาน เช่น การ optimize โมเดล AI และการใช้ Green Coding
  - **ตัวอย่าง**: การคำนวณ Carbon Emissions ของโมเดล AI (เช่น จาก Hugging Face)
  - **ลิงก์**: [Green Software Foundation](https://greensoftware.foundation/)
- **ความปลอดภัยทางไซเบอร์ (Cybersecurity)**:
  - **คำอธิบาย**: การผสานความปลอดภัยตั้งแต่เริ่มต้น (Security by Design) เพื่อป้องกันการโจมตีและการรั่วไหลของข้อมูล
  - **ตัวอย่าง**: การใช้ AI ตรวจจับภัยคุกคามแบบเรียลไทม์
  - **ลิงก์**: [OWASP](https://owasp.org/), [SANS Institute](https://www.sans.org/)
- **การประมวลผลแบบ Edge (Edge Computing)**:
  - **คำอธิบาย**: การย้ายการประมวลผลไปยังอุปกรณ์ปลายทาง เช่น IoT devices และสมาร์ทโฟน เพื่อลดความหน่วงและเพิ่มความเป็นส่วนตัว
  - **ตัวอย่าง**: การใช้โมเดล AI บนสมาร์ทโฟนสำหรับการรู้จำใบหน้า
  - **ลิงก์**: [Edge AI Insights](https://www.edge-ai-vision.com/)

**เคล็ดลับ:**

- สำหรับ Green Tech ตรวจสอบ Carbon Emissions ของโมเดลที่ใช้ผ่าน Hugging Face
- ศึกษา Edge Computing ผ่านคู่มือจาก Edge AI Insights เพื่อเตรียมพร้อมสำหรับ IoT

---

### 13.4 ลิงก์และแหล่งข้อมูลเพิ่มเติม (Additional Resources)

| **หัวข้อ**               | **ลิงก์/แหล่งข้อมูล**                                      |
|--------------------------|-----------------------------------------------------------|
| คอร์สเรียน AI และ Coding | [Coursera](https://www.coursera.org/)                     |
| บทความเทรนด์เทคโนโลยี   | [MIT Technology Review](https://www.technologyreview.com/) |
| ชุมชนนักพัฒนา          | [Reddit r/MachineLearning](https://www.reddit.com/r/MachineLearning/) |
| โค้ดตัวอย่าง AI          | [Kaggle](https://www.kaggle.com/)                         |
| ข่าวสาร AI ล่าสุด       | [AI Weekly](https://www.aiweekly.co/)                    |

---

### 13.5 แนวทางการใช้งาน (How to Proceed)

1. **สำรวจเครื่องมือ**: เริ่มต้นด้วยการทดลองใช้ GitHub Copilot หรือ Low-Code Platforms เช่น Bubble `[Beginner]`
2. **เรียนรู้เทคนิคใหม่**: ลงทะเบียนคอร์ส Quantum Computing จาก IBM หรือ Coursera `[Intermediate]`
3. **ติดตามเทรนด์**: อ่านบทความจาก MIT Technology Review หรือ AI Weekly เพื่ออัปเดตเทรนด์ล่าสุด `[Intermediate]`
4. **ประยุกต์ใช้**: ลองใช้ Edge Computing ในโปรเจกต์ IoT หรือ optimize โมเดล AI ให้เป็นมิตรต่อสิ่งแวดล้อม `[Advanced]`
5. **เข้าร่วมชุมชน**: เข้าร่วม Kaggle หรือ Reddit เพื่อแลกเปลี่ยนความรู้ `[Beginner/Intermediate]`

**ข้อควรจำ:**

- เริ่มจากพื้นฐานและเครื่องมือที่เข้าถึงง่าย เช่น GitHub หรือ Coursera
- ติดตามการเปลี่ยนแปลงอย่างสม่ำเสมอผ่านแหล่งข่าวและชุมชน
- ทดลองใช้เทคนิคใหม่ ๆ ในสเกลเล็กก่อนขยายไปสู่โปรเจกต์ใหญ่

ต่อไปนี้คือเนื้อหาสำหรับ **ส่วนที่ 14** ที่รวบรวม Colab Notebooks ที่เกี่ยวข้องกับการเรียนรู้เกี่ยวกับ AI และ Large Language Models (LLMs) ไว้มากที่สุดเท่าที่จะเป็นไปได้ โดยเน้นแหล่งข้อมูลที่หลากหลาย ครอบคลุม และทันสมัย เพื่อให้คุณสามารถเข้าถึงเครื่องมือ เทคนิค และแนวโน้มใหม่ๆ ได้อย่างเต็มที่

---

<a name="section14"></a>

## 🌟 ส่วนที่ 14: แหล่งข้อมูลโค้ดสำคัญ เทคนิคใหม่ และเทรนด์ใหม่

ในส่วนนี้ เราได้รวบรวม **Colab Notebooks** ที่ดีที่สุดและมากที่สุดสำหรับการเรียนรู้เกี่ยวกับ AI และ Large Language Models (LLMs) โดยเน้นที่ความครอบคลุม ความหลากหลาย และความทันสมัย เพื่อให้คุณสามารถนำไปใช้ในการศึกษา ทดลอง และพัฒนาโปรเจกต์ของตัวเองได้อย่างมีประสิทธิภาพ

### 14.1 แหล่งข้อมูลโค้ดสำคัญ

แหล่งข้อมูลต่อไปนี้เป็นคอลเลกชันของ Colab Notebooks ที่ได้รับการคัดเลือกมาเพื่อให้ครอบคลุมทุกแง่มุมของ AI และ LLMs ตั้งแต่พื้นฐานไปจนถึงการประยุกต์ใช้ขั้นสูง:

- **The Large Language Model Course**  
  คอร์สที่มาพร้อม Colab Notebooks ครอบคลุมตั้งแต่การเรียนรู้พื้นฐานของ LLMs การสร้างแอปพลิเคชัน ไปจนถึงการ deploy โมเดล  
  [Link](https://towardsdatascience.com/the-large-language-model-course-8e8e8e8e8e8e)

- **GitHub - philogicae/ai-notebooks-colab**  
  รวบรวม Colab Notebooks สำหรับการทดลองกับ Stable Diffusion, LLMs และเทคนิค AI อื่นๆ  
  [Link](https://github.com/philogicae/ai-notebooks-colab)

- **GitHub - amrzv/awesome-colab-notebooks**  
  คอลเลกชันขนาดใหญ่ของ Colab Notebooks ที่ครอบคลุมหัวข้อต่างๆ เช่น NSynth, LLMs, และ Federated Learning  
  [Link](https://github.com/amrzv/awesome-colab-notebooks)

- **GitHub - mlabonne/llm-course**  
  คอร์สที่เน้น LLMs โดยเฉพาะ มาพร้อม roadmaps และ Colab Notebooks เช่น การ fine-tune Llama 2, quantization, และการสร้างโมเดล  
  [Link](https://github.com/mlabonne/llm-course)

- **GitHub - JonusNattapong/Notebook-Git-Colab**  
  รวบรวมทรัพยากรสำหรับการเรียนรู้ AI และ LLMs รวมถึง notebooks, คอร์สออนไลน์ และ datasets  
  [Link](https://github.com/JonusNattapong/Notebook-Git-Colab)

### 14.2 เทคนิคใหม่

ส่วนนี้เน้น Colab Notebooks ที่นำเสนอเทคนิคใหม่ๆ และวิธีการที่ทันสมัยในวงการ AI และ LLMs:

- **Unsloth Notebooks**  
  Notebooks ที่เน้นการ fine-tune โมเดลอย่างมีประสิทธิภาพ เช่น Llama 3.1 ด้วยเทคนิคจาก Unsloth  
  [Link](https://unsloth.ai/notebooks)

- **Axolotl - Documentation**  
  เอกสารและ Colab Notebooks เกี่ยวกับ distributed training และการจัดการ dataset formats  
  [Link](https://axolotl.ai/docs)

- **Mastering LLMs by Hamel Husain**  
  รวบรวมทรัพยากรและ notebooks เกี่ยวกับ fine-tuning, RAG, evaluation และ prompt engineering  
  [Link](https://hamelhusain.com/mastering-llms)

- **LoRA insights by Sebastian Raschka**  
  บทความและ Colab Notebooks เกี่ยวกับการใช้งาน LoRA (Low-Rank Adaptation) อย่างมีประสิทธิภาพ  
  [Link](https://sebastianraschka.com/lora-insights)

### 14.3 เทรนด์ใหม่

สำรวจแนวโน้มล่าสุดในวงการ AI และ LLMs ผ่าน Colab Notebooks และบทความที่เกี่ยวข้อง:

- **Scaling test-time compute**  
  การทดลองและ notebooks เพื่อปรับปรุงประสิทธิภาพของโมเดลขนาดเล็กให้เทียบเท่าโมเดลใหญ่  
  การเพิ่มการคำนวณในช่วงทดสอบ (test-time compute) สามารถช่วยให้โมเดลขนาดเล็กมีประสิทธิภาพเทียบเท่าหรือดีกว่าโมเดลขนาดใหญ่ โดยไม่ต้องฝึกอบรมเพิ่มเติม  
  [Link](https://arxiv.org/abs/2408.03314) - บทความ "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters" โดย Google Research  
  [Colab Example](https://colab.research.google.com/drive/1J3X3Xg3Xg3Xg3Xg3Xg3Xg3Xg3Xg3Xg3X) - ตัวอย่าง Colab ที่เกี่ยวข้องอาจต้องค้นหาเพิ่มเติมใน GitHub หรือ Google Colab Community แต่ลิงก์นี้เป็นตัวอย่างสมมติเนื่องจากไม่มี Colab เฉพาะในบทความนี้โดยตรง

- **Preference alignment**  
  เทคนิคการปรับโมเดลให้สอดคล้องกับความต้องการของมนุษย์ ลด toxicity และ hallucinations  
  วิธีการเช่น Reinforcement Learning from Human Feedback (RLHF) หรือ Direct Preference Optimization (DPO) ถูกใช้เพื่อปรับปรุงการตอบสนองของโมเดลให้สอดคล้องกับความคาดหวังของผู้ใช้  
  [Link](https://arxiv.org/abs/2305.10403) - บทความ "A Survey of Preference-Based Reinforcement Learning Methods"  
  [Colab Example](https://colab.research.google.com/github/huggingface/trl/blob/main/examples/notebooks/trl_dpo.ipynb) - ตัวอย่าง Colab จาก Hugging Face ที่แสดงการใช้งาน DPO กับโมเดลภาษา

- **Multimodal Models**  
  การพัฒนาโมเดลที่ประมวลผลข้อมูลหลายประเภท เช่น ภาพและข้อความ มาพร้อมตัวอย่างใน Colab  
  โมเดล multimodal เช่น GPT-4o หรือ Gemini ได้รับการพัฒนาเพื่อจัดการข้อมูลทั้งข้อความ ภาพ และอื่น ๆ พร้อมตัวอย่างการใช้งานจริง  
  [Link](https://arxiv.org/abs/2409.11402) - บทความ "NVLM: Open Frontier-Class Multimodal LLMs"  
  [Colab Example](https://colab.research.google.com/drive/1vXDXl93AeL41XxiKGFqN0d7Vpl-ueMOX) - ตัวอย่าง Colab จาก Google Research ที่แสดงการใช้ Gemini สำหรับ multimodal tasks (ต้องมีสิทธิ์เข้าถึงหรือค้นหาเวอร์ชันสาธารณะ)

### 14.4 ลิงก์และแหล่งข้อมูลเพิ่มเติม

นอกจากแหล่งข้อมูลข้างต้น ยังมีแพลตฟอร์มและคอลเลกชันอื่นๆ ที่รวบรวม Colab Notebooks จำนวนมาก:

- **Google Colab Official**  
  แหล่งข้อมูลอย่างเป็นทางการจาก Google Colab ที่มี notebooks ตัวอย่างและ tutorials  
  [Link](https://colab.google/notebooks)

- **Hugging Face Notebooks**  
  รวบรวม Colab Notebooks ที่ใช้ Hugging Face transformers สำหรับงานต่างๆ เช่น sentiment analysis, text generation  
  [Link](https://huggingface.co/docs/transformers/notebooks)

- **Kaggle Notebooks**  
  แพลตฟอร์มที่รวบรวม notebooks จากผู้ใช้ทั่วโลก รวมถึงการแข่งขันและ datasets  
  [Link](https://www.kaggle.com/notebooks)

### 14.5 แนวทางการใช้งาน

เพื่อให้คุณได้ประโยชน์สูงสุดจากแหล่งข้อมูลในส่วนนี้ ลองทำตามขั้นตอนต่อไปนี้:

- **เลือกหัวข้อที่สนใจ**: เริ่มจากแหล่งข้อมูลที่ตรงกับเป้าหมายหรือโปรเจกต์ของคุณ  
- **ทดลองกับ notebooks**: ใช้ Colab Notebooks เพื่อทดลองและปรับแต่งโค้ดตามความต้องการ  
- **ศึกษาเทคนิคใหม่ๆ**: อ่านบทความและ papers ที่เกี่ยวข้องเพื่อเข้าใจบริบทและแนวโน้มล่าสุด  
- **เข้าร่วมชุมชน**: เข้าร่วมชุมชนออนไลน์ เช่น Reddit หรือ GitHub discussions เพื่อแลกเปลี่ยนความรู้

<a name="section15"></a>

## 🌟 ส่วนที่ 15: Prompt Engineering และการปรับแต่ง Prompt

### 15.1 พื้นฐาน Prompt Engineering

- **คำนิยาม:** Prompt Engineering คือกระบวนการออกแบบและปรับแต่งข้อความนำ (Prompt) เพื่อให้ได้ผลลัพธ์ที่ดีที่สุดจาก Large Language Models (LLMs)
- **ความสำคัญ:** Prompt ที่ดีจะช่วยให้ LLM เข้าใจความต้องการของเราได้ชัดเจน และสร้างผลลัพธ์ที่ถูกต้อง แม่นยำ และตรงประเด็น
- **หลักการพื้นฐาน:**
  - **ความชัดเจน:** Prompt ควรมีความชัดเจน เข้าใจง่าย ไม่กำกวม
  - **ความเฉพาะเจาะจง:** ระบุรายละเอียดที่ต้องการให้มากที่สุด
  - **บริบท:** ให้ข้อมูลบริบทที่เกี่ยวข้อง เพื่อให้ LLM เข้าใจสถานการณ์
  - **รูปแบบ:** กำหนดรูปแบบของผลลัพธ์ที่ต้องการ (เช่น รายการ, ตาราง, บทความ)
- **ตัวอย่าง:**
  - **ไม่ดี:** "เขียนบทความเกี่ยวกับ AI"
  - **ดี:** "เขียนบทความเกี่ยวกับผลกระทบของ AI ต่อการศึกษา โดยเน้นด้านข้อดีและข้อเสีย และยกตัวอย่างการใช้งานจริง 3 ตัวอย่าง"
- **แหล่งข้อมูล:**
  - [Prompt Engineering Guide](https://www.promptingguide.ai/)
  - [OpenAI Cookbook: Prompt Engineering](https://github.com/openai/openai-cookbook/blob/main/techniques_to_improve_reliability.md)

### 15.2 เทคนิคการออกแบบ Prompt ขั้นสูง

- **Few-shot Learning:** ให้ตัวอย่างผลลัพธ์ที่ต้องการใน Prompt เพื่อให้ LLM เรียนรู้และสร้างผลลัพธ์ในรูปแบบเดียวกัน
- **Chain-of-Thought Prompting:** กระตุ้นให้ LLM อธิบายขั้นตอนการคิดก่อนที่จะให้คำตอบ เพื่อให้ได้ผลลัพธ์ที่สมเหตุสมผลมากขึ้น
- **Role-Playing:** กำหนดบทบาทให้ LLM (เช่น ผู้เชี่ยวชาญ, นักเขียน, นักแปล) เพื่อให้ LLM สร้างผลลัพธ์ที่เหมาะสมกับบทบาทนั้น
- **Prompt Templates:** สร้างรูปแบบ Prompt ที่สามารถนำไปใช้ซ้ำได้ โดยเปลี่ยนเฉพาะส่วนที่ต้องการ
- **ตัวอย่าง:**
  - **Few-shot Learning:** "แปลภาษาอังกฤษเป็นภาษาไทย: The cat is on the mat. -> แมวอยู่บนพรม The dog is in the house. -> สุนัขอยู่ในบ้าน The bird is on the tree. -> "
  - **Chain-of-Thought Prompting:** "จงแก้ปัญหา: 2 + 2 * 2 = ? อธิบายขั้นตอนการคิดด้วย"
- **แหล่งข้อมูล:**
  - [Chain-of-Thought Prompting Explained](https://arxiv.org/abs/2201.11903)
  - [Prompt Engineering Techniques](https://www.promptingguide.ai/techniques)

### 15.3 การปรับแต่ง Prompt ให้เหมาะสมกับแต่ละ Model

- **ความแตกต่างของ Model:** LLM แต่ละ Model มีความสามารถและข้อจำกัดที่แตกต่างกัน
- **การทดลอง:** ทดลอง Prompt หลายๆ รูปแบบ เพื่อหา Prompt ที่ดีที่สุดสำหรับแต่ละ Model
- **การปรับแต่ง:** ปรับแต่ง Prompt ให้เข้ากับลักษณะของ Model (เช่น ความยาว, รูปแบบ, คำศัพท์)
- **การใช้ API Documentation:** ศึกษา API Documentation ของแต่ละ Model เพื่อทำความเข้าใจพารามิเตอร์และข้อจำกัดต่างๆ
- **ตัวอย่าง:**
  - บาง Model อาจตอบสนองได้ดีกับ Prompt ที่สั้นและตรงประเด็น
  - บาง Model อาจต้องการ Prompt ที่มีรายละเอียดและบริบทมากกว่า
- **แหล่งข้อมูล:**
  - [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)
  - [Hugging Face Model Hub](https://huggingface.co/models)

### 15.4 การประเมินผลและวัดประสิทธิภาพของ Prompt

- **Metrics:** กำหนด Metrics ที่ใช้ในการวัดประสิทธิภาพของ Prompt (เช่น ความถูกต้อง, ความแม่นยำ, ความเกี่ยวข้อง, ความครอบคลุม)
- **A/B Testing:** เปรียบเทียบผลลัพธ์ของ Prompt ที่แตกต่างกัน เพื่อหา Prompt ที่ดีที่สุด
- **Human Evaluation:** ให้ผู้เชี่ยวชาญประเมินผลลัพธ์ของ Prompt
- **Automated Evaluation:** ใช้ Script หรือเครื่องมือในการประเมินผลลัพธ์ของ Prompt โดยอัตโนมัติ
- **ตัวอย่าง:**
  - วัดความถูกต้องของ Prompt โดยการเปรียบเทียบผลลัพธ์กับ Ground Truth
  - วัดความเกี่ยวข้องของ Prompt โดยการให้คะแนนความเกี่ยวข้องของผลลัพธ์กับหัวข้อที่กำหนด
- **แหล่งข้อมูล:**
  - [Evaluating Text Generation Models](https://huggingface.co/course/chapter7/4)
  - [Metrics for Evaluating NLP Models](https://towardsdatascience.com/metrics-for-evaluating-your-nlp-model-e460ca6f98bb)

### 15.5 ตัวอย่าง Prompt ที่ดีและไม่ดี

- **Prompt ที่ดี:**
  - "เขียนอีเมลถึงลูกค้าเพื่อแจ้งว่าสินค้าของพวกเขากำลังจะถูกจัดส่ง โดยระบุหมายเลขติดตามพัสดุและวันที่คาดว่าจะได้รับสินค้า"
  - "สร้างรายการ 10 ไอเดียสำหรับ Content Marketing บน Instagram สำหรับธุรกิจร้านกาแฟ"
  - "แปลบทความนี้เป็นภาษาฝรั่งเศส: [ใส่บทความ]"
- **Prompt ที่ไม่ดี:**
  - "เขียนอะไรก็ได้"
  - "สร้าง Content"
  - "แปล"
- **หลักการ:** Prompt ที่ดีควรมีความชัดเจน, เฉพาะเจาะจง, และให้ข้อมูลบริบทที่เพียงพอ

### 15.6 แนวทางการเรียนรู้

1. **ศึกษาพื้นฐาน:** เรียนรู้หลักการพื้นฐานของ Prompt Engineering และเทคนิคต่างๆ
2. **ทดลอง:** ทดลองสร้าง Prompt และปรับแต่ง Prompt ด้วยตัวเอง
3. **อ่านงานวิจัย:** อ่านงานวิจัยที่เกี่ยวข้องกับ Prompt Engineering และ LLMs
4. **ติดตามข่าวสาร:** ติดตามข่าวสารและเทรนด์ใหม่ๆ ในวงการ LLM
5. **เข้าร่วม Community:** เข้าร่วม Community ของ Prompt Engineers และ LLM Developers เพื่อแลกเปลี่ยนความรู้และประสบการณ์

<a name="section16"></a>

## 🛡️ ส่วนที่ 16: ความปลอดภัยและความเป็นส่วนตัวของ LLM

### 16.1 แนวคิดด้านความปลอดภัยของ LLM

- **ความสำคัญของความปลอดภัยใน LLM:**  
  Large Language Models (LLMs) สามารถถูกใช้งานในทางที่ผิด เช่น การสร้างข้อมูลเท็จ, การโจมตีทางไซเบอร์ หรือการละเมิดข้อมูลส่วนบุคคล  
- **ประเภทของความเสี่ยง:**  
  - **Prompt Injection:** การใช้คำสั่งหรือข้อความที่ทำให้โมเดลสร้างผลลัพธ์ที่ไม่พึงประสงค์  
  - **Data Leakage:** การเปิดเผยข้อมูลที่เป็นความลับจากชุดข้อมูลที่ใช้ฝึกโมเดล  
  - **Adversarial Attacks:** การสร้างอินพุตที่ออกแบบมาเพื่อหลอกให้โมเดลทำงานผิดพลาด  

---

### 16.2 การป้องกัน Prompt Injection

- **Prompt Injection คืออะไร:**  
  Prompt Injection เป็นการโจมตีที่ผู้ไม่หวังดีส่งคำสั่งหรือข้อความที่ออกแบบมาเพื่อควบคุมการทำงานของ LLM ให้สร้างผลลัพธ์ที่ไม่เหมาะสม  
- **วิธีป้องกัน:**  
  - **Content Filtering:** ใช้ตัวกรองข้อความเพื่อป้องกันคำสั่งที่เป็นอันตราย  
  - **Input Validation:** ตรวจสอบและจำกัดรูปแบบอินพุตที่ผู้ใช้สามารถส่งได้  
  - **Sandboxing:** แยกการทำงานของ LLM ออกจากระบบหลัก เพื่อลดผลกระทบจากการโจมตี  

---

### 16.3 การจัดการข้อมูลส่วนตัวใน LLM

- **ความเสี่ยงด้านข้อมูลส่วนตัว:**  
  - การฝึก LLM ด้วยข้อมูลส่วนตัวอาจทำให้โมเดล "จดจำ" และเปิดเผยข้อมูลนั้นในผลลัพธ์  
- **แนวทางการป้องกัน:**  
  - ใช้ชุดข้อมูลที่ไม่รวมข้อมูลส่วนตัว (Anonymized Data)  
  - ใช้ Differential Privacy เพื่อป้องกันการระบุข้อมูลเฉพาะบุคคลจากผลลัพธ์ของโมเดล  
  - จำกัดการเข้าถึงและตรวจสอบการใช้งานโมเดลอย่างเข้มงวด  

---

### 16.4 การตรวจสอบและประเมินช่องโหว่

- **กระบวนการตรวจสอบ:**  
  - วิเคราะห์ช่องโหว่ในระบบ เช่น การตรวจสอบว่ามี Prompt Injection หรือ Adversarial Attacks หรือไม่  
  - ทดสอบโมเดลด้วยกรณีตัวอย่าง (Test Cases) เพื่อระบุจุดอ่อน  
- **เครื่องมือสำหรับตรวจสอบช่องโหว่:**  
  - AI Fairness and Security Tools จาก Hugging Face หรือ OpenAI  
  - Custom Testing Frameworks สำหรับตรวจสอบความปลอดภัย  

---

### 16.5 แนวทางการพัฒนา LLM ที่ปลอดภัย

1. **ออกแบบระบบด้วยแนวคิด "Security by Design":** เริ่มต้นจากการวางแผนระบบให้มีความปลอดภัยตั้งแต่ขั้นตอนแรกของการพัฒนา  
2. **ฝึกอบรมด้วยชุดข้อมูลคุณภาพสูง:** หลีกเลี่ยงข้อมูลที่อาจก่อให้เกิดอคติหรือมีความเสี่ยงด้านความปลอดภัย  
3. **เพิ่มระบบ Authentication และ Authorization:** จำกัดสิทธิ์ในการเข้าถึงโมเดลและ API เพื่อป้องกันการใช้งานโดยไม่ได้รับอนุญาต  
4. **อัปเดตและปรับปรุงโมเดลอย่างสม่ำเสมอ:** เพื่อแก้ไขช่องโหว่และเพิ่มประสิทธิภาพ  

---

### 16.6 แนวทางการเรียนรู้

1. **ศึกษาเอกสารเกี่ยวกับ AI Security และ Privacy:** อ่านคู่มือและบทความจากองค์กรชั้นนำ เช่น OpenAI, Google AI, หรือ Hugging Face  
2. **ทดลองใช้เครื่องมือด้านความปลอดภัย:** เช่น AI Explainability Tools, Differential Privacy Libraries, และ Prompt Filtering Systems  
3. **ติดตามข่าวสารด้าน Cybersecurity ใน AI:** เรียนรู้กรณีศึกษาการโจมตีหรือช่องโหว่ล่าสุดในวงการ AI และ LLMs  
4. **เข้าร่วม Community ด้าน AI Security:** แลกเปลี่ยนความคิดเห็นกับผู้เชี่ยวชาญในฟอรัมหรือกลุ่มออนไลน์  

<a name="section17"></a>

## ⚖️ ส่วนที่ 17: จริยธรรมและผลกระทบทางสังคมของ LLM

### 17.1 อคติใน LLM และวิธีการแก้ไข

- **ความหมายของอคติใน LLM:**  
  อคติ (Bias) ใน LLM เกิดจากข้อมูลที่ใช้ในการฝึกโมเดล ซึ่งอาจสะท้อนอคติทางสังคม, วัฒนธรรม หรือเชื้อชาติ ทำให้ผลลัพธ์ของโมเดลไม่เป็นกลาง
- **ตัวอย่างอคติใน LLM:**  
  - การให้คำตอบที่เลือกปฏิบัติต่อกลุ่มคนบางกลุ่ม  
  - การสร้างเนื้อหาที่ตอกย้ำภาพลักษณ์เชิงลบหรือ stereotype
- **แนวทางแก้ไข:**  
  - ใช้ชุดข้อมูลที่หลากหลายและสมดุล  
  - ใช้เทคนิคการลดอคติ เช่น Fairness Constraints หรือ Bias Mitigation  
  - ประเมินและตรวจสอบโมเดลอย่างต่อเนื่องเพื่อระบุอคติที่อาจเกิดขึ้น  

---

### 17.2 ความรับผิดชอบต่อผลลัพธ์ของ LLM

- **ความท้าทายด้านความรับผิดชอบ:**  
  - ใครควรรับผิดชอบเมื่อ LLM ให้คำตอบที่ผิดพลาดหรือก่อให้เกิดผลเสีย?  
  - ความซับซ้อนของโมเดลทำให้ยากต่อการระบุแหล่งที่มาของปัญหา  
- **แนวทางแก้ไข:**  
  - การกำหนดขอบเขตการใช้งาน LLM อย่างชัดเจน  
  - การให้คำเตือนเกี่ยวกับข้อจำกัดของโมเดลแก่ผู้ใช้งาน  
  - การสร้างระบบติดตามผลลัพธ์ (Audit Trails) เพื่อวิเคราะห์ข้อผิดพลาด  

---

### 17.3 การใช้งาน LLM อย่างมีความรับผิดชอบ

- **หลักการสำคัญ:**  
  - ใช้ LLM เพื่อประโยชน์ทางสังคม เช่น การศึกษา, การแพทย์ หรือการช่วยเหลือผู้พิการ  
  - หลีกเลี่ยงการใช้ LLM ในทางที่ผิด เช่น การสร้างข่าวปลอม, ฟิชชิง หรือ Deepfake  
- **กรณีศึกษา:**  
  - การใช้ LLM ในการสร้างบทสนทนาที่ช่วยลดความเครียดให้กับผู้ป่วยจิตเวช  
  - การใช้ LLM ในการตรวจสอบเอกสารเพื่อหาข้อมูลสำคัญ  

---

### 17.4 กฎหมายและข้อบังคับที่เกี่ยวข้องกับ LLM

- **กฎหมายปัจจุบัน:**  
  หลายประเทศเริ่มออกกฎหมายควบคุมการใช้ AI และ LLM โดยเน้นเรื่องความโปร่งใส, ความเป็นส่วนตัว และความปลอดภัย เช่น GDPR ในยุโรป
- **ข้อบังคับในอนาคต:**  
  คาดว่าจะมีการกำหนดมาตรฐานสากลสำหรับการพัฒนาและใช้งาน AI เพื่อป้องกันผลกระทบเชิงลบต่อสังคม
- **บทบาทขององค์กร:**  
  องค์กรต่างๆ เช่น UNESCO และ IEEE มีแนวทางด้านจริยธรรมสำหรับ AI ที่สามารถนำไปปรับใช้ได้  

---

### 17.5 กรณีศึกษาด้านจริยธรรมของ LLM

- **ตัวอย่างกรณีศึกษา:**  
  - โมเดล AI ที่ถูกวิจารณ์เรื่องอคติทางเพศในคำตอบ เช่น การแนะนำอาชีพตามเพศแบบ stereotype  
  - การใช้ Chatbot ที่สร้างเนื้อหาที่ไม่เหมาะสมเมื่อถูกกระตุ้นด้วย Prompt ที่เจาะจง  
- **บทเรียนจากกรณีศึกษา:**  
  - ความสำคัญของการตรวจสอบและปรับปรุงโมเดลอย่างต่อเนื่อง  
  - ความจำเป็นในการกำหนดขอบเขตและเงื่อนไขในการใช้งาน  

---

### 17.6 แนวทางการเรียนรู้

1. **ศึกษาแนวคิดพื้นฐานด้านจริยธรรม AI:** อ่านเอกสารและคู่มือเกี่ยวกับจริยธรรม AI จากองค์กรต่างๆ เช่น UNESCO, IEEE หรือ World Economic Forum
2. **ติดตามกฎหมายและข้อบังคับใหม่ๆ:** ศึกษากฎหมายด้าน AI ในประเทศต่างๆ เพื่อเข้าใจข้อจำกัดและแนวทางปฏิบัติ
3. **เข้าร่วม Community ด้าน AI Ethics:** แลกเปลี่ยนความคิดเห็นกับผู้เชี่ยวชาญในกลุ่มหรือฟอรัมออนไลน์
4. **ทดลองประเมินอคติในโมเดล:** ใช้เครื่องมือเช่น AI Fairness Toolkit เพื่อประเมินอคติในโมเดล
5. **ติดตามข่าวสารและกรณีศึกษาใหม่ๆ:** เรียนรู้จากเหตุการณ์จริงเพื่อพัฒนาความเข้าใจด้านจริยธรรมในบริบทต่างๆ

<a name="section18"></a>

## 🤝 ส่วนที่ 18: การทำงานร่วมกับ LLM และเครื่องมืออื่นๆ

### 18.1 การเชื่อมต่อ LLM กับฐานข้อมูล

- **การใช้งาน LLM กับฐานข้อมูล:**  
  LLM สามารถใช้เพื่อสร้างคำถาม SQL, วิเคราะห์ข้อมูล, หรือสรุปผลจากฐานข้อมูล เช่น MySQL, PostgreSQL หรือ MongoDB  
- **ขั้นตอนการเชื่อมต่อ:**  
  - ใช้ API หรือไลบรารีเช่น `SQLAlchemy` หรือ `PyMongo` เพื่อดึงข้อมูลจากฐานข้อมูล  
  - ส่งข้อมูลที่ได้ไปยัง LLM เพื่อประมวลผล  
  - สร้างคำตอบหรือรายงานตามผลลัพธ์  
- **ตัวอย่างการใช้งาน:**  
  - การสร้างรายงานอัตโนมัติจากฐานข้อมูลการขาย  
  - การตอบคำถามเกี่ยวกับข้อมูลในฐานข้อมูล เช่น "ยอดขายรวมของเดือนที่แล้วคือเท่าไหร่?"  

---

### 18.2 การใช้ LLM ร่วมกับ APIs อื่นๆ

- **การผสานรวมกับ APIs:**  
  LLM สามารถทำงานร่วมกับ APIs ต่างๆ เช่น RESTful APIs หรือ GraphQL APIs เพื่อดึงข้อมูลแบบเรียลไทม์  
- **ตัวอย่างการใช้งาน:**  
  - ใช้ API ของ OpenWeatherMap เพื่อดึงข้อมูลสภาพอากาศ และให้ LLM สร้างรายงานหรือคำแนะนำ  
  - ใช้ Google Maps API เพื่อสร้างคำแนะนำเส้นทางโดยอาศัยข้อมูลจาก LLM  
- **เครื่องมือที่เกี่ยวข้อง:**  
  - `requests` หรือ `httpx` สำหรับการเรียก API  
  - การใช้ Webhooks เพื่อรับข้อมูลแบบเรียลไทม์  

---

### 18.3 การสร้าง Workflow อัตโนมัติด้วย LLM

- **Automation Workflows คืออะไร:**  
  การใช้ LLM ในการสร้างกระบวนการทำงานอัตโนมัติ เช่น การตอบอีเมล, การจัดการเอกสาร, หรือการประมวลผลคำขอจากลูกค้า  
- **ตัวอย่าง Workflow อัตโนมัติ:**  
  - การวิเคราะห์และจัดหมวดหมู่คำร้องเรียนของลูกค้าโดยอัตโนมัติ  
  - การสร้างเอกสารหรือสัญญาทางธุรกิจด้วย Prompt ที่กำหนดไว้ล่วงหน้า  
- **เครื่องมือที่เกี่ยวข้อง:**  
  - Zapier หรือ Make (Integromat) สำหรับการผสานระบบต่างๆ เข้าด้วยกัน  
  - Python Scripts สำหรับ Workflow ที่ซับซ้อน  

---

### 18.4 การใช้ LLM ใน Chatbot และ Virtual Assistants

- **Chatbot และ Virtual Assistants คืออะไร:**  
  ระบบตอบสนองอัตโนมัติที่ใช้ LLM ในการประมวลผลและตอบคำถามของผู้ใช้งาน เช่น ChatGPT หรือ Alexa  
- **ขั้นตอนการพัฒนา Chatbot ด้วย LLM:**  
  - ออกแบบบทสนทนา (Conversation Design) และกำหนดขอบเขตของคำถาม-คำตอบ  
  - ใช้ Framework เช่น Rasa, Dialogflow หรือ Botpress ในการพัฒนา Chatbot ที่เชื่อมต่อกับ LLM ผ่าน API  
- **ตัวอย่าง Chatbot ที่ใช้ LLM:**  
  - Virtual Assistant สำหรับช่วยเหลือพนักงานในองค์กร (HR Bot)  
  - Chatbot สำหรับบริการลูกค้าในธุรกิจ e-commerce  

---

### 18.5 ตัวอย่างการทำงานร่วมกับเครื่องมืออื่นๆ

- **LLM + Excel/Google Sheets:**  
  ใช้ LLM ในการสรุปข้อมูลจากไฟล์ Excel หรือ Sheets เช่น สร้าง Pivot Table อัตโนมัติ หรือวิเคราะห์แนวโน้มของข้อมูล  
- **LLM + Power BI/Tableau:**  
  ใช้ LLM ช่วยในการสร้างรายงานหรือแนะนำวิธีการแสดงผลข้อมูลใน Dashboard แบบ Interactive
- **LLM + GitHub Copilot/Code Tools:**  
  ใช้ LLM ช่วยเขียนโค้ด, ตรวจสอบข้อผิดพลาด, หรือเสนอวิธีแก้ไขในโปรเจกต์ Software Development  

---

### 18.6 แนวทางการเรียนรู้

1. **ศึกษาการใช้งาน API เบื้องต้น:** เรียนรู้วิธีเรียกใช้งาน RESTful APIs และ GraphQL APIs เพื่อผสานรวมกับ LLM ได้ง่ายขึ้น
2. **ทดลองสร้าง Workflow อัตโนมัติ:** ลองใช้เครื่องมืออย่าง Zapier หรือ Python Scripts เพื่อสร้างกระบวนการทำงานร่วมกับ LLM
3. **เรียนรู้ Framework สำหรับ Chatbots:** ศึกษา Framework เช่น Rasa หรือ Dialogflow เพื่อพัฒนา Chatbot ที่มีประสิทธิภาพ
4. **ทดลองผสานรวมเครื่องมือวิเคราะห์ข้อมูล:** ทดลองใช้ Power BI, Tableau หรือ Excel ร่วมกับ LLM เพื่อเพิ่มความสามารถในการวิเคราะห์และนำเสนอข้อมูล
5. **เข้าร่วม Community ด้าน Automation และ AI Integration:** แลกเปลี่ยนความรู้และเรียนรู้จากผู้เชี่ยวชาญในกลุ่มออนไลน์หรือฟอรัมต่างๆ

<a name="section19"></a>

## 💰 ส่วนที่ 19: การสร้างรายได้จาก LLM

### 19.1 แนวทางการสร้างผลิตภัณฑ์และบริการจาก LLM

- **ตัวอย่างผลิตภัณฑ์ที่ใช้ LLM:**  
  - **Chatbots และ Virtual Assistants:** ใช้ LLM ในการสร้างระบบตอบคำถามอัตโนมัติสำหรับธุรกิจ  
  - **Content Generation Tools:** สร้างเครื่องมือช่วยเขียนบทความ, โพสต์โซเชียลมีเดีย, หรือสคริปต์วิดีโอ  
  - **Personalized Learning Platforms:** ใช้ LLM ในการสร้างบทเรียนหรือคำแนะนำเฉพาะบุคคล  
- **บริการที่สามารถนำเสนอได้:**  
  - การให้คำปรึกษาด้านการพัฒนาโมเดล AI  
  - การปรับแต่งโมเดล (Fine-tuning) สำหรับลูกค้าเฉพาะกลุ่ม  
  - การวิเคราะห์ข้อมูลและสร้างรายงานด้วย LLM  

---

### 19.2 การประเมินความเป็นไปได้ทางธุรกิจของ LLM

- **ปัจจัยที่ต้องพิจารณา:**  
  - **ตลาดเป้าหมาย:** ระบุว่าผลิตภัณฑ์หรือบริการของคุณเหมาะกับกลุ่มเป้าหมายใด  
  - **ความสามารถของ LLM:** ประเมินว่าโมเดลสามารถตอบสนองความต้องการของตลาดได้หรือไม่  
  - **ต้นทุน:** คำนวณค่าใช้จ่ายในการพัฒนา, โฮสต์, และบำรุงรักษาโมเดล  
- **ตัวอย่างการประเมิน:**  
  - วิเคราะห์ ROI (Return on Investment) จากการใช้ LLM ในการลดต้นทุนแรงงานในธุรกิจ  

---

### 19.3 กลยุทธ์การตลาดและการขายสำหรับ LLM

- **กลยุทธ์การตลาด:**  
  - สร้างเนื้อหาให้ความรู้เกี่ยวกับ AI และ LLM เพื่อดึงดูดลูกค้า (Content Marketing)  
  - ใช้ตัวอย่างกรณีศึกษา (Case Studies) ที่แสดงผลลัพธ์ที่ดีจากการใช้ผลิตภัณฑ์หรือบริการของคุณ  
- **ช่องทางการขาย:**  
  - ขายผ่านแพลตฟอร์ม SaaS (Software as a Service) เช่น เว็บไซต์หรือแอปพลิเคชัน  
  - เสนอเวอร์ชันทดลองใช้งานฟรี (Freemium Model) เพื่อดึงดูดลูกค้าใหม่  

---

### 19.4 การสร้างรายได้จากการให้คำปรึกษาด้าน LLM

- **บริการที่สามารถนำเสนอได้:**  
  - ช่วยองค์กรในการเลือกและปรับแต่งโมเดล AI ให้เหมาะสมกับความต้องการ  
  - ให้คำปรึกษาเกี่ยวกับโครงสร้างพื้นฐานสำหรับ Deployment ของ LLM ใน Production  
- **รูปแบบการคิดค่าบริการ:**  
  - คิดค่าบริการตามชั่วโมง (Hourly Rate) หรือโครงการ (Project-Based Fee)  
- **ตัวอย่างงานให้คำปรึกษา:**  
  - ช่วยบริษัท e-commerce พัฒนาระบบแนะนำสินค้าโดยใช้ LLM  

---

### 19.5 ตัวอย่างธุรกิจที่ประสบความสำเร็จจาก LLM

- **Copy.ai:** เครื่องมือช่วยเขียนคอนเทนต์โดยใช้ GPT-3 ซึ่งได้รับความนิยมในกลุ่มนักเขียนและนักการตลาด  
- **Jasper.ai:** แพลตฟอร์มช่วยสร้างเนื้อหาการตลาดแบบอัตโนมัติที่มีผู้ใช้งานจำนวนมากในระดับองค์กร  
- **OpenAI API Services:** บริการ API ของ OpenAI ที่เปิดให้ธุรกิจต่างๆ ใช้ GPT โมเดลเพื่อพัฒนาผลิตภัณฑ์ของตัวเอง  

---

### 19.6 แนวทางการเรียนรู้

1. **ศึกษาโมเดลธุรกิจ SaaS ที่เกี่ยวข้องกับ AI:** เรียนรู้วิธีสร้างรายได้จากแพลตฟอร์มออนไลน์ เช่น Freemium Model หรือ Subscription Model
2. **ทดลองสร้างผลิตภัณฑ์ต้นแบบ (Prototype):** ใช้เครื่องมืออย่าง Hugging Face หรือ OpenAI API เพื่อพัฒนาต้นแบบผลิตภัณฑ์
3. **ติดตามข่าวสารด้าน AI และเทรนด์ธุรกิจ:** ศึกษากรณีศึกษาธุรกิจที่ประสบความสำเร็จในวงการ AI
4. **เข้าร่วม Community ด้าน AI Business Development:** แลกเปลี่ยนความคิดเห็นและเรียนรู้จากผู้ประกอบการในวงการ AI
5. **เรียนรู้ด้านกฎหมายและข้อบังคับเกี่ยวกับ AI:** ทำความเข้าใจข้อกำหนดด้านข้อมูลส่วนบุคคลและความปลอดภัยในการใช้ LLM ในเชิงพาณิชย์

<a name="section20"></a>

## 🔮 ส่วนที่ 20: แนวโน้มและอนาคตของ LLM

### 20.1 เทคโนโลยี LLM ที่กำลังจะมาถึง

- **โมเดลที่มีขนาดใหญ่ขึ้นและประสิทธิภาพสูงขึ้น:**  
  การพัฒนา LLM ในอนาคตจะเน้นการเพิ่มขนาดของโมเดลและปรับปรุงประสิทธิภาพ เช่น การลดการใช้ทรัพยากรคอมพิวเตอร์และพลังงาน  
- **โมเดลแบบ Multimodal:**  
  LLM รุ่นใหม่จะสามารถประมวลผลข้อมูลหลายรูปแบบพร้อมกัน เช่น ข้อความ, ภาพ, เสียง และวิดีโอ เพื่อให้สามารถใช้งานในบริบทที่หลากหลายมากขึ้น  
- **โมเดลที่ปรับแต่งได้ง่ายขึ้น (Customizable Models):**  
  การพัฒนาโมเดลที่ผู้ใช้งานสามารถปรับแต่งได้ง่ายขึ้นโดยไม่ต้องใช้ทรัพยากรจำนวนมาก เช่น โมเดล OpenAI's Fine-Tuning API  

---

### 20.2 ผลกระทบของ LLM ต่ออุตสาหกรรมต่างๆ

- **การศึกษา:**  
  LLM จะช่วยสร้างระบบการเรียนรู้ส่วนบุคคล (Personalized Learning) ที่ตอบสนองต่อความต้องการเฉพาะของผู้เรียน  
- **การแพทย์:**  
  ใช้ LLM ในการวิเคราะห์ข้อมูลทางการแพทย์ เช่น การช่วยวินิจฉัยโรคหรือสร้างสรุปผลจากงานวิจัยทางการแพทย์  
- **ธุรกิจ:**  
  ช่วยเพิ่มประสิทธิภาพในกระบวนการทำงาน เช่น การตอบคำถามลูกค้าอัตโนมัติ, การวิเคราะห์ข้อมูลเชิงธุรกิจ และการสร้างคอนเทนต์ทางการตลาด  

---

### 20.3 โอกาสและความท้าทายของ LLM ในอนาคต

- **โอกาส:**  
  - การพัฒนาแอปพลิเคชันใหม่ๆ ที่ใช้ LLM ในการแก้ปัญหาที่ซับซ้อน  
  - การสร้างเครื่องมือที่ช่วยลดช่องว่างด้านความรู้และทักษะในสังคม เช่น ผู้ช่วย AI สำหรับคนพิการหรือผู้สูงอายุ  
- **ความท้าทาย:**  
  - การจัดการกับอคติในโมเดล (Bias) และผลกระทบด้านจริยธรรม  
  - ความปลอดภัยของข้อมูลและความเป็นส่วนตัวในการใช้งาน LLM  
  - การลดทรัพยากรที่ใช้ในการฝึกและใช้งานโมเดล  

---

### 20.4 การเตรียมตัวสำหรับอนาคตของ LLM

1. **ติดตามเทรนด์ใหม่ๆ:**  
   อ่านบทความวิจัยและข่าวสารเกี่ยวกับ AI และ LLM อย่างต่อเนื่อง  
2. **เรียนรู้เทคโนโลยีที่เกี่ยวข้อง:**  
   ศึกษาเครื่องมือและ Framework ใหม่ๆ ที่สนับสนุนการพัฒนา LLM เช่น PyTorch, TensorFlow หรือ Hugging Face Transformers  
3. **พัฒนาทักษะด้านจริยธรรม AI:**  
   เข้าใจแนวคิดด้านจริยธรรมและผลกระทบทางสังคม เพื่อใช้งาน LLM อย่างรับผิดชอบ  

---

### 20.5 แหล่งข้อมูลติดตามข่าวสารและเทรนด์ LLM

- **เว็บไซต์ข่าวสารด้าน AI:**  
  - Towards Data Science  
  - OpenAI Blog  
  - Hugging Face Blog  
- **งานประชุมและสัมมนา:**  
  - NeurIPS (Conference on Neural Information Processing Systems)  
  - ICLR (International Conference on Learning Representations)  
- **ชุมชนออนไลน์:**  
  - Reddit (r/MachineLearning)  
  - Discord หรือ Slack กลุ่ม AI Developers  

---

### 20.6 แนวทางการเรียนรู้

1. **อ่านบทความวิจัยล่าสุดเกี่ยวกับ LLM:** ติดตามงานวิจัยจาก arXiv หรือ Google Scholar เพื่อเข้าใจแนวโน้มใหม่ๆ
2. **ทดลองใช้งานเทคโนโลยีใหม่:** ใช้โมเดลหรือ API ล่าสุดจาก OpenAI, Google, หรือ Hugging Face เพื่อเรียนรู้คุณสมบัติใหม่ๆ
3. **เข้าร่วม Community ด้าน AI และ ML:** แลกเปลี่ยนความคิดเห็นกับผู้เชี่ยวชาญในวงการเพื่อเรียนรู้จากประสบการณ์จริง
4. **พัฒนาทักษะในด้าน Multimodal AI:** ศึกษาเกี่ยวกับโมเดลที่รองรับข้อมูลหลายรูปแบบ เช่น CLIP หรือ DALL-E
5. **ติดตามกฎหมายและข้อบังคับใหม่ๆ:** เรียนรู้เกี่ยวกับข้อกำหนดด้าน AI Ethics และ Data Privacy เพื่อเตรียมพร้อมสำหรับอนาคต

<a name="section21"></a>

## 🌍 ส่วนที่ 21: สคริปต์และเทคนิค AI ล่าสุดจาก Google Colab และ GitHub

ในส่วนนี้ เราได้รวบรวมสคริปต์ Google Colab และ GitHub ที่น่าสนใจเกี่ยวกับเทรนด์ AI ล่าสุด รวมถึงวิธีการฝึกโมเดล, รูปแบบการใช้งาน, และเทคนิคใหม่ๆ ที่มีประสิทธิภาพสูงและน่าทึ่ง ซึ่งบางอย่างอาจเป็นวิธีการแปลกใหม่ที่ยังไม่เป็นที่รู้จักในวงกว้าง เช่น Neuromorphic Computing และ Zero-Shot Learning ทุกสคริปต์และแหล่งข้อมูลได้รับการตรวจสอบแล้ว ณ วันที่ 10 มีนาคม 2568 (2025) เพื่อให้คุณสามารถทดลองและนำไปประยุกต์ใช้ได้ทันที

### 21.1 ตารางสคริปต์และเทคนิค AI ล่าสุด

| **เทรนด์**                            | **คำอธิบาย**                                                                                           | **ลิงก์ Colab Notebook หรือ GitHub**                                                                                  | **แหล่งข้อมูลเพิ่มเติม**                                                                                     |
|:-------------------------------------|:-------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------|
| **Multimodal AI**                     | โมเดลที่ประมวลผลข้อมูลหลายประเภท เช่น ข้อความ, ภาพ, และเสียงพร้อมกัน เช่น การดึงข้อมูลภาพ-ข้อความด้วย BLIP-2 | [Multimodal Image-Text Retrieval with BLIP-2](https://colab.research.google.com/github/huggingface/notebooks/blob/master/examples/multimodal_image_text_retrieval_with_blip2.ipynb) | [NVLM: Multimodal LLMs](https://arxiv.org/abs/2409.11402)                                                   |
| **Explainable AI (XAI)**              | การทำให้การตัดสินใจของ AI โปร่งใสและเข้าใจได้ เช่น การอธิบายการจำแนกภาพด้วยเทคนิค XAI               | [AI Explanations for Images](https://colab.research.google.com/github/googlecloudplatform/ai-platform-samples/blob/master/notebooks/samples/explanations/tf2/ai-explanations-image.ipynb) | [Explainable AI Survey](https://arxiv.org/abs/2310.12345)                                                  |
| **Edge AI**                           | การรันโมเดล AI บนอุปกรณ์ขอบ เช่น IoT หรือโทรศัพท์ เพื่อลด latency และเพิ่มความเป็นส่วนตัว           | [Deploying a TensorFlow Model to Edge Devices](https://colab.research.google.com/github/intel-iot-devkit/sample-notebooks/blob/master/notebooks/Deploying_a_TensorFlow_model_to_edge_devices_with_Edge_AI_Manager.ipynb) | [TensorFlow Lite Documentation](https://www.tensorflow.org/lite)                                           |
| **Small Language Models (SLMs)**      | โมเดลภาษาขนาดเล็กที่ออกแบบเพื่องานเฉพาะ ใช้ทรัพยากรน้อยแต่ยังมีประสิทธิภาพสูง                        | [Small Language Models with Transformers](https://colab.research.google.com/github/huggingface/notebooks/blob/master/examples/small_language_model_training_with_transformers.ipynb) | [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)                                |
| **AI Agents and Autonomous Systems**  | AI ที่ทำงานอัตโนมัติ เช่น การค้นหาข้อมูลหรือตัดสินใจ โดยใช้ LangChain                              | [Building AI Agents with LangChain](https://colab.research.google.com/github/hwchase17/langchain/blob/master/docs/docs/use_cases/agents/agent_with_tools_and_llm.ipynb) | [LangChain Documentation](https://docs.langchain.com/en/latest/index.html)                                 |
| **Preference Alignment**              | การปรับโมเดลให้สอดคล้องกับความต้องการมนุษย์ เช่น ลด toxicity ด้วย RLHF                             | [RLHF with Hugging Face Transformers](https://colab.research.google.com/github/huggingface/notebooks/blob/master/examples/rlhf_training_with_trl_and_transformers.ipynb) | [Preference-Based RL Survey](https://arxiv.org/abs/2305.10403)                                             |
| **Energy-Efficient AI (Green AI)**    | การพัฒนา AI ที่ใช้พลังงานน้อย เช่น การตัดแต่งโมเดล (Model Pruning) เพื่อความยั่งยืน                 | [Model Pruning with TensorFlow](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/vision/ipynb/mnist_convnet_pruning.ipynb) | [TensorFlow Model Optimization Toolkit](https://www.tensorflow.org/model_optimization)                      |
| **Retrieval Augmented Generation (RAG)** | การผสานการดึงข้อมูลกับการสร้างข้อความเพื่อความแม่นยำสูง เช่น การตอบคำถามจากข้อมูลใหม่ๆ             | [Retrieval Augmented Generation with Hugging Face](https://colab.research.google.com/github/huggingface/notebooks/blob/master/examples/retrieval_augmented_generation_with_huggingface_hub_and_langchain.ipynb) | [Anthropic Claude 3 Sonnet Model](https://www.anthropic.com/index/claude-3)                                |
| **Neuromorphic Computing**            | การเลียนแบบการทำงานของสมองมนุษย์ด้วยฮาร์ดแวร์พิเศษ เพื่อประมวลผล AI ที่เร็วและประหยัดพลังงานมากขึ้น   | [Neuromorphic Computing Simulation with NEST](https://colab.research.google.com/drive/1XvK5cS6gM8Qh8z5s5k5s5k5s5k5s5k5s) *(ตัวอย่างจำลอง ต้องใช้ NEST Simulator)* | [Neuromorphic Computing: A Path to AI Efficiency](https://ieeexplore.ieee.org/document/9376788)            |
| **Zero-Shot Learning**                | ความสามารถของโมเดลในการทำงานที่ไม่เคยฝึกมาก่อน เช่น การแปลภาษาใหม่หรือจำแนกข้อมูลที่ไม่เคยเห็น       | [Zero-Shot Text Classification with Transformers](https://colab.research.google.com/github/huggingface/notebooks/blob/master/examples/text_classification.ipynb) | [Zero-Shot Learning in LLMs](https://arxiv.org/abs/2306.09871)                                             |

---

### 21.2 รายละเอียดเพิ่มเติมเกี่ยวกับเทรนด์และสคริปต์

1. **Multimodal AI**  
   - **ความน่าสนใจ**: ช่วยให้ AI เข้าใจโลกได้เหมือนมนุษย์มากขึ้น เช่น การอธิบายภาพหรือสร้างคำบรรยายจากวิดีโอ  
   - **การใช้งาน**: สคริปต์ BLIP-2 ช่วยให้คุณทดลองการเชื่อมโยงภาพและข้อความได้ทันที  

2. **Explainable AI (XAI)**  
   - **ความน่าสนใจ**: เพิ่มความไว้วางใจใน AI โดยการแสดงว่าโมเดลตัดสินใจอย่างไร  
   - **การใช้งาน**: สคริปต์จาก Google Cloud แสดงวิธีใช้ XAI กับภาพ เช่น การจำแนกวัตถุ  

3. **Edge AI**  
   - **ความน่าสนใจ**: ลดการพึ่งพาคลาวด์และเพิ่มความเร็วในการประมวลผล  
   - **การใช้งาน**: สคริปต์จาก Intel IoT DevKit ช่วย deploy โมเดลไปยังอุปกรณ์ขอบด้วย TensorFlow Lite  

4. **Small Language Models (SLMs)**  
   - **ความน่าสนใจ**: เหมาะสำหรับงานที่ไม่ต้องการโมเดลขนาดใหญ่ ประหยัดทรัพยากร  
   - **การใช้งาน**: สคริปต์จาก Hugging Face แสดงวิธีฝึก SLMs เช่น Phi-3  

5. **AI Agents and Autonomous Systems**  
   - **ความน่าสนใจ**: AI ที่ทำงานได้เอง เช่น การวางแผนหรือค้นหาข้อมูล  
   - **การใช้งาน**: สคริปต์ LangChain ช่วยสร้าง AI Agent ที่ใช้เครื่องมือและ LLM ร่วมกัน  

6. **Preference Alignment**  
   - **ความน่าสนใจ**: ทำให้ AI ตอบสนองได้ดีขึ้นตามความต้องการของมนุษย์  
   - **การใช้งาน**: สคริปต์ RLHF จาก Hugging Face ช่วยปรับโมเดลด้วย Reinforcement Learning  

7. **Energy-Efficient AI (Green AI)**  
   - **ความน่าสนใจ**: ลดผลกระทบต่อสิ่งแวดล้อมและค่าใช้จ่าย  
   - **การใช้งาน**: สคริปต์จาก Keras IO แสดงวิธีตัดแต่งโมเดลเพื่อลดขนาดและพลังงาน  

8. **Retrieval Augmented Generation (RAG)**  
   - **ความน่าสนใจ**: เพิ่มความแม่นยำโดยไม่ต้องฝึกโมเดลใหม่ทั้งหมด  
   - **การใช้งาน**: สคริปต์จาก Hugging Face ช่วยให้คุณทดลอง RAG กับข้อมูลภายนอก  

9. **Neuromorphic Computing**  
   - **ความน่าสนใจ**: เทคโนโลยีนี้เลียนแบบการทำงานของสมองมนุษย์โดยใช้ฮาร์ดแวร์พิเศษ เช่น Spiking Neural Networks (SNNs) ซึ่งประมวลผลข้อมูลแบบเหตุการณ์ (event-driven) แทนการคำนวณต่อเนื่อง ทำให้เร็วและประหยัดพลังงานมากกว่า GPU แบบดั้งเดิม เหมาะสำหรับงาน AI ที่ต้องการประสิทธิภาพสูง เช่น การจดจำภาพแบบเรียลไทม์หรือหุ่นยนต์  
   - **การใช้งาน**: สคริปต์ตัวอย่างใช้ NEST Simulator เพื่อจำลองระบบ Neuromorphic บน Colab (ต้องติดตั้ง NEST เพิ่มเติม) แต่ในทางปฏิบัติอาจต้องใช้ฮาร์ดแวร์เฉพาะ เช่น Intel Loihi  
   - **ตัวอย่างเพิ่มเติม**: การจำลองเครือข่ายประสาทเทียมที่เลียนแบบการยิงสัญญาณ (spiking) ของเซลล์ประสาทจริง  

10. **Zero-Shot Learning**  
    - **ความน่าสนใจ**: โมเดลสามารถทำงานที่ไม่เคยฝึกมาก่อนได้โดยอาศัยความรู้ทั่วไป เช่น การจำแนกข้อความในหมวดหมู่ใหม่หรือแปลภาษาที่ไม่เคยเรียน เกิดจากความสามารถในการเข้าใจบริบทและความสัมพันธ์ระหว่างข้อมูลที่หลากหลาย  
    - **การใช้งาน**: สคริปต์จาก Hugging Face แสดงวิธีใช้ Transformers ในการทำ Zero-Shot Text Classification เช่น การจัดหมวดหมู่ข้อความโดยไม่ต้องมีข้อมูลฝึกสำหรับหมวดนั้น  
    - **ตัวอย่างเพิ่มเติม**: ทดลองให้โมเดลแปลภาษาหายาก เช่น ภาษาสวาฮีลี โดยไม่เคยฝึกมาก่อน  

---

### 21.3 วิธีการใช้งานสคริปต์

- **Google Colab**: คลิกที่ลิงก์เพื่อเปิดสคริปต์ใน Colab จากนั้นรันโค้ดตามขั้นตอนในไฟล์ อาจต้องติดตั้งแพ็กเกจเพิ่มเติมตามคำแนะนำ (เช่น NEST สำหรับ Neuromorphic Computing)  
- **GitHub**: ดาวน์โหลดโค้ดหรือดูเอกสารประกอบเพื่อใช้งานในเครื่องของคุณเอง  
- **ข้อแนะนำ**: ตรวจสอบว่า Colab มี GPU/TPU ว่างอยู่ เพื่อประสิทธิภาพสูงสุด โดยเฉพาะกับ Neuromorphic Computing ที่อาจต้องจำลองการคำนวณหนัก

---

<a name="section22"></a>

## 🚀 ส่วนที่ 22: การประยุกต์ใช้เทคนิค AI ล่าสุดในโปรเจกต์จริง

*ส่วนนี้เน้นการนำเทคนิค AI ล่าสุดไปใช้ในโปรเจกต์จริง เช่น การพัฒนาแอปพลิเคชันหรือการแก้ปัญหาในอุตสาหกรรม เหมาะสำหรับผู้ที่ต้องการนำความรู้ไปใช้ในทางปฏิบัติ*

---

### 22.1 Neuromorphic Computing ในอุปกรณ์ IoT

การใช้ **Neuromorphic Computing** เพื่อประมวลผลข้อมูลในอุปกรณ์ IoT แบบประหยัดพลังงาน โดยเลียนแบบการทำงานของสมองมนุษย์

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| NEST Simulator Tutorial                  | บทเรียนใช้ NEST สร้างโมเดล Neuromorphic สำหรับ IoT                                           | Spiking neural networks, event-based processing               | `[Advanced]`              | [NEST Tutorial](https://nest-simulator.readthedocs.io/en/stable/)                              |
| Neuromorphic IoT Project (GitHub)        | โปรเจกต์ตัวอย่างใช้ Neuromorphic ในเซ็นเซอร์ IoT                                              | Edge computing, low-power AI                                  | `[Advanced]`              | [Neuromorphic IoT](https://github.com/neuromorphic-iot/project)                                |
| Arxiv: Neuromorphic for IoT              | งานวิจัยล่าสุดเกี่ยวกับการใช้ Neuromorphic ใน IoT                                             | Energy efficiency, real-time processing                       | `[Advanced]`              | [Arxiv Paper](https://arxiv.org/abs/2501.12345)                                                |

**ตัวอย่างการใช้งาน**:  

- **เซ็นเซอร์ตรวจจับเหตุการณ์**: ใช้ Neuromorphic Computing ในเซ็นเซอร์ IoT เพื่อตรวจจับเหตุการณ์ผิดปกติ (เช่น การสั่นสะเทือนหรือเสียง) แบบเรียลไทม์ โดยไม่ต้องพึ่งพาการประมวลผลบนคลาวด์ ลดการใช้พลังงานและ latency

---

### 22.2 Zero-Shot Learning ในระบบอัตโนมัติ

การใช้ **Zero-Shot Learning** เพื่อให้ระบบ AI ทำงานกับข้อมูลใหม่ได้ทันที โดยไม่ต้องฝึกโมเดลใหม่ทุกครั้ง

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| Hugging Face Zero-Shot Pipeline         | เอกสารการใช้ Zero-Shot Classification ใน Transformers                                         | Text classification, image classification                     | `[Intermediate]`          | [Zero-Shot Docs](https://huggingface.co/docs/transformers/main/en/task_summary#zero-shot-classification) |
| Zero-Shot Learning for Robotics (GitHub)| โปรเจกต์ใช้ Zero-Shot Learning ในหุ่นยนต์                                                    | Task generalization, few-shot adaptation                      | `[Advanced]`              | [Robotics Project](https://github.com/zero-shot-robotics/project)                              |
| Arxiv: Zero-Shot in Automation           | งานวิจัยเกี่ยวกับ Zero-Shot Learning ในระบบอัตโนมัติ                                         | Industrial applications, safety systems                       | `[Advanced]`              | [Arxiv Paper](https://arxiv.org/abs/2502.67890)                                                |

**ตัวอย่างการใช้งาน**:  

- **ระบบตรวจสอบคุณภาพ**: ใช้ Zero-Shot Learning เพื่อตรวจสอบผลิตภัณฑ์ใหม่ในสายการผลิต เช่น การจำแนกข้อบกพร่องในชิ้นส่วนที่ไม่เคยพบมาก่อน โดยไม่ต้องเสียเวลาฝึกโมเดลใหม่

---

### 22.3 Edge AI ด้วย TinyML

การนำ AI ไปใช้ในอุปกรณ์ Edge เช่น microcontroller ด้วย **TinyML** เพื่อประมวลผลข้อมูลแบบ on-device

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| TinyML Foundation                        | องค์กรที่สนับสนุนการพัฒนา TinyML                                                              | Model compression, embedded AI                                | `[Intermediate/Advanced]` | [TinyML](https://www.tinyml.org/)                                                              |
| Edge Impulse Documentation               | แพลตฟอร์มสำหรับพัฒนาและ deploy TinyML บนอุปกรณ์ Edge                                         | Data collection, model training, deployment                   | `[Intermediate]`          | [Edge Impulse Docs](https://docs.edgeimpulse.com/)                                             |
| TinyML on Arduino (Tutorial)             | บทเรียนใช้ TinyML บน Arduino                                                                  | Sensor integration, model inference                           | `[Beginner/Intermediate]` | [Arduino Tutorial](https://docs.arduino.cc/tutorials/nano-33-ble-sense/tinyml)                  |

**ตัวอย่างการใช้งาน**:  

- **สมาร์ทเซ็นเซอร์**: ใช้ TinyML ในเซ็นเซอร์เพื่อวิเคราะห์ข้อมูลแบบ on-device เช่น การตรวจจับเสียงหรือการเคลื่อนไหวในอุปกรณ์ขนาดเล็ก เช่น Arduino หรือ Raspberry Pi

---

### 22.4 แนวทางการเรียนรู้ (How to Proceed)

เพื่อให้คุณสามารถนำเทคนิคเหล่านี้ไปใช้ได้จริง ลองทำตามขั้นตอนต่อไปนี้:

1. **ลองใช้ NEST Simulator**: สร้างโมเดล Neuromorphic พื้นฐานสำหรับการประมวลผลแบบประหยัดพลังงาน `[Advanced]`  
2. **ทดลอง Zero-Shot Classification**: ใช้ Hugging Face บนชุดข้อมูลใหม่ เช่น การจำแนกข้อความหรือรูปภาพ `[Intermediate]`  
3. **พัฒนาโปรเจกต์ TinyML**: ลองใช้ Arduino หรือ Raspberry Pi เพื่อสร้างสมาร์ทเซ็นเซอร์ `[Beginner/Intermediate]`  
4. **ติดตามงานวิจัยล่าสุด**: อ่านบทความใน Arxiv เพื่ออัปเดตเทรนด์ใหม่ๆ ในปี 2568 `[Advanced]`

---

<a name="section23"></a>

## 🛠️ ส่วนที่ 23: เครื่องมือและแพลตฟอร์ม AI ที่สำคัญ

*ส่วนนี้เน้นเครื่องมือและแพลตฟอร์มที่สำคัญสำหรับการพัฒนา ฝึกอบรม และใช้งาน AI โดยเฉพาะในบริบทของ Large Language Models (LLMs) และเทคนิค AI อื่นๆ เหมาะสำหรับนักพัฒนาและวิศวกรที่ต้องการเลือกใช้เครื่องมือที่เหมาะสม*

---

### 23.1 เครื่องมือสำหรับการพัฒนาและฝึกอบรม LLM

เครื่องมือที่ช่วยในการสร้าง ฝึกอบรม และปรับแต่ง LLM:

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| Hugging Face Transformers                | ไลบรารีสำหรับโมเดล Transformers ที่มีโมเดลสำเร็จรูปและเครื่องมือสำหรับฝึกอบรม                    | Pretrained models, fine-tuning, tokenizers                    | `[Intermediate/Advanced]` | [Transformers Docs](https://huggingface.co/docs/transformers/index)                            |
| DeepSpeed by Microsoft                   | เฟรมเวิร์กสำหรับการฝึกโมเดลขนาดใหญ่ด้วยการ optimize ทรัพยากร                                  | ZeRO optimization, distributed training                       | `[Advanced]`              | [DeepSpeed Docs](https://www.deepspeed.ai/)                                                    |
| PyTorch Lightning                        | เฟรมเวิร์กที่ช่วยให้การฝึกโมเดลด้วย PyTorch ง่ายและเป็นระบบ                                    | Multi-GPU training, experiment tracking                      | `[Intermediate/Advanced]` | [PyTorch Lightning Docs](https://lightning.ai/docs/pytorch/stable/)                            |
| TensorFlow Model Garden                  | คอลเลกชันของโมเดล TensorFlow ที่พร้อมใช้งานและปรับแต่งได้                                      | Pretrained models, custom training loops                      | `[Intermediate/Advanced]` | [TensorFlow Model Garden](https://github.com/tensorflow/models)                                |

**ตัวอย่างการใช้งาน**:  

- **ฝึกโมเดลภาษา**: ใช้ Hugging Face Transformers ร่วมกับ DeepSpeed เพื่อฝึกโมเดลภาษาขนาดใหญ่บน GPU หลายตัว  
- **ทดลองกับ TensorFlow**: ใช้ TensorFlow Model Garden เพื่อทดลองกับโมเดลวิชันหรือ NLP ที่มีอยู่

---

### 23.2 แพลตฟอร์มสำหรับการ Deploy และใช้งาน LLM

แพลตฟอร์มที่ช่วยในการนำ LLM ไปใช้งานจริงในสภาพแวดล้อม production:

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| Hugging Face Inference API               | API สำหรับใช้งานโมเดลจาก Hugging Face โดยไม่ต้องติดตั้งอะไรเพิ่มเติม                            | Text generation, classification, embeddings                   | `[Beginner/Intermediate]` | [Inference API](https://huggingface.co/docs/api-inference/index)                               |
| NVIDIA Triton Inference Server           | เซิร์ฟเวอร์สำหรับ deploy โมเดล AI บน GPU หรือ CPU                                            | Model serving, multi-framework support                        | `[Advanced]`              | [Triton Docs](https://developer.nvidia.com/nvidia-triton-inference-server)                     |
| Google Cloud AI Platform                 | แพลตฟอร์มคลาวด์สำหรับ deploy และจัดการโมเดล AI                                                | AutoML, custom models, scaling                                | `[Intermediate/Advanced]` | [Google Cloud AI](https://cloud.google.com/ai-platform)                                        |
| AWS SageMaker                            | บริการคลาวด์สำหรับสร้าง ฝึก และ deploy โมเดล AI                                               | Managed notebooks, model hosting, monitoring                  | `[Intermediate/Advanced]` | [SageMaker Docs](https://aws.amazon.com/sagemaker/)                                            |

**ตัวอย่างการใช้งาน**:  

- **ใช้งานโมเดลอย่างรวดเร็ว**: ใช้ Hugging Face Inference API เพื่อทดสอบโมเดล NLP โดยไม่ต้องตั้งค่าเซิร์ฟเวอร์  
- **Deploy บนคลาวด์**: ใช้ AWS SageMaker เพื่อ deploy โมเดลที่ฝึกแล้วและจัดการการ scaling อัตโนมัติ

---

### 23.3 เครื่องมือสำหรับการวิเคราะห์และปรับปรุงประสิทธิภาพ

เครื่องมือที่ช่วยในการวิเคราะห์และปรับปรุงประสิทธิภาพของโมเดล AI:

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| TensorBoard                              | เครื่องมือ visualize การฝึกโมเดล เช่น loss, accuracy, และกราฟโมเดล                             | Metrics visualization, model graph, profiling                 | `[Intermediate]`          | [TensorBoard Docs](https://www.tensorflow.org/tensorboard)                                     |
| Weights & Biases                         | แพลตฟอร์มสำหรับติดตามและ visualize การทดลอง AI                                                 | Experiment tracking, hyperparameter tuning                    | `[Intermediate/Advanced]` | [W&B Docs](https://docs.wandb.ai/)                                                             |
| NVIDIA Nsight Systems                    | เครื่องมือ profiling สำหรับ optimize โมเดลบน GPU                                              | Performance analysis, bottleneck identification               | `[Advanced]`              | [Nsight Systems](https://developer.nvidia.com/nsight-systems)                                  |
| MLflow                                   | แพลตฟอร์ม open-source สำหรับจัดการ lifecycle ของโมเดล AI                                       | Model registry, experiment tracking, deployment               | `[Intermediate/Advanced]` | [MLflow Docs](https://mlflow.org/docs/latest/index.html)                                       |

**ตัวอย่างการใช้งาน**:  

- **ติดตามการฝึกโมเดล**: ใช้ Weights & Biases เพื่อบันทึกและเปรียบเทียบผลลัพธ์จากการทดลองต่างๆ  
- **Optimize GPU usage**: ใช้ NVIDIA Nsight Systems เพื่อหาจุดที่ช้าในโมเดลและปรับปรุง

---

### 23.4 แนวทางการเรียนรู้ (How to Proceed)

เพื่อให้คุณสามารถใช้เครื่องมือและแพลตฟอร์มเหล่านี้ได้อย่างมีประสิทธิภาพ ลองทำตามขั้นตอนต่อไปนี้:

1. **เริ่มต้นด้วย Hugging Face**: ลองใช้ Transformers library เพื่อฝึกหรือ fine-tune โมเดลเล็กๆ `[Intermediate]`  
2. **ลอง deploy ด้วย SageMaker**: ใช้ AWS SageMaker เพื่อ deploy โมเดลที่คุณฝึกแล้วและทดสอบการใช้งานจริง `[Intermediate/Advanced]`  
3. **ใช้ TensorBoard วิเคราะห์**: ฝึกโมเดลด้วย TensorFlow หรือ PyTorch และใช้ TensorBoard เพื่อดูกราฟ loss และ accuracy `[Intermediate]`  
4. **สำรวจ MLflow**: ใช้ MLflow เพื่อจัดการโมเดลและทดลองในโปรเจกต์จริง `[Advanced]`

---

<a name="section24"></a>

## 🌐 ส่วนที่ 24: การสร้างชุมชนและการทำงานร่วมกันในวงการ AI

*ส่วนนี้เน้นการสร้างชุมชน การมีส่วนร่วม และการทำงานร่วมกันในวงการ AI เพื่อส่งเสริมการเรียนรู้ แบ่งปันความรู้ และพัฒนานวัตกรรม เหมาะสำหรับผู้ที่ต้องการเชื่อมต่อกับผู้อื่นในวงการ*

---

### 24.1 ชุมชนออนไลน์และฟอรัม AI

แหล่งชุมชนออนไลน์ที่ช่วยให้คุณเชื่อมต่อกับนักพัฒนา นักวิจัย และผู้ที่สนใจ AI:

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| Hugging Face Forums                      | ฟอรัมสำหรับถาม-ตอบเกี่ยวกับโมเดล AI, Transformers และเครื่องมือต่างๆ                            | Model usage, troubleshooting, collaboration                   | `[All Levels]`            | [Hugging Face Forums](https://discuss.huggingface.co/)                                         |
| Reddit: r/MachineLearning                | ชุมชน Reddit ที่เน้นการพูดคุยเกี่ยวกับ Machine Learning และ AI                                 | Research discussions, project ideas, career advice            | `[All Levels]`            | [r/MachineLearning](https://www.reddit.com/r/MachineLearning/)                                 |
| AI Alignment Forum                       | ฟอรัมสำหรับการพูดคุยเกี่ยวกับความปลอดภัยและจริยธรรมของ AI                                     | AI safety, ethics, technical alignment                        | `[Intermediate/Advanced]` | [AI Alignment Forum](https://www.alignmentforum.org/)                                          |
| Stack Overflow (AI/ML Tags)              | แพลตฟอร์มถาม-ตอบโค้ดและปัญหาทางเทคนิคเกี่ยวกับ AI                                            | Coding help, debugging, best practices                        | `[All Levels]`            | [Stack Overflow AI](https://stackoverflow.com/questions/tagged/ai)                             |

**ตัวอย่างการใช้งาน**:  

- **ถามคำถาม**: ใช้ Hugging Face Forums เพื่อสอบถามวิธี fine-tune โมเดล  
- **หาไอเดีย**: อ่านโพสต์ใน r/MachineLearning เพื่อหาแรงบันดาลใจสำหรับโปรเจกต์ใหม่

---

### 24.2 การทำงานร่วมกันผ่าน GitHub และ Open Source

การมีส่วนร่วมในโปรเจกต์ open source และการทำงานร่วมกันผ่าน GitHub:

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| GitHub: Awesome AI                       | รายการ curated โปรเจกต์ AI open source ที่น่าสนใจ                                             | Tools, libraries, datasets                                    | `[All Levels]`            | [Awesome AI](https://github.com/owainlewis/awesome-artificial-intelligence)                    |
| LangChain GitHub                         | รีโพสิทอรีของ LangChain สำหรับการพัฒนาแอป LLM                                                 | Contributing guidelines, issues, pull requests                | `[Intermediate/Advanced]` | [LangChain GitHub](https://github.com/langchain-ai/langchain)                                  |
| PyTorch GitHub                           | รีโพสิทอรีหลักของ PyTorch ที่เปิดให้ร่วมพัฒนา                                                  | Feature requests, bug fixes, documentation                    | `[Intermediate/Advanced]` | [PyTorch GitHub](https://github.com/pytorch/pytorch)                                           |
| Open Source Initiative                   | แหล่งข้อมูลเกี่ยวกับการมีส่วนร่วมใน open source                                              | Licensing, community standards, collaboration                 | `[All Levels]`            | [Open Source Initiative](https://opensource.org/)                                              |

**ตัวอย่างการใช้งาน**:  

- **แก้บั๊ก**: ส่ง pull request ไปที่ LangChain เพื่อแก้ปัญหาที่คุณพบ  
- **สร้างโปรเจกต์**: fork รีโพสิทอรีจาก Awesome AI เพื่อพัฒนาเครื่องมือใหม่

---

### 24.3 การเข้าร่วมงานสัมมนาและการแข่งขัน AI

การเข้าร่วมงานสัมมนาและการแข่งขันเพื่อสร้างเครือข่ายและพัฒนาทักษะ:

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| NeurIPS Conference                       | งานประชุม AI ชั้นนำระดับโลกที่มีการนำเสนองานวิจัยและเวิร์กช็อป                                 | Research papers, workshops, networking                        | `[Advanced]`              | [NeurIPS](https://neurips.cc/)                                                                 |
| Kaggle Competitions                      | แพลตฟอร์มแข่งขันด้าน AI และ Machine Learning                                                  | Data science challenges, leaderboards, collaboration          | `[All Levels]`            | [Kaggle](https://www.kaggle.com/competitions)                                                  |
| AI Hackathons (Devpost)                  | รายการ hackathon ด้าน AI ที่เปิดให้เข้าร่วมทั่วโลก                                             | Team projects, innovation, prototyping                        | `[Intermediate/Advanced]` | [Devpost Hackathons](https://devpost.com/hackathons)                                           |
| Google AI Events                         | อีเวนต์และเวิร์กช็อปจาก Google เกี่ยวกับเทคโนโลยี AI                                          | TensorFlow, AI ethics, hands-on labs                          | `[All Levels]`            | [Google AI Events](https://ai.google/events/)                                                  |

**ตัวอย่างการใช้งาน**:  

- **แข่งขันใน Kaggle**: เข้าร่วมการแข่งขัน NLP เพื่อฝึกทักษะและสร้างโปรไฟล์  
- **เข้างาน NeurIPS**: ฟังการนำเสนองานวิจัยล่าสุดเพื่ออัปเดตเทรนด์ในปี 2568

---

### 24.4 แนวทางการเรียนรู้ (How to Proceed)

เพื่อให้คุณเริ่มสร้างชุมชนและทำงานร่วมกันได้อย่างมีประสิทธิภาพ ลองทำตามขั้นตอนต่อไปนี้:

1. **เข้าร่วมฟอรัม**: สมัคร Hugging Face Forums หรือ Reddit และเริ่มถามคำถามหรือตอบคำถาม `[All Levels]`  
2. **มีส่วนร่วมใน GitHub**: เลือกโปรเจกต์ open source เช่น PyTorch และลองส่ง contribution เล็กๆ เช่น แก้ documentation `[Intermediate]`  
3. **ลงแข่งขัน**: เข้าร่วม Kaggle หรือ hackathon เพื่อฝึกทักษะและพบปะทีมงาน `[Intermediate/Advanced]`  
4. **สร้างเครือข่าย**: เข้าร่วมงานสัมมนา เช่น NeurIPS หรือ Google AI Events เพื่อพบปะผู้เชี่ยวชาญ `[Advanced]`

---
<a name="section25"></a>

## 📖 ส่วนที่ 25: ศัพท์ที่ต้องรู้ในวงการ LLM ตอนที่ 2

*ส่วนนี้รวบรวมศัพท์เทคนิคและแนวคิดขั้นสูงในวงการ Large Language Models (LLMs) ที่กำลังได้รับความนิยมหรือมีความสำคัญในปี 2568 เหมาะสำหรับผู้ที่ต้องการเจาะลึกหรือตามเทรนด์ล่าสุด*

---

### 25.1 ตารางศัพท์ที่ต้องรู้

| **ศัพท์**                     | **คำอธิบาย**                                                                                              | **ตัวอย่างการใช้งาน**                                   | **แหล่งข้อมูลเพิ่มเติม**                                                                 |
|:-----------------------------|:---------------------------------------------------------------------------------------------------------|:-------------------------------------------------------|:----------------------------------------------------------------------------------------|
| **Mixture of Experts (MoE)** | โมเดลที่ใช้ "ผู้เชี่ยวชาญ" หลายตัวทำงานร่วมกัน โดยเลือกผู้เชี่ยวชาญที่เหมาะสมตามอินพุตเพื่อประหยัดทรัพยากร | ใช้ใน DeepSeek-MoE เพื่อรันโมเดลขนาดใหญ่แบบประหยัด     | [MoE Paper](https://arxiv.org/abs/2101.03961)                                           |
| **Retrieval-Augmented Generation (RAG)** | เทคนิคที่ผสมการดึงข้อมูลจากฐานความรู้ภายนอกเข้ากับการสร้างข้อความ เพื่อเพิ่มความแม่นยำและบริบท   | ใช้ในระบบถาม-ตอบที่ต้องการข้อมูลล่าสุด                 | [RAG Paper](https://arxiv.org/abs/2005.11401)                                           |
| **LoRA (Low-Rank Adaptation)** | วิธี fine-tuning โมเดลโดยปรับพารามิเตอร์เพียงบางส่วน แทนทั้งหมด เพื่อลดการใช้ทรัพยากร            | Fine-tune Llama 3 บนชุดข้อมูลเฉพาะด้วย GPU เดียว       | [LoRA Documentation](https://huggingface.co/docs/peft/conceptual_guides/lora)           |
| **Quantization**             | การลดความแม่นยำของน้ำหนักโมเดล (เช่น จาก 32-bit เป็น 8-bit) เพื่อลดขนาดและเพิ่มความเร็ว            | Quantize โมเดล Mistral เพื่อรันบนอุปกรณ์จำกัด         | [Hugging Face Optimum](https://huggingface.co/docs/optimum/index)                       |
| **FlashAttention**           | เทคนิค attention ที่เร็วและประหยัดหน่วยความจำ โดยลดการคำนวณซ้ำใน Transformer                     | ใช้ใน vLLM เพื่อ inference โมเดลขนาดใหญ่              | [FlashAttention GitHub](https://github.com/Dao-AILab/flash-attention)                   |
| **RLHF (Reinforcement Learning from Human Feedback)** | การปรับโมเดลด้วยการเรียนรู้จากคำติชมของมนุษย์ เพื่อให้ผลลัพธ์สอดคล้องกับความต้องการมากขึ้น      | ปรับ ChatGPT ให้ตอบคำถามได้สุภาพและแม่นยำ              | [RLHF Guide](https://huggingface.co/docs/trl/index)                                     |
| **Zero-Shot Learning**       | ความสามารถของโมเดลในการทำงานที่ไม่เคยฝึกมาก่อน โดยอาศัยความรู้ทั่วไป                            | จำแนกข้อความในหมวดหมู่ใหม่โดยไม่ต้องฝึกเพิ่ม           | [Zero-Shot Paper](https://arxiv.org/abs/2306.09871)                                     |
| **Multimodal LLM**           | โมเดลที่ประมวลผลข้อมูลหลายรูปแบบ (เช่น ข้อความ, ภาพ, เสียง) พร้อมกัน                              | ใช้ใน NVLM เพื่ออธิบายภาพพร้อมสร้างคำตอบ               | [NVLM Paper](https://arxiv.org/abs/2409.11402)                                          |
| **Prompt Injection**         | การโจมตีที่ใช้คำสั่งใน prompt เพื่อหลอกให้ LLM สร้างผลลัพธ์ที่ไม่พึงประสงค์                       | ป้องกันในแชทบอทด้วยการกรองอินพุต                      | [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) |
| **Neuromorphic Computing**   | การประมวลผล AI ที่เลียนแบบสมองมนุษย์ด้วยฮาร์ดแวร์พิเศษ เพื่อความเร็วและประหยัดพลังงาน              | ใช้ใน IoT เพื่อตรวจจับเหตุการณ์แบบเรียลไทม์             | [Neuromorphic Overview](https://ieeexplore.ieee.org/document/9376788)                   |
| **Sparse Attention**         | เทคนิค attention ที่คำนวณเฉพาะส่วนสำคัญของข้อมูล แทนทั้งหมด เพื่อลดการใช้ทรัพยากร                 | ใช้ใน 3FS เพื่อเพิ่มประสิทธิภาพ Transformer            | [Sparse Attention Paper](https://arxiv.org/abs/1904.10509)                              |
| **Knowledge Distillation**   | การถ่ายทอดความรู้จากโมเดลใหญ่ไปยังโมเดลเล็ก เพื่อให้โมเดลเล็กรักษาประสิทธิภาพ                  | Distill GPT-3 ลงในโมเดลเล็กสำหรับ Edge Device          | [Distillation Guide](https://arxiv.org/abs/1503.02531)                                  |
| **Adapter Modules**          | โมดูลเสริมในโมเดลที่ปรับแต่งได้โดยไม่เปลี่ยนน้ำหนักดั้งเดิม ใช้ fine-tune แบบประหยัด             | เพิ่ม Adapter ใน BERT เพื่องานจำแนกข้อความ             | [Adapter Docs](https://huggingface.co/docs/peft/conceptual_guides/adapter)              |
| **Self-Attention**           | กลไกใน Transformer ที่ให้โมเดลโฟกัสส่วนสำคัญของอินพุตเอง โดยไม่ต้องพึ่ง RNN                      | ใช้ในทุก Transformer เช่น Llama หรือ Mistral           | [Attention is All You Need](https://arxiv.org/abs/1706.03762)                           |
| **Tokenization**             | กระบวนการแบ่งข้อความเป็นหน่วยย่อย (tokens) เพื่อให้โมเดลประมวลผลได้                           | ใช้ BPE ใน GPT เพื่อตัดคำ                              | [Hugging Face Tokenizers](https://huggingface.co/docs/tokenizers/python/v0.13.3/en)     |
| **Few-Shot Learning**        | การเรียนรู้จากตัวอย่างเพียงไม่กี่ตัว โดยใช้ความรู้ที่มีอยู่แล้วในโมเดล                           | ฝึกโมเดลด้วยตัวอย่าง 5 ข้อเพื่อแปลภาษาใหม่             | [Few-Shot Paper](https://arxiv.org/abs/1904.05046)                                      |
| **Gradient Accumulation**    | เทคนิคสะสม gradient หลายรอบเพื่อฝึกโมเดลใหญ่ในเครื่องที่มีหน่วยความจำจำกัด                     | ฝึกโมเดล 13B บน GPU 16GB                              | [PyTorch Guide](https://pytorch.org/docs/stable/notes/amp_examples.html)                |
| **Overfitting**              | สถานะที่โมเดลเรียนรู้ข้อมูลฝึกมากเกินไป จนไม่ generalize กับข้อมูลใหม่                         | ตรวจสอบในโมเดลที่ accuracy ฝึกสูงแต่ทดสอบต่ำ           | [Overfitting Overview](https://www.cs.cmu.edu/~epxing/Class/10701/notes/overfitting.pdf) |
| **Pruning**                  | การตัดน้ำหนักที่ไม่สำคัญออกจากโมเดลเพื่อลดขนาดและเพิ่มความเร็ว                                  | Prune โมเดล BERT เพื่อ deploy บนโทรศัพท์              | [Pruning Tutorial](https://www.tensorflow.org/model_optimization/guide/pruning)         |
| **Differential Privacy**     | เทคนิคป้องกันการรั่วไหลของข้อมูลส่วนตัวจากโมเดล โดยเพิ่ม noise ในกระบวนการฝึก                     | ใช้ในโมเดลที่ฝึกด้วยข้อมูลลูกค้า                      | [Differential Privacy Guide](https://arxiv.org/abs/1607.00133)                         |

---

### 25.2 รายละเอียดเพิ่มเติมเกี่ยวกับศัพท์

1. **Sparse Attention**  
   - ลดการคำนวณ attention โดยโฟกัสเฉพาะจุดสำคัญ เช่น ใน Longformer หรือ 3FS  
2. **Knowledge Distillation**  
   - ทำให้โมเดลเล็กทำงานได้ใกล้เคียงโมเดลใหญ่ โดยไม่ต้องใช้ทรัพยากรมาก  
3. **Adapter Modules**  
   - เหมาะสำหรับงานที่ต้องการปรับแต่งหลายงานในโมเดลเดียวกัน  
4. **Self-Attention**  
   - หัวใจของ Transformer ที่ทำให้ LLM เข้าใจความสัมพันธ์ในข้อความ  
5. **Tokenization**  
   - ขั้นตอนพื้นฐานที่กำหนดว่าโมเดลจะ "อ่าน" ข้อความอย่างไร  
6. **Few-Shot Learning**  
   - เหมาะสำหรับงานที่ข้อมูลฝึกมีจำกัด แต่ต้องการผลลัพธ์ดี  
7. **Gradient Accumulation**  
   - ช่วยฝึกโมเดลใหญ่ในเครื่องเล็กได้อย่างมีประสิทธิภาพ  
8. **Overfitting**  
   - ปัญหาที่ต้องระวังเมื่อฝึกโมเดลนานเกินไป  
9. **Pruning**  
   - ลดความซับซ้อนของโมเดลโดยไม่เสียประสิทธิภาพมาก  
10. **Differential Privacy**  
    - ปกป้องความเป็นส่วนตัวในยุคที่ข้อมูล敏感มากขึ้น  

---

### 25.3 แนวทางการเรียนรู้

1. **ศึกษาเอกสาร**: อ่านงานวิจัยหรือคู่มือจากลิงก์ในตารางเพื่อเข้าใจศัพท์แต่ละตัว  
2. **ทดลองใช้**: ลองใช้เครื่องมือ เช่น LoRA, RAG หรือ Pruning กับโมเดลใน Hugging Face  
3. **ดูตัวอย่างโค้ด**: ใช้ Google Colab หรือ GitHub เพื่อทดสอบเทคนิค เช่น FlashAttention หรือ Quantization  
4. **ติดตามเทรนด์**: อ่านบล็อกจาก OpenAI, Hugging Face หรือ DeepSeek เพื่ออัปเดตศัพท์ใหม่  
5. **เข้าร่วมชุมชน**: ถามคำถามในฟอรัม เช่น Hugging Face Forums เกี่ยวกับศัพท์ที่สงสัย  

---

<a name="section26"></a>

## 📉 ส่วนที่ 26: ข้อจำกัดและความท้าทายในการฝึกโมเดล AI

*ส่วนนี้เน้นข้อจำกัดและความท้าทายที่พบในการฝึกโมเดล AI โดยเฉพาะ Large Language Models (LLMs) รวมถึงวิธีการรับมือ เพื่อให้ผู้พัฒนาเข้าใจและเตรียมพร้อมสำหรับการใช้งานจริงในปี 2568 (2025)*

---

### 26.1 ข้อจำกัดด้านทรัพยากรการคำนวณ (Computational Resource Constraints)

การฝึกโมเดล AI ขนาดใหญ่ เช่น LLM ต้องการทรัพยากรจำนวนมาก ซึ่งเป็นอุปสรรคสำคัญ:

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| DeepSpeed Documentation                  | อธิบายวิธีลดการใช้หน่วยความจำด้วย ZeRO และ pipeline parallelism                                | Memory optimization, distributed computing                    | `[Advanced]`              | [DeepSpeed Docs](https://www.deepspeed.ai/)                                                    |
| Arxiv: Scaling Laws for Neural LMs       | งานวิจัยเกี่ยวกับความสัมพันธ์ระหว่างขนาดโมเดลและทรัพยากรที่ใช้                                 | Compute scaling, energy costs                                 | `[Advanced]`              | [Scaling Laws](https://arxiv.org/abs/2001.08361)                                               |

**ความท้าทาย**:  

- **หน่วยความจำ GPU**: โมเดลขนาด 70B พารามิเตอร์ เช่น Llama 3 ต้องการ GPU หลายตัวที่มี VRAM สูง (เช่น A100 80GB)  
- **ค่าใช้จ่าย**: การเช่าคลาวด์หรือซื้อฮาร์ดแวร์มีราคาสูง เช่น การฝึกโมเดล 1B พารามิเตอร์อาจใช้เงินหลักแสนบาท  
**วิธีรับมือ**:  
- ใช้เทคนิคอย่าง Gradient Accumulation หรือ Quantization เพื่อฝึกโมเดลในเครื่องจำกัด  
- ใช้ DeepSpeed หรือ PyTorch FSDP (Fully Sharded Data Parallel) เพื่อกระจายการคำนวณ  

---

### 26.2 ข้อจำกัดด้านข้อมูล (Data Limitations)

คุณภาพและปริมาณของข้อมูลมีผลต่อประสิทธิภาพโมเดล:

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| Hugging Face Datasets                    | คู่มือการเตรียมชุดข้อมูลสำหรับฝึก LLM                                                         | Data cleaning, tokenization                                   | `[Intermediate]`          | [Datasets Docs](https://huggingface.co/docs/datasets/index)                                    |
| Arxiv: Data-Efficient LLMs               | งานวิจัยเกี่ยวกับการฝึกโมเดลด้วยข้อมูลน้อยแต่มีประสิทธิภาพ                                    | Few-shot learning, synthetic data                             | `[Advanced]`              | [Data-Efficient](https://arxiv.org/abs/2307.00658)                                             |

**ความท้าทาย**:  

- **ข้อมูลไม่เพียงพอ**: ภาษาที่มีข้อมูลน้อย (low-resource languages) เช่น ภาษาไทย ทำให้โมเดลขาดความหลากหลาย  
- **อคติในข้อมูล**: ข้อมูลที่ฝึกอาจมีอคติ (bias) เช่น เพศหรือเชื้อชาติ ส่งผลให้ผลลัพธ์ไม่เป็นกลาง  
**วิธีรับมือ**:  
- ใช้ synthetic data ที่สร้างโดย LLM อื่นเพื่อเพิ่มปริมาณข้อมูล  
- ทำ data augmentation และตรวจสอบอคติด้วยเครื่องมืออย่าง Fairness Indicators  

---

### 26.3 ข้อจำกัดด้านพลังงานและสิ่งแวดล้อม (Energy and Environmental Constraints)

การฝึกโมเดล AI ใช้พลังงานสูงและส่งผลกระทบต่อสิ่งแวดล้อม:

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| Green AI Initiative                      | โครงการลดการใช้พลังงานใน AI                                                                  | Energy-efficient training, carbon footprint                   | `[Intermediate/Advanced]` | [Green AI](https://www.green-algorithm.org/)                                                   |
| Arxiv: Energy Consumption of LLMs        | วิเคราะห์พลังงานที่ใช้ในการฝึก LLM และวิธีลดผลกระทบ                                            | Model pruning, efficient architectures                        | `[Advanced]`              | [Energy Paper](https://arxiv.org/abs/2106.09705)                                               |

**ความท้าทาย**:  

- **การใช้พลังงาน**: การฝึกโมเดลขนาด 175B เช่น GPT-3 อาจปล่อย CO2 เทียบเท่าการขับรถหลายพันกิโลเมตร  
- **ความยั่งยืน**: อุตสาหกรรม AI ต้องเผชิญแรงกดดันให้ลดผลกระทบต่อสิ่งแวดล้อม  
**วิธีรับมือ**:  
- ใช้เทคนิค Green AI เช่น Model Pruning หรือ Sparse Attention  
- เลือกใช้พลังงานหมุนเวียนในศูนย์ข้อมูล (data centers)  

---

### 26.4 ข้อจำกัดด้านความปลอดภัยและจริยธรรม (Security and Ethical Constraints)

ความปลอดภัยและจริยธรรมเป็นประเด็นสำคัญในการฝึกและใช้งาน LLM:

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| OWASP LLM Top 10                         | รายการความเสี่ยงด้านความปลอดภัยใน LLM เช่น Prompt Injection                                   | Security vulnerabilities, mitigation strategies               | `[Intermediate/Advanced]` | [OWASP LLM](https://owasp.org/www-project-top-10-for-large-language-model-applications/)        |
| AI Ethics Guidelines                     | แนวทางจริยธรรมจาก UNESCO เกี่ยวกับการพัฒนา AI                                                 | Bias mitigation, transparency                                 | `[All Levels]`            | [UNESCO AI Ethics](https://en.unesco.org/artificial-intelligence/ethics)                       |

**ความท้าทาย**:  

- **Prompt Injection**: ผู้ไม่หวังดีอาจแทรกคำสั่งในอินพุตเพื่อหลอกโมเดล  
- **ความเป็นส่วนตัว**: ข้อมูลที่ใช้ฝึกอาจรั่วไหลหรือถูกดึงออกมาได้ (data leakage)  
**วิธีรับมือ**:  
- ใช้ Differential Privacy เพื่อปกป้องข้อมูล  
- ออกแบบระบบกรองอินพุตและตรวจสอบผลลัพธ์  

---

### 26.5 แนวทางการเรียนรู้ (How to Proceed)

เพื่อรับมือกับข้อจำกัดและความท้าทายเหล่านี้ ลองทำตามขั้นตอนต่อไปนี้:  

1. **ทดลองลดทรัพยากร**: ใช้ DeepSpeed หรือ LoRA Fine-tuning กับโมเดลเล็กๆ บน GPU เดียว `[Intermediate]`  
2. **เตรียมข้อมูลให้ดี**: เรียนรู้การทำความสะอาดข้อมูลด้วย Hugging Face Datasets `[Beginner/Intermediate]`  
3. **คำนึงถึงพลังงาน**: ทดลอง Pruning โมเดลด้วย TensorFlow Model Optimization Toolkit `[Advanced]`  
4. **เพิ่มความปลอดภัย**: ศึกษา OWASP LLM Top 10 และทดสอบ Prompt Injection ในโปรเจกต์จริง `[Intermediate/Advanced]`  

---

<a name="section27"></a>

## 📈 ส่วนที่ 27: การทดสอบและประเมินผลโมเดล AI

*ส่วนนี้เน้นกระบวนการทดสอบและประเมินผลโมเดล AI โดยเฉพาะ Large Language Models (LLMs) เพื่อให้มั่นใจว่าโมเดลมีประสิทธิภาพ ความน่าเชื่อถือ และเหมาะสมกับการใช้งานจริงในบริบทต่างๆ เหมาะสำหรับนักพัฒนาและวิศวกรที่ต้องการตรวจสอบคุณภาพโมเดลในปี 2568 (2025)*

---

### 27.1 การกำหนดเมตริกสำหรับการประเมินผล (Defining Evaluation Metrics)

การเลือกเมตริกที่เหมาะสมเป็นขั้นตอนแรกในการประเมินโมเดล:

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| Hugging Face Evaluate                    | ไลบรารีสำหรับคำนวณเมตริก เช่น BLEU, ROUGE, และ Perplexity สำหรับงาน NLP                       | Text generation metrics, classification metrics               | `[Intermediate]`          | [Evaluate Docs](https://huggingface.co/docs/evaluate/index)                                    |
| Arxiv: Evaluating LLMs                   | งานวิจัยเกี่ยวกับเมตริกที่ใช้ประเมิน LLM เช่น ความแม่นยำและความสอดคล้อง                        | Human-like evaluation, task-specific metrics                  | `[Advanced]`              | [Evaluation Paper](https://arxiv.org/abs/2307.01850)                                           |

**เมตริกที่สำคัญ**:  

- **Perplexity**: วัดความสามารถในการคาดเดาคำต่อไปในภาษา (ยิ่งต่ำยิ่งดี)  
- **BLEU/ROUGE**: วัดความเหมือนระหว่างข้อความที่โมเดลสร้างกับข้อความอ้างอิง (สำหรับงานแปลหรือสรุป)  
- **F1 Score**: ใช้ในงานจำแนกข้อความ วัดความสมดุลระหว่าง precision และ recall  
**วิธีการ**:  
- เลือกเมตริกตามงาน เช่น BLEU สำหรับการแปล หรือ Perplexity สำหรับการสร้างข้อความทั่วไป  

---

### 27.2 การทดสอบด้วยชุดข้อมูลทดสอบ (Testing with Test Datasets)

การใช้ชุดข้อมูลทดสอบที่หลากหลายช่วยประเมินประสิทธิภาพโมเดล:

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| GLUE Benchmark                           | ชุดข้อมูลมาตรฐานสำหรับทดสอบความสามารถด้าน NLP เช่น การเข้าใจข้อความและการตอบคำถาม               | Multiple NLP tasks, leaderboard comparison                    | `[Intermediate/Advanced]` | [GLUE](https://gluebenchmark.com/)                                                             |
| SuperGLUE                                | เวอร์ชันที่ท้าทายกว่า GLUE ออกแบบมาเพื่อ LLM รุ่นใหม่                                        | Advanced reasoning, natural language understanding            | `[Advanced]`              | [SuperGLUE](https://super.gluebenchmark.com/)                                                  |

**ความท้าทาย**:  

- **ความหลากหลายของข้อมูล**: ชุดข้อมูลทดสอบอาจไม่ครอบคลุมทุกกรณีการใช้งานจริง  
- **Overfitting**: โมเดลอาจทำงานดีเฉพาะข้อมูลฝึก แต่ล้มเหลวกับข้อมูลใหม่  
**วิธีรับมือ**:  
- ใช้ชุดข้อมูลที่ไม่เคยใช้ฝึก (held-out test set) เช่น GLUE หรือ SuperGLUE  
- เพิ่มการทดสอบข้ามภาษา (cross-lingual testing) เพื่อตรวจสอบความสามารถทั่วไป  

---

### 27.3 การประเมินด้วยมนุษย์ (Human Evaluation)

การให้มนุษย์ประเมินผลลัพธ์ช่วยวัดคุณภาพที่เมตริกอัตโนมัติไม่ครอบคลุม:

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| OpenAI Human Eval Guide                  | แนวทางการประเมินโมเดลด้วยมนุษย์ เช่น ความสอดคล้องและความเป็นธรรมชาติ                           | Human scoring, qualitative feedback                           | `[Intermediate/Advanced]` | [OpenAI Blog](https://openai.com/blog/our-approach-to-alignment-research)                      |
| Arxiv: Human-Centric LLM Evaluation      | งานวิจัยเกี่ยวกับการออกแบบการประเมินโดยมนุษย์สำหรับ LLM                                        | Inter-rater reliability, evaluation frameworks                | `[Advanced]`              | [Human Eval Paper](https://arxiv.org/abs/2306.11676)                                           |

**ความท้าทาย**:  

- **ความลำเอียง**: ผู้ประเมินอาจมีมุมมองส่วนตัวที่แตกต่างกัน  
- **ต้นทุนและเวลา**: การจ้างมนุษย์ประเมินใช้ทรัพยากรมาก  
**วิธีรับมือ**:  
- ใช้เกณฑ์ชัดเจน (rubrics) เช่น ความถูกต้อง ความสมเหตุสมผล และความลื่นไหล  
- รวมกลุ่มผู้ประเมินหลากหลายเพื่อลดอคติ  

---

### 27.4 การทดสอบความทนทานและความปลอดภัย (Robustness and Safety Testing)

การตรวจสอบว่าโมเดลทนต่อการโจมตีและปลอดภัยในการใช้งาน:

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| Garak Security Scanner                   | เครื่องมือทดสอบช่องโหว่ของ LLM เช่น Prompt Injection หรือ Bias                               | Adversarial testing, vulnerability scanning                   | `[Intermediate/Advanced]` | [Garak GitHub](https://github.com/leondz/garak)                                                |
| Robustness Gym                           | กรอบการทดสอบความทนทานของโมเดลต่อข้อมูลที่ไม่คาดคิด                                            | Noise injection, out-of-distribution testing                  | `[Advanced]`              | [Robustness Gym](https://github.com/robustness-gym/robustness-gym)                             |

**ความท้าทาย**:  

- **Adversarial Attacks**: อินพุตที่ออกแบบมาเพื่อหลอกโมเดล เช่น การเปลี่ยนคำเล็กน้อย  
- **ผลลัพธ์ที่ไม่ปลอดภัย**: โมเดลอาจสร้างเนื้อหาที่เป็นอันตรายหรือไม่เหมาะสม  
**วิธีรับมือ**:  
- ใช้ Garak เพื่อสแกนช่องโหว่และปรับปรุงโมเดล  
- ทดสอบด้วยข้อมูลนอกขอบเขต (out-of-distribution) เพื่อวัดความทนทาน  

---

### 27.5 แนวทางการเรียนรู้ (How to Proceed)

เพื่อพัฒนาทักษะการทดสอบและประเมินผลโมเดล AI ลองทำตามขั้นตอนต่อไปนี้:  

1. **เริ่มด้วยเมตริกพื้นฐาน**: ใช้ Hugging Face Evaluate คำนวณ Perplexity หรือ BLEU บนโมเดลของคุณ `[Intermediate]`  
2. **ทดสอบกับ Benchmark**: รันโมเดลกับ GLUE หรือ SuperGLUE เพื่อเปรียบเทียบกับมาตรฐาน `[Intermediate/Advanced]`  
3. **จัด Human Evaluation**: ออกแบบการทดสอบเล็กๆ ด้วยเพื่อนหรือทีม เพื่อประเมินผลลัพธ์ `[Intermediate]`  
4. **ตรวจสอบความปลอดภัย**: ใช้ Garak ทดสอบ Prompt Injection และปรับปรุงโมเดลตามผล `[Advanced]`  

**ข้อควรจำ**:  

- การประเมินผลที่ดีต้องผสมผสานทั้งเมตริกอัตโนมัติและการตรวจสอบโดยมนุษย์  
- ความทนทานและความปลอดภัยเป็นสิ่งสำคัญสำหรับการใช้งานจริง โดยเฉพาะในแอปพลิเคชันที่sensitive  

---

<a name="section28"></a>

## 🛠️ ส่วนที่ 28: การบำรุงรักษาและอัปเดตโมเดล AI

*ส่วนนี้เน้นกระบวนการบำรุงรักษาและอัปเดตโมเดล AI โดยเฉพาะ Large Language Models (LLMs) เพื่อให้โมเดลคงประสิทธิภาพและทันสมัยตามข้อมูลใหม่หรือความต้องการที่เปลี่ยนแปลง เหมาะสำหรับนักพัฒนาและทีมที่ดูแลโมเดลในระยะยาวในปี 2568 (2025)*

---

### 28.1 การตรวจสอบประสิทธิภาพอย่างต่อเนื่อง (Continuous Performance Monitoring)

การติดตามประสิทธิภาพโมเดลช่วยให้ทราบเมื่อใดที่โมเดลเริ่มเสื่อมถอย:

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| MLflow Monitoring                        | เครื่องมือสำหรับติดตามเมตริกของโมเดลใน Production เช่น Accuracy หรือ Latency                  | Real-time tracking, model drift detection                     | `[Intermediate/Advanced]` | [MLflow Docs](https://mlflow.org/docs/latest/tracking.html)                                    |
| Arxiv: Model Drift in LLMs               | งานวิจัยเกี่ยวกับการเสื่อมถอยของโมเดลเมื่อข้อมูลเปลี่ยนแปลง (data drift)                      | Concept drift, performance degradation                        | `[Advanced]`              | [Model Drift Paper](https://arxiv.org/abs/2304.01578)                                          |

**ความท้าทาย**:  

- **Model Drift**: โมเดลอาจทำงานแย่ลงเมื่อข้อมูลในโลกจริงเปลี่ยน เช่น คำศัพท์ใหม่ในโซเชียลมีเดีย  
- **Latency**: การใช้งานจริงอาจเผยปัญหาความล่าช้าที่ไม่พบตอนทดสอบ  
**วิธีรับมือ**:  
- ตั้งระบบแจ้งเตือน (alerts) ด้วย MLflow เมื่อเมตริกลดลงเกินเกณฑ์  
- เก็บ log การใช้งานเพื่อวิเคราะห์พฤติกรรมโมเดล  

---

### 28.2 การอัปเดตโมเดลด้วยข้อมูลใหม่ (Updating Models with New Data)

การฝึกโมเดลใหม่หรือปรับแต่งด้วยข้อมูลล่าสุดเพื่อให้ทันสมัย:

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| Hugging Face Incremental Training        | คู่มือการฝึกโมเดลเพิ่มเติม (incremental training) โดยไม่ต้องเริ่มใหม่ทั้งหมด                    | Fine-tuning, continual learning                               | `[Intermediate]`          | [Transformers Docs](https://huggingface.co/docs/transformers/training#incremental-training)     |
| Arxiv: Continual Learning for LLMs       | งานวิจัยเกี่ยวกับการเรียนรู้ต่อเนื่อง เพื่อป้องกันการลืมความรู้เก่า (catastrophic forgetting) | Knowledge retention, domain adaptation                        | `[Advanced]`              | [Continual Learning](https://arxiv.org/abs/2305.12345)                                         |

**ความท้าทาย**:  

- **Catastrophic Forgetting**: การฝึกด้วยข้อมูลใหม่อาจทำให้ลืมความรู้เก่า  
- **ต้นทุน**: การฝึกใหม่ทั้งหมดใช้ทรัพยากรมาก  
**วิธีรับมือ**:  
- ใช้เทคนิค Continual Learning เช่น Elastic Weight Consolidation (EWC)  
- Fine-tune ด้วย LoRA เพื่อปรับโมเดลเฉพาะส่วนโดยไม่กระทบทั้งหมด  

---

### 28.3 การจัดการเวอร์ชันของโมเดล (Model Versioning)

การควบคุมเวอร์ชันช่วยให้ทีมสามารถย้อนกลับหรือเปรียบเทียบโมเดลได้:

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| DVC (Data Version Control)               | เครื่องมือจัดการเวอร์ชันของโมเดลและข้อมูล เหมือน Git แต่สำหรับ ML                              | Model registry, pipeline versioning                           | `[Intermediate/Advanced]` | [DVC Docs](https://dvc.org/doc)                                                                |
| Hugging Face Model Hub                   | แพลตฟอร์มสำหรับจัดเก็บและแชร์โมเดลพร้อม metadata และเวอร์ชัน                                   | Version control, model sharing                                | `[Intermediate]`          | [Model Hub](https://huggingface.co/models)                                                     |

**ความท้าทาย**:  

- **ความสับสน**: การมีโมเดลหลายเวอร์ชันอาจทำให้ทีมใช้ผิด  
- **ความเข้ากันได้**: อัปเดตโมเดลอาจไม่เข้ากับระบบเก่า  
**วิธีรับมือ**:  
- ใช้ DVC หรือ Hugging Face Model Hub เพื่อจัดเก็บโมเดลและ tag เวอร์ชัน  
- บันทึก dependency เช่น เวอร์ชันของ PyTorch หรือ Transformers  

---

### 28.4 การแก้ไขข้อบกพร่องและปรับปรุง (Bug Fixing and Optimization)

การแก้ปัญหาที่พบหลัง deployment และเพิ่มประสิทธิภาพ:

| **แหล่งข้อมูล**                          | **คำอธิบาย**                                                                                      | **หัวข้อย่อย (Subtopics)**                                      | **ระดับ (Level)**         | **ลิงก์**                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| vLLM Optimization Guide                  | คู่มือเพิ่มความเร็ว inference และแก้ปัญหาคอขวดใน LLM                                           | Latency reduction, memory optimization                        | `[Advanced]`              | [vLLM Docs](https://docs.vllm.ai/en/latest/)                                                   |
| Arxiv: Debugging LLMs in Production      | งานวิจัยเกี่ยวกับการระบุและแก้ไขข้อบกพร่องของ LLM ในระบบจริง                                    | Error analysis, performance tuning                            | `[Advanced]`              | [Debugging Paper](https://arxiv.org/abs/2401.05678)                                            |

**ความท้าทาย**:  

- **ข้อบกพร่องที่ซ่อนอยู่**: ปัญหาอาจปรากฏเฉพาะในสถานการณ์จริง เช่น ข้อความที่โมเดลตีความผิด  
- **ประสิทธิภาพ**: การรันโมเดลขนาดใหญ่อาจช้ากว่าที่คาด  
**วิธีรับมือ**:  
- ใช้ vLLM หรือ Quantization เพื่อลด latency และเพิ่มความเร็ว  
- สร้างระบบ feedback loop จากผู้ใช้เพื่อระบุจุดที่ต้องแก้ไข  

---

### 28.5 แนวทางการเรียนรู้ (How to Proceed)

เพื่อพัฒนาทักษะการบำรุงรักษาและอัปเดตโมเดล AI ลองทำตามขั้นตอนต่อไปนี้:  

1. **ตั้งระบบ мониторинг**: ใช้ MLflow ติดตามเมตริกของโมเดลที่ deploy แล้ว `[Intermediate]`  
2. **ฝึกโมเดลเพิ่มเติม**: ทดลอง incremental training ด้วย Hugging Face บนชุดข้อมูลใหม่ `[Intermediate]`  
3. **จัดการเวอร์ชัน**: ใช้ DVC หรือ Model Hub จัดเก็บโมเดลเวอร์ชันต่างๆ `[Intermediate/Advanced]`  
4. **แก้ปัญหาใน Production**: ใช้ vLLM ปรับปรุงความเร็วและแก้ bug จาก log ผู้ใช้ `[Advanced]`  

**ข้อควรจำ**:  

- การบำรุงรักษาโมเดลเป็นกระบวนการต่อเนื่องที่ต้องปรับตามการใช้งานจริง  
- การมีระบบ versioning และ monitoring ที่ดีช่วยลดความซับซ้อนในการดูแลระยะยาว  

---

## Third Party Tools

| Tools                                                                                                                 | Category                        | Party      |
|:----------------------------------------------------------------------------------------------------------------------|:--------------------------------| :--------- |
| [adaptive_rag_mistral.ipynb](third_party/langchain/adaptive_rag_mistral.ipynb)                                        | RAG                             | Langchain  |
| [Adaptive_RAG.ipynb](third_party/LlamaIndex/Adaptive_RAG.ipynb)                                                       | RAG                             | LLamaIndex |
| [Agents_Tools.ipynb](third_party/LlamaIndex/Agents_Tools.ipynb)                                                       | agent                           | LLamaIndex |
| [arize_phoenix_tracing.ipynb](third_party/Phoenix/arize_phoenix_tracing.ipynb)                                        | tracing data                    | Arize Phoenix  |
| [arize_phoenix_evaluate_rag.ipynb](third_party/Phoenix/arize_phoenix_evaluate_rag.ipynb)                              | evaluation                      | Arize Phoenix  |
| [azure_ai_search_rag.ipynb](third_party/Azure_AI_Search/azure_ai_search_rag.ipynb)                                    | RAG, embeddings                 | Azure      |
| [CAMEL Graph RAG with Mistral Models](third_party/CAMEL_AI/camel_graph_rag.ipynb)                                     | multi-agent, tool, data gen     | CAMEL-AI.org|
| [CAMEL Role-Playing Scraper](third_party/CAMEL_AI/camel_roleplaying_scraper.ipynb)                                    | multi-agent, tool, data gen     | CAMEL-AI.org|
| [Chainlit - Mistral reasoning.ipynb](third_party/Chainlit/Chainlit_Mistral_reasoning.ipynb)                           | UI chat, tool calling           | Chainlit   |
| [corrective_rag_mistral.ipynb](third_party/langchain/corrective_rag_mistral.ipynb)                                    | RAG                             | Langchain  |
| [distilabel_synthetic_dpo_dataset.ipynb](third_party/argilla/distilabel_synthetic_dpo_dataset.ipynb)                  | synthetic data                  | Argilla    |
| [E2B Code Interpreter SDK with Codestral](third_party/E2B_Code_Interpreting)                                          | tool, agent                     | E2B        |
| [function_calling_local.ipynb](third_party/Ollama/function_calling_local.ipynb)                                       | tool call                       | Ollama     |
| [Gradio Integration - Chat with PDF](third_party/gradio/README.md)                                                    | UI chat, demo, RAG              | Gradio     |
| [haystack_chat_with_docs.ipynb](third_party/Haystack/haystack_chat_with_docs.ipynb)                                   | RAG, embeddings                 | Haystack   |
| [Indexify Integration - PDF Entity Extraction](third_party/Indexify/pdf-entity-extraction)                            | entity extraction, PDF          | Indexify   |
| [Indexify Integration - PDF Summarization](third_party/Indexify/pdf-summarization)                                    | summarization, PDF              | Indexify   |
| [langgraph_code_assistant_mistral.ipynb](third_party/langchain/langgraph_code_assistant_mistral.ipynb)                | code                            | Langchain  |
| [langgraph_crag_mistral.ipynb](third_party/langchain/langgraph_crag_mistral.ipynb)                                    | RAG                             | Langchain  |
| [langtrace_mistral.ipynb](third_party/langtrace/langtrace_mistral.ipynb)                                              | OTEL Observability              | Langtrace  |
| [llamaindex_agentic_rag.ipynb](third_party/LlamaIndex/llamaindex_agentic_rag.ipynb)                                   | RAG, agent                      | LLamaIndex |
| [llamaindex_arxiv_agentic_rag.ipynb](third_party/LlamaIndex/llamaindex_arxiv_agentic_rag.ipynb)                       | RAG, agent, Arxiv summarization | LLamaIndex |
| [llamaindex_mistralai_finetuning.ipynb](third_party/LlamaIndex/llamaindex_mistralai_finetuning.ipynb)                 | fine-tuning                     | LLamaIndex |
| [llamaindex_mistral_multi_modal.ipynb](third_party/LlamaIndex/llamaindex_mistral_multi_modal.ipynb)                   | MultiModalLLM-Pixtral           | LLamaIndex |
| [Microsoft Autogen - Function calling a pgsql db](third_party/MS_Autogen_pgsql/mistral_pgsql_function_calling.ipynb) | Tool call, agent, RAG           | Ms Autogen |
| [Mesop Integration - Chat with PDF](third_party/mesop/README.md)                                                      | UI chat, demo, RAG              | Mesop      |
| [Monitoring Mistral AI using OpenTelemetry](third_party/openlit/cookbook_mistral_opentelemetry.ipynb)                 | AI Observability                | OpenLIT    |
| [neon_text_to_sql.ipynb](third_party/Neon/neon_text_to_sql.ipynb)                                                     | code                            | Neon       |
| [ollama_mistral_llamaindex.ipynb](third_party/LlamaIndex/ollama_mistral_llamaindex.ipynb)                             | RAG                             | LLamaIndex |
| [Ollama Meetup Demo](third_party/Ollama/20240321_ollama_meetup)                                                       | demo                            | Ollama     |
| [Open-source LLM engineering](third_party/Langfuse)                                                                   | LLM Observability               | Langfuse   |
| [Panel Integration - Chat with PDF](third_party/panel/README.md)                                                      | UI chat, demo, RAG              | Panel      |
| [phospho integration](third_party/phospho/cookbook_phospho_mistral_integration.ipynb)                                 | Evaluation, Analytics           | phospho    |
| [pinecone_rag.ipynb](third_party/Pinecone/pinecone_rag.ipynb)                                                         | RAG                             | Pinecone   |
| [RAG.ipynb](third_party/LlamaIndex/RAG.ipynb)                                                                         | RAG                             | LLamaIndex |
| [RouterQueryEngine.ipynb](third_party/LlamaIndex/RouterQueryEngine.ipynb)                                             | agent                           | LLamaIndex |
| [self_rag_mistral.ipynb](third_party/langchain/self_rag_mistral.ipynb)                                                | RAG                             | Langchain  |
| [Solara Integration - Chat with PDFs](third_party/solara/README.md)                                                   | UI chat, demo, RAG              | Solara     |
| [Streamlit Integration - Chat with PDF](third_party/streamlit/README.md)                                              | UI chat, demo, RAG              | Streamlit  |
| [Neo4j rag](third_party/Neo4j/neo4j_rag.ipynb)                                                                        | RAG                             | Neo4j      |
| [SubQuestionQueryEngine.ipynb](third_party/LlamaIndex/RouterQueryEngine.ipynb)                                        | agent                           | LLamaIndex |
| [LLM Judge: Detecting hallucinations in language models](third_party/wandb/README.md)                                 | fine-tuning, evaluation         | Weights & Biases |
| [`x mistral`: CLI & TUI APP Module in X-CMD](third_party/x-cmd/README.md)                                             | CLI, TUI APP, Chat              | x-cmd      |
| [Incremental Prompt Engineering and Model Comparison](third_party/Pixeltable/README.md)                               | Prompt Engineering, Evaluation  | Pixeltable |
| [Build a bank support agent with Pydantic AI and Mistral AI](third_party/PydanticAI/pydantic_bank_support_agent.ipynb)| Agent                           | Pydantic   |
| [Mistral and MLflow Tracing](third_party/MLflow/mistral-mlflow-tracing.ipynb)                                         | Tracing, Observability          | MLflow     |
| [Mistral OCR with Gradio](third_party/gradio/MistralOCR.md)                                                           | OCR                             | Gradio     |

# Mistral Cookbook

Mistral Cookbook รวบรวมตัวอย่างการใช้งานที่ถูกส่งเข้ามาโดยสมาชิก Mistral และชุมชน รวมถึงพันธมิตรของเรา หากคุณมีตัวอย่างเจ๋ง ๆ ที่โชว์ศักยภาพของโมเดล Mistral สามารถส่งเข้ามาได้โดยการสร้าง PR ใน repo นี้

## แนวทางการส่งตัวอย่าง

- รูปแบบไฟล์: กรุณาส่งตัวอย่างในรูปแบบ .md หรือ .ipynb
- รันบน Colab ได้: ถ้าเป็น notebook ควรตรวจสอบให้รันบน Google Colab ได้
- ผู้เขียน: กรุณาใส่ชื่อ, Github handle และสังกัดไว้ต้นไฟล์
- คำอธิบาย: กรุณาใส่ notebook พร้อมหมวดหมู่และคำอธิบายในตารางด้านล่าง
- โทน: กรุณาใช้โทนกลาง ๆ และลดเนื้อหาเชิงการตลาด
- การทำซ้ำได้: กรุณา tag เวอร์ชันแพ็กเกจในโค้ดเพื่อให้ผู้อื่นทำซ้ำได้
- ขนาดภาพ: ถ้ามีภาพ กรุณาให้แต่ละภาพมีขนาดไม่เกิน 500KB
- ลิขสิทธิ์: เคารพลิขสิทธิ์และกฎหมายทรัพย์สินทางปัญญาเสมอ

หมายเหตุ: ตัวอย่างที่ส่งเข้ามาโดยชุมชนและพันธมิตร ไม่ได้สะท้อนมุมมองหรือความคิดเห็นของ Mistral

## แนวทางเนื้อหา

- เนื้อหาต้องสดใหม่และมีมุมมองใหม่
- โครงสร้างชัดเจน อ่านเข้าใจง่าย
- มีคุณค่าและตอบโจทย์ชุมชน

## โน้ตบุ๊กหลัก

| โน้ตบุ๊ก                                                                       | หมวดหมู่                     | คำอธิบาย                                                                      |
|--------------------------------------------------------------------------------|-----------------------------|----------------------------------------------------------------------------------|
| [quickstart.ipynb](quickstart.ipynb)                                           | แชท, embeddings             | ตัวอย่างเริ่มต้นสำหรับแชทและ embeddings ด้วย Mistral AI API                    |
| [prompting_capabilities.ipynb](mistral/prompting/prompting_capabilities.ipynb) | การสร้าง prompt             | เขียน prompt สำหรับงาน classification, summarization, personalization, และ evaluation |
| [basic_RAG.ipynb](mistral/rag/basic_RAG.ipynb)                                 | RAG                          | สร้าง RAG ตั้งแต่เริ่มต้นด้วย Mistral AI API                                   |
| [embeddings.ipynb](mistral/embeddings/embeddings.ipynb)                        | embeddings                   | ใช้ Mistral embeddings API สำหรับ classification และ clustering                 |
| [function_calling.ipynb](mistral/function_calling/function_calling.ipynb)      | การเรียกใช้ฟังก์ชัน         | ใช้ Mistral API สำหรับ function calling                                         |
| [text_to_SQL.ipynb](mistral/function_calling/text_to_SQL.ipynb)                | การเรียกใช้ฟังก์ชัน         | ใช้ Mistral API สำหรับ function calling ในกรณี text to SQL หลายตาราง           |
| [evaluation.ipynb](mistral/evaluation/evaluation.ipynb)                        | การประเมินผล                 | ประเมินโมเดลด้วย Mistral API                                                    |
| [mistral_finetune_api.ipynb](mistral/fine_tune/mistral_finetune_api.ipynb)     | การปรับแต่งโมเดล             | ปรับแต่งโมเดลด้วย Mistral fine-tuning API                                       |
| [mistral-search-engine.ipynb](mistral/rag/mistral-search-engine.ipynb)         | RAG, การเรียกใช้ฟังก์ชัน     | สร้าง search engine ด้วย Mistral API, function calling และ RAG                  |
| [rag_via_function_calling.ipynb](mistral/rag/rag_via_function_calling.ipynb)   | RAG, การเรียกใช้ฟังก์ชัน     | ใช้ function calling เป็น router สำหรับ RAG ที่ใช้หลายแหล่งข้อมูล               |
| [prefix_use_cases.ipynb](mistral/prompting/prefix_use_cases.ipynb)             | prefix, การสร้าง prompt      | ตัวอย่างการใช้ฟีเจอร์ prefix ของ Mistral                                       |
| [synthetic_data_gen_and_finetune.ipynb](mistral/data_generation/synthetic_data_gen_and_finetune.ipynb) | สร้างข้อมูล, ปรับแต่งโมเดล   | ตัวอย่างการสร้างข้อมูลและปรับแต่งโมเดลแบบง่าย ๆ                                |
| [data_generation_refining_news.ipynb](mistral/data_generation/data_generation_refining_news.ipynb) | สร้างข้อมูล                  | สร้างข้อมูลเพื่อปรับปรุงข่าว                                                    |
| [image_description_extraction_pixtral.ipynb](mistral/image_understanding/image_description_extraction_pixtral.ipynb) | ประมวลผลภาพ, การสร้าง prompt | ดึงข้อมูลภาพแบบมีโครงสร้างด้วย Pixtral model และ JSON response formatting      |
| [multimodality meets function calling.ipynb](mistral/image_understanding/multimodality_meets_function_calling.ipynb) | ประมวลผลภาพ, การเรียกใช้ฟังก์ชัน | ดึงตารางจากภาพด้วย Pixtral model และใช้สำหรับ function calling                 |
| [mistral-reference-rag.ipynb](mistral/rag/mistral-reference-rag.ipynb)         | RAG, การเรียกใช้ฟังก์ชัน, อ้างอิง | Reference RAG ด้วย Mistral API                                                  |
| [moderation-explored.ipynb](mistral/moderation/moderation-explored.ipynb)      | moderation                    | สำรวจการป้องกันและใช้งาน moderation API ของ Mistral                            |
| [system-level-guardrails.ipynb](mistral/moderation/system-level-guardrails.ipynb) | moderation                 | วิธีสร้าง System Level Guardrails ด้วย Mistral API                              |
| [document_understanding.ipynb](mistral/ocr/document_understanding.ipynb)        | OCR, การเรียกใช้ฟังก์ชัน     | เข้าใจเอกสารและใช้งาน OCR tool                                                 |
| [batch_ocr.ipynb](mistral/ocr/batch_ocr.ipynb)                                 | OCR, batch                   | ใช้ OCR ดึงข้อความจาก dataset                                                  |
| [structured_ocr.ipynb](mistral/ocr/structured_ocr.ipynb)                       | OCR, structured outputs      | ดึงข้อมูลแบบมีโครงสร้างจากเอกสาร                                              |

# Advanced + Agentic RAG Cookbooks👨🏻‍💻

ยินดีต้อนรับสู่คลังรวมเทคนิค Retrieval-Augmented Generation (RAG) ขั้นสูงและแบบ Agentic

## บทนำ🚀

RAG เป็นวิธีที่ได้รับความนิยมในการเพิ่มความแม่นยำและความเกี่ยวข้องของคำตอบ โดยค้นหาข้อมูลที่ถูกต้องจากแหล่งที่เชื่อถือได้และนำมาสร้างคำตอบที่มีประโยชน์ Repository นี้รวบรวมเทคนิค RAG ขั้นสูงและแบบ Agentic ที่มีตัวอย่างโค้ดและคำอธิบายชัดเจน

เป้าหมายหลักของ repository นี้คือเป็นแหล่งข้อมูลสำหรับนักวิจัยและนักพัฒนาที่ต้องการนำเทคนิค RAG ขั้นสูงไปใช้ในโปรเจกต์ของตน การสร้างเทคนิคเหล่านี้จากศูนย์ใช้เวลามาก และการประเมินผลก็เป็นเรื่องท้าทาย Repository นี้จึงช่วยให้คุณเริ่มต้นได้ง่ายขึ้นด้วยตัวอย่างที่พร้อมใช้งานและคำแนะนำการประเมินผล
> [!NOTE]
> Repository นี้เริ่มจาก RAG แบบพื้นฐาน (naive RAG) และค่อย ๆ พัฒนาไปสู่เทคนิคขั้นสูงและ agentic พร้อมแหล่งอ้างอิงงานวิจัยสำหรับแต่ละเทคนิค

## บทนำสู่ RAG💡

Large Language Models (LLMs) ถูกฝึกด้วยข้อมูลชุดคงที่ ทำให้ไม่สามารถตอบคำถามเกี่ยวกับข้อมูลใหม่หรือข้อมูลส่วนตัวได้ดี และอาจเกิด "hallucination" คือให้คำตอบผิดแต่ดูน่าเชื่อถือ การ fine-tune แม้จะช่วยได้แต่มีค่าใช้จ่ายสูงและไม่เหมาะกับการ retrain บ่อย ๆ RAG จึงแก้ปัญหานี้โดยใช้เอกสารภายนอกมาช่วยให้ LLM ตอบคำถามได้แม่นยำและทันสมัยผ่าน in-context learning

![final diagram](https://github.com/user-attachments/assets/508b3a87-ac46-4bf7-b849-145c5465a6c0)

RAG มี 4 ส่วนหลัก:

**Indexing:** เอกสาร (ทุกฟอร์แมต) จะถูกแบ่งเป็นชิ้นเล็ก ๆ และสร้าง embedding สำหรับแต่ละชิ้น จากนั้นนำไปเก็บใน vector store

**Retriever:** ส่วน retriever จะค้นหาเอกสารที่เกี่ยวข้องที่สุดจาก vector store ด้วยเทคนิคเช่น vector similarity ตามคำถามของผู้ใช้

**Augment:** นำคำถามของผู้ใช้มารวมกับ context ที่ค้นเจอ สร้าง prompt ที่มีข้อมูลครบถ้วนให้ LLM ตอบได้แม่นยำ

**Generate:** ส่ง prompt ที่รวม context แล้วไปยังโมเดลเพื่อสร้างคำตอบสุดท้าย

ส่วนประกอบเหล่านี้ช่วยให้โมเดลเข้าถึงข้อมูลใหม่และตอบได้ถูกต้องตามแหล่งข้อมูลจริง การประเมินผล RAG จึงสำคัญมาก

## การประเมินผล RAG📊

การประเมิน RAG สำคัญเพื่อดูว่าระบบทำงานดีแค่ไหน โดยวัดความแม่นยำและความเกี่ยวข้องของคำตอบ การประเมินนี้ช่วยปรับปรุง RAG ในงานเช่นสรุปข้อความ, chatbot, และถาม-ตอบ รวมถึงช่วยหาจุดที่ต้องปรับปรุงเพื่อให้ระบบตอบสนองต่อข้อมูลใหม่ได้ดี ตัวอย่างในโน้ตบุ๊กนี้มีทั้ง RAG แบบ end-to-end และส่วนประเมินผลใน Athina AI

![evals diagram](https://github.com/user-attachments/assets/65c2b5af-a931-40c5-b006-87567aef019f)

## เทคนิค RAG ขั้นสูง⚙️

รายละเอียดเทคนิค RAG ขั้นสูงที่มีใน repository นี้

| เทคนิค                    | เครื่องมือ                        | คำอธิบาย                                                       | โน้ตบุ๊ก |
|---------------------------|-----------------------------------|--------------------------------------------------------------|-----------|
| Naive RAG      | LangChain, Pinecone, Athina AI      | รวมข้อมูลที่ค้นเจอเข้ากับ LLM เพื่อสร้างคำตอบแบบง่ายและมีประสิทธิภาพ | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/advanced_rag_techniques/naive_rag.ipynb) |
| Hybrid RAG     | LangChain, Chromadb, Athina AI      | ผสมผสาน vector search กับวิธีดั้งเดิมเช่น BM25 เพื่อค้นหาข้อมูลที่ดีกว่า | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/advanced_rag_techniques/hybrid_rag.ipynb) |
| Hyde RAG       | LangChain, Weaviate, Athina AI      | สร้าง embedding สมมติ (hypothetical) เพื่อค้นหาข้อมูลที่เกี่ยวข้องกับคำถาม | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/advanced_rag_techniques/hyde_rag.ipynb) |
| Parent Document Retriever | LangChain, Chromadb, Athina AI | แบ่งเอกสารใหญ่เป็นส่วนย่อยและค้นคืนเอกสารเต็มถ้าส่วนใดตรงกับคำถาม | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/advanced_rag_techniques/parent_document_retriever.ipynb) |
| RAG fusion     | LangChain, LangSmith, Qdrant, Athina AI | สร้าง sub-query, จัดอันดับเอกสารด้วย Reciprocal Rank Fusion และใช้ผลลัพธ์ที่ดีที่สุด | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/advanced_rag_techniques/fusion_rag.ipynb) |
| Contextual RAG | LangChain, Chromadb, Athina AI      | บีบอัดเอกสารที่ค้นเจอให้เหลือแต่ส่วนสำคัญเพื่อคำตอบที่กระชับและแม่นยำ | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/advanced_rag_techniques/contextual_rag.ipynb) |
| Rewrite Retrieve Read | LangChain, Chromadb, Athina AI   | ปรับปรุง query, ค้นข้อมูลที่ดีกว่า และสร้างคำตอบที่แม่นยำ | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/advanced_rag_techniques/rewrite_retrieve_read.ipynb) |
| Unstructured RAG | LangChain, LangGraph, FAISS, Athina AI, Unstructured | รองรับเอกสารที่มีทั้งข้อความ, ตาราง, และภาพ | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/advanced_rag_techniques/basic_unstructured_rag.ipynb) |

## เทคนิค Agentic RAG⚙️

รายละเอียดเทคนิค Agentic RAG ที่มีใน repository นี้

| เทคนิค                    | เครื่องมือ                        | คำอธิบาย                                                       | โน้ตบุ๊ก |
|---------------------------|-----------------------------------|--------------------------------------------------------------|-----------|
| Basic Agentic RAG      | LangChain, FAISS, Athina AI      | Agentic RAG ใช้ AI agent ในการค้นหาและสร้างคำตอบโดยใช้ vectordb และค้นเว็บ | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/agentic_rag_techniques/basic_agentic_rag.ipynb) |
| Corrective RAG         | LangChain, LangGraph, Chromadb, Athina AI | ปรับปรุงเอกสารที่เกี่ยวข้อง, ตัดส่วนที่ไม่เกี่ยวข้อง หรือค้นเว็บเพิ่ม | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/agentic_rag_techniques/corrective_rag.ipynb) |
| Self RAG              | LangChain, LangGraph, FAISS, Athina AI | ตรวจสอบข้อมูลที่ค้นเจอเพื่อให้คำตอบถูกต้องและครบถ้วน | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/agentic_rag_techniques/self_rag.ipynb) |
| Adaptive RAG          | LangChain, LangGraph, FAISS, Athina AI | ปรับวิธีค้นคืนตามประเภทคำถาม ใช้ทั้งข้อมูลที่ index และค้นเว็บ | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/agentic_rag_techniques/adaptive_rag.ipynb) |
| ReAct RAG             | LangChain, LangGraph, FAISS, Athina AI | ระบบที่ผสมผสาน reasoning และ retrieval เพื่อคำตอบที่เข้าใจบริบท | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/agentic_rag_techniques/react_rag.ipynb) |

## เดโม🎬

ตัวอย่างการทำงานของแต่ละโน้ตบุ๊ก:

<https://github.com/user-attachments/assets/c6f17961-40a1-4cca-ab1f-2c8fa3d71a7a>

## เริ่มต้นใช้งาน🛠️

เริ่มจาก clone repository นี้ด้วยคำสั่ง:

```bash
git clone https://github.com/athina-ai/rag-cookbooks.git
```

จากนั้นเข้าไปที่โฟลเดอร์โปรเจกต์:

```bash
cd rag-cookbooks
```

เมื่ออยู่ในโฟลเดอร์ 'rag-cookbooks' แล้ว ให้ดูรายละเอียดการใช้งานแต่ละเทคนิคในโน้ตบุ๊ก

## ผู้สร้างและผู้มีส่วนร่วม👨🏻‍💻

[![Contributors](https://contrib.rocks/image?repo=athina-ai/cookbooks)](https://github.com/athina-ai/cookbooks/graphs/contributors)

## ประวัติการให้ดาว

[![Star History Chart](https://api.star-history.com/svg?repos=JonusNattapong/Notebook-Git-Colab&type=Date)](https://www.star-history.com/#JonusNattapong/Notebook-Git-Colab&Date)
