with sr. Microphone() as source:
  print('[search python search Youtube]')
  print('speak Now!! \n')
  audio r3.listen(source)
  if 'python' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url='https://www.edureka.co/'
    with sr.Microphone() as source:
      print('\n search the query \n')
      audio r2.listen(source)
    try:
      get r2.recognize_google(audio)
      print(get) wb.get().open_new(url+get)
    except sr.UnknownValueError:
        print('Unable to recognize')
    except sr.RequestError as e: 
      print('failed'.format(e))
  if 'video' in r1.recognize_google(audio):
    r1= sr. Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
      print('\n search the query \n')
      audio r2.listen(source)
      try:
        get r1.recognize_google(audio)
        print(get) 
        wb.get().open_new(url+get)
      except sr.UnknownValueError:
        print('Unable to recognize')
      except sr. RequestError as e:
        print('failed'.format(e))
