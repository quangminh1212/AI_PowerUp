# 🚀 مكتبة المهارات - AI Skills Library

&lt;div align="center"&gt;

![Skills Library](screenshot.png)

[![HTML](https://img.shields.io/badge/HTML-5-orange?style=flat-square&logo=html5)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS](https://img.shields.io/badge/CSS-3-blue?style=flat-square&logo=css3)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow?style=flat-square&logo=javascript)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Tailwind](https://img.shields.io/badge/Tailwind-3-cyan?style=flat-square&logo=tailwind-css)](https://tailwindcss.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

**مكتبة تفاعلية لمهارات AI المستندة إلى مشروع antigravity-awesome-skills**

[🌐 معاينة حية](https://yourusername.github.io/skills-library) | [📥 تحميل الملف](https://github.com/yourusername/skills-library/archive/refs/heads/main.zip)

&lt;/div&gt;

---

## 📋 نظرة عامة

مكتبة المهارات هي واجهة ويب تفاعلية احترافية لتصفح و البحث في أكثر من **300 مهارة** للذكاء الاصطناعي، مصنفة في 6 أقسام رئيسية. المكتبة تسهل على المطورين والمستخدمين العثور على المهارات المناسبة لاحتياجاتهم ونسخها بسهولة للاستخدام في prompts.

### ✨ المميزات الرئيسية

- 🔍 **بحث فوري ذكي** - بحث في اسم المهارة، الوصف، الفائدة، وطريقة الاستخدام
- 📑 **تصنيفات واضحة** - 6 أقسام منظمة: APIs، Azure، AWS، مراجعة الكود، قواعد البيانات، AI Agents
- 📋 **نسخ بنقرة واحدة** - نسخ اسم أي مهارة بسهولة
- 🎯 **تنقل سريع** - انتقال فوري بين الأقسام المختلفة
- 📱 **تصميم متجاوب** - يعمل على جميع الأجهزة (جوال، تابلت، ديسكتوب)
- 🎨 **واجهة عصرية** - تصميم زجاجي (Glassmorphism) مع رسوم متحركة سلسة

---

## 🗂️ التصنيفات المتاحة

| التصنيف | الأيقونة | عدد المهارات | الوصف |
|---------|----------|-------------|-------|
| **واجهات البرمجة APIs** | 🔌 | 25+ | تصميم، أمان، وإدارة APIs |
| **منصة Azure السحابية** | ☁️ | 100+ | الذكاء الاصطناعي، التخزين، والإدارة |
| **منصة AWS السحابية** | 🟠 | 5 | الخوادم بدون إدارة والأمان |
| **مراجعة الكود وإعادة الهيكلة** | 📝 | 16 | الجودة، التنظيف، والتوثيق |
| **قواعد البيانات** | 🗄️ | 9 | التصميم، الإدارة، والتحسين |
| **الوكلاء الذكيين والذكاء الاصطناعي** | 🤖 | 24+ | بناء وإدارة أنظمة AI المتقدمة |

---

## 🚀 طريقة الاستخدام

### الاستخدام المحلي
1. قم بتحميل الملف `index.html`
2. افتحه في أي متصفح حديث (Chrome, Firefox, Edge, Safari)
3. لا يحتاج لإنترنت بعد التحميل (ما عدا الخطوط والأيقونات)

### الاستخدام على GitHub Pages
1. ارفع الملف إلى مستودع GitHub
2. فعّل GitHub Pages من إعدادات المستودع
3. سيتم نشر الموقع تلقائياً على `username.github.io/repo-name`

---

## 🛠️ التقنيات المستخدمة

- **HTML5** - هيكل الصفحة
- **Tailwind CSS** (عبر CDN) - التصميم والتنسيق
- **JavaScript (Vanilla)** - التفاعل والبحث
- **Font Awesome** - الأيقونات
- **Google Fonts (Cairo)** - الخط العربي

---

## 📸 لقطة شاشة

&lt;div align="center"&gt;

![Preview](screenshot.png)

&lt;/div&gt;

---

## 🔧 التخصيص

يمكنك تعديل المهارات بسهولة عن طريق تعديل مصفوفة `skillsData` في ملف `index.html`:

```javascript
const skillsData = [
    {
        id: "your-category",
        title: "اسم التصنيف",
        subtitle: "وصف مختصر",
        description: "وصف مفصل",
        icon: "fa-icon-name",
        color: "blue",
        skills: [
            {
                name: "@skill-name",
                desc: "الوصف",
                benefit: "الفائدة",
                usage: "طريقة الاستخدام"
            }
        ]
    }
];
