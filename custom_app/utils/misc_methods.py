import frappe
""""
the plan is to fetch the required details from the settings pages and send to the customer in whatever requirement
"""
def submit_inv(doc,event):
    settings_doc = frappe.get_doc("Settings Page")
    if doc._action=='submit':
        customer_doc = frappe.get_doc("Customer",doc.customer)
        if customer_doc.email_id:
            send_doctype_print(doc,settings_doc)
            send_customer_mail(doc,settings_doc)
        else:
            send_doctype_print(doc,settings_doc)
            send_doctype_print(doc,settings_doc)


def send_doctype_print(doc,settings):
    pf = settings.sales_invoice_print_format if doc.doctype =="Sales Invoice" else settings.delivery_note_print_format
    email_acc= settings.sales_invoice_email if doc.doctype =="Sales Invoice" else settings.delivery_note_email
    #Trying to ensure the print format defaults to standard if the field is not set
    pf = pf if pf!="" else None
    doc_print = frappe.attach_print(doc.doctype,doc.name,print_format=pf)
    
    email_args={
                "recipients": [email_acc],
                "message": "",
                "subject": doc.name,
                "attachments": [doc_print],
                "reference_doctype": doc.doctype,
                "reference_name": doc.name
                
    }

    frappe.sendmail(
            recipients=email_args['recipients'],
            message=email_args['message'],
            subject=email_args['subject'],
            attachments=email_args['attachments'],
            reference_doctype=doc.doctype,
            reference_name=doc.name
    )

def send_customer_mail(doc,settings):
    pf = settings.sales_invoice_print_format if doc.doctype =="Sales Invoice" else settings.delivery_note_print_format
    email_acc= frappe.get_value("Customer",doc.customer,'email_id')
    #Trying to ensure the print format defaults to standard if the field is not set
    pf = pf if pf!="" else None
    doc_print = frappe.attach_print(doc.doctype,doc.name,print_format=pf)
    email_args={
                "recipients": [email_acc],
                "message": settings.sales_invoice_message if doc.doctype=="Sales Invoice" else settings.delivery_note_message,
                "subject": doc.name,
                "attachments": [doc_print],
                "reference_doctype": doc.doctype,
                "reference_name": doc.name
    }
    frappe.sendmail(
            recipients=email_args['recipients'],
            message=email_args['message'],
            subject=email_args['subject'],
            attachments=email_args['attachments2'],
            reference_doctype=doc.doctype,
            reference_name=doc.name
    )