#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re

personal_model = '"study"'
commit_name = '"update btaudio"'
git_status_str = 'git status |find ' + personal_model
git_commit_str = 'git commit -m ' + commit_name
git_push_str = ''
matchStr = r':\s+'


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
    print(os.popen('git status').read())


def git_commit():
    print(os.popen(git_commit_str).read())


def git_push():
    print(os.popen(git_push_str).read())


def fast_push_personal_module():
    git_status()
    git_add(get_change_file_list1(get_file_status_list()))
    git_commit()
    git_push()


fast_push_personal_module()
