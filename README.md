# minilab_script

MininetLab的运行脚本，运行之前，确保本地有python3，Mininet与Quagga环境。方式如下：

#### Python3环境

```bash
pip3 install termcolor
```

#### Mininet安装

```bash
git clone https://github.com/mininet/mininet.git
cd mininet/util
./install.sh -3n
```

#### Quagga安装

```
echo "deb http://cn.archive.ubuntu.com/ubuntu/ focal-updates main restricted"  | tee -a /etc/apt/sources.list.d/quagga.list
apt update
apt-cache policy quagga # 如果执行了上面的操作，这一部应该可以看到列表中有quagga
apt install quagga=1.2.4-4ubuntu0.4
```
