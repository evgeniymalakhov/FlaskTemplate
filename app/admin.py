from flask import url_for
from flask_admin import Admin as FlaskAdmin, AdminIndexView as IndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from werkzeug.utils import redirect


class AdminIndexView(IndexView):
    def is_accessible(self):
        return current_user.is_administrator()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('main.index'))


class RolesAdminView(ModelView):
    create_modal = True
    edit_modal = True


class UserAdminView(ModelView):
    can_view_details = True
    column_exclude_list = ['password_hash', 'updated_at']
    column_searchable_list = ['first_name', 'last_name', 'username', 'email']
    column_filters = ['first_name', 'last_name', 'username', 'email']
    form_excluded_columns = ['password_hash']
    column_details_exclude_list = ['password_hash']
    create_modal = True
    edit_modal = True
    details_modal = True
    can_export = True
    page_size = 25

    def is_accessible(self):
        return current_user.is_administrator()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('main.index'))


class Admin(FlaskAdmin):
    def init_app(self, app):
        super(Admin, self).init_app(app,
                                    index_view=AdminIndexView())
        from . import db
        from .models import (User, Role)  # more models here
        self.add_view(UserAdminView(User, db.session, category='Visitors'))
        self.add_view(RolesAdminView(Role, db.session, category='Visitors'))
        # more calls to `add_view` here