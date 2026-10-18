# airgeddon
[![Version-shield]](https://raw.githubusercontent.com/v1s1t0r1sh3r3/airgeddon/master/CHANGELOG.md) [![Bash4.2-shield]](http://tldp.org/LDP/abs/html/bashver4.html#AEN21220) [![License-shield]](https://raw.githubusercontent.com/v1s1t0r1sh3r3/airgeddon/master/LICENSE.md) [![Docker-shield]](https://hub.docker.com/r/v1s1t0r1sh3r3/airgeddon/) [![Discord-shield]](https://discord.gg/sQ9dgt9)

[![Paypal-shield]](https://www.paypal.com/paypalme/airgeddon) [![Cryptocurrencies-shield]](https://v1s1t0r1sh3r3/airgeddon/wiki/Contributing-&-Code-of-Conduct)


> This is a multi-use bash script for Linux systems to audit wireless networks.

![Banner]

---

All the needed info about how to "install | use | enjoy" `airgeddon` is present at [GitHub's Wiki].

- *I. Content & Features*
  - [Home]
  - [Features]
  - [Screenshots]
  - [Wallpapers]


- *II. Requirements*
  - [Requirements]
  - [Compatibility]
	 - [Cards and Chipsets]
	 - [Wayland]
	 - [Consistent Network Device Naming]
	 - [Kali Nethunter]
  - [Essential Tools]
  - [Optional Tools]
	 - [BeEF Tips]
	 - [Hashcat Tips]
	 - [Bettercap Tips]
  - [Update Tools]
  - [Internal Tools]
  - [Known incompatibilities]


- *III. Getting started*
  - [Installation & Usage]
  - [Options]
  - [Docker]
	 - [Linux]
	 - [Mac OSX]
	 - [Windows]
  - [Other Sources]
  - [FAQ & Troubleshooting]


- *IV. Learning*
  - [CWP Certification]


- *V. Project & Development*
  - [Official Website]
  - [Plugins system]
	 - [Plugins development]
	 - [Plugins Hall of Fame]
  - [Supported Languages]
  - [Contributing & Code of Conduct]
  - [Security Policy]
  - [Merchandising Online Shop]
  - [Changelog]
  - [Disclaimer & License]
  - [Contact]


- *VI. Acknowledgments & References*
  - [Hat Tip To]
  - [Inspiration]

---

[Banner]: https://raw.githubusercontent.com/v1s1t0r1sh3r3/airgeddon/master/imgs/banners/airgeddon_banner.png "We will conquer the earth!!"
[GitHub's Wiki]: https://v1s1t0r1sh3r3/airgeddon/wiki

[Home]: https://v1s1t0r1sh3r3/airgeddon/wiki
[Features]: https://v1s1t0r1sh3r3/airgeddon/wiki/Features
[Screenshots]: https://v1s1t0r1sh3r3/airgeddon/wiki/Screenshots
[Wallpapers]: https://v1s1t0r1sh3r3/airgeddon/wiki/Wallpapers
[Requirements]: https://v1s1t0r1sh3r3/airgeddon/wiki/Requirements
[Compatibility]: https://v1s1t0r1sh3r3/airgeddon/wiki/Compatibility
[Cards and Chipsets]: https://v1s1t0r1sh3r3/airgeddon/wiki/Cards%20and%20Chipsets
[Wayland]: https://v1s1t0r1sh3r3/airgeddon/wiki/Wayland
[Consistent Network Device Naming]: https://v1s1t0r1sh3r3/airgeddon/wiki/Consistent%20Network%20Device%20Naming
[Kali Nethunter]: https://v1s1t0r1sh3r3/airgeddon/wiki/Kali%20Nethunter
[Essential Tools]: https://v1s1t0r1sh3r3/airgeddon/wiki/Essential%20Tools
[Optional Tools]: https://v1s1t0r1sh3r3/airgeddon/wiki/Optional%20Tools
[BeEF Tips]: https://v1s1t0r1sh3r3/airgeddon/wiki/BeEF%20Tips
[Hashcat Tips]: https://v1s1t0r1sh3r3/airgeddon/wiki/Hashcat%20Tips
[Bettercap Tips]: https://v1s1t0r1sh3r3/airgeddon/wiki/Bettercap%20Tips
[Update Tools]: https://v1s1t0r1sh3r3/airgeddon/wiki/Update%20Tools
[Internal Tools]: https://v1s1t0r1sh3r3/airgeddon/wiki/Internal%20Tools
[Known incompatibilities]: https://v1s1t0r1sh3r3/airgeddon/wiki/Known%20incompatibilities
[Installation & Usage]: https://v1s1t0r1sh3r3/airgeddon/wiki/Installation%20&%20Usage
[Options]: https://v1s1t0r1sh3r3/airgeddon/wiki/Options
[Docker]: https://v1s1t0r1sh3r3/airgeddon/wiki/Docker
[Linux]: https://v1s1t0r1sh3r3/airgeddon/wiki/Docker%20Linux
[Mac OSX]: https://v1s1t0r1sh3r3/airgeddon/wiki/Docker%20Mac%20OSX
[Windows]: https://v1s1t0r1sh3r3/airgeddon/wiki/Docker%20Windows
[Other Sources]: https://v1s1t0r1sh3r3/airgeddon/wiki/Other%20Sources
[FAQ & Troubleshooting]: https://v1s1t0r1sh3r3/airgeddon/wiki/FAQ%20&%20Troubleshooting
[CWP Certification]: https://v1s1t0r1sh3r3/airgeddon/wiki/CWP%20Certification
[Plugins system]: https://v1s1t0r1sh3r3/airgeddon/wiki/Plugins%20System
[Plugins development]: https://v1s1t0r1sh3r3/airgeddon/wiki/Plugins%20Development
[Plugins Hall of Fame]: https://v1s1t0r1sh3r3/airgeddon/wiki/Plugins%20Hall%20of%20Fame
[Supported Languages]: https://v1s1t0r1sh3r3/airgeddon/wiki/Supported%20Languages
[Contributing & Code of Conduct]: https://v1s1t0r1sh3r3/airgeddon/wiki/Contributing-&-Code-of-Conduct
[Security Policy]: https://v1s1t0r1sh3r3/airgeddon/security/policy
[Merchandising Online Shop]: https://airgeddon.creator-spring.com/
[Changelog]: https://v1s1t0r1sh3r3/airgeddon/wiki/Changelog
[Disclaimer & License]: https://v1s1t0r1sh3r3/airgeddon/wiki/Disclaimer%20&%20License
[Contact]: https://v1s1t0r1sh3r3/airgeddon/wiki/Contact
[Hat Tip To]: https://v1s1t0r1sh3r3/airgeddon/wiki/Hat%20Tip%20To
[Inspiration]: https://v1s1t0r1sh3r3/airgeddon/wiki/Inspiration
[Official Website]: https://airgeddon.pro/

[Version-shield]: https://img.shields.io/badge/version-12.01-blue.svg?style=flat-square&colorA=273133&colorB=0093ee "Latest version"
[Bash4.2-shield]: https://img.shields.io/badge/bash-4.2%2B-blue.svg?style=flat-square&colorA=273133&colorB=00db00 "Bash 4.2 or later"
[License-shield]: https://img.shields.io/badge/license-GPL%20v3%2B-blue.svg?style=flat-square&colorA=273133&colorB=bd0000 "GPL v3+"
[Docker-shield]: https://img.shields.io/docker/automated/v1s1t0r1sh3r3/airgeddon.svg?style=flat-square&colorA=273133&colorB=a9a9a9 "Docker rules!"
[Discord-shield]: https://img.shields.io/discord/629812069964840991.svg?style=flat-square&colorA=273133&colorB=CBA317&logo=discord&label=Discord%20chat
[Paypal-shield]: https://img.shields.io/badge/donate-paypal-blue.svg?style=flat-square&colorA=273133&colorB=b008bb "Paypal"
[Cryptocurrencies-shield]: https://img.shields.io/badge/donate-cryptocurrencies-blue.svg?style=flat-square&colorA=273133&colorB=f7931a "Cryptocurrencies"
