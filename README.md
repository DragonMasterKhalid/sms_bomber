# SMS Bomber - Educational Tool
> Developed by DragonMasterKhalid

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Platform](https://img.shields.io/badge/Platform-Termux-green)
![License](https://img.shields.io/badge/License-Educational%20Use-only-red)

## 📖 Description
This is an educational SMS testing tool created for learning purposes and security research. The tool demonstrates how SMS APIs work and should only be used for educational purposes.

## ⚠️ Legal Disclaimer
**THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY!**

- ✅ **Allowed**: Testing your own systems, Educational learning
- ❌ **Prohibited**: Harassment, Unauthorized testing, Illegal activities

**By using this tool, you agree to:**
- Use only on numbers you own or have permission to test
- Accept all legal responsibilities for your actions
- Not misuse the tool for malicious purposes

## 🚀 Features
- Multi-threaded testing
- Rate limiting protection
- Real-time statistics
- Password protected
- Auto-update system
- Educational purpose focused

## 📦 Installation

### Termux Installation
```bash
# Update and install dependencies
pkg update && pkg upgrade
pkg install python git -y

# Clone repository
git clone https://github.com/DragonMasterKhalid/sms_bomber.git
cd sms_bomber

# Install requirements
pip install -r requirements.txt

# Run the tool
python sms_bomber.py
