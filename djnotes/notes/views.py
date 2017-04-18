from django.shortcuts import render
from django.views.generic import View
from notes.models import Note
from notes.forms import NoteForm
from django.http import Http404

class Index(View):
    template_name = 'notes/index.html'

    def get_context_data(self):
        context = {
                'notes': Note.objects.order_by('-id')
                }
        return context

    # Handles GET Request
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    # Handles POST Request
    def post(self, request, *args, **kwargs):
        form = NoteForm(request.POST)
        context = self.get_context_data()

        if (form.is_valid()):
            form.save()
        return render(request, self.template_name, context )

class Update(View):
	template_name = 'notes/update.html'
	
	def get_context_data(self, **kwargs):
		context = {}
		try:
			note_id = kwargs.get('pk', 0)
			note = Note.objects.get(id=note_id)
		except Note.DoesNotExist:
			raise Http404
		else:
			context['note'] = note
			return context

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		form = NoteForm(request.POST, instance=context.get('note'))
		if form.is_valid():
			form.save()
		return render(request, self.template_name, context)
