
import gzip
f_in = open('newfile.txt', 'rb')
f_out = gzip.open('newfile.txt.gz', 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()

import gzip
f = gzip.open('newfile.txt.gz', 'rb')
f_out = open('newfile.txt','wb')
file_content = f.read()
f_out.write(file_content)
f.close()
f_out.close()