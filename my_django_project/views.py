from django.http import HttpResponse
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('''
            <h2>API Service</h2>
            <hr>
            <br>
            取得API 1 (Swagger REST API List) ➜ <a href="./swagger/">Http://localhost:8000/swagger/</a>
            <br>
            取得API 2 (Default REST API List) ➜ <a href="./api/">Http://localhost:8000/api/</a>
            <hr>
            Admin View Data ➜ <a href="./admin/">Http://localhost:8000/admin/</a>
        ''')
