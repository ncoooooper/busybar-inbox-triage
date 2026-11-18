# Inbox Triage

Read unread count and the age of your oldest unread message without showing mail contents.

Seven unread messages could all be new, or one could have been waiting since Monday. The second page gives the count a time dimension without putting anyone’s subject line on a shared desk.

## Check how long a message has been waiting

1. Configure one IMAP folder and start the companion. The front shows its unread count.
2. Turn the wheel to **OLDEST UNREAD**. In the recording, seven messages are unread and the oldest has waited three days.
3. Use the rear display for the current reading and **Start** to keep the age page selected.

![The front switches from seven unread messages to an oldest age of three days.](media/guide/check-unread-age.gif)

## Check the count after triage

1. Open your mail client to read or file messages. The bar only reads the mailbox status.
2. Unpin if needed, turn back to **UNREAD**, then click to refresh the companion reading.
3. If the account connection fails, consult the rear status. After a successful read, an offline indicator distinguishes the last available data from a fresh result.

![The oldest age of 3d gives way to an unread count of seven.](media/guide/return-to-mail-count.gif)

## Example from the emulator

The companion requests the unread count and internal arrival dates. A message marked unread in the mail client can affect both figures. No message bodies or subjects are needed for either calculation. Simulated IMAP transport exercising the real read-only status, search, date fetch and parsing path. No personal mailbox was connected.

## Set up the source

Configure IMAP host, port and folder. Set IMAP_USER and either IMAP_PASSWORD (an app password if required) or IMAP_OAUTH_TOKEN on the computer. STATUS reads UNSEEN. For age, a read-only selection requests only INTERNALDATE for unread message IDs, never message bodies or subjects. Providers must enable IMAP. Expired credentials yield an offline state; OAuth refresh is handled by the owner.

## Connect the bar

Copy companion/example.json to a private config.json and adjust it for your source. From the project folder run `python3 companion/serve.py --config config.json`. Use Python 3.10+. Set Local companion URL to `http://127.0.0.1:8770/reading` on the emulator and allow local port 8770. On hardware, bind the companion to a trusted LAN interface and set its reachable address. The wheel browses pages. Click refreshes. Start pins or unpins the current page. The last good reading is labeled offline after a source error.

## Run in the emulator

Open BUSY Bar Emulator. From this repository, run:

```sh
~/.busy-emulator/bin/busy-emulator dev --once
```

Press **Back** to exit.

The GIFs are excerpts from the emulator recording. Each front-display pixel is shown at 9× its original width and height. The end frames pause for reading.

[Full recording](media/controls.mp4) · [Rear display](screenshots/back-1.png) · [Firmware test](EMULATOR-QA.md) · [MIT license](LICENSE)
