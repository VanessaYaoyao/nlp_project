from django.shortcuts import render
# Create your views here.
from .fun import Autochecker4Chinese
import string
def index(request):
    if request.method=='POST':
        sentences = request.POST.get('sentences')
        if not sentences:
            msg = '输入内容不能为空'
            return render(request, 'index.html', {'msg': msg})
        for i in sentences:
            if i<'\u4e00' or '\u9fff'<i and (i in string.punctuation) :
                msg = '输入内容不合规'
                return render(request, 'index.html', {'msg': msg})
        correct_sent = Autochecker4Chinese.auto_correct_sentence(sentences)
        lst=[]
        for j in range(len(sentences)):
            if sentences[j]!=correct_sent[j]:
                lst.append(j)
        original_sentence=sentences
        corrected_sentence=correct_sent
        return render(request,'index.html',{'original_sentence': original_sentence,'corrected_sentence':corrected_sentence,'lst':lst})

    else:
        return render(request,'index.html')