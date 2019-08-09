# -*- coding: utf-8 -*-

import pyaudio
import wave
from aip import AipSpeech

#类定义
class box:
#定义基本属性
	frames_per_buffer = 1024
	format_type = pyaudio.paInt16
	channels = 1
	rate = 16000
	record_seconds = 5  #设置录音的时间长度
	filename = "output.wav"
	input_bool = True
	app_id = 'AppID'
	api_key = 'API Key'
	secret_key  = 'Secret Key'
	#可回收物列表
	waste_map_dict = {
	"废纸":"可回收垃圾",
	"塑料":"可回收垃圾",
	"玻璃":"可回收垃圾",
	"金属":"可回收垃圾",
	"布料":"可回收垃圾",
	"卫生纸":"其它（干垃圾）",
	"餐厨垃圾装袋":"其它（干垃圾）",
	"果壳":"其它（干垃圾）",
	"尘土":"其它（干垃圾）",
	"剩菜剩饭":"厨余（湿垃圾）",
	"骨头":"厨余（湿垃圾）",
	"菜根菜叶":"厨余（湿垃圾）",
	"果皮":"厨余（湿垃圾）",
	"电池":"有害垃圾",
	"荧光管":"有害垃圾",
	"灯泡":"有害垃圾",
	"水银温度计":"有害垃圾",
	"油漆桶":"有害垃圾",
	"过期药品":"有害垃圾",
	"过期化妆品":"有害垃圾"
	} 


	def sound_recording(self):
		p = pyaudio.PyAudio()
		stream = p.open(
			format=self.format_type,
			channels=self.channels,
			rate=self.rate,
			input=self.input_bool,
			frames_per_buffer=self.frames_per_buffer
			)

		print("********start recording********")
		frames =  []
		for i in range(0, int(self.rate / self.frames_per_buffer * self.record_seconds)):
			data = stream.read(self.frames_per_buffer)
			frames.append(data)
		print("********done recording********")
		stream.stop_stream()
		stream.close()
		p.terminate()
		wf = wave.open(self.filename, 'wb')
		wf.setnchannels(self.channels)
		wf.setsampwidth(p.get_sample_size(self.format_type))
		wf.setframerate(self.rate)
		wf.writeframes(b''.join(frames))
		wf.close()
	
	def get_file_content(self, filePath):
		with open(filePath, 'rb') as fp:
			return fp.read()

	def message(self):
		client = AipSpeech(self.app_id, self.api_key, self.secret_key)
		json_data = client.asr(self.get_file_content('D:/python37/program/output.wav'), 'pcm', 16000,{'dev_pid': 1536
			})
		error_no = json_data['err_no']
		if error_no == 0:
			print("解析成功")
			num = 0
			waste_list = json_data['result'][0].split("逗号")
			#循环判断是属于哪种垃圾
			for name in waste_list:
				if name in self.waste_map_dict:
					num = num + 1
					print(name + '是' + self.waste_map_dict[name] + '\n')
				elif name == '退出程序':
					num = -1
					break
				else:
					num = num + 1
					print("没有检测到符合条件的垃圾")
			if num > 0:
				self.sound_recording()
				self.message()

		else:
			print("解析失败")
			print(json_data['err_msg'])
	
# 实例化类
box_class = box()
box_class.sound_recording()
box_class.message()
