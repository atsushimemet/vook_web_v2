from django.shortcuts import render

from .forms import SearchForm


# Create your views here.
def index(request):
    products = [
        "levis-denim-501-50s-XX",
        "levis-denim-501-50s-BigE",
        "levis-denim-501-50s-赤耳",
    ]
    return render(
        request,
        "vook_web/index.html",
        {
            "product_0": products[0],
            "product_1": products[1],
            "product_2": products[2],
        },
    )


def about(request):
    return render(
        request,
        "vook_web/about.html",
        {},
    )


def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            brand = form.cleaned_data["brand"]
            item = form.cleaned_data["item"]
            model = form.cleaned_data["model"]
            age = form.cleaned_data["age"]
            # ここでフォームの値を使用して、ページをレンダリングする
            context = {"brand": brand}
            return render(
                request,
                "vook_web/product_page.html",
                {"brand": brand, "item": item, "model": model, "age": age},
            )
    else:
        form = SearchForm()
    context = {"form": form}
    return render(request, "vook_web/search.html", context)


def article(request):
    return render(
        request,
        "vook_web/article.html",
        {},
    )


def community(request):
    return render(
        request,
        "vook_web/community.html",
        {},
    )


def product_page(request, product_name):
    # 商品ページのビュー関数
    return render(request, "vook_web/product_page.html", {"product_name": product_name})
