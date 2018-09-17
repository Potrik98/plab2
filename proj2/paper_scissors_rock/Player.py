from paper_scissors_rock.Action import Action


class Player:
    def __init__(self):
        pass

    def choose_action(self) -> Action:
        raise NotImplementedError()

    def accept_result(self,
                      my_action: Action,
                      other_action: Action,
                      result: int) -> None:
        raise NotImplementedError()

    def get_name(self) -> str:
        raise NotImplementedError()
