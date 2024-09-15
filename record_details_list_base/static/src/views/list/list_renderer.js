/** @odoo-module **/

import { ListRenderer } from "@web/views/list/list_renderer";
import { markup } from "@odoo/owl";
import { patch } from "@web/core/utils/patch";
import { session } from "@web/session";
import { useService } from "@web/core/utils/hooks";

patch(ListRenderer.prototype, {
    setup() {
        super.setup(...arguments);
        this.orm = useService("orm");
    },
    checkMethodExists() {
        const sessionInfo = session;
        if (sessionInfo.allowed_models.includes(this.props.list?.model?.config?.resModel || this.props.list?.evalContext?.params?.model)) {
            return true;
        }
        return false;
    },
    getRecordDetails(record) {
        let details = "";
        if (record.data.view_record_details) {
            details = markup(record.data.view_record_details);
        }
        return details;
    },
    async expandRecordDetails(record) {
        if (record.data.view_record_details) {
            delete record.data.view_record_details;
            return;
        }
        const record_details = await this.orm.call("fetch.record.details", "action_fetch_record_details", [this.props.list?.model?.config?.resModel || this.props.list?.evalContext?.params?.model, record.evalContext.active_id]);
        record.data.view_record_details = markup(record_details);
    },
});
