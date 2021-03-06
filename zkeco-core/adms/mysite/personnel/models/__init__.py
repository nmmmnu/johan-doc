#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from base.models import CachingModel
from base.operation import Operation,ModelOperation
from model_emp import Employee, EmpForeignKey
from model_area import Area
from model_dept import Department
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from depttree import DeptTree,ZDeptChoiceWidget,ZDeptMultiChoiceWidget
from empwidget import ZEmpChoiceWidget
from model_morecardempgroup import AccMoreCardEmpGroup
from model_report import EmpItemDefine
from model_leave import LeaveLog
from model_issuecard import CardType,IssueCard
from model_empchange import EmpChange

verbose_name=_(u"人事")
_menu_index=1
def app_options():
    from base.options import  SYSPARAM,PERSONAL
    return (
        #参数名称, 参数默认值，参数显示名称，解释
        ('personnel_default_page','data/personnel/Employee/', u"%s"%_(u'人事默认页面'), '',PERSONAL,False),
    )

def testlarge():
    for i in range(2,51):
        t=Department()
        t.name="dept_" + str(i)
        t.parent_id=i
        t.save()
        
        for j in range(100):
            x=Department()
            x.name="dept_" + str(i) + "_" + str(j)
            x.parent=t
            x.save()
                
    
