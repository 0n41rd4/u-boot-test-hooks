import os
import travis_tftp
import travis_http

env__net_uses_pci = True
env__net_dhcp_server = True
env__net_tftp_readable_file = travis_tftp.file2env('u-boot')
env__efi_loader_helloworld_file = travis_tftp.file2env('lib/efi_loader/helloworld.efi')
env__efi_loader_grub_file = travis_tftp.file2env('grub_loongarch64.efi')
env__efi_fit_tftp_file = {
    "dn" : os.environ['UBOOT_TRAVIS_BUILD_DIR'],
}

env__efi_loader_httpprotocol_file = travis_http.file2env('lib/efi_loader/netdump.efi', 'lib/efi_loader/netdump.efi')

env__efi_helloworld_net_http_test_skip = False
