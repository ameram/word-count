from django.shortcuts import render
import operator


def home(request):
    return render(request, 'index.html')


def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_dict = {}

    for word in word_list:
        if word in word_dict:
            # increase
            word_dict[word]+=1
        else:
            word_dict[word] = 1
            # Add

    sorted_word = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'full_text': fulltext[:30], 'count':len(word_list),
                                         'worddict':sorted_word})

def about(request):
    return render(request, 'about.html')
