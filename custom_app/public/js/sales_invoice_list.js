frappe.listview_settings['Sales Invoice'] = {
    onload: function(listview) {
        var method = "custom_app.utils.misc_methods.email_docprint_from_list";

		listview.page.add_menu_item(__("Send Print"), function() {
			listview.call_for_selected_items(method);
		});

    }
}