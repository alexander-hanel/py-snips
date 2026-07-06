"""
    Author: Alexander Hanel
    Description:  
    Version: 1
    Last Update: 2026/06/06
"""


# ------------------------------------------------

def test_import():
    import importlib.util
    
    module_name = "module_name"
    module_exists = importlib.util.find_spec(module_name) is not None
    if module_exists:
        return True
    else:
        return False

# ------------------------------------------------

def load_json(file_path):
    """non-large file size JSON"""
    import json 
    from pathlib import Path
    
    path_file = Path(file_path)
    if file_path.exist():
        try:
            data = json.loads(path_file.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"JSON Errors: {e}")
            return None 
        return data 
   
def load_large_json(file_path):
    """large file size JSON"""
    import json 
    from pathlib import Path
    
    path_file = Path(file_path)
    if file_path.exist():
        try:
            with path_file.open("r", encoding="utf-8") as file:
                data = json.load(file)
                # do stuff here 
        except Exception as e:
            print(f"JSON Errors: {e}")
            return None 
        return data 

def json_dump_vs_dumps():
    """differene between JSON dump and dumps"""
    import json 
    from pathlib import Path

    data = {"user": "Alice", "active": True}
    # json.dumps converts the dict into a JSON string 
    json_string = json.dumps(data)
    # json.dump is when you need to write to a file 
    with open("data.json", "w") as file_obj: 
        json.dump(data, file_obj)

def json_load_vs_loads():
    import json 
    
    json_string = '{"name": "Alice", "is_admin": true}'
    # json.loads converts a JSON text string to JSON object type
    data = json.loads(json_string)
    # json.load converts a file object to JSON 
    with open("data.json", "r") as file:
        data = json.load()
    
def write_json(file_path, data):
    import json 
    
    try:
        with file_path.open("w", encoding="utf-8") as f:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"JSON Write {e}")

# ------------------------------------------------

def glob_dir(file_path="."):
    """example how to use glob"""
    import glob 
    
    for _file in glob.glob(file_path + "/*"):
        print(_file)

def glob_dir_recur(file_path="."):
    """Example of using glob to search all sub-directories"""
    import glob 
    
    for _file in glob.glob(file_path + "/**/*", recursive=True):
        print(_file)

# ------------------------------------------------

def isinstance_example():
    """example of using isinstance"""
    if isinstance(2, int):
        print(True)
    if isinstance(2.0, float):
        print(True)
    if isinstance("x", str):
        print(True)
    if isinstance({'a':1}, dict):
        print(True)
    if isinstance([1,2,3], list):
        print(True)

# ------------------------------------------------

def intenum_example():
    from enum import IntEnum

    class MYNUMS(IntEnum):
        NUM_1 = 1
        NUM_2 = 2
        NUM_3 = 3
    print(MYNUMS.NUM_1)
    print(MYNUMS.NUM_2==3)

# ------------------------------------------------

def named_tuple_example():
    """example using namedtuples"""
    from collections import namedtuple

    # first create the namedtuple class 
    MyNameTuple = namedtuple("Label", ["name1", "num", "mylist"])
    # add content to the object
    my_tuple = MyNameTuple(name1="abc", num=1234, mylist=[1,2,3])
    print(my_tuple)
    print(my_tuple.name1)
    print(my_tuple.mylist)

# ------------------------------------------------

def deque_example():
    """linked list example using deque"""
    from collections import deque
    queue = deque([2])
    queue.append(3)  
    queue.appendleft(1) 
    print(queue)
    queue.reverse()
    print(queue)

# ------------------------------------------------

def logging_example():
    import logging 
    import sys
    # configure logging to file showing only INFO
    logging.basicConfig(
        level=logging.INFO,                         
        format="%(asctime)s - %(levelname)s - %(message)s", # Set output format
        handlers=[
            logging.FileHandler("app.log", mode="a"),  # Appends to a file
        ]
    ) 
    # log to file 
    logging.debug("This will not log to a file")        
    logging.info("Will log to a file")       
    logging.warning("Will log to a file")        
    logging.error("Will log to a file")     
    
    # change the configuration to log only to stdout
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s", # Set output format  
        handlers=[logging.StreamHandler(sys.stdout)],                 
        force=True,
    ) 
    logging.debug("This will log")        
    logging.info("Will log ")       
    logging.warning("Will log")        
    logging.error("Will log")     

