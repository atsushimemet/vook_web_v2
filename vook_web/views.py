from django.shortcuts import render


# Create your views here.
def index(request):
    products = ["denim-501-50s-XX", "denim-501-50s-BigE", "denim-501-50s-赤耳"]
    return render(
        request,
        "vook_web/index.html",
        {
            "product_0": products[0],
            "product_1": products[1],
            "product_2": products[2],
        },
    )


def product_page(request, product_name):
    # 商品ページのビュー関数
    return render(request, "vook_web/product_page.html", {"product_name": product_name})
