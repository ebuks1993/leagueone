from rest_framework.pagination import PageNumberPagination

class gamePagination (PageNumberPagination):
    max_page_size=8
