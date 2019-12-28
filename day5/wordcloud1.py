
import jieba #分词库
import matplotlib.pyplot as plt#会图库

from wordcloud import STOPWORDS, WordCloud#词云库

def generate_wordcloud():
    comments=[]
    with open('maoyan.csv',mode='r',encoding='utf-8') as f:
        rows = f.readlines()
        for row in rows:
            comment = row.split(':')[0]
            if comment !='':
                comments.append(comment)

    comment_after_split = jieba.cut(str(comments),cut_all=False)
    words = ''.join(comment_after_split)
    print(words)

    stopwords = STOPWORDS.copy()
    stopwords.add('电影')
    stopwords.add('一出')
    stopwords.add('好戏')
    stopwords.add('有点')

    bg_image = plt.imread('123.jpg')
    wc = WordCloud(width=1024,height=768,background_color='white',mask=bg_image,stopwords=stopwords,max_font_size=400,
                   random_state=50,font_path='STKAITI.TTF')

    wc.generate_from_text(words)
    wc.to_file('output/词云图.jpg')
    plt.imshow(wc)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    generate_wordcloud()
