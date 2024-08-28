from rest_framework.routers import DefaultRouter

from rating_revolution.views import CompanyViewSet, ReviewerViewSet, ReviewViewSet, LoginViewSet

router = DefaultRouter()

router.register(r'companies', CompanyViewSet, basename='companies')
router.register(r'reviewers', ReviewerViewSet, basename='reviewers')
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'auth', LoginViewSet, basename='login')

urlpatterns = router.urls
