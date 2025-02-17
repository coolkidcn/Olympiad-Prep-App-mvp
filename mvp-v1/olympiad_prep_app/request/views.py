from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json
from openai import OpenAI

# Create your views here.
def customRequest(request, input):
    input_dict = json.loads(input)
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        #api_key="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",
        api_key="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",
    )

    system_prompt = """
    "You are a JSON generator. Respond **ONLY** with valid JSON using this schema: {"data": {"answer": "...", "key_points": []}}"
    Dont use backlash n '\n'
    """
    if 'system_prompt' in input_dict.keys():
        system_prompt = input_dict['system_prompt']
    
    user_prompt = "Explain photosynthesis in 3 key points"
    if 'user_prompt' in input_dict.keys():
        user_prompt = input_dict['user_prompt']
         
    messages = [{"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}]

    response = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=messages,
        response_format={
            'type': 'json_object'
        }
    )
    if response.choices != None:
        response_content = response.choices[0].message.content

        if not response_content:
            return "The response is empty. Let's check why."
            
        else:
            response_content = response_content.strip().replace("```json", "").replace("```", "")
            try:
                data = json.loads(response_content)
                return  response_content
            except json.JSONDecodeError as e:
                pass

    return "No response. Let's check why." 

def request(request):
    data = {
        'message': 'Hello, world!',
        'status': 200
    }
    return JsonResponse(data)

def map(request, user):
    response  = requests.get("http://127.0.0.1:8000/request/")
    response_dict = response.json() 
  
    return JsonResponse(response_dict)

def recall(request, data):
    data = json.loads(data)
    return JsonResponse(data)

def aiRequest(request, input):
    airequest = customRequest(request, input)
    try:
        airequest = json.loads(airequest)
    except ValueError  as e:
            return HttpResponse(airequest + " value")
    except TypeError as e:
         return HttpResponse(airequest + " type")
    return JsonResponse(airequest)
