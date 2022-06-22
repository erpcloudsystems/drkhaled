# Copyright (c) 2022, erpcloud.systems and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class InternalSelling(Document):
	@frappe.whitelist()
	def validate(self):
		totals = 0
		for x in self.items:
			x.valuation_rate = frappe.db.get_value("Bin", {'item_code': x.item_code, 'warehouse': self.from_warehouse},
                                          'valuation_rate')
			rate = x.qty * x.valuation_rate
			x.amount = rate + (rate * x.additional_rate / 100)
			totals += x.amount
			self.total_amount = totals

	@frappe.whitelist()
	def on_submit(self):
		## Auto Create Draft Stock Entry On Submit
		new_doc = frappe.get_doc({
			"doctype": "Stock Entry",
			"stock_entry_type": "Material Transfer",
			"purpose": "Material Transfer",
			"posting_date": self.posting_date,
			"from_warehouse": self.from_warehouse,
			"to_warehouse": self.to_warehouse,
			"internal_selling": self.name,
			"branch": self.branch,

		})
		is_items = frappe.db.sql(""" select a.idx, a.name, a.item_code, a.item_name, a.item_group, a.qty, a.uom
		                                                           from `tabInternal Selling Item` a join `tabInternal Selling` b
		                                                           on a.parent = b.name
		                                                           where b.name = '{name}'
		                                                       """.format(name=self.name), as_dict=1)

		for c in is_items:
			items = new_doc.append("items", {})
			items.idx = c.idx
			items.item_code = c.item_code
			items.item_name = c.item_name
			items.item_group = c.item_group
			items.s_warehouse = self.from_warehouse
			items.t_warehouse = self.to_warehouse
			items.qty = c.qty
			items.uom = c.uom


		new_doc.insert(ignore_permissions=True)
		frappe.msgprint("  تم إنشاء حركة مخزنية بحالة مسودة رقم " + new_doc.name)

## Auto Create Draft Payment Entry On Submit
		paid_from = frappe.db.get_value("Mode of Payment Account", {'parent': self.from_mode_of_payment},
										  'default_account')
		paid_to = frappe.db.get_value("Mode of Payment Account", {'parent': self.to_mode_of_payment},
                                          'default_account')
		new_doc2 = frappe.get_doc({
			"doctype": "Payment Entry",
			"payment_type": "Internal Transfer",
			"posting_date": self.posting_date,
			"mode_of_payment": self.from_mode_of_payment,
			"mode_of_payment_2": self.to_mode_of_payment,
			"paid_amount": self.total_amount,
			"received_amount": self.total_amount,
			"internal_selling": self.name,
			"branch": self.branch,
			"cost_center": self.cost_center,
			"source_exchange_rate": 1,
			"target_exchange_rate": 1,
			"paid_from": paid_from,
			"paid_to": paid_to,

		})

		new_doc2.insert(ignore_permissions=True)
		frappe.msgprint("  تم إنشاء تحويل داخلي بحالة مسودة رقم " + new_doc2.name)
		self.payment_entry = new_doc2.name
		self.pe_status = new_doc2.status
		self.save()
		self.reload()

