import os
import binascii

def file2env(file_name, payload_name, server_ip="10.0.2.2", addr=None):
    """Create dictionary describing file

    @file_name:     name of the file to be described
    @payload_name:  name of the payload to be downloaded
    @server_ip:      IP of the HTTP server
    @addr:      address used for loading the file as int (e.g. 0x40400000)
    Return:     dictionary describing the file with entries
                * fn: 'lib/efi_loader/netdump.efi',         # file name
                * size: 5058624,                                 # file length in bytes
                * crc32: 'c2244b26',                             # CRC32 check sum
                * addr: 0x40400000,                              # load address
                * payload: 'http://10.0.2.2/path/to/payload',    # file uri
                * payload_length: 6354745,                       # file length in bytes
                * payload_crc32: 'b22e4a36',                     # CRC32 check sum
    """
    file_full = os.environ['UBOOT_TRAVIS_BUILD_DIR'] + "/" + file_name

    if not os.path.isfile(file_full):
        return None

    payload_full = os.environ['UBOOT_TRAVIS_BUILD_DIR'] + "/" + payload_name

    if not os.path.isfile(payload_full):
        return None

    payload_uri = "http://" + server_ip + "/" + payload_name

    ret = {
        "fn": file_name,
        "size": os.path.getsize(file_full),
        "payload": payload_uri,
        "payload_length": os.path.getsize(payload_full),
    }

    with open(file_full, 'rb') as fd:
        ret["crc32"] = hex(binascii.crc32(fd.read()) & 0xffffffff)[2:]

    with open(payload_full, 'rb') as fd:
        ret["payload_crc32"] = hex(binascii.crc32(fd.read()) & 0xffffffff)[2:]

    if addr is not None:
        ret['addr'] = addr

    return ret
