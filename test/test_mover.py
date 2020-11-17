import pytest
import os
from groot.Mover import Mover


@pytest.fixture
def mover():
	return Mover()


def test_split_filename_and_ext(mover):
	# Arrange
	filename = 'testing.pdf'

	# Act
	mover._split_ext(filename)

	# Assert
	assert mover.file_name == 'testing'
	assert mover.file_ext == '.pdf'


def test_get_current_file_path(mover):
	filename = 'testing.pdf'
	mover.filename = filename
	sending_filename = mover._get_current_file_path(filename)
	withdout_filename = mover._get_current_file_path()
	assert sending_filename == os.path.join(os.getcwd(), filename)
	assert withdout_filename == os.path.join(os.getcwd(), filename)


def test_set_next_file_path(mover):
	mover.filename = 'testing.docx'
	sending_filename = mover._set_next_file_path('PDF', 'testing.pdf')
	without_filename = mover._set_next_file_path('Docs')
	assert sending_filename == os.path.join(os.getcwd(), 'PDF', 'testing.pdf')
	assert without_filename == os.path.join(os.getcwd(), 'Docs', 'testing.docx')


def test_increment_consecutive_number(mover):

	# Looking for any number inside parenthesis
	res = mover._increment_consecutive_number('testing(1).pdf', '(1)')
	assert res == 'testing(2).pdf'


def test_add_consecutive_to_filename(mover):
	new_name = mover._add_consecutive_to_filename('testing.pdf')
	new_name_2 = mover._add_consecutive_to_filename('testing(10).pdf')
	assert new_name == 'testing(1).pdf'
	assert new_name_2 == 'testing(11).pdf'