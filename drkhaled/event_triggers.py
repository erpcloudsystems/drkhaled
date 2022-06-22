from __future__ import unicode_literals
import frappe
from frappe import auth
import datetime
import json, ast


################ Quotation
@frappe.whitelist()
def quot_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def quot_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def quot_onload(doc, method=None):
    pass
@frappe.whitelist()
def quot_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def quot_validate(doc, method=None):
    pass
@frappe.whitelist()
def quot_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def quot_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def quot_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def quot_before_save(doc, method=None):
    pass
@frappe.whitelist()
def quot_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def quot_on_update(doc, method=None):
    pass


################ Sales Order
@frappe.whitelist()
def so_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def so_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def so_onload(doc, method=None):
    pass
@frappe.whitelist()
def so_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def so_validate(doc, method=None):
    pass
@frappe.whitelist()
def so_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def so_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def so_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def so_before_save(doc, method=None):
    pass
@frappe.whitelist()
def so_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def so_on_update(doc, method=None):
    pass


################ Delivery Note
@frappe.whitelist()
def dn_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def dn_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def dn_onload(doc, method=None):
    pass
@frappe.whitelist()
def dn_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def dn_validate(doc, method=None):
    pass
@frappe.whitelist()
def dn_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def dn_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def dn_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def dn_before_save(doc, method=None):
    pass
@frappe.whitelist()
def dn_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def dn_on_update(doc, method=None):
    pass

################ Sales Invoice
@frappe.whitelist()
def siv_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def siv_after_insert(doc, method=None):
    pass
def siv_onload(doc, method=None):
    pass
@frappe.whitelist()
def siv_before_validate(self, method=None):
    if not self.sales_team:
        frappe.throw("Please Fill Sales Person Table")
    commission = (self.total *10 ) /100
    count_sales_team = len(self.get("sales_team"))
    contribution = 100 / count_sales_team

    if self.sales_team:
        for x in self.sales_team:
            x.allocated_percentage = contribution
            if self.branch == "المرغني":
                if self.service_type == "اصلاح":
                    x.incentives = 8 / count_sales_team
                if self.service_type == "تغيير" and self.total >= 950 and self.total <= 1400:
                    x.incentives = 25 /count_sales_team
                if self.service_type == "تغيير" and self.total < 950:
                    x.incentives = 0
                if self.service_type == "تغيير" and self.total > 1400:
                    x.incentives = 50 /count_sales_team

            if self.branch != "المرغني":
                if self.service_type == "تغيير" and self.total >= 300:
                    x.incentives = 25 / count_sales_team
                if self.service_type == "تغيير" and self.total < 300:
                    x.incentives = 10 / count_sales_team
                if self.service_type == "اصلاح" and count_sales_team == 1:
                    x.incentives = 5
                if self.service_type == "اصلاح" and count_sales_team > 1:
                    x.incentives = 4

            if self.service_type not in ("تغيير", "اصلاح"):
                x.incentives = commission / count_sales_team
    self.sales_team2 = {}
    if not self.sales_team2:
        commission = (self.total *10 ) /100
        count_sales_team = len(self.get("sales_team"))
        contribution = 100 / count_sales_team
        if self.branch in ("عمار بن ياسر", "المعادي","منشية التحرير","ارابيلا","سيتي ستارز","First Mall","المرغني","المهندسين") and self.service_type == "تغيير":
            sales_team = self.append("sales_team2", {})
            sales_team.sales_person = "عمولة الادارة"
            sales_team.incentives = 30
        if self.branch in ("عمار بن ياسر", "المعادي","منشية التحرير","ارابيلا","سيتي ستارز","First Mall","المرغني","المهندسين") and self.service_type == "Anti Fog":
            commission2 = (self.total *20 ) /100
            sales_team = self.append("sales_team2", {})
            sales_team.sales_person = "عمولة الادارة"
            sales_team.incentives = commission2
    if not self.sales_team3:
        if  self.service_type == "تغيير":
            commission3 = (self.total *12 ) /100
            sales_team = self.append("sales_team3", {})
            sales_team.sales_person = "عمولة مشتريات الادارة"
            sales_team.incentives = commission3

