
from __future__ import unicode_literals

import json
import urllib
import frappe
from frappe import _, throw

@frappe.whitelist()
def octopart_lookup(sq_number):

	# Get the api key from settings
	
	sq = frappe.get_doc('Supplier Quotation', sq_number)
	supplier = frappe.get_value('Supplier',sq.supplier,'octopart_seller_name') or sq.supplier
	for item in sq.items:
		mfg, mfg_pn = frappe.get_value('Item', item.item_code, ['manufacturer','manufacturer_part_no'])
		
		url = 'http://octopart.com/api/v3/parts/match?'
		url += '&queries=[{{"mpn_or_sku":"{0}"}}]'.format(mfg_pn)
		url += '&apikey=615e3382'

		data = urllib.urlopen(url).read()
		response = json.loads(data)

		found = 0
		
		item.rate = 0
		if 'results' in response:
			for result in response['results']:
			
				for item_result in result['items']:
					if item_result['manufacturer']['name'] == mfg:
					
						for offer in item_result['offers']:
							if offer['seller']['name'] == supplier:
				
								if sq.currency in offer['prices']:
									for qty_rate in offer['prices'][sq.currency]:
										if qty_rate[0] <= item.qty:
											item.rate = qty_rate[1]
								else:
									frappe.msgprint("Cannot find quoted price in {0}".format(sq.currency))
							else:
								frappe.msgprint("Cannot find seller")
		if item.rate > 0:
			frappe.msgprint("Best rate that {0} supplies item {1} at is {2}".format(sq.supplier, item.item_code,item.rate))
	sq.save()

	
		
