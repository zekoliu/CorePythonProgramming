
import nntplib
import socket

HOST = 'your.nntp.server'
GRNM = 'comp.lang.python'
USER = 'wesley'
PASS = 'youllNeverGuess'

def main():
    try:
        n = nntplib.NNTP(HOST)
    except socket.gaierror, e:
        print 'Error: cannot reach host "%s"' % HOST
        print ' ("%s")' % eval(str(e))[1]
        return
    except nntplib.NNTPPermanentError, e:
        print 'ERROR: access denied on "%s"' % HOST
        print '     ("%s")' % str(e)
        return
    print '*** Connected to host "%s"' % HOST

    try:
        rsp, ct, fst, lst, grp = n.group(GRNM)
    except nntplib.NNTPTemporaryError, e:
        print 'ERROR: cannot load ground "%s"' % GRNM
        print '  ("%s")' % str(e)
        print '  Server may require authentication'
        print '  Uncomment/edit login line above'
        n.quit()
        return
    except nntplib.NNTPTemporaryError, e:
        print 'ERROR: ground "%s" unavailable' % GRNM
        print '  ("%s")' % str(e)
        n.quit()
        return
    print '*** Found newsground "%s"' % GRNM

    rng = '%s-%s' % (lst, lst)
    rsp
