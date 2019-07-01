# Advisory: Private Internet Access (PIA) Android App Can Be Crashed via Large Download [CVE-2017-15882]

## 摘要

    私有Internet访问（PIA）VPN服务提供的Android应用程序可以通过下载包含当前VPN服务器列表的大文件来崩溃。

    这可以被MITM攻击者通过拦截和替换此文件来利用。 虽然文件是经过数字签名的，但它不是通过SSL提供的，并且应用程序不包含用于检查提供的文件是否非常大的逻辑。

供应商已在v1.3.3.1中修复此问题，用户应安装最新版本。
## Bug Details 

## PoC

## 厂商回应

## 相关信息

## 奖金信息

## 作者

## 时间轴