@frappe.whitelist()
def siv_validate(self, method=None):
    pass
@frappe.whitelist()
def siv_on_submit(self, method=None):
   '''
    if not self.sales_team:
        commission = (self.total *10 ) /100
        count_sales_team = len(self.get("sales_team"))
        contribution = 100 / count_sales_team
        if self.branch in ("عمار بن ياسر", "المعادي","منشية التحرير","ارابيلا","سيتي ستارز","First Mall","المرغني","المهندسين") and self.service_type == "تغيير":
            commission2 = (self.total *30 ) /100
            sales_team = self.append("sales_team2", {})
            sales_team.sales_person = "عمولة الادارة"
            sales_team.incentives = 30
        if self.branch in ("عمار بن ياسر", "المعادي","منشية التحرير","ارابيلا","سيتي ستارز","First Mall","المرغني","المهندسين") and self.service_type == "Anti Fog":
            commission2 = (self.total *20 ) /100
            sales_team = self.append("sales_team", {})
            sales_team.sales_person = "عمولة الادارة"
            sales_team.incentives = commission2
   
    sales_team = frappe.db.sql(""" select a.sales_person, a.contact_no, a.allocated_percentage, a.allocated_amount, a.commission_rate, a.incentives
		                                                           from `tabDaily Team` b join `tabSales Team` a
		                                                           on a.parent = b.name
		                                                           where b.pos_profile = '{posprofile}'
                                                                   and b.date = '{date}'
                                                                   and b.docstatus = 1
		                                                       """.format(posprofile=self.pos_profile,date=self.posting_date), as_dict=1)

    for c in sales_team:
        sales_team = self.append("sales_team", {})
        sales_team.sales_person = c.sales_person
        sales_team.contact_no = c.contact_no
    '''
@frappe.whitelist()
def siv_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def siv_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def siv_before_save(doc, method=None):
    pass
@frappe.whitelist()
def siv_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def siv_on_update(doc, method=None):
    pass


################ Payment Entry
@frappe.whitelist()
def pe_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def pe_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def pe_onload(doc, method=None):
    pass
@frappe.whitelist()
def pe_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def pe_validate(doc, method=None):
    pass
@frappe.whitelist()
def pe_on_submit(doc, method=None):
    if doc.internal_selling:
        frappe.db.set_value('Internal Selling', doc.internal_selling, 'pe_status', doc.status)
        frappe.db.set_value('Internal Selling', doc.internal_selling, 'paid_amount', doc.paid_amount)
@frappe.whitelist()
def pe_on_cancel(doc, method=None):
    if doc.internal_selling:
        frappe.db.set_value('Internal Selling', doc.internal_selling, 'pe_status', doc.status)
        frappe.db.set_value('Internal Selling', doc.internal_selling, 'paid_amount', 0)
@frappe.whitelist()
def pe_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def pe_before_save(doc, method=None):
    pass
@frappe.whitelist()
def pe_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def pe_on_update(doc, method=None):
    pass

################ Journal Entry
@frappe.whitelist()
def je_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def je_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def je_onload(doc, method=None):
    pass
@frappe.whitelist()
def je_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def je_validate(doc, method=None):
    pass
@frappe.whitelist()
def je_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def je_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def je_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def je_before_save(doc, method=None):
    pass
@frappe.whitelist()
def je_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def je_on_update(doc, method=None):
    pass

################ Material Request
@frappe.whitelist()
def mr_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def mr_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def mr_onload(doc, method=None):
    pass
@frappe.whitelist()
def mr_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def mr_validate(doc, method=None):
    pass
