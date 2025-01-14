#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Yuuki Ishizaka
# SPDX-License-Identifier: BSD-3-Clause

from setuptools import setup
import os
from glob import glob

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],  # 単一パッケージの場合は明示的に指定
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py') or []),  # launch ファイルが空でもエラーにならないように
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yuuki',
    maintainer_email='yuuki@example.com',  # プレースホルダーを実際のメールアドレスに変更
    description='A package for practice',
    license='BSD-3-Clause',
    tests_require=['pytest', 'ament_pytest'],  # 追加のテスト依存関係
    entry_points={
    'console_scripts': [
        'talker = mypkg.talker:main',
        'listener = mypkg.listener:main',
    ],
},

)

