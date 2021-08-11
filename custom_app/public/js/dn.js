frappe.ui.form.on("Delivery Note",{
    refresh:(frm)=>{
        if(!frm.is_new()){
            console.log("LOADED")
            frm.add_custom_button(__('Print Label'),()=>{
                console.log("Clicked Print")
            })
        }
    }
})