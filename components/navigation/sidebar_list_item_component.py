from typing import Pattern

import allure
from playwright.sync_api import Page, expect
from components.base_components import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.sidebar_icon = Icon(page, '{identifier}-drawer-list-item-icon', 'Sidebar icon')
        self.sidebar_title = Text(page, '{identifier}-drawer-list-item-title-text', 'Sidebar title')
        self.sidebar_button = Button(page, '{identifier}-drawer-list-item-button', 'Sidebar button')

    @allure.step('Check visible "{title}" sidebar list item')
    def check_visible(self, title: str, identifier: str):
        self.sidebar_icon.check_visible(identifier=identifier)

        self.sidebar_title.check_visible(identifier=identifier)
        self.sidebar_title.check_have_text(title, identifier=identifier)

        self.sidebar_button.check_visible(identifier=identifier)


    def navigate(self, expected_url: Pattern[str], identifier: str):
        self.sidebar_button.click(identifier=identifier)
        self.check_current_url(expected_url)
