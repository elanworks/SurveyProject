from . import models as m


class PostModelForm(forms.ModelForm):
	class Meta:
		model = m.Post
