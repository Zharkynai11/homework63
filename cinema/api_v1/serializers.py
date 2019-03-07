from webapp.models import *
from rest_framework import serializers

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:category-detail')

    class Meta:
        model = Category
        fields = ('url', 'id', 'name', 'description')

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:movie-detail')
    category = CategorySerializer(many=True)
    class Meta:
        model = Movie
        fields = ('url', 'id', 'name', 'description', 'poster', 'release_date', 'finish_date','category')

class HallSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:hall-detail')

    class Meta:
        model = Hall
        fields = ('url', 'id', 'name')

class SeatSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:seat-detail')
    hall = HallSerializer(many=True)
    class Meta:
        model = Seat
        fields = ('url', 'id', 'raw', 'pos','hall')


class SaleSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:sale-detail')
    class Meta:
        model = Sale
        fields = ('url', 'id', 'name', 'amount','begin','end')

class ShowSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:show-detail')
    hall = HallSerializer()
    movie = MovieSerializer()
    class Meta:
        model = Show
        fields = ('url', 'id', 'begin', 'end', 'price','hall','movie')

class ReserveSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:reserve-detail')
    show = ShowSerializer()
    seats = SeatSerializer(many=True)

    class Meta:
        model = Reserve
        fields = ('url', 'id', 'code', 'status','created','updated','show','seats')

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:ticket-detail')
    show = ShowSerializer()
    seat = SeatSerializer()
    sale = SaleSerializer()

    class Meta:
        model = Ticket
        fields = ('url', 'id', 'returned','show','seat','sale')
