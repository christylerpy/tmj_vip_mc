# -*- coding: utf-8 -*-
import re
import pandas as pd
import functools


class MiddlewareArsenal:
    """
    -*- 容器 -*-
    使用类作为容器放置各种数据处理中间件函数, 函数名称对应doc_reference中的identity.
    然后把函数转换成字典形式保存, 需要处理数据时直接用identity来索引调用.
    注: 不需要实例化此类, 调用实例方法时, self指定为None即可
    """

    def mc_daily_sales(self, **kwargs) -> pd.DataFrame():
        print('mc_daily_sales')

    def vip_daily_sales(self, **kwargs) -> pd.DataFrame():
        print('vip_daily_sales')


middleware_dict = MiddlewareArsenal.__dict__
aa = []
bb = []
for func_name, func in middleware_dict.items():
    if not re.match(r'^__\w+__$', func_name):  # 如果有大量的regular匹配需求, 最好先调用compile
        aa.append(func_name)
        bb.append(functools.partial(func, self=None))
middleware_arsenal = dict(zip(aa, bb))

middleware_arsenal["vip_daily_sales"]()


# dd()


class AssemblyLines:
    """
    -*- 容器 -*-
    各个dataframe之间的整合所需的加工函数在此类的内部类中定义.
    dataframe之间有主、从的区分, 1主单/多从的方式调用.
    主从索引都是identity, 通过内部类的类属性来定义操作method的实参
    所有的内部类的操作method统一命名为assemble, 因此内部类的method定义为class method会更方便调用.
    注: 不需要实例化此类, 直接调用类方法
    """

    class VipElementWiseStockInventory:
        """
        匹配每个唯品条码对应的各仓库存, 首先应把唯品条码map到tmj组合及单品.

        """
        pass

    class VipElementWiseDailySales:
        pass

    class McElementWiseDailySales:
        pass

    class VipCombinedWithMc:
        pass

    class VipNotes:
        pass
