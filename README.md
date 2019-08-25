# BtBatch2Aria2
bt文件批量导入aria2，并选择文件大小最大的文件进行下载。Aria2需要开启rpc服务。如果你需要其他选择策略，请自行修改源代码。

Import multiple bt files into aria2 at once, and then download the largest file in each bt. Make sure aria2 opened its rpc service. If you want to select files in each bt by using a different strategy, you can modify the code to do so.

# 使用方法(How to Use)
    帮助（Help):
    python bb2a.py --help
    启动（Start to Add):
    python bb2a.py <server> <bt-dir>
    参数（parameters）：
    server      如（like): http://192.168.3.99:6800/
    bt-dir      bt文件的目录（the dir of your bittorrents）
    例子（example):
    python bb2a.py http://192.168.1.100/ /home/root/bts/
