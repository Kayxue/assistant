from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Expense
from .forms import *

## Create your views here.
## 支出紀錄列表
class ExpenseList(LoginRequiredMixin, ListView):
    model = Expense
    ordering = ['-id']  # 反向排序
    paginate_by = 10    # 每頁顯示幾筆

## 新增支出紀錄
class ExpenseCreate(LoginRequiredMixin, CreateView):
    #model = Expense
    form_class = MoneyForm
    model = Expense
    template_name = 'form.html'         # 指定使用 form.html 這個頁面範本

    def get_success_url(self):
        return reverse('expense_list')  # 新增成功返回支出紀錄列表頁面

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '新增支出'
        return context

## 修改支出紀錄
class ExpenseUpdate(LoginRequiredMixin, UpdateView):
    form_class = MoneyForm
    model = Expense
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('expense_list')  # 修改成功返回支出紀錄列表頁面
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '修改支出'
        return context

## 刪除支出紀錄
class ExpenseDelete(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse('expense_list')  # 刪除成功返回支出紀錄列表頁面

class Userinfo(LoginRequiredMixin, TemplateView):
    template_name="userinfo.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '使用者資訊'
        return context
