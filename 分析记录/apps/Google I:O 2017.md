# Google I/O 2017

## 摘要
    "Google I/O 2017 Application for Android"没有使用SSL检索信息来填充应用程序。这将允许MITM攻击者将自己的内容注入应用程序。谷歌在v5.1.4中修复了该问题。
## 正文
	该app是Google 为其年度i/o会议制定的配套应用程序。此特定版本是在2017年5月为I/O会议制定的。
	在对该app进行网络层面的测试时，发现应用程序未使用SSL。这将允许MITM攻击者使用ARP欺骗、DNS接管等方法将自己的内容注入到应用程序。

	复现这个问题在v5.0.3:
	1.安装
	2.设置代理，不使用SSL证书，并且代理与安卓设备在同一网络中。
	3.打开app，点击“feed”选项。
	4.观察捕捉到的流量。

	URL was “http://storage.googleapis.com/io2017-festivus/manifest_v1.json”

	这个url 让设备下载以下url：

	http://storage.googleapis.com/io2017-festivus:blocks_v5.json

	http://storage.googleapis.com/io2017-festivus/map_v4.json

	http://storage.googleapis.com/io2017-festivus/session_data_v1.100.json

	同样也能在I/O 2016 app（github的source code）中找到http的字眼。

	本测试在Android7.0.1，Google I/O version 5.0.3，burpsuit without SSl证书。
## Proof of Concept
	
	/ 

## Vendor Response
	
	此问题已向供应商报告，并在5.1.4版中修复。

## References 

	CVE ID: CVE-2017-9045

	Google I/O 2016 source code: https://github.com/google/iosched

## Bounty Information
	
	/

## Credits

	https://wwws.nightwatchcybersecurity.com/2017/05/17/advisory-google-io-2017-android-app/

## Timeline

	2017-05-11: Initial report to the vendor

	2017-05-11: Report triaged by the vendor and bug filed

	2017-05-13: Fixed version released by the vendor

	2017-05-16: Draft advisory sent to vendor for comment

	2017-05-17: Public disclosure