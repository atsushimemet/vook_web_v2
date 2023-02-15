from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "vook_web/index.html", {})


def product_page(request, product_name):
    # 商品ページのビュー関数
    return render(request, "vook_web/product_page.html", {"product_name": product_name})
