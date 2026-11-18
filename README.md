# Inbox Triage

Read unread count and the age of your oldest unread message without showing mail contents.

Configure IMAP host, port and folder. Set IMAP_USER and either IMAP_PASSWORD (an app password if required) or IMAP_OAUTH_TOKEN on the computer. STATUS reads UNSEEN. For age, a read-only selection requests only INTERNALDATE for unread message IDs, never message bodies or subjects. Providers must enable IMAP. Expired credentials yield an offline state; OAuth refresh is handled by the owner.

## Connect the bar

Copy companion/example.json to a private config.json and adjust it for your source. From the project folder run `python3 companion/serve.py --config config.json`. Use Python 3.10+. Set Local companion URL to `http://127.0.0.1:8770/reading` on the emulator and allow local port 8770. On hardware, bind the companion to a trusted LAN interface and set its reachable address. The wheel browses pages. Click refreshes. Start pins or unpins the current page. The last good reading is labeled offline after a source error.

## Run locally

From this folder, run `~/.busy-emulator/bin/busy-emulator dev --once` with BUSY Bar Emulator open. Back exits.

![BUSY Bar front display](screenshots/front-1.png)
