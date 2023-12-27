from django.urls import path, include

import dashboard.views.dashboard
import dashboard.views.historical_index


urlpatterns = [
    # get index-data (routes for index data)
    path('get-index-data', dashboard.views.historical_index.HistoricalIndexAPIView.get_index_data, name='get-index-data'),
]