from django.http import Http404

class NotLoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            raise Http404()

        return super(NotLoginRequiredMixin, self).dispatch(request, *args, **kwargs)
