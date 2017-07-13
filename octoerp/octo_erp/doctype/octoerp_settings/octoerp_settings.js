// Copyright (c) 2017, Velometro and contributors
// For license information, please see license.txt

frappe.ui.form.on('OctoERP Settings', {
	refresh: function(frm) {

	},
	seller_lookup: function(frm) {
		if (frm.doc.seller){
			frappe.call({
				method: "octoerp.octo_erp.octo_erp.octopart_seller",
				args:{
					"seller": frm.doc.seller
				},
			});
		} else {
			msgprint("Fill in Seller field");
		}
		frm.set_value("seller", "");
	}
});
