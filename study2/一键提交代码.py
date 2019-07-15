#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys

system_filter_command = 'grep'
personal_model = '"study"'
commit_name = '"update btaudio"'

git_status_str = 'git status |' + system_filter_command + ' ' + personal_model
git_commit_str = 'git commit -m ' + commit_name
git_push_str = ''
matchStr = r':\s+'


def init_system_info():
    global system_filter_command
    global git_status_str
    if 'win' in sys.platform:
        system_filter_command = 'find'
    git_status_str = 'git status |' + system_filter_command + ' ' + personal_model


def get_input_arg():
    global personal_model
    global git_status_str
    if len(sys.argv) == 2:
        personal_model = '\"%s\"' % sys.argv[1]
    if len(sys.argv) > 2:
        print('本脚本不支持两个及以上的命令行参数')
        sys.exit(0)
    git_status_str = 'git status |' + system_filter_command + ' ' + personal_model


def get_change_file_list1(output_list):
    new_lines = list(re.split(r':\s+', line) for line in output_list)
    return list(map(lambda item: item[len(item) - 1], new_lines))


def get_change_file_list2(output_list):
    def get_file_path(item):
        start_index = 0
        try:
            start_index = re.search(matchStr, item).end()
        finally:
            return item[start_index:]

    return list(map(lambda item: get_file_path(item), output_list))


def git_status():
    print(os.popen(git_status_str).read())


def get_file_status_list():
    command_output = os.popen(git_status_str).readlines()
    output_lines = list(ite.strip() for ite in command_output)
    return output_lines


def git_add(file_list):
    for file in file_list:
        git_add_str = 'git add ' + file
        os.popen(git_add_str)
    print(os.popen('git status',).read())


def git_commit():
    print(os.popen(git_commit_str).read())


def git_push():
    print(os.popen(git_push_str).read())


def fast_push_personal_module():
    git_status()
    git_add(get_change_file_list1(get_file_status_list()))
    git_commit()
    git_push()


init_system_info()
get_input_arg()
fast_push_personal_module()