@frappe.whitelist()
def mr_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def mr_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def mr_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def mr_before_save(doc, method=None):
    pass
@frappe.whitelist()
def mr_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def mr_on_update(doc, method=None):
    pass

################ Purchase Order
@frappe.whitelist()
def po_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def po_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def po_onload(doc, method=None):
    pass
@frappe.whitelist()
def po_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def po_validate(doc, method=None):
    pass
@frappe.whitelist()
def po_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def po_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def po_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def po_before_save(doc, method=None):
    pass
@frappe.whitelist()
def po_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def po_on_update(doc, method=None):
    pass

################ Purchase Receipt
@frappe.whitelist()
def pr_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def pr_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def pr_onload(doc, method=None):
    pass
@frappe.whitelist()
def pr_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def pr_validate(doc, method=None):
    pass
@frappe.whitelist()
def pr_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def pr_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def pr_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def pr_before_save(doc, method=None):
    pass
@frappe.whitelist()
def pr_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def pr_on_update(doc, method=None):
    pass


################ Purchase Invoice
@frappe.whitelist()
def piv_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def piv_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def piv_onload(doc, method=None):
    pass
@frappe.whitelist()
def piv_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def piv_validate(doc, method=None):
    pass
@frappe.whitelist()
def piv_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def piv_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def piv_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def piv_before_save(doc, method=None):
    pass
@frappe.whitelist()
def piv_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def piv_on_update(doc, method=None):
    pass

################ Employee Advance
@frappe.whitelist()
def emad_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def emad_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def emad_onload(doc, method=None):
    pass
@frappe.whitelist()
def emad_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def emad_validate(doc, method=None):
    pass
@frappe.whitelist()
def emad_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def emad_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def emad_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def emad_before_save(doc, method=None):
    pass
@frappe.whitelist()
def emad_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def emad_on_update(doc, method=None):
    pass

################ Expense Claim
@frappe.whitelist()
def excl_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def excl_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def excl_onload(doc, method=None):
    pass
@frappe.whitelist()
def excl_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def excl_validate(doc, method=None):
    pass
@frappe.whitelist()
def excl_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def excl_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def excl_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def excl_before_save(doc, method=None):
    pass
@frappe.whitelist()
def excl_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def excl_on_update(doc, method=None):
    pass

################ Stock Entry
@frappe.whitelist()
def ste_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def ste_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def ste_onload(doc, method=None):
    pass
@frappe.whitelist()
def ste_before_validate(doc, method=None):
    basicrate = 0
    total = 0
    total2 = 0
    total3 = 0
    doc.total_incoming_value = 0
    doc.total_amount = 0
    if doc.stock_entry_type == "Material Transfer" and doc.from_warehouse == "مخزن الشركة - DK":
        for x in doc.items:
            for y in doc.additional_costs:
               basicrate = (x.basic_rate*20/100)+x.basic_rate
               x.basic_rate = basicrate
               x.basic_amount = basicrate * x.qty
               x.amount = basicrate * x.qty
               total += x.amount
               total2+= y.amount
               total3 = total + total2
               doc.total_amount = total3
               doc.total_incoming_value = total3


@frappe.whitelist()
def ste_validate(doc, method=None):
    pass
    '''
    basicrate = 0
    total = 0
    total2 = 0
    total3 = 0
    for x in doc.items:
        for y in doc.additional_costs:
            if doc.stock_entry_type == "Material Transfer" and doc.from_warehouse == "مخزن الشركة - DK":
               basicrate = (x.basic_rate*20/100)+x.basic_rate
               x.basic_rate = basicrate
               x.basic_amount = basicrate * x.qty
               x.amount = basicrate * x.qty
               total += x.amount 
               total2 += y.amount
               total3 = total + total2
               doc.total_amount = 0
               doc.total_amount = total3
               doc.total_incoming_value = 0
               doc.total_incoming_value = total3
           
    '''



