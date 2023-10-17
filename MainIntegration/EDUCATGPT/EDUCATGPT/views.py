from django.shortcuts import render
from django.http import JsonResponse
import json
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .mainintegration7 import  chatBot, load_chat_state
@csrf_exempt 

def load_chat(request):
    try:
        print("load chat \n")
        body_unicode = request.body.decode('utf-8')
        request_data = json.loads(body_unicode)
        print(request_data)
        print("\n\n")      #request data é um array onde o index 0 tem um array de dicts para a memoria do chat e o index 1 tem um dict de metadados do chat
        print(type(request_data))
        load_chat_state(request_data[0], request_data[1])
        return JsonResponse({'load status': "sucess"})
    
    except Exception as e:

        print("entrou na função de load com erro")
        return JsonResponse({"error teste": str(e)})
@csrf_exempt 
def chat(request):
   if request.method == "POST":
        try:
            # Obtenha a mensagem do usuário do corpo da solicitação
            body_unicode = request.body.decode('utf-8')
            request_data = json.loads(body_unicode)
            print(request_data)
            user_message = request_data
            print(type(user_message))      

            #Chame o modelo de chat com a mensagem do usuário
            botClass = chatBot(user_message)
            response = botClass.chatModel()
        
        
            #Obtenha a resposta gerada pelo chatbot
            bot_response = response['assistant']  #key 'assistent' para o bot e 'user' para o usuario
            print(bot_response)
            print("entrou na função sem erro")
            #Retorne a resposta como JSON
            return JsonResponse({'assistant': bot_response})

        except Exception as e:
            print("entrou na função de chat com erro")
            return JsonResponse({"error teste": str(e)})
   else: 
        return JsonResponse({"teste GET": "teste GET"})
  

