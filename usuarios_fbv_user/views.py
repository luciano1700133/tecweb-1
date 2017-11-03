from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from usuarios_fbv_user.models import usuario

class usuarioForm(ModelForm):
    class Meta:
        model = usuario
        fields = ['nome', 'ra']

@login_required
def usuario_list(request, template_nome='usuarios_fbv_user/usuario_list.html'):
    if request.user.is_superuser:
        usuario = usuario.objects.all()
    else:
        usuario = usuario.objects.filter(user=request.user)
    data = {}
    data['object_list'] = usuario
    return render(request, template_nome, data)

@login_required
def usuario_create(request, template_nome='usuarios_fbv_user/usuario_form.html'):
    form = usuarioForm(request.POST or None)
    if form.is_valid():
        usuario = form.save(commit=False)
        usuario.user = request.user
        usuario.save()
        return redirect('usuarios_fbv_user:usuario_list')
    return render(request, template_nome, {'form':form})

@login_required
def usuario_update(request, pk, template_nome='usuarios_fbv_user/usuario_form.html'):
    if request.user.is_superuser:
        usuario= get_object_or_404(usuario, pk=pk)
    else:
        usuario= get_object_or_404(usuario, pk=pk, user=request.user)
    form = usuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('usuarios_fbv_user:usuario_list')
    return render(request, template_nome, {'form':form})

@login_required
def usuario_delete(request, pk, template_nome='usuarios_fbv_user/usuario_confirm_delete.html'):
    if request.user.is_superuser:
        usuario= get_object_or_404(usuario, pk=pk)
    else:
        usuario= get_object_or_404(usuario, pk=pk, user=request.user)
    if request.method=='POST':
        usuario.delete()
        return redirect('usuarios_fbv_user:usuario_list')
    return render(request, template_nome, {'object':usuario})
