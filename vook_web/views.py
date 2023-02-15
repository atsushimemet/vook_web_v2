from django.shortcuts import render


# Create your views here.
def index(request):
    products = ["denim/501/50s/XX", "denim/501/50s/BigE", "denim/501/50s/66前期"]
    return render(request, "vook_web/index.html", {"products": products})


def product_page(request, product_name):
    # 商品ページのビュー関数
    return render(request, "vook_web/product_page.html", {"product_name": product_name})
