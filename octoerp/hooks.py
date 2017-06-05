# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "octoerp"
app_title = "Octo-ERP"
app_publisher = "Velometro"
app_description = "App for using Octo-part to look up part pricing and availability"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "bcornwellmott@velometro.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/octoerp/css/octoerp.css"
# app_include_js = "/assets/octoerp/js/octoerp.js"

# include js, css files in header of web template
# web_include_css = "/assets/octoerp/css/octoerp.css"
# web_include_js = "/assets/octoerp/js/octoerp.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "octoerp.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "octoerp.install.before_install"
# after_install = "octoerp.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "octoerp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Fixtures
# --------
fixtures = ["Custom Field"]

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"octoerp.tasks.all"
# 	],
# 	"daily": [
# 		"octoerp.tasks.daily"
# 	],
# 	"hourly": [
# 		"octoerp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"octoerp.tasks.weekly"
# 	]
# 	"monthly": [
# 		"octoerp.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "octoerp.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "octoerp.event.get_events"
# }

