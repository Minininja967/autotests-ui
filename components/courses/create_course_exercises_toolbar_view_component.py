from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CreateCourseExercisesToolbarViewComponent(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.create_exercise_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

    def check_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Exercises')

        expect(self.create_exercise_button).to_be_visible()


    def click_create_exercise_button(self):
        self.create_exercise_button.click()
