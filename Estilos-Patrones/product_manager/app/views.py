from flask import Blueprint, render_template
from .patterns.singleton import ConfigManager
from .patterns.observer import OrderNotifier, User
from .patterns.strategy import StandardShipping, ExpressShipping, FreeShipping
from .patterns.factory import ProductFactory
from .patterns.decorator import BaseProduct, ExtraWarranty, GiftWrap
from .patterns.builder import OrderBuilder

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return render_template("base.html")

@main_bp.route("/singleton")
def singleton_view():
    config = ConfigManager()
    config.set("store_name", "Tech Store")
    store_name = config.get("store_name")
    return render_template("singleton.html", store_name=store_name)

@main_bp.route("/observer")
def observer_view():
    notifier = OrderNotifier()
    user1 = User("Alice")
    user2 = User("Bob")
    notifier.subscribe(user1)
    notifier.subscribe(user2)
    notifier.notify("Order placed!")
    return render_template("observer.html", users=[user1.name, user2.name])

@main_bp.route("/strategy")
def strategy_view():
    weight = 3  # Example weight
    costs = {
        "Standard": StandardShipping().calculate(weight),
        "Express": ExpressShipping().calculate(weight),
        "Free": FreeShipping().calculate(weight)
    }
    return render_template("strategy.html", costs=costs)

@main_bp.route("/factory")
def factory_view():
    laptop = ProductFactory.create_product("laptop")
    phone = ProductFactory.create_product("phone")
    return render_template("factory.html", products=[laptop, phone])

@main_bp.route("/decorator")
def decorator_view():
    base_product = BaseProduct("Tablet", 300)
    customized_product = GiftWrap(ExtraWarranty(base_product))
    return render_template("decorator.html", product=customized_product.description(), cost=customized_product.cost())

@main_bp.route("/builder")
def builder_view():
    builder = OrderBuilder()
    builder.add_product(GiftWrap(BaseProduct("Laptop", 1000)))
    builder.add_product(ExtraWarranty(BaseProduct("Phone", 500)))
    builder.set_shipping(StandardShipping().calculate(5))
    order = builder.build()
    return render_template("builder.html", order=order.details())
