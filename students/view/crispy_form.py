
from django.forms import ModelForm
from ..models import Podii
from crispy_forms.helper import FormHelper
from django.core.urlresolvers import reverse


#form
class form(ModelForm):
    class Meta:
        model = Podii
        fields = '__all__'

    def __init__(self,*args, **kwargs):
        super(form,self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

            # return HttpResponseRedirect(
            #     u'%s?status_message=5' %  reverse('main'))


        # set form tag attributes
        self.helper.form_action = reverse('podii_add')
        # self.helper.form_action = u'%s?status_message=5' % reverse('podii_add')

        self.helper.form_method = 'POST'
        self.helper.form_class = 'col-sm-12 form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-8 input-group'