import datetime as dt
import os
import pytest
import shutil


from src.utils import (
    get_datetime,
    get_date
)


class TestUtils:
    """test src.utils functions."""
    test_folder=os.path.join(
        os.getcwd(),
        "test_utils"
    )

    @classmethod
    def setup_class(cls):
        os.mkdir(cls.test_folder)

    @classmethod
    def teardown_class(cls):
        shutil.rmtree(cls.test_folder)

    @staticmethod
    def setup_method():
        print("Setup method!")

    @staticmethod
    def teardown_method():
        print("Teardown method!")

    def test_get_datetime(self):
        assert isinstance(get_datetime(), dt.datetime)
        assert isinstance(get_datetime(timezone="Europe/Lisbon"), dt.datetime)

    def test_get_date(self, mocker):
        assert isinstance(get_date(), dt.date)
        with mocker.patch("src.utils.get_datetime", return_value=dt.datetime(11, 11, 11)):
            assert get_date() == dt.datetime(11, 11, 11).date()
