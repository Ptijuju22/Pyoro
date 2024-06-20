import math
from pyoro.entity.entities.entity import Entity
from pyoro.entity.entities.pyoros.pyoro_tongue import PyoroTongue
from pyoro.entity.entities.tongue import Tongue
from pyoro.entity.entities.tongue_piece import TonguePiece
from pyoro.entity.entity_direction import EntityDirection
from pyoro.entity.operators.operator import Operator
from pyoro.game.game_state import GameState


class TonguePieceOperator(Operator):
    def get_tongue_pieces_needed_count(self) -> int | None:
        pyoro = self.find_entity(PyoroTongue)
        tongue = self.find_entity(Tongue)

        if not pyoro or not tongue:
            return None

        match tongue.direction:
            case EntityDirection.RIGHT:
                return math.ceil(
                    2
                    * (tongue.pos[0] - (pyoro.pos[0] + pyoro.SIZE[0] / 2))
                    / TonguePiece.SIZE[0]
                )
            case EntityDirection.LEFT:
                return math.ceil(
                    2
                    * (
                        (pyoro.pos[0] + pyoro.SIZE[0] / 2)
                        - (tongue.pos[0] + tongue.SIZE[0])
                    )
                    / TonguePiece.SIZE[0]
                )

    def spawn_tongue_piece(self) -> None:
        pyoro = self.find_entity(PyoroTongue)
        tongue = self.find_entity(Tongue)
        tongue_pieces = self.filter_entities(TonguePiece)
        tongue_pieces_count = len(tongue_pieces)
        need_tongue_pieces_count = self.get_tongue_pieces_needed_count()

        if not pyoro or not tongue or not need_tongue_pieces_count:
            return None

        for i in range(tongue_pieces_count, need_tongue_pieces_count):
            self.add_entity(TonguePiece(pyoro, tongue, i))

    def remove_tongue_piece(self) -> None:
        tongue_pieces = self.filter_entities(TonguePiece)
        tongue_pieces_count = len(tongue_pieces)
        need_tongue_pieces_count = self.get_tongue_pieces_needed_count()

        def find_tongue_piece(tongue_piece_index: int) -> TonguePiece | None:
            for tongue_piece in tongue_pieces[::-1]:
                if tongue_piece.index == tongue_piece_index:
                    return tongue_piece
            return None

        if not need_tongue_pieces_count:
            return None

        for i in range(tongue_pieces_count, need_tongue_pieces_count, -1):
            tongue_piece = find_tongue_piece(i - 1)

            if tongue_piece:
                self.remove_entity(tongue_piece)
                tongue_piece.kill()

    def clear_tongue_pieces(self) -> None:
        tongue_pieces = self.filter_entities(TonguePiece)

        for tongue_piece in tongue_pieces:
            self.remove_entity(tongue_piece)
            tongue_piece.kill()

    def update(self, game_state: GameState) -> None:
        pyoro = self.find_entity(PyoroTongue)
        tongue = self.find_entity(Tongue)

        if pyoro and tongue:
            if tongue.get_extending():
                self.spawn_tongue_piece()
            else:
                self.remove_tongue_piece()
        return super().update(game_state)

    def collide(self, entity1: Entity, entity2: Entity) -> None:
        if (
            isinstance(entity1, PyoroTongue)
            and isinstance(entity2, Tongue)
            and not entity2.get_extending()
        ):
            self.clear_tongue_pieces()
        return super().collide(entity1, entity2)
