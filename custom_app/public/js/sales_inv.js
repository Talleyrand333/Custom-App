frappe.ui.form.on("Sales Invoice",{
    onload: function(frm){
       if(!frm.is_new()){
        frm.add_custom_button(__("Print"),()=>{
            frappe.call({
                method:'custom_app.utils.misc_methods.email_docprint',
                args:{
                'docname':frm.doc.name,
            },
            callback:(res)=>{
                console.log(res)
                res.message ? frappe.show_alert(`Email Sent to ${res.message}`) : frappe.show_alert(`An Error Occured, Please cCeck Error Logs`)
            }
            })
            
        })
       }
    }
})