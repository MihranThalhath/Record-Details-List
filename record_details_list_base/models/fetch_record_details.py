from odoo import api, models


class FetchRecordDetails(models.AbstractModel):
    _name = "fetch.record.details"
    _description = "Fetch Record Details"

    @api.model
    def action_fetch_record_details(self, model_name, record_id):
        method_exists = self.check_method_exists(model_name)
        if not method_exists:
            return False
        if not model_name or not record_id:
            return False
        model = self.env[model_name].sudo()
        record = model.browse(record_id)
        line_details = getattr(record, "fetch_record_details")()
        return line_details

    @api.model
    def check_method_exists(self, model_name: str) -> bool:
        if not model_name:
            return False
        model = self.env[model_name].sudo()
        if not hasattr(model, "fetch_record_details"):
            return False
        return True
