"""Read unread count and oldest unread age from the owner's read-only IMAP mailbox."""
import email.utils,imaplib,os,re,time
from datetime import datetime
from serve import page
INTERVAL=120
def read_mail(o):
    folder=o.get("folder","INBOX");host=o["host"]
    if any(c in folder for c in '\r\n"\\'):raise ValueError("Unsupported folder name")
    with imaplib.IMAP4_SSL(host,int(o.get("port",993)),timeout=12) as mail:
        user=os.environ["IMAP_USER"]
        if "IMAP_OAUTH_TOKEN" in os.environ:
            response=("user="+user+"\x01auth=Bearer "+os.environ["IMAP_OAUTH_TOKEN"]+"\x01\x01").encode()
            mail.authenticate("XOAUTH2",lambda _:response)
        else:mail.login(user,os.environ["IMAP_PASSWORD"])
        quoted='"'+folder+'"'
        status,data=mail.status(quoted,"(UNSEEN)")
        if status!="OK":raise ValueError("Mailbox status unavailable")
        match=re.search(rb"\bUNSEEN\s+(\d+)",b" ".join(v for v in data if isinstance(v,bytes)),re.I)
        if not match:raise ValueError("Invalid mailbox status")
        count=int(match[1])
        if not count:return count,None
        if mail.select(quoted,readonly=True)[0]!="OK":raise ValueError("Mailbox unavailable")
        status,rows=mail.uid("search",None,"UNSEEN")
        if status!="OK":raise ValueError("Unread search failed")
        ids=rows[0].split();oldest=None
        for offset in range(0,len(ids),150):
            result,metadata=mail.uid("fetch",b",".join(ids[offset:offset+150]),"(INTERNALDATE)")
            if result!="OK":raise ValueError("Date lookup failed")
            for entry in metadata:
                if not isinstance(entry,bytes):continue
                d=re.search(rb'INTERNALDATE "([^"]+)"',entry)
                if d:
                    parsed=datetime.strptime(d[1].decode("ascii"),"%d-%b-%Y %H:%M:%S %z").timestamp()
                    oldest=parsed if oldest is None else min(oldest,parsed)
        return len(ids),oldest
def snapshot(o,m):
    count,oldest=read_mail(o)
    days=None if oldest is None else int(max(0,time.time()-oldest)//86400)
    return dict(state="Read-only IMAP",key=str(count),alert=count==0,pages=[
      page("UNREAD",count,"Unread in selected folder",o.get("folder","INBOX")[:25]),
      page("OLDEST UNREAD","--" if days is None else str(days)+"d","No unread messages" if not count else "Since delivery","No bodies or subjects read")])
