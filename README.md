# Cantoproject

Code for visit report on [PYCON HK 2021 Cantonese Selfish Project 廣東話自肥企劃](https://youtu.be/S23Q_mqTeJQ "PYCON HK 2021 Cantonese Selfish Project 廣東話自肥企劃") (homework for an AI course)

[pycanto.ipynb](https://github.com/chitwitgit/Cantoproject/blob/main/pycanto.ipynb "pycanto.ipynb") is the jupyter notebook used to try out Cantonese word segmentation

[testwav2vec.ipynb](https://github.com/chitwitgit/Cantoproject/blob/main/pycanto.ipynb "testwav2vec.ipynb") is the jupyter notebook used to try running the wav2vec model on my macbook. The first part of the code works on Windows, place a .wav file in the project folder and replace 'x.wav' in the code accordingly.

[x.wav](https://github.com/chitwitgit/Cantoproject/blob/main/x.wav "testwav2vec.ipynb") a placeholder wav file for [testwav2vec.ipynb](https://github.com/chitwitgit/Cantoproject/blob/main/pycanto.ipynb "testwav2vec.ipynb")

[main.py](https://github.com/chitwitgit/Cantoproject/blob/main/pycanto.ipynb "main.py"). Run the code on python console to locate the bug(reason that the kernel died)
Debug message: Process finished with exit code 132 (interrupted by signal 4: SIGILL)
This is an illegal instruction error from assembly level, and compiling the module from source does not work.

[wav2vec.ipynb](https://github.com/chitwitgit/Cantoproject/blob/main/pycanto.ipynb "wav2vec.ipynb") is the final jupyter notebook to run the model on the Common Voice dataset which I am unable to run on any OS due to issues:

I tried to run the code in Jupyter notebook on my macbook pro, but the kernel died. From running the python code and reading the debug message, I learnt that it has something to do with the Apple M1 processor not being able to run the wav2vec model. So, I tried compiling the corresponding module from source and still, no luck. I then ran the code on my slow windows computer, and it worked.

I then tried to modify the code to run tests on several audio clips from the <a href="https://commonvoice.mozilla.org/zh-HK/datasets" data-type="URL" data-id="https://commonvoice.mozilla.org/zh-HK/datasets">Common Voice Dataset</a>. However, the clips are of mp3 format which I cannot find a way for python to read mp3 files in Windows OS and I am not interested in converting them all into .wav files. Therefore, I booted up a Linux Virtual Machine to try to run the code.

![](https://github.com/chitwitgit/Cantoproject/blob/main/vm.png)

The Linux VM also raised an illegal instruction error when importing pandas, and at that point I was burnt out and gave up on trying to use the code to run the model on the Common Voice dataset.

Please tell me if you can run the code successfully.