@frappe.whitelist()
def ste_on_submit(doc, method=None):
    #fbranch = frappe.db.get_value('Branch', {'warehouse': doc.from_warehouse}, ['name'])

    #tbranch = frappe.db.get_value('Branch', {'warehouse': doc.to_warehouse}, ['name'])

    if doc.stock_entry_type == "Material Transfer":
            tmode = frappe.get_value('Branch', {'warehouse': doc.from_warehouse}, ['mode_of_payment'])

            fmode = frappe.get_value('Branch', {'warehouse': doc.to_warehouse}, ['mode_of_payment'])

            paid_from = frappe.db.get_value("Mode of Payment Account", {'parent': fmode},
                                            'default_account')
            paid_to = frappe.db.get_value("Mode of Payment Account", {'parent': tmode},
                                          'default_account')

            new_doc = frappe.get_doc({
                "doctype": "Payment Entry",
                "posting_date": doc.posting_date,
                "payment_type": "Internal Transfer",
                "mode_of_payment": fmode,
                "mode_of_payment_2": tmode,
                "paid_amount": doc.total_amount,
                "received_amount": doc.total_amount,
                "source_exchange_rate": 1,
			    "target_exchange_rate": 1,
                "paid_from": paid_from,
                "paid_to": paid_to,



            })
            new_doc.insert(ignore_permissions=True)

            frappe.msgprint(new_doc.name + "  تم إنشاء تحويل داخلي بحالة مسودة رقم ")
@frappe.whitelist()
def ste_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def ste_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def ste_before_save(doc, method=None):
    pass
@frappe.whitelist()
def ste_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def ste_on_update(doc, method=None):
    pass

################ Blanket Order
@frappe.whitelist()
def blank_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def blank_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def blank_onload(doc, method=None):
    pass
@frappe.whitelist()
def blank_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def blank_validate(doc, method=None):
    pass
@frappe.whitelist()
def blank_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def blank_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def blank_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def blank_before_save(doc, method=None):
    pass
@frappe.whitelist()
def blank_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def blank_on_update(doc, method=None):
    pass
################ Attendance
@frappe.whitelist()
def att_on_submit(self, method=None):
    ## Auto Create Submit Extra Salary On Submit
    Component = frappe.get_value('Salary Component', {'branch': self.branch, 'extra_salary' : 1}, ['name'])
    if self.status == "Present":
        new_doc = frappe.get_doc({
                "doctype": "Extra Salary",
                "salary_component": Component,
                "type": "Earning",
                "currency": "EGP",
                "amount": "1",
                "employee": self.employee,
                "branch": self.branch,
                "employee_name": self.employee_name,
                "payroll_date": self.attendance_date,
                "branch": self.branch,
                "shift": self.shift,
                })
        new_doc.insert(ignore_permissions=True)
        new_doc.submit()

    if self.late_entry:
        new_doc = frappe.get_doc({
                "doctype": "Extra Salary",
                "salary_component": self.salary_component,
                "type": "Deduction",
                "currency": "EGP",
                "amount": "1",
                "employee": self.employee,
                "branch": self.branch,
                "employee_name": self.employee_name,
                "payroll_date": self.attendance_date,
                "branch": self.branch,
                "shift": self.shift,
                })
        new_doc.insert(ignore_permissions=True)
        new_doc.submit()
@frappe.whitelist()
def att_on_cancel(doc, method=None):
    pass

################ Sales Distribution
@frappe.whitelist()
def sa_dist_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def sa_dist_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def sa_dist_onload(doc, method=None):
    pass
