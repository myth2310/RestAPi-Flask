from flask import Flask,jsonify
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)


data = [
    {
        "title" : "Cara Memasak",
        "desc" : "Cara sederhana memasak",
        "img" : "https://www.bing.com/ck/a?!&&p=c7b9b30eb32607f7JmltdHM9MTY5NDkwODgwMCZpZ3VpZD0wOTY0YWQxMS0zODJlLTY1OTAtMzE4MC1iZTlkMzk1OTY0MmEmaW5zaWQ9NTY1OQ&ptn=3&hsh=3&fclid=0964ad11-382e-6590-3180-be9d3959642a&u=a1L2ltYWdlcy9zZWFyY2g_cT1nYW1iYXIgcG9yb3JvJkZPUk09SVFGUkJBJmlkPTlCNUIyRkQ4RDUzQzQyQjY4QTNFMUQ2MURDNTk4MTVCQzE1MDVDMkY&ntb=1"
    },
    {
        "title" : "Cara Mencuci",
        "desc" : "Cara sederhana memasak",
        "img" : "https://www.bing.com/ck/a?!&&p=c7b9b30eb32607f7JmltdHM9MTY5NDkwODgwMCZpZ3VpZD0wOTY0YWQxMS0zODJlLTY1OTAtMzE4MC1iZTlkMzk1OTY0MmEmaW5zaWQ9NTY1OQ&ptn=3&hsh=3&fclid=0964ad11-382e-6590-3180-be9d3959642a&u=a1L2ltYWdlcy9zZWFyY2g_cT1nYW1iYXIgcG9yb3JvJkZPUk09SVFGUkJBJmlkPTlCNUIyRkQ4RDUzQzQyQjY4QTNFMUQ2MURDNTk4MTVCQzE1MDVDMkY&ntb=1"
    },
    {
        "title" : "Cara Menyupir",
        "desc" : "Cara sederhana memasak",
        "img" : "https://www.bing.com/ck/a?!&&p=c7b9b30eb32607f7JmltdHM9MTY5NDkwODgwMCZpZ3VpZD0wOTY0YWQxMS0zODJlLTY1OTAtMzE4MC1iZTlkMzk1OTY0MmEmaW5zaWQ9NTY1OQ&ptn=3&hsh=3&fclid=0964ad11-382e-6590-3180-be9d3959642a&u=a1L2ltYWdlcy9zZWFyY2g_cT1nYW1iYXIgcG9yb3JvJkZPUk09SVFGUkJBJmlkPTlCNUIyRkQ4RDUzQzQyQjY4QTNFMUQ2MURDNTk4MTVCQzE1MDVDMkY&ntb=1"
    },
]

class GetAllData(Resource):
    def get(self):
        output = jsonify(data)
        return output

class GetDetailData(Resource):
    def get(self,id):
        index = id
        selectData = data[index]
        output = jsonify(selectData)
        return output

api.add_resource(GetAllData,"/api/data", methods=["GET"])
api.add_resource(GetDetailData,"/api/data/<int:id>", methods=["GET"])

if __name__ == "__main__":
    app.run(debug=True,port=5000)