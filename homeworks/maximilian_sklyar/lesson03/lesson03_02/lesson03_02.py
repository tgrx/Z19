import timeit
import test_data
from decimal import Decimal as D


def timeit_res(file_name):
    try:
        file = open(file_name, "w")
        for opr in test_data.operation:
            statement = ""
            j = 1
            file.write("Timeit operation {opr}: \n".format(opr=opr[0]))
            for data in test_data.test_data:
                if data[-1] == "int":
                    statement = "{a} {opr} {b}".format(
                        a=int(data[0]), opr=opr[-1], b=int(data[1])
                    )
                if data[-1] == "float":
                    statement = "{a} {opr} {b}".format(
                        a=float(data[0]), opr=opr[-1], b=float(data[1])
                    )
                if data[-1] == "complex":
                    statement = "{a} {opr} {b}".format(
                        a=complex(data[0]), opr=opr[-1], b=complex(data[1])
                    )
                if data[-1] == "decimal":
                    statement = "{a} {opr} {b}".format(
                        a=D(data[0]), opr=opr[-1], b=D(data[1])
                    )
                file.write(
                    "{j}. {stmt}: timeit -> {tmt} ns\n".format(
                        j=j,
                        stmt=statement,
                        tmt=timeit.repeat(stmt=statement, repeat=1)[0],
                    )
                )
                j += 1
        return True
    except IOError as e:
        return e


timeit_res("lesson03_02.result.txt")
