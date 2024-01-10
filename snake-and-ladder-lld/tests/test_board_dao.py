import unittest
from unittest import TestCase

from dao.board import BoardDao
from exceptions import BoardNotFoundException
from models.board import Board
from services.board import BoardService


class TestBoardDao(TestCase):
    def setUp(self) -> None:
        self.b0 = Board(id="b0", size=100, cells=[])
        BoardDao.BoardMap[self.b0.id] = self.b0

    def test_get_board_by_id(self):
        board = BoardDao().get_by_id(id=self.b0.id)
        self.assertIsNotNone(board)
        self.assertEqual(board.id, self.b0.id)

    def test_get_board_for_invalid_if(self):
        with self.assertRaises(BoardNotFoundException):
            board = BoardDao().get_by_id(id=123)

if __name__ == '__main__':
    unittest.main()