import os
import time

class UtilitiesManager:

    def __init__(self) -> None:
        print('Utilities mgr init')

    def helper1(self) -> str:
        print('Utils mgr helper 1')

    def downloadWait(self, downloadsPath) -> bool:
        seconds = 0
        downloadWait = True
        fileDownloaded = False
        while downloadWait and seconds < 30:
            time.sleep(1)
            downloadWait = False
            for fname in os.listdir(downloadsPath):
                if fname.endswith('.crdownload'):
                    downloadWait = True
            seconds += 1
            fileDownloaded = True
        return fileDownloaded