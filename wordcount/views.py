from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def count(request):
    full_text = request.GET['fulltext']
    
    word_list = full_text.lower().split() #모두 소문자로 저장
    
    word_dictionary = {}
    
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    
    for key in word_dictionary.keys():
        if key == "fuck":
            word_dictionary["XXXX"] = word_dictionary.pop(key) #욕은 X로 저장
        
    return render(request, 'wordcount/count.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items() })


