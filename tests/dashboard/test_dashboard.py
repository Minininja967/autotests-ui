import pytest
import allure

from config import settings
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.parent_suite import AllureParentSuite
from tools.allure.stories import AllureStory
from tools.allure.sub_suite import AllureSubSuite
from tools.allure.suite import AllureSuite
from tools.allure.tags import AllureTag
from allure_commons.types import Severity
from pages.dashboard.dashboard_page import DashboardPage
from tools.routes import AppRoute


@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@allure.parent_suite(AllureParentSuite.LMS)
@allure.suite(AllureSuite.DASHBOARD)
@allure.sub_suite(AllureSubSuite.DASHBOARD)
class TestDashboard:
    @allure.title('Check displaying of dashboard page')
    @allure.severity(Severity.NORMAL)
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)
        dashboard_page_with_state.navbar.check_visible(settings.test_user.username)
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.dashboard_toolbar.check_visible()
        dashboard_page_with_state.students_chart_view.check_visible('Students')
        dashboard_page_with_state.activities_chart_view.check_visible('Activities')
        dashboard_page_with_state.courses_chart_view.check_visible('Courses')
        dashboard_page_with_state.scores_chart_view.check_visible('Scores')
