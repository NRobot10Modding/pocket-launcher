import minecraft_launcher_lib as mc
import subprocess

mc_dir = './minecraft/'
all_ver_info = mc.utils.get_available_versions(mc_dir)

ver_list = []
av_ver_list = []

def install_version():
    for version in all_ver_info:
        ver_list.append(version["id"])

    print(ver_list)

install_version()
