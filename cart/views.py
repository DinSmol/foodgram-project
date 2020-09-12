from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from recipes.models import Recipe
from .cart import Cart


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Recipe, id=product_id)
    cart.add(product=product)



def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    # import pdb; pdb.set_trace()
    print(cart.__dict__)
    res = []
    for val in cart.cart.values():
        res.append(val)
    # import pdb; pdb.set_trace()
    return render(request, 'shopList.html', {'cart': res})


# from django.shortcuts import get_object_or_404
# from django.utils.datastructures import MultiValueDictKeyError
# from rest_framework.response import Response
# from rest_framework import status, viewsets, filters
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from .permissions import IsOwnerOrReadOnly
# from .models import Post, Comment, Group, Follow
# from .serializers import PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer



# class PurchasesView(viewsets.ModelViewSet):
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#     def get_queryset(self):
#             queryset = Post.objects.all()
#             group = self.request.query_params.get('group', None)
#             if group is not None:
#                 queryset = queryset.filter(group=group)
#             return queryset

#     def perform_create(self, serializer):
#         if serializer.is_valid:
#             serializer.save(author=self.request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
import json

# from .models import Article
# from .serializers import ArticleSerializer


class PurcasesView(APIView):
    def get(self, request):
        # articles = Article.objects.all()
        # serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    def post(self, request, *args, **kwargs):
        
        id = request.data.get('id')
        cart = Cart(request)
        product = get_object_or_404(Recipe, id=id)
        cart.add(product=product)
        return render(request, 'shopList.html', {'cart': cart})
        # article = request.data.get("article")
        # # Create an article from the above data
        # serializer = ArticleSerializer(data=article)
        # if serializer.is_valid(raise_exception=True):
        #     article_saved = serializer.save()
        # return Response({"success": "Article '{}' created successfully".format(article_saved.title)})

    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()

        return Response({
            "success": "Article '{}' updated successfully".format(article_saved.title)
        })

    def delete(self, request):
        id = request.data.get('id')
        cart = Cart(request)
        cart.remove(product=product)
        return Response(status=status.HTTP_204_NO_CONTENT)