from bs4 import BeautifulSoup
import json
import requests


def cache_products(brand):
    def response_decorator(response_func):
        def wrapper():
            products = response_func()

            try:
                f = open("products.json", "r+")
                file_data = json.load(f)
                f.seek(0)
            except FileNotFoundError:
                f = open("products.json", "w")
                file_data = dict()
            finally:
                file_data[brand] = products
                json.dump(file_data, f, indent=4)
                f.close()

            return products

        return wrapper

    return response_decorator


@cache_products("Sennheiser")
def sennheiser_response():
    items = []

    url = "https://en-ca.sennheiser.com/music-headphones-portable"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    search_results = soup.find("div", attrs={"class": "layout", "id": "search-results__resultlist"}).find_all("article")

    for result in search_results:
        item_attrs = json.loads(result.attrs["data-gtm-impression"])

        name = item_attrs["name"]
        image_src = result.find("img").get("data-srcset").split(",")[0].split(" ")[0].strip()
        price = str(item_attrs["price"])

        product = {"name": name, "image_url": image_src, "price": price}
        items.append(product)

    return items


@cache_products("JBL")
def jbl_response():
    items = []

    url = "https://ca.jbl.com/headphones/?brwseAll=true"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    search_results = soup.find("div", class_="search-result-items").find_all("div", class_="grid-tile product-tile")

    for result in search_results:
        name = result.find("a", class_="productname-link").get("title")
        image_src = result.find("img").get("data-src")
        price = result.find("a", class_="product-pricing").text.strip().split("\n")[0][1:]

        product = {"name": name, "image_url": image_src, "price": price}
        items.append(product)

    return items


@cache_products("Skullcandy")
def skullcandy_response():
    items = []

    url = "https://www.skullcandy.ca/shop/"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    search_results = soup.find("div", class_="productGrid").find_all("div", class_="card-content")

    for result in search_results:
        name = result.get("data-ga-name")
        image_src = result.find("img").get("data-src")
        price = result.get("data-ga-price")

        product = {"name": name, "image_url": image_src, "price": price}
        items.append(product)

    return items
