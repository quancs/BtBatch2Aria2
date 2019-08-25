import xmlrpc.client
import xmlrpc
import os
import argparse

def handle(s, btFile):
    print('handle bittorrent file: ', str(btFile))
    ret=s.aria2.addTorrent(xmlrpc.client.Binary(open(btFile, mode='rb').read()),[],{'pause':'true'})
    print("add bt: ",str(ret))
    waiting = s.aria2.tellWaiting(0, 1000,
                              ["gid", "totalLength", "completedLength", "uploadSpeed", "downloadSpeed", "connections",
                               "numSeeders", "seeder", "status", "errorCode", "verifiedLength",
                               "verifyIntegrityPending", "files", "bittorrent", "infoHash"])
    for w in waiting:
        gid=w['gid']
        if gid!=ret:
            continue
        #print(w['gid'],w['files'])
        # max-selection strategy
        maxLen=0
        maxFPath=''
        maxFIndex='0'
        for f in w['files']:
            #print(f['length'],f['path'])
            if int(f['length'])>maxLen:
                maxLen=int(f['length'])
                maxFPath=f['path']
                maxFIndex=f['index']
        print('max file: ',str(maxLen),maxFIndex,str(maxFPath))
        # max-selection strategy end
        cret=s.aria2.changeOption(gid,{'select-file':maxFIndex})# select multiple files example: 'select-file':'5,6,7,8'
        print('select file: ',cret)
        tret=s.aria2.tellStatus(gid)
        print('after selection: ', tret['files'][int(maxFIndex)-1])
        uret=s.aria2.unpause(gid)
        print('unpause: ',uret)
    print('over: ',str(btFile))



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.description = 'bt批量导入aria2，并选择文件大小最大的文件进行下载'
    parser.add_argument("server", help="like: http://192.168.3.99:6800/", type=str)
    parser.add_argument("dir", help="the dir of your bittorrents", type=str)
    args = parser.parse_args()
    s = xmlrpc.client.ServerProxy(args.server+"rpc")
    flist=os.listdir(args.dir)
    for i in range(0, len(flist)):
        btFile = os.path.join(args.dir, flist[i])
        if os.path.isfile(btFile):
            handle(s,btFile)
    print("Done")
