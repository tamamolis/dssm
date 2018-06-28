### dssm
## dependency
- tensorflow(1.2.0)
### how to use (эмбеддинги)
- mkdir model
- in dir model create file 'vocab.txt'
- mkdir output
- cd preprocess
- python preprocess.py
- cd src/run
- python train.py
- python test.py
#### <b style='color:blue'>DONE</b>, всё работает, есть результат

### how to use w2v FINAL
- в data_provider есть get_w2v(filepath, sentence_length=20), который принимает тексты, а возвращает их в виде np.array w2v массивов. для этого нужен [GoogleNews-vectors-negative300.bin.gz](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit) в папочке dataset
- в файле dssm.py надо было закоммитить self.words, чтобы использовались ВНЕШНИЕ эмбеддинги, а не инициализировались свои
- embedding_dim надо было везде поменять на 300.
- __если захочется обратно поменять на onehot_vec__, то надо в data_provider load_dataset исправить get_w2v на get_onehot_vec и раскоммитить self.words
#### <b style='color:blue'>DONE</b>, всё работает, нет результата, надо выучить

### how to use fasttext
- всё то же самое, что с w2v, но надо скачать данные fasttext. пока не сделано

### how to use OUTPUT
- на выходе два файла: diff1.txt и test1.txt, которые получаются при помощи функций write_result и write_diff.
  - про функцию write_result:
    - сначала грузим запросы с помощью функции load_file_data() (просто считывает построчно данные и возвращает список)
    - затем грузим документы с помощью той же функции
    - затем вызываем pred(), который у нас тоже описан, он возвращает предикты по всем запросам и документам
    - в файл test1.txt пишем следующее: query[i] + doc[i] + pred[i]
  - про функцию write_diff:
    - первые три пункта такие же
    - label получаются из load_label_data(). Лейблы бывают 0  или 1
    - в файл diff1.txt пишем ТОЛЬКО ЕСЛИ pred[i] != label[i]
    - если уловие выше выполнено, то пишем query[i] + doc[i] + pred[i] + label[i]
