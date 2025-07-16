import re
import allure
from playwright.sync_api import Page

from components.base_components import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SidebarListItemComponent(page,'logout')
        self.courses_list_item = SidebarListItemComponent(page, 'courses')
        self.dashboard_list_item = SidebarListItemComponent(page, 'dashboard')

    @allure.step('Check visible sidebar')
    def check_visible(self):
        self.logout_list_item.check_visible('Logout','logout')
        self.courses_list_item.check_visible('Courses', 'courses')
        self.dashboard_list_item.check_visible('Dashboard', 'dashboard')

    @allure.step('Click logout on sidebar')
    def click_logout(self):
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"), 'logout')

    @allure.step('Click courses on sidebar')
    def click_courses(self):
        self.courses_list_item.navigate(re.compile(r".*/#/courses"), 'courses')

    @allure.step('Click dashboard on sidebar')
    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"), 'dashboard')