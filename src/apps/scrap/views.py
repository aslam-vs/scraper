from django.shortcuts import render
from django.views.generic import View

from .lib import scraper_call_fun


class ScrapDetails(View):

    """ScrapDetails view """

    def get(self, request):
        """get method for ScrapDetails """
        return_data = {}

        return render(request, "home.html", return_data)

    def post(self, request):
        """post method for ScrapDetails """

        input_url = request.POST['input_url']
        print input_url

        return_data = scraper_call_fun(input_url)
        return_data['input_url'] = input_url

        return render(request, "home.html", return_data)
