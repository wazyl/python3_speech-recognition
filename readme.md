本程序基于windows10环境下 Python3.7.3和百度语音识别完成

首先需要安装pyaudio python3.7安装pyaudio 可见链接 https://blog.csdn.net/a506681571/article/details/85201279

百度语音需要去百度智能云注册账号 登录账号 并创建百度语音识别应用 替换掉 voice.py 里面的 AppID 、API Key 、Secret Key三个信息

python voice.py 运行程序 录入垃圾名称 来获取是哪种垃圾类别。

友情提示：

1.录音时间为5秒，可以自己去根据自己需要修改录音时长

2.如果要区分多个多种垃圾 要再每个垃圾名称后面录入逗号语音

3.默认检测语音，循环判断出结果以后还可以继续执行，如果想退出程序的话，可以再最后录入退出程序，waste_map_dict只是一个简单的demo，如有需要请自行丰富。

如有问题，请联系我 QQ：1160325080 



