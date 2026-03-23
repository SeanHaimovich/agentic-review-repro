"""Tests for ReportService dropdown generation."""

import pytest

from app.services.report_service import ReportService, User


@pytest.fixture
def acme_user():
    return User(id=1, tenant_id="acme", department_ids=[10, 20, 30])


@pytest.fixture
def globex_user():
    return User(id=2, tenant_id="globex", department_ids=[40, 50])


class TestGetDropdownOptions:
    def test_returns_departments_for_user(self, acme_user):
        result = ReportService.get_dropdown_options(acme_user)
        assert "Engineering" in result["departments"]
        assert "Sales" in result["departments"]

    def test_departments_are_deduplicated(self, acme_user):
        result = ReportService.get_dropdown_options(acme_user)
        # dept ids 20 and 30 both have name "Sales" — should appear once
        assert result["departments"].count("Sales") == 1

    def test_returns_locations_for_user(self, acme_user):
        result = ReportService.get_dropdown_options(acme_user)
        assert "HQ - San Francisco" in result["locations"]
        assert "Branch - New York" in result["locations"]

    def test_locations_scoped_to_tenant(self, acme_user):
        result = ReportService.get_dropdown_options(acme_user)
        # globex locations must not leak into acme results
        assert "Main Office - London" not in result["locations"]
        assert "Warehouse - Berlin" not in result["locations"]

    def test_globex_user_sees_own_data(self, globex_user):
        result = ReportService.get_dropdown_options(globex_user)
        assert "Research" in result["departments"]
        assert "Main Office - London" in result["locations"]
        # acme data must not appear
        assert "HQ - San Francisco" not in result["locations"]

    def test_empty_department_ids(self):
        user = User(id=99, tenant_id="acme", department_ids=[])
        result = ReportService.get_dropdown_options(user)
        assert result["departments"] == []
        assert result["locations"] == []