@frappe.whitelist()
def sa_dist_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def sa_dist_validate(self, method=None):
    totalcommission = 0
    totals = 0
    sales_distribution_table = frappe.db.sql(""" select `tabSales Invoice`.posting_date as date, sum(`tabSales Invoice`.total) as total
		                                                           from `tabSales Invoice`  
		                                                           where `tabSales Invoice`.posting_date BETWEEN  '{Fromdate}' and '{todate}'
                                                                   and `tabSales Invoice`.distribution = 0
                                                                   and `tabSales Invoice`.branch = "المرغني"
                                                                   and `tabSales Invoice`.docstatus = 1
                                                                   GROUP BY `tabSales Invoice`.posting_date
		                                                       """.format(Fromdate=self.from_date,todate=self.to_date), as_dict=1)

    self.sales_distribution_table = {}
    for c in sales_distribution_table:
        if c.total >=10000 and c.total <=20000:
            totalcommission = 500
        if c.total >=20001 and c.total <=30000:
            totalcommission = 1000
        if c.total >=30001 and c.total <=40000:
            totalcommission = 1500
        if c.total >=40001 and c.total <=50000:
            totalcommission = 2000
        if c.total >=50001 and c.total <=60000:
            totalcommission = 2500
        if c.total >=60001 and c.total <=70000:
            totalcommission = 3000
        if c.total >=70001 and c.total <=80000:
            totalcommission = 3500
        if c.total >=80001 and c.total <=90000:
            totalcommission = 4000
        if c.total >=90001 and c.total <=100000:
            totalcommission = 4500
        if c.total >=90001:
            totalcommission = 5000
        row = self.append("sales_distribution_table", {})
        row.date = c.date
        row.amount_eligible_for_commission = c.total
        row.total_commission = totalcommission
        totals += row.total_commission
    self.nahla = round(totals / 8 )
    subtotal = totals - self.nahla
    self.ahmed =round( subtotal / 3)
    self.ismaeel = round(subtotal / 3)
    self.mohamed = round(subtotal / 3)
    if not self.sales_distribution_table:
        frappe.throw("Please Select Another Period")

