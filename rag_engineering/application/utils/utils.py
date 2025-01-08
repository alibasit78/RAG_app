import pickle
import sys


def dump_pickle_file(output_filepath: str, data) -> None:
    try:
        with open(output_filepath, "wb") as encoded_pickle:
            pickle.dump(data, encoded_pickle)
    except Exception as e:
        raise(e)

def dump_text_file(output_filepath: str, data) -> None:
    try:
        with open(output_filepath, "w") as fw:
            if isinstance(data, dict):
                for key, value in data.items():
                    fw.write(str(key)+'\n')
                    fw.write(str(value)+'\n')
                    fw.write('\n')
            else:
                fw.write(str(data))
    except Exception as e:
        raise(e)