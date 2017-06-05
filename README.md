## Octo-ERP

App for using Octo-part to look up part pricing and availability

To implement, add this to your custom script for 'Supplier Quotation':

	frappe.ui.form.on("Supplier Quotation",{
		refresh: function(frm) {
			frm.add_custom_button(__("Octopart Lookup"), function(foo) {

					frappe.call({
						method:"octoerp.octo_erp.octo_erp.octopart_lookup",
						args: {
							sq_number: cur_frm.doc.name
						}, 
						callback: function(r) { 
							frm.reload_doc();

						}
					});
			});
		}
	});
		
#### License

MIT