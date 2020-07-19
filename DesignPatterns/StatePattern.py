
import enum

class Canvas:

    def mouseDown(self):
        pass

    def mouseUp(self):
        pass

# class ToolType(enum.Enum):

#     pass

ToolType = enum.Enum("T", "SELECTION ERASE")


if __name__ == "__main__":

    print(ToolType.SELECTION)
    