# ------------------------------------------------

def write_yaml():
    """example to write pylaml"""
    # validate pyyaml is installed, it is not default
    import importlib.util    
    module_name = "yaml"
    module_exists = importlib.util.find_spec(module_name) is not None
    if module_exists:
        import yaml
    else:
        print("Module Not Installed: pip -m install pyyaml")
        return
    # yaml is installed write yaml file
    data = {
        "app_name": "Task Manager",
        "version": 1.2,
        "features": ["auth", "notifications", "billing"],
        "settings": {
            "theme": "dark",
            "notifications_enabled": True
        }
    }
    from pathlib import Path
    # Write the dictionary to a YAML file
    output_path = Path("data/output.yaml")
    with open(output_path, "w") as file:
        yaml.dump(data, file, default_flow_style=False, sort_keys=False)

def load_yaml():
    """example to load pylaml"""
    # validate pyyaml is installed, it is not default
    import importlib.util    
    module_name = "yaml"
    module_exists = importlib.util.find_spec(module_name) is not None
    if module_exists:
        import yaml
    else:
        print("Module Not Installed: pip -m install pyyaml")
        return
    # load yaml file 
    from pathlib import Path
    input_path = Path("data/output.yaml")
    with open(input_path, 'r') as file:
        config = yaml.safe_load(file)
    print(config)
    
# ------------------------------------------------

def crc_data():
    """crc hash a block of data using zlib"""
    import zlib
    # requires bytes type
    data = b"Hello, World!"
    checksum = zlib.crc32(data)
    print(f"CRC32 (Decimal): {checksum}")
    print(f"CRC32 (Hex): {hex(checksum)}")

# ------------------------------------------------

def hexdump(data=None, chunks_of=16):
    if not data:
        data = b"Example data: 1234567890"
    for i in range(0, len(data), chunks_of):
        chunk = data[i:i + chunks_of]
        offset = f"{i:08x}"
        hex_bytes = " ".join(f"{b:02x}" for b in chunk)
        hex_bytes = f"{hex_bytes:<{chunks_of * 3 - 1}}"
        ascii_text = "".join(chr(b) if 32 <= b <= 126 else "." for b in chunk)
        print(f"{offset}:  {hex_bytes}  |{ascii_text}|")

# ------------------------------------------------

def gzip_compress_file():
    """gzip compress file"""
    import gzip
    from pathlib import Path
    # input and output paths
    input_path = Path("data/output.yaml")
    output_path = Path("data/output.gz")
    # read, compress and write data
    with open(input_path, "rb") as f_in:
        with gzip.open(output_path, "wb") as f_out:
            f_out.write(f_in.read())

def gzip_decompress_file():
    """gzip decompress file"""
    import gzip
    from pathlib import Path
    # input and output paths
    output_path = Path("data/output-d.yaml")
    input_path = Path("data/output.gz")
    # read, compress and write data
    # for compress and decompress the only difference is where the gzip.open and file open is
    with gzip.open(input_path, "rb") as f_in:
        with open(output_path, "wb") as f_out:
            f_out.write(f_in.read())

def gzip_compress_memory():
    """gzip compress memory"""
    import gzip 
    raw_bytes = b"Compress this specific byte sequence."
    compressed_bytes = gzip.compress(raw_bytes)
    print("compressed")
    hexdump(compressed_bytes)
    decompressed = gzip.decompress(compressed_bytes)
    print("decompressed")
    hexdump(decompressed)

def gzip_decompress_memory():
    """gzip decompress memory"""
    import gzip 
    raw_bytes = b"Compress this specific byte sequence."
    compressed_bytes = gzip.compress(raw_bytes)
    hexdump(compressed_bytes)

