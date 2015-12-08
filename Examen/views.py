from django.shortcuts import render, redirect
from .models import Examen
from .forms import ContestarExamenForm


def ver_examenes(request):
    # hacer prueba
    examenes = Examen.objects.all()

    return render(request, 'Examen/ver_examenes.html', {'examenes': examenes})


def revisar_examen(request):
    calificacion = 0
    if request.method == "POST":
        form = ContestarExamenForm(request.POST)
        if form.is_valid():
            examenC = Examen.objects.get(id=request.POST.get('id'))
            examenN = form.save(commit=False)
            if(examenC.respuesta1 == examenN.respuesta1):
                calificacion += 20
            if(examenC.respuesta2 == examenN.respuesta2):
                calificacion += 20
            if(examenC.respuesta3 == examenN.respuesta3):
                calificacion += 20
            if(examenC.respuesta4 == examenN.respuesta4):
                calificacion += 20
            if(examenC.respuesta5 == examenN.respuesta5):
                calificacion += 20
        else:
            return redirect('examenes')
    return redirect('examenes')


def contestar_examen(request):
    examen = None
    if request.POST.get('id'):
        examen = Examen.objects.get(id=request.POST.get('id'))
        form = ContestarExamenForm()
        form.fields['respuesta1'].label = examen.pregunta1
        form.fields['respuesta2'].label = examen.pregunta2
        form.fields['respuesta3'].label = examen.pregunta3
        form.fields['respuesta4'].label = examen.pregunta4
        form.fields['respuesta5'].label = examen.pregunta5
    return render(request, 'Examen/contestar_examen.html',{'form':form, 'id':examen.id, 'titulo':examen.titulo})

    #else:
        # estado = Estado.objects.get(id=request.POST.get('id'))
        # form = EstadoForm(request.POST, instance=estado)
        # if form.is_valid():
        #     estado = form.save()
        #     estado.save()
        #     return redirect('listar')
    # return render(request, 'estados/estado_nuevo.html', {'form': form,'id':estado.id, 'etiqueta':'Actualizar'})
    # if request.method == "POST":
    #     form = ExamenForm(request.POST)
    #     if form.is_valid():
    #         examen = form.save()
    #         examen.save()
    #         return redirect('examenes')
    # else:
    #     examen = Examen.objects.get(id=request.POST.get('id'))
    #     preguntas = [examen.titulo, examen.pregunta1,
    #         examen.pregunta2, examen.pregunta3, examen.pregunta4, examen.pregunta5]
    #     form = ContestarExamenForm()
    # return render(request, 'Examen/contestar_examen.html',{'form':form, 'preguntas':preguntas})
