from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from usuarios_fbv.models import Usuario

class usuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'data_nascimento', 'email', 'endereco', 'operadora']

def usuario_list(request, template_nome='usuarios_fbv/usuario_list.html'):
    usuario = usuario.objects.all()
    data = {}
    data['object_list'] = usuario
    return render(request, template_nome, data)

def usuario_create(request, template_nome='usuarios_fbv/usuario_form.html'):
    form = usuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('usuarios_fbv:usuario_list')
    return render(request, template_nome, {'form':form})

def usuario_update(request, pk, template_nome='usuarios_fbv/usuario_form.html'):
    usuario= get_object_or_404(usuario, pk=pk)
    form = usuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('usuarios_fbv:usuario_list')
    return render(request, template_nome, {'form':form})

def usuario_delete(request, pk, template_nome='usuarios_fbv/usuario_confirm_delete.html'):
    usuario= get_object_or_404(usuario, pk=pk)
    if request.method=='POST':
        usuario.delete()
        return redirect('usuarios_fbv:usuario_list')
    return render(request, template_nome, {'object':usuario})