# ------------------------------------------------

def zip_compress_file():
    import zipfile
    from pathlib import Path
    # input and output paths
    input_path = Path("data/output.yaml")
    output_path = Path("data/output.zip")
    # write the file into the ZIP archive
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zip_ref:
        zip_ref.write(input_path, arcname=input_path.name)

def zip_decompress_file():
    import zipfile
    from pathlib import Path
    # Open the ZIP file in read mode
    with zipfile.ZipFile("data/output.zip", "r") as zip_ref:
        # Extract all contents into the specified directory
        zip_ref.extractall("data/unzipped")

def zip_compress_memory():
    import io
    import zipfile
    # create ZIP bytes without writing an archive to disk
    memory_file = io.BytesIO()
    with zipfile.ZipFile(memory_file, "w", compression=zipfile.ZIP_DEFLATED) as zip_ref:
        zip_ref.writestr("message.txt", "Hello from an in-memory ZIP file.")
    zip_bytes = memory_file.getvalue()
    print("compressed")
    hexdump(zip_bytes)

def zip_decompress_memory():
    import io
    import zipfile
    # create example ZIP bytes in memory
    memory_file = io.BytesIO()
    with zipfile.ZipFile(memory_file, "w", compression=zipfile.ZIP_DEFLATED) as zip_ref:
        zip_ref.writestr("message.txt", "Hello from an in-memory ZIP file.")
    # read the ZIP bytes from memory
    memory_file.seek(0)
    with zipfile.ZipFile(memory_file, "r") as zip_ref:
        data = zip_ref.read("message.txt")
    print(data.decode("utf-8"))

# ------------------------------------------------

def hash_data():
    """example how to hash data and print hex-hash"""
    import hashlib
    byte_data = b"Hello, World!" 
    # uncomment if you need algorithms available 
    # print(hashlib.algorithms_available)
    hex_dig = hashlib.sha256(byte_data).hexdigest()
    print(hex_dig)

# ------------------------------------------------

def cytypes_math():
    import ctypes 
    # ctypes integers wrap like fixed-width CPU registers
    max_u64 = ctypes.c_uint64(0xffffffffffffffff)
    print(hex(max_u64.value))
    max_u64.value += 1
    print(hex(max_u64.value))
    neg_one = ctypes.c_int64(-1)
    same_bits = ctypes.c_uint64(neg_one.value)
    print(hex(same_bits.value))
    rax = ctypes.c_uint64(0xfffffffffffffff0)
    rax.value += 0x30
    print(hex(rax.value))

def cytype_enum():
    import ctypes 
    import struct
    # from https://github.com/alexander-hanel/coffcoff/blob/main/coffcoff.py#L109C1-L122C13
    class AUXSYMBOLFUNCDEF(ctypes.Structure):
        """
        Described in [PE-COFF] 5.5.1 Auxiliary Format 1: Function Definitions
        """
        _pack_ = 1
        _fields_ = [
            ("tag_index", ctypes.c_uint),
            ("total_size", ctypes.c_uint),
            ("pointer_to_line_number", ctypes.c_uint),
            ("pointer_to_next_function", ctypes.c_uint),
            ("unused", ctypes.c_ushort),
        ]

        def __new__(cls, buffer):
            return cls.from_buffer_copy(buffer)

        def __init__(self, data):
            self.raw_size = len(data)

    # create example bytes and parse them as a ctypes structure
    raw_bytes = struct.pack("<IIIIH", 1, 4096, 8192, 12288, 0)
    hexdump(raw_bytes)
    func_def = AUXSYMBOLFUNCDEF(raw_bytes)
    print(func_def.tag_index)
    print(func_def.total_size)
    print(func_def.pointer_to_line_number)
    print(func_def.pointer_to_next_function)
    print(func_def.unused)
    print(func_def.raw_size)

# ------------------------------------------------

def read_value_little_endian():
    import struct 
    # b"\x01\x00\x00\x00" is the integer 1 in little-endian byte order
    data = b"\x01\x00\x00\x00"
    value = struct.unpack("<I", data)[0]
    print(value)

