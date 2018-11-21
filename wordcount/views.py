from django.http import HttpResponse
from django.shortcuts import render
import operator

def home_page(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    full_text = request.GET['fulltext']
    # Split given text with space as separator.
    word_splitted = full_text.split()
    # Empty dict for adding words as keys and counts as value.
    word_dict = {}
    for word in word_splitted:
        if word in word_dict:
            # Increase the number
            word_dict[word] += 1
        else:
            # Add to the dictionary
            word_dict[word] = 1
    # Getting list of tuples [(key, value)...]
    word_list = word_dict.items()
    # Sort word_list based on count value.
    sorted(word_list, key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'full_text': full_text, 
                                          'count': len(word_splitted),
                                          'word_dict': word_list})