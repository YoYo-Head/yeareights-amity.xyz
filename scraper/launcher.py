import time
import subprocess
import os

pythonV = r".venv\Scripts\python.exe"

scraper = os.path.dirname(__file__)

request = os.path.join(scraper, 'request.py')
reform = os.path.join(scraper, 'reform.py')

def launch() -> None:
    subprocess.run(pythonV, 'launcher.py')

if __name__ == '__main__':
    subprocess.run([pythonV, request])
    time.sleep(0.5)
    subprocess.run([pythonV, reform])

