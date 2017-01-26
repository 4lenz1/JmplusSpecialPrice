import requests
import sys


res  = requests.get('http://class.ruten.com.tw/user/index00.php?s=jmplus01&d=4797150&o=0&m=1')



print(res.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding), file = open('data.txt', 'w'))
