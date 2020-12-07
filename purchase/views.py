# coding=utf8

from django.shortcuts import render
from pyecharts.charts import Bar
from django_echarts.views.backend import EChartsBackendView


class BackendEChartsTemplate(EChartsBackendView):
    template_name = "chart.html"

    def get_echarts_instance(self, *args, **kwargs):
        bar = Bar("我的第一个图表", "这里是副标题")
        bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
        abc = PurchaseStatusModel.objects.raw(
            "select ps.id, ps.quantity, subq.status, subq.created_at from (select pid, status, created_at from (select purchase_id as pid, status, created_at, row_Number()  over (Partition by purchase_id order by (case when status = 'dispatched' then 1 when status = 'delivered' then 2 end )) as rn from purchase_purchasestatusmodel) as sqb group by 1,2,3, sqb.rn having rn = max(rn)) as subq inner join purchase_purchasemodel as ps on ps.id = pid"
        )
        return bar