@frappe.whitelist()
def sa_dist_on_submit(self, method=None):
    totalcommission = 0
    totals = 0
    sales_distribution_table = frappe.db.sql(""" select `tabSales Invoice`.posting_date as date, sum(`tabSales Invoice`.total) as total
		                                                           from `tabSales Invoice`  
		                                                           where `tabSales Invoice`.posting_date BETWEEN  '{Fromdate}' and '{todate}'
                                                                   and `tabSales Invoice`.distribution = 0
                                                                   and `tabSales Invoice`.branch = "المرغني"
                                                                   and `tabSales Invoice`.docstatus = 1
                                                                   GROUP BY `tabSales Invoice`.posting_date
		                                                       """.format(Fromdate=self.from_date,todate=self.to_date), as_dict=1)

    self.sales_distribution_table = {}
    for c in sales_distribution_table:
        if c.total >=10000 and c.total <=20000:
            totalcommission = 500
        if c.total >=20001 and c.total <=30000:
            totalcommission = 1000
        if c.total >=30001 and c.total <=40000:
            totalcommission = 1500
        if c.total >=40001 and c.total <=50000:
            totalcommission = 2000
        if c.total >=50001 and c.total <=60000:
            totalcommission = 2500
        if c.total >=60001 and c.total <=70000:
            totalcommission = 3000
        if c.total >=70001 and c.total <=80000:
            totalcommission = 3500
        if c.total >=80001 and c.total <=90000:
            totalcommission = 4000
        if c.total >=90001 and c.total <=100000:
            totalcommission = 4500
        if c.total >=90001:
            totalcommission = 5000
        row = self.append("sales_distribution_table", {})
        row.date = c.date
        row.amount_eligible_for_commission = c.total
        row.total_commission = totalcommission
        totals += row.total_commission
    nahla = round(totals / 8 )
    subtotal = totals - self.nahla
    ahmed =round( subtotal / 3)
    ismaeel = round(subtotal / 3)
    mohamed = round(subtotal / 3)
    acctotal = nahla + ahmed + mohamed + ismaeel
    accounts = [
				{
					"doctype": "Journal Entry Account",
					"account": "ايراد فرع الميرغني - DK",
					"credit": acctotal,
					"debit": 0,
					"credit_in_account_currency": acctotal				}
			]
    accounts1 = [
				{
					"doctype": "Journal Entry Account",
					"account": "جاري /  احمد - DK",
					"credit": 0,
					"debit": ahmed,
					"debit_in_account_currency": ahmed				}
			]
    accounts.extend(accounts1)
    accounts2 = [
				{
					"doctype": "Journal Entry Account",
					"account": "جاري / محمد - DK",
					"credit": 0,
					"debit": mohamed,
					"debit_in_account_currency": mohamed				}
			]
    accounts.extend(accounts2)
    accounts3 = [
				{
					"doctype": "Journal Entry Account",
					"account": "جاري/ اسماعيل - DK",
					"credit": 0,
					"debit": ismaeel,
					"debit_in_account_currency": ismaeel				}
			]
    accounts.extend(accounts3)
    accounts4 = [
				{
					"doctype": "Journal Entry Account",
					"account": "جاري / نهلة - DK",
					"credit":0 ,
					"debit": nahla,
					"debit_in_account_currency": nahla		}
			]
    accounts.extend(accounts4)
    new_doc = frappe.get_doc({
				"doctype": "Journal Entry",
				"voucher_type": "Journal Entry",
				"reference_doctype": "Sales Distribution",
				"reference_link": self.name,
				"cheque_no": self.name,
				"cheque_date": self.to_date,
				"posting_date": self.to_date,
				"accounts": accounts,
			})

    new_doc.insert(ignore_permissions=True)
    new_doc.submit()
    frappe.msgprint(new_doc.name + "  تم إنشاء قيد يومية رقم ")

    sales_distribution_table = frappe.db.sql(""" select `tabSales Invoice`.name as name,`tabSales Invoice`.posting_date as date, sum(`tabSales Invoice`.total) as total
		                                                           from `tabSales Invoice`  
		                                                           where `tabSales Invoice`.posting_date BETWEEN  '{Fromdate}' and '{todate}'
                                                                   and `tabSales Invoice`.distribution = 0
                                                                   and `tabSales Invoice`.docstatus = 1
                                                                   GROUP BY `tabSales Invoice`.posting_date
		                                                       """.format(Fromdate=self.from_date,todate=self.to_date), as_dict=1)
    for z in sales_distribution_table:
     frappe.db.set_value('Sales Invoice', z.name, 'distribution', '1', update_modified=False)
     frappe.db.set_value('Sales Invoice', z.name, 'sales_distribution', self.name, update_modified=False)

@frappe.whitelist()
def sa_dist_on_cancel(self, method=None):
    sales_distribution_table = frappe.db.sql(""" select `tabSales Invoice`.name as name,`tabSales Invoice`.posting_date as date, sum(`tabSales Invoice`.total) as total
		                                                           from `tabSales Invoice`  
		                                                           where `tabSales Invoice`.posting_date BETWEEN  '{Fromdate}' and '{todate}'
                                                                   and `tabSales Invoice`.distribution = 1
                                                                   and `tabSales Invoice`.sales_distribution = '{name}'
                                                                   and `tabSales Invoice`.docstatus = 1
                                                                   GROUP BY `tabSales Invoice`.posting_date
		                                                       """.format(Fromdate=self.from_date,todate=self.to_date,name=self.name), as_dict=1)
    for z in sales_distribution_table:
     frappe.db.set_value('Sales Invoice', z.name, 'distribution', '0', update_modified=False)
     frappe.db.set_value('Sales Invoice', z.name, 'sales_distribution', '', update_modified=False)

@frappe.whitelist()
def sa_dist_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def sa_dist_before_save(doc, method=None):
    pass
@frappe.whitelist()
def sa_dist_before_cancel(doc, method=None):
    pass