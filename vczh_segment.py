import jieba
with open('weibovczh.txt','r',encoding='utf-8',errors= 'ignore') as article:
    words = jieba.cut(article.read())
    word_freq = {}
    for w in words:
        if w in word_freq:
            word_freq[w] += 1
        else:
            word_freq[w] = 1
    freq_word = []
    for w, freq in word_freq.items():
        freq_word.append((w,freq))

    freq_word.sort(key = lambda x: x[1], reverse = True)
    with open('vczhfrequence','w',encoding='utf-8') as result:
        for word, freq in freq_word:
            result.write(str(freq)+':'+str(word)+'\n')