# ------------------------------------------------

def xor(data=None, Key=None):
    from itertools import cycle
    data = b"Hello, World\x00\x00\x00\x00"
    key = b"temp"
    xored_bytes = bytes(b1 ^ b2 for b1, b2 in zip(data, cycle(key)))
    hexdump(xored_bytes) 

# ------------------------------------------------

def scan_buffer_yara(buffer, yara):
    """example to scan bytes with a YARA rule"""
    if buffer is None:
        buffer = b"This file contains the word malware."
    if yara is None:
        try:
            import yara
        except ImportError:
            print("Module Not Installed: pip -m install yara-python")
            return
    rule_source = """
rule ContainsMalwareWord
{
    strings:
        $word = "malware"
    condition:
        $word
}
"""
    rules = yara.compile(source=rule_source)
    matches = rules.match(data=buffer)
    print(matches)

# ------------------------------------------------

def load_env():
    """load enviornmental variables"""
    import os 
    import importlib.util
    module_name = "dotenv"
    module_exists = importlib.util.find_spec(module_name) is not None
    if module_exists:
        from dotenv import load_dotenv
    else:
        print("Module Not Installed: pip -m install python-dotenv")
        return
    
    load_dotenv()
    my_var = os.getenv("HOME")
    print(my_var)

def load_path_env():
    """load enviornmental variables from a .env file"""
    import os 
    from pathlib import Path
    import importlib.util
    module_name = "dotenv"
    module_exists = importlib.util.find_spec(module_name) is not None
    if module_exists:
        from dotenv import load_dotenv
    else:
        print("Module Not Installed: pip -m install python-dotenv")
        return
   
    dotenv_path = Path('data/.env')
    load_dotenv(dotenv_path=dotenv_path)
    my_var = os.getenv("TEST")
    print(my_var)

# ------------------------------------------------

def interquartile_range(values):
    """use interquartile range to find outliers within a list"""
    def median(values):
        n = len(values)
        if n % 2 == 1:
            return values[n // 2]
        return (values[n // 2 - 1] + values[n // 2]) / 2
    
    def quartiles(values):
        values = sorted(values)
        n = len(values)
        mid = n // 2
        if n % 2 == 0:
            lower = values[:mid]
            upper = values[mid:]
        else:
            lower = values[:mid]
            upper = values[mid + 1:]
        q1 = median(lower)
        q3 = median(upper)
        return q1, q3

    def find_outliers(values):
        q1, q3 = quartiles(values)
        iqr = q3 - q1
        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)
        return [
            value
            for value in values
            if value < lower_bound or value > upper_bound
        ]
    
    # validate types 
    if not isinstance(values, list):
        print("Incorrect type: pass list of integers")
        return None 
    if False in [isinstance(x, int) for x in values]:
        print("Incorrect type: pass list of integers")
        return None 
    print(find_outliers(values))

# print(interquartile_range([12, 14, 13, 15, 16, 14, 15, 13, 400]))

# ------------------------------------------------

def f_strings():
    """common f string operations"""
    example_str = "Hello, World"
    example_num = 111
    # variable name must be surrunded by { } 
    print(f"{example_str}, {example_num}")
    # note <, > and ^ 
    # left align 
    print(f"|{example_str:<22}|")
    # right align 
    print(f"|{example_str:>22}|")
    # center align 
    print(f"|{example_str:^22}|")
    # numbers, decimal .IntSpaceF 
    print(f"{example_num:.2f}")
    # 0 is the pad, 10 is the total width .3f is the padding of decimal  
    print(f"{example_num:010.3f}")
    # format hex  
    print(f"{example_num:#x}")


def activate_venv():
    print(""" 
    python -m venv myenv
    source myenv/bin/activate # bash 
    myenv\\Scripts\\activate.bat # windows 
    deactivate # leave 
    rm -rf myenv # delete on linux 
    rmdir /s /q myenv # delete via powershell 
    """)

activate_venv()