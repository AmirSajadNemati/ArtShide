from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from order.models import Order, OrderDetail
from utils import sms_kaveh
# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView

from account.models import User
from user_panel.forms import EditProfileModelForm, ChangePasswordForm


@method_decorator(login_required, name='dispatch')
class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel/user_panel_dashboard.html'


@login_required()
def user_panel_menu_component(request: HttpRequest):
    return render(request, 'user_panel/components/user_panel_menu_component.html', context={})


@method_decorator(login_required, name='dispatch')
class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(instance=current_user)

        context = {
            'form': edit_form,
            'current_user': current_user
        }
        return render(request, 'user_panel/edit_profile_page.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)

        context = {
            'form': edit_form,
            'current_user': current_user
        }
        return render(request, 'user_panel/edit_profile_page.html', context)

@method_decorator(login_required, name='dispatch')
class UserCoursesPage(View):
    def get(self, requset:HttpRequest):
        user_courses = requset.user.course.filter(is_active=True)
        context = {
            'user_courses': user_courses
        }
        return render(requset, 'user_panel/user_purchased_courses_page.html', context)

@method_decorator(login_required, name='dispatch')
class UserExamsPage(View):
    def get(self, requset:HttpRequest):
        return render(requset, 'user_panel/user_exams_page.html', {})

@method_decorator(login_required, name='dispatch')
class ChangePasswordPage(View):
    def get(self, request: HttpRequest):
        # todo: empty the value of current password
        context = {
            'form': ChangePasswordForm()
        }
        return render(request, 'user_panel/change_password_page.html', context)

    def post(self, request: HttpRequest):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_user: User = User.objects.filter(id=request.user.id).first()
            if current_user.check_password(form.cleaned_data.get('current_password')):
                current_user.set_password(form.cleaned_data.get('password'))
                current_user.save()
                logout(request)
                return redirect(reverse('login-page'))

            else:
                form.add_error('current_password', 'کلمه ی عبور اشتباه می باشد!')

        context = {
            'form': form
        }
        return render(request, 'user_panel/change_password_page.html', context)

# Order
@login_required()
def user_cart(request: HttpRequest):
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)
    total_amount = current_order.calculate_total_price()
    current_user = request.user

    context = {
        'order': current_order,
        'sum': total_amount,
        'current_user': current_user
    }
    return render(request, 'user_panel/user_basket.html', context)


@login_required()
def remove_order_detail(request):
    detail_id = request.GET.get('detail_id')
    if detail_id is None:
        return JsonResponse({
            'status': 'not_found_detail_id'
        })

    deleted_count, deleted_dict = OrderDetail.objects.filter(
        id=detail_id,
        order__is_paid=False,
        order__user__id=request.user.id).delete()

    if deleted_count == 0:
        return JsonResponse({
            'status': 'detail_not_found'
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(
        is_paid=False,
        user_id=request.user.id)
    total_amount = current_order.calculate_total_price()
    print(total_amount)

    context = {
        'order': current_order,
        'sum': total_amount
    }

    return JsonResponse({
        'status': 'success',
        'body': render_to_string('user_panel/user_basket_content.html', context)
    })


