app_name = "lwp_auto"
app_title = "Auto LWP"
app_publisher = "Indictrans Technologies"
app_description = "Calculate auto lwp"
app_icon = "icon-table"
app_color = "#589494"
app_email = "lwp@indic.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/lwp_auto/css/lwp_auto.css"
# app_include_js = "/assets/lwp_auto/js/lwp_auto.js"

# include js, css files in header of web template
# web_include_css = "/assets/lwp_auto/css/lwp_auto.css"
# web_include_js = "/assets/lwp_auto/js/lwp_auto.js"

fixtures = ["Custom Script"]

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "lwp_auto.install.before_install"
after_install = "lwp_auto.auto_lwp.doctype.auto_calculate_lwp.auto_calculate_lwp.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "lwp_auto.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Salary Slip": {
		"validate": "lwp_auto.auto_lwp.doctype.auto_calculate_lwp.auto_calculate_lwp.auto_calculate_lwp2"
	}
}

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
# 		"lwp_auto.tasks.all"
# 	],
# 	"daily": [
# 		"lwp_auto.tasks.daily"
# 	],
# 	"hourly": [
# 		"lwp_auto.tasks.hourly"
# 	],
# 	"weekly": [
# 		"lwp_auto.tasks.weekly"
# 	]
# 	"monthly": [
# 		"lwp_auto.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "lwp_auto.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "lwp_auto.event.get_events"
# }

