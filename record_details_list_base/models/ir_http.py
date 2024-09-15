from odoo import models


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    def session_info(self):
        res = super().session_info()
        allowed_models = []
        # find all models that have fetch_record_list_details method
        model_ids = self.env["ir.model"].sudo().search([("transient", "=", False)])
        for model in model_ids:
            try:
                getattr(self.env[model.model].sudo(), "fetch_record_details")
                allowed_models.append(model.model)
            except AttributeError:
                pass
        res["allowed_models"] = allowed_models
        return res
