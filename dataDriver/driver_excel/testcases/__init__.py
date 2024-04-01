import openpyxl
import pytest
from dataDriver.driver_excel.func.operation_excel import my_add1


# 用到exceL文件中的数据时，就需要读取出来
def test_get_excel():
        """
        解析Excel数据
        :return: [[1,1,2],[3,6,9],[1,209, 309]]
        """

    #获取工作薄
    book = openpyxl.load_workbook('../datas/data.xlsx')
    #获取工作表sheet1
    sheet = book.active
    # 读取数据
    cells = sheet['A1':'C3']
    print(cells)
    values = []
    for row in cells:
        data = []
        for cell in row:
            data.append(cell.value)
        values.append(data)
    print(values)
    return values


class TestWithEXCEL:
    @pytest.mark.parametrize('x,y,expected', test_get_excel(), ids=[1, 2, 3])
    def test_add1(self, x, y, expected):
        assert my_add1(int(x), int(y)) == int(expected)
