from components.base_components import BaseComponent
from playwright.sync_api import expect


class CreateCourseExerciseFormComponent(BaseComponent):
    def click_delete_button(self, index: int):
        delete_button = self.page.get_by_test_id(
            f'create-course-exercise-{index}-box-toolbar-delete-exercise-button'
        )
        delete_button.click()

    def check_visible(self, index: int, title: str, description: str):
        subtitle = self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-subtitle-text')
        title_input = self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input')
        description_input = self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input')

        expect(subtitle).to_be_visible()
        expect(subtitle).to_have_text(f'#{index + 1} Exercise')

        expect(title_input.locator('label')).to_be_visible()
        expect(title_input.locator('label')).to_have_text('Title')
        expect(title_input.locator('input')).to_be_visible()
        expect(title_input.locator('input')).to_have_value(title)

        expect(description_input.locator('label')).to_be_visible()
        expect(description_input.locator('label')).to_have_text('Description')
        expect(description_input.locator('input')).to_be_visible()
        expect(description_input.locator('input')).to_have_value(description)

    def fill_create_exercise_form(self, index: int, title: str, description: str):
        title_input = self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input')
        description_input = self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input')

        title_input.fill(title)
        expect(title_input).to_have_value(title)

        description_input.fill(description)
        expect(description_input).to_have_value(description)