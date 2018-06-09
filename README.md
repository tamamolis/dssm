# dssm
## dependency
- tensorflow(1.2.0)
## how to use
- mkdir model
- in dir model create file 'vocab.txt'
- mkdir output
- cd preprocess
- python preprocess.py
- cd src/run
- python train.py
- python test.py
# how to w2v
- в файле preprocess.py есть generate_vocab(), который создаёт файл vec.txt
- в файле dssm.py есть флаг fine_tune, заменить на True, тогда будет v2w вместо эмбеддингов
- в dssm.py есть метод load_w2v(), который считывает из vec.txt
# w2v troubles
- проблемы с созданием vec.txt, потому что оттуда только считывается. есть ощущение, что перепутаны файлы vec.txt и w2v_corpus.txt, потому что w2v_corpus.txt создаётся и никак не используется
