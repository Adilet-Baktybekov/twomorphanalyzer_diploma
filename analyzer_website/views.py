from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
import mimetypes
from django.http.response import HttpResponse
import os
import sys
import csv
import re
sys.path.append('../backend/main_analyzer.py')
from backend.main_analyzer import Word
from .models import *

def home(request):
    return render(request, 'analyzer_website/main.html')

def about(request):
    all_content_kg = KyrgyzLang.objects.all()
    all_modal_window = ModalWindow.objects.all()
    print(all_modal_window)
    return render(request, 'analyzer_website/about.html', {'all_content_kg': all_content_kg, 'all_modal_window': all_modal_window})

def analyzer(request):
      return render(request, 'analyzer_website/analyzer.html')
def analyzer2(request):
    return render(request, 'analyzer_website/analyzer2.html')
def validate(request):
   if request.method == 'POST':
      word = request.POST["words"]
      ans = Word(word)
      res = ans.search_word_db(ans.change_word)
      root = ans.root
      part_of_speech = ans.part_of_speech
      all_symbols = ans.symbols_list
      all_endings = ans.symbols
      text_res = ans.result_text
      dict = {
          'word': word,
          'root': root,
          'part_of_speech': part_of_speech,
          'all_symbols': all_symbols,
          'all_endings': all_endings,
          'text': text_res
      }
      return render(request, 'analyzer_website/response.html', dict)
dict = {}
def validate2(request):
   if request.method == 'POST':

       sentences = request.POST["words"]
       sentences = str(sentences).strip()
       #sentences_list = re.split(r'[!.?]', sentences)
       all_text = ''
       text = ''
       '''for sentence in sentences_list:
           sentence = str(sentence).lstrip()'''
       words_list = sentences.split(' ')
       for word in words_list:
           word = str(word).strip()
           ans = Word(word)
           res = ans.search_word_db(ans.change_word)
           all_text = all_text + str(ans.result_text) + ' '

       dict = {
           'sentences': sentences,
           'res': all_text
       }
       return render(request, 'analyzer_website/response2.html', dict)
def validate3(request):
   if request.method == 'POST':
      word = request.POST["words"]
      symbols = request.POST["symbols"]
      all = word + ", " + symbols
      arr = all.split(',')
      with open('backend/csv_files/new_words.csv', 'a', encoding='UTF8', newline='') as f:
          writer = csv.writer(f, delimiter=";")
          writer.writerow(arr)
      return render(request, 'analyzer_website/response.html', dict)

def upload(request):
    text = ''
    sentences = ''
    all_text = ''
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        text = uploaded_file.read().decode('utf-8', errors='ignore')
        #text = str(text)[2:]
        #text = str(text)[:-1]
        #print(text)
        #f = open(str(uploaded_file), "r")
        #print(f.read())
        sentences = str(text).strip()
        # sentences_list = re.split(r'[!.?]', sentences)
        all_text = ''
        text = ''
        words_list = sentences.split(' ')
        for word in words_list:
            word = str(word).strip()
            if not word == '':
                ans = Word(word)
                res = ans.search_word_db(ans.change_word)
                all_text = all_text + str(ans.result_text) + ' '
    file = open("myfile.txt", 'w', encoding='UTF8')
    file.write(str(all_text))
    file.close()
    dict = {
        'sentences': sentences,
        'res': all_text
    }
    return render(request, 'analyzer_website/response2.html', dict)
def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'myfile.txt'
    # Define the full file path
    filepath = BASE_DIR + '/' + filename
    # Open the file for reading content
    path = open(filepath, 'r', encoding='UTF8')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response