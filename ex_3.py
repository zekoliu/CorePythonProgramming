
from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR = 'smtp.python.is.cool'
POP3SVR = 'pop.python.is.cool'

orifHdrs = ['From: zekoliu@foxmail.com', 'To: zekoliu@foxmail.com', 'Subject: test msg']
origBody = ['xxx', 'yyy', 'zzz']
origMsg = '\r\n\r\n'.join(['\r\n'.join(orifHdrs), '\r\n'.join(origBody)])

sendSvr = SMTP(SMTPSVR)
errs = sendSvr.sendmail('zekoliu@foxmail.com', ('zekoliu@fixmail.com',), origMsg)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10)

recvSvr = POP3(POP3SVR)
recvSvr.user('zekoliu')
recvSvr.pass_('kobeliumvp')
rep, msg, siz = recvSvr.retr(recvSvr.stat()[0])

seq = msg.index('')
recvBoby = msg[seq+1:]
assert origBody == recvBoby