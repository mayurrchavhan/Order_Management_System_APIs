from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Order, OrderItem
from django.contrib.auth.models import User
from .serializers import ProductSerializer, UserSerializer, OrderSerializer
from django.contrib.auth.hashers import make_password


@api_view(['POST'])
def register_user(request):
    data = request.data
    user = User.objects.create(
        first_name=data['name'],
        username=data['email'],
        email=data['email'],
        password=make_password(data['password'])
    )
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_user_profile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_user_by_id(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_order_items(request):
    user = request.user
    data = request.data

    order_items = data['order_items']

    if order_items and len(order_items) == 0:
        return Response({'detail': 'No Order Items'})
    else:
        # create order
        order = Order.objects.create(
            user=user,
            Price=data['Price'],
        )
    # orderItem in order for-loop
        for i in order_items:
            product = Product.objects.get(_id=i['product'])
            item = OrderItem.objects.create(
                product=product,
                order=order,
                name=product.name,
                qty=i['qty'],
                price=i['price'],
                image=product.image.url,
            )
        # update stock
            product.countInStock -= item.qty
            product.save()
    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_orders(request):
    try:
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)
    except:
        return Response({'detail': 'Order does not exist'})


@api_view(['GET'])
def get_order_by_id(request, pk):
    try:
        order = Order.objects.get(_id=pk)
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)
    except:
        return Response({'detail': 'Order does not exist'})

