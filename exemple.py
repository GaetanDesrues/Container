import logging
import treefiles as tf

from pyctn.container import Ct


def main():
    with Ct("azeaze-ct") as ct:
        ct.add(arg1="some data")
        tf.dump_json(ct / "my_data.json", [1, 2, 3])


log = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    log = tf.get_logger()

    main()
    with Ct("azeaze-ct") as ct:
        print(ct)
        print(ct.my_data)
        print(ct.arg1)
