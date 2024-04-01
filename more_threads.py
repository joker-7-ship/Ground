# 定义Thread
import threading


class DoubanMovieThread(threading.Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
    def run(self):
#抓取网页内容#将任务分配给多个线程执行
    def run_threads(urls):
        threads =[DoubanMovieThread(url)
        for url in urls]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
#主函数
if __name__=='__main__':
    urls =[f'{i* 25}' for i in range(10)]
    run_threads(urls)