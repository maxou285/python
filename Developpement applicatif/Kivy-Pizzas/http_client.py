from kivy.network.urlrequest import UrlRequest
import json

class HttpClient:
    def get_pizzas(self, on_complete, on_error):
        url = "https://maximedurand.pythonanywhere.com/api/GetPizzas"

        def data_received(req, result):
            data = json.loads(result)
            pizza_dict = []
            for i in data:
                pizza_dict.append(i["fields"])
            print("data_received")
            if on_complete != None:
                on_complete(pizza_dict)

        def data_error(req, error):
            #print("data_error" + str(error))
            if on_error:
                on_error(str(error))
        def data_failure(req, error):
            print("data_failure")
            if on_error:
                on_error("Erreur serveur : " + str(req.resp_status))

        req = UrlRequest(url, on_success=data_received, on_error=data_error, on_failure=data_failure)