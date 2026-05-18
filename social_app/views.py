from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Post, Comentario, Like


def pagina_inicial(request):
    posts = Post.objects.all().order_by('-criado_em')
    return render(request, 'social_app/pagina_inicial.html', {'posts': posts})


def detalhe_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentarios = post.comentarios.all().order_by('criado_em')

    if request.method == 'POST':
        texto = request.POST.get('texto')
        if texto and request.user.is_authenticated:
            Comentario.objects.create(post=post, autor=request.user, texto=texto)
        return redirect('detalhe_post', post_id=post.id)

    return render(request, 'social_app/detalhe_post.html', {
        'post': post,
        'comentarios': comentarios,
    })


def perfil_utilizador(request, username):
    utilizador = get_object_or_404(User, username=username)
    posts = Post.objects.filter(autor=utilizador).order_by('-criado_em')
    return render(request, 'social_app/perfil.html', {
        'utilizador': utilizador,
        'posts': posts,
    })


def dar_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user.is_authenticated:
        like, criado = Like.objects.get_or_create(post=post, utilizador=request.user)
        if not criado:
            like.delete()
    return redirect('pagina_inicial')