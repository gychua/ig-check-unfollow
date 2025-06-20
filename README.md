# Instagram Follower Management Automation

This project helps you manage your Instagram followers and following lists.

## Features
- Compare your Instagram followers (`followers_1.json`) and following (`following.json`) directly.
- Generate a user-friendly HTML report (`output.html`) showing users you follow who don't follow you back.

---

## Setup Instructions

### 1. Clone or Download the Project

```
git clone <your-repo-url>
cd ig
```

### 2. Install Python and Dependencies

Make sure you have Python 3.8+ installed.

---

## How to Export Your Instagram Followers and Following

1. **Go to https://accountscenter.instagram.com/info_and_permissions/dyi/.**
2. **Request a download** for your account data (choose JSON format for easier parsing).
3. **Wait for the email from Instagram** and download the ZIP file.
4. **Extract the ZIP file.** Inside, you'll find files like `followers_1.json` and `following.json` in the `followers_and_following` folder.
5. **Copy `followers_1.json` and `following.json` into this project folder.**

---

## Usage

### 1. Find Users You Follow Who Don't Follow You Back

```
python check_usernames.py
```
- This will generate `output.html` with clickable links for each user you follow who doesn't follow you back.

---

## Notes
- Use these scripts responsibly. Instagram may restrict or block accounts for excessive automation.
- Always review the list before taking any action.

---

## Troubleshooting
- If you get errors about missing packages, ensure you have installed all dependencies with `pip install` as needed.
- If Instagram changes its data export format, the script may need to be updated.

---

## License
MIT
