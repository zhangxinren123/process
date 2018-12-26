import multiprocessing

def download_data(q):	
	#下载的数据
	data=[123,456,789,321,654,987]
	for each in data:
		q.put(each)
	
	print('已经下载好文件了')
  

def analysis_data(q):
	waitting_data=[]
	#从队列中获取数据
	while True:
		content=q.get()
		waitting_data.append(content)
		if q.empty():
			break
	print('数据为:',waitting_data)

def main():
	#创建队列Q
	q=multiprocessing.Queue()
	#创建进程
	t1 = multiprocessing.Process(target=download_data, args=(q,))
	t2 = multiprocessing.Process(target=analysis_data, args=(q,))
	t1.start()
	t2.start()

if __name__ == '__main__':
	main()