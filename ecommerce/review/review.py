from decimal import Decimal

from checkout.models import DeliveryOptions
from django.conf import settings
from store.models import Product


class review:
    """
    A base review class, providing some default behaviors that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        review = self.session.get(settings.review_SESSION_ID)
        if settings.review_SESSION_ID not in request.session:
            review = self.session[settings.review_SESSION_ID] = {}
        self.review = review

    def add(self, product, qty):
        """
        Adding and updating the users review session data
        """
        product_id = str(product.id)

        if product_id in self.review:
            self.review[product_id]["qty"] = qty
        else:
            self.review[product_id] = {"price": str(product.regular_price), "qty": qty}

        self.save()

    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and return products
        """
        product_ids = self.review.keys()
        products = Product.objects.filter(id__in=product_ids)
        review = self.review.copy()

        for product in products:
            review[str(product.id)]["product"] = product

        for item in review.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item

    def __len__(self):
        """
        Get the review data and count the qty of items
        """
        return sum(item["qty"] for item in self.review.values())

    def update(self, product, qty):
        """
        Update values in session data
        """
        product_id = str(product)
        if product_id in self.review:
            self.review[product_id]["qty"] = qty
        self.save()

    def get_subtotal_price(self):
        return sum(Decimal(item["price"]) * item["qty"] for item in self.review.values())

    def get_delivery_price(self):
        newPrice = 0.00

        if "purchase" in self.session:
            newPrice = DeliveryOptions.objects.get(id=self.session["purchase"]["delivery_id"]).delivery_price

        return newPrice

    def get_total_price(self):
        newPrice = 0.00
        subtotal = sum(Decimal(item["price"]) * item["qty"] for item in self.review.values())

        if "purchase" in self.session:
            newPrice = DeliveryOptions.objects.get(id=self.session["purchase"]["delivery_id"]).delivery_price

        total = subtotal + Decimal(newPrice)
        return total

    def review_update_delivery(self, deliveryPrice=0):
        subtotal = sum(Decimal(item["price"]) * item["qty"] for item in self.review.values())
        total = subtotal + Decimal(deliveryPrice)
        return total

    def delete(self, product):
        """
        Delete item from session data
        """
        product_id = str(product)

        if product_id in self.review:
            del self.review[product_id]
            self.save()

    def clear(self):
        # Remove review from session
        del self.session[settings.review_SESSION_ID]
        # del self.session["address"]
        # del self.session["purchase"]
        self.save()

    def save(self):
        self.session.modified = True
