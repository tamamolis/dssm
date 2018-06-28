# coding=utf-8
from __future__ import print_function
import numpy as np
import gensim

train_query_path = '../../dataset/train_query.txt'
train_doc_path = '../../dataset/train_doc.txt'
train_label_path = '../../dataset/train_label.txt'
valid_query_path = '../../dataset/valid_query.txt'
valid_doc_path = '../../dataset/valid_doc.txt'
valid_label_path = '../../dataset/valid_label.txt'
test_query_path = '../../dataset/test_query.txt'
test_doc_path = '../../dataset/test_doc.txt'
test_label_path = '../../dataset/test_label.txt'


def load_train_dataset():
    return load_dataset(train_query_path, train_doc_path, train_label_path)


def load_valid_dataset():
    return load_dataset(valid_query_path, valid_doc_path, valid_label_path)


def load_test_dataset():
    return load_dataset(test_query_path, test_doc_path, test_label_path)


def load_dataset(query_path, doc_path, label_path):
    #    global train_query, train_doc, train_label, test_query, test_doc, test_label
    query_data = get_w2v(query_path, sentence_length=20)
    doc_data = get_w2v(doc_path)
    label_data = get_label(label_path)
    print(np.shape(query_data), np.shape(doc_data), np.shape(label_data))
    assert query_data.shape == doc_data.shape
    assert query_data.shape[0] == label_data.shape[0]
    return query_data, doc_data, label_data


def get_onehot_vec(filepath, sentence_length=20):
    global vocab
    data_set = []
    fr = open(filepath)
    for row in fr.readlines():
        temp = []
        row = row.strip().split()
        if len(row) == 0:
            print("sentence has no word")
            continue
        for word in row:
            if word in vocab:
                temp.append(vocab[word])
        if len(temp) > sentence_length:
            temp = temp[:sentence_length]
        elif len(temp) < sentence_length:
            temp = temp + [0] * (sentence_length - len(temp))
        data_set.append(temp)
    fr.close()
    return np.asarray(data_set, dtype=np.int32)


def get_w2v(filepath, sentence_length=20):
    global vocab
    data_set = []

    w2v_path = "../../dataset/GoogleNews-vectors-negative300.bin.gz"
    model = gensim.models.KeyedVectors.load_word2vec_format(w2v_path, binary=True)

    # sentences = gensim.models.word2vec.PathLineSentences('/Users/kate/PycharmProjects/dssm/raw_data/w2v_corpus.txt')
    # model = gensim.models.Word2Vec(sentences, min_count=1, size=300)

    fr = open(filepath)
    for row in fr.readlines():
        temp = []
        row = row.strip().split()

        for word in row:
            if word in vocab:
                try:
                    temp.append(model[word])
                except KeyError:
                    # print('word: ', word)
                    w = np.zeros((300))
                    temp.append(w)
        if len(temp) > sentence_length:
            temp = temp[:sentence_length]
        elif len(temp) < sentence_length:
            for i in range(sentence_length - np.shape(temp)[0]):
                zero_array = np.zeros((1, 300))
                temp = np.concatenate((temp, zero_array), axis=0)

        data_set.append(temp)
    return np.asarray(data_set)


def get_label(filepath):
    label = []
    fr = open(filepath)
    for row in fr.readlines():
        array = row.strip().split(' ')
        if row.strip() == '' or len(array) != 2:
            continue
        vec = []
        for i in array:
            vec.append(int(i))
        label.append(vec)
    fr.close()
    return np.asarray(label, dtype=np.int32)


def load_vocab():
    vocab_path = '../../model/vocab.txt'
    vocab = {}
    fr = open(vocab_path)
    index = 0
    for row in fr.readlines():
        word = row.strip()
        if word == '':
            continue
        vocab[word] = index
        index += 1
    fr.close()
    return vocab
    # fw.close()


vocab = load_vocab()

if __name__ == "__main__":
    load_vocab()