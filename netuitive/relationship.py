
class Relationship(object):

    """
        A relationship of other Elements to this Element

        :param fqn: FQN of the other Element
        :type name: string
    """

    def __init__(self, fqn):
        self.fqn = fqn
