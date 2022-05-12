from django.shortcuts import render, redirect
from .models import VideoSugestao, Menssagens, SobreMim
from random import choice
from django.contrib import messages
import requests
from json import loads
from decouple import config


def index(request):
    menssagens_obj = Menssagens.objects.order_by('-id')
    videos_obj = VideoSugestao.objects.order_by('-id')
    detalhes_sobre_mim = SobreMim.objects.all()[0]

    if request.method != 'POST':
        return render(request, 'index.html', {
            'menssagens': menssagens_obj,
            'videos': videos_obj,
            'aleatorio': choice(videos_obj),
            'sobremim': detalhes_sobre_mim,
        })
    
    usuario = request.POST.get('usuario')
    menssagem = request.POST.get('menssagem')
    salvar = Menssagens(usuario=usuario, menssagem=menssagem)

    captcha_token = request.POST.get('g-recaptcha-response')
    cap_url = 'https://www.google.com/recaptcha/api/siteverify'
    cap_secret = config('cap_secret')#coloque seu hash do captcha se acordo com o que irá no front. Tudo nas variavis no arquivo .env que vc criará na raiz do projeto
    cap_data = {'secret': cap_secret, 'response': captcha_token}
    cap_server_response = requests.post(url=cap_url, data=cap_data)
    cap_json = loads(cap_server_response.text)
    if not cap_json['success']:
        messages.error(request, 'Resposta do captcha Errada!')
        return redirect('index')
    try:
        if len(usuario) < 3 or len(menssagem) < 3:
            messages.info(request, 'Nome de usuário e menssagem precisa ser maior que 3 caracteres!')
            return redirect('index')

    except TypeError:
        pass
    else:
        messages.success(request, 'Menssagem Enviada!')
        salvar.save()

    link_video = request.POST.get('linkvideo')
    user_video = request.POST.get('usuariovideo')

    link_base = ''
    try:
        if len(user_video) < 3:
            messages.info(request, 'Usuário da Sugestão precisa ser maior que 3 caractere!')
            return redirect('index')

        if 'youtu' in link_video and '=' not in link_video:
                    link_base = 'https://www.youtube.com/embed/' + link_video.split('/')[-1]

        elif 'youtu' in link_video:
            depoisigual = link_video.find('=')
            link_base = 'https://www.youtube.com/embed/' + link_video[depoisigual+1:]

        elif 'vimeo' in link_video:
            link_base = 'https://player.vimeo.com/video/' + link_video.split('/')[-1]

        else:
            messages.error(request, 'Somente Links do Youtube e do Vimeo!')
            return redirect('index')
    except TypeError:
        return redirect('index')

    video = VideoSugestao(link_video=link_base, usuario_video=user_video)
    messages.success(request, 'Sugestão de Video Enviada!')
    video.save()

    return redirect('index')


#Feito por Marcelo Araujo